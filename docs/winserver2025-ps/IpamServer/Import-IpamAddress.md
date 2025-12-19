---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamAddress.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/import-ipamaddress?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-IpamAddress
---

# 导入 Ipam 地址

## 摘要
将IP地址导入到IPAM服务器中。

## 语法

### 导入（默认设置）
```
Import-IpamAddress -Path <String> -AddressFamily <AddressFamily> [-ErrorPath <String>] [-Force]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InventoryImport
```
Import-IpamAddress -Path <String> -AddressFamily <AddressFamily> [-ErrorPath <String>] [-Force]
 -ManagedByService <String> -ServiceInstance <String> -NetworkId <String> [-StartIpAddress <IPAddress>]
 [-EndIpAddress <IPAddress>] [-NetworkType <VirtualizationType>] [-AddressSpace <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Import-IpamAddress` cmdlet 用于从逗号分隔值（CSV）文件中导入 IP 地址，并将其存储到 IP 地址管理（IPAM）服务器中。

该cmdlet支持两种参数集。`Import`参数集用于将CSV文件中的IP地址对象添加到IPAM服务器中，并使用CSV文件中指定的更新信息来更新现有的地址对象。

请使用 `InventoryImport` 参数集来定期导入并更新所有与指定 IP 地址范围相匹配的 IP 地址对象。这些地址是通过结合使用 `NetworkId`、`ManagedByService`、`ServiceInstance`、`StartIPAddress` 和 `EndIPAddress` 这些参数来识别的。除了添加新的地址和修改现有地址之外，该操作还会移除那些与指定 IP 地址范围匹配但不存在于所导入的 `.csv` 文件中的地址。只有当该地址范围确实存在于 IPAM 服务器上时，对这些地址范围的导入和更新操作才会成功完成。

在您导入的CSV文件中，唯一必填的字段是IP地址。其他与特定地址相关的字段或自定义字段可以以任意顺序出现在该CSV文件中。

IPAM 的 Windows PowerShell 导入功能支持英文格式的 CSV 文件以及服务器本地化版本的 CSV 文件。IPAM 服务器会通过 CSV 文件中是否存在 “IPAddress” 这一字段名称来判断该文件应采用哪种格式进行处理；如果 CSV 文件中没有 “IPAddress” 字段，那么这些文件将会按照服务器本地化的字段名称和枚举值格式进行解析。导入对象的日期和时间值的显示格式将遵循运行 IPAM 服务器的计算机所使用的本地化设置，而不是协调世界时（UTC）。

## 示例

### 示例 1：导入 IPv4 地址
```
PS C:\> Import-IpamAddress -AddressFamily IPv4 -Path "C:\Addressv4.csv" -Force
```

该命令将文件 C:\Addressv4.csv 中的 IPv4 地址导入到 IPAM 服务器中。新地址会被添加，现有地址也会被更新。如果出现错误，这些错误会以 CSV 文件格式记录在用户的 Documents 文件夹中。该命令无需用户确认即可执行。

### 示例 2：导入 IPv4 地址并记录错误信息
```
PS C:\> Import-IpamAddress -AddressFamily IPv4 -Path "C:\addressv4.csv" -ErrorPath "C:\" -Force
```

此命令将文件 `C:\Addressv4.csv` 中的 IPv4 地址导入到 IPAM 服务器中。该命令会添加新的地址，同时也会修改现有的地址。此外，该命令还会记录在导入 CSV 文件过程中出现的错误（错误信息会被保存在路径为 `C:\` 的目录下）。

该命令包含了 *PassThru* 参数，因此它会将结果显示在控制台中。

### 示例 3：导入并更新某个范围内的 IPv4 地址
```
PS C:\> Import-IpamAddress -AddressFamily IPv4 -Path "C:\addressupdatev4.csv" -ManagedByService "IPAM" -ServiceInstance "Localhost" -NetworkId "10.10.10.0/24"
Confirm

Imports a csv file as an update of all IP address records that belong to the specified IP address range. Along with adding new addresses and editing existing addresses, this operation also deletes addresses belonging to the specified IP address range from IPAM database, that are not present in the csv file update being imported.


Continue with this operation?

[Y] Yes  [N] No  [?] Help  :Y
```

此命令会从指定的路径导入并更新所有属于网络ID 10.10.10.0/24范围内的IPv4地址。这些地址来自IPAM（IP地址管理）服务以及名为Localhost的服务实例。该cmdlet会将起始IP地址设置为10.10.10.1，将结束IP地址设置为10.10.10.254。它还会添加新的地址、修改现有的地址，并移除那些不属于CSV文件中指定范围的地址。默认情况下，在计算起始和结束IP地址时，包含全零（0）或全一（1）的主机ID会被忽略。

### 示例 4：导入并更新具有起始地址和结束地址的 IPv4 地址
```
PS C:\> Import-IpamAddress -AddressFamily IPv4 -Path "C:\Addressupdatev4.csv" -ManagedByService "IPAM" -ServiceInstance "Localhost" -NetworkId "10.10.10.0/24" -StartIpAddress 10.10.10.1 -EndIpAddress 10.10.10.50 -Force
```

此命令会从文件 C:\Addressupdatev4.csv 中导入并更新所有属于以下范围的 IPv4 地址：网络 ID 为 10.10.10.0/24、起始 IP 地址为 10.10.10.1、结束 IP 地址为 10.10.10.50、管理服务为 IPAM，以及服务实例为 Localhost。该命令会添加新的地址、修改现有的地址，并删除那些属于指定范围但未包含在 CSV 文件中的地址。此外，该命令还会将 CSV 文件中出现的错误记录到用户的 Documents 文件夹中。

## 参数

### -AddressFamily
指定导入文件中IP地址记录的地址家族。CSV文件中的IP地址记录必须属于您为该参数指定的地址家族。

该参数的可接受值为：

- IPv4
- IPv6

```yaml
Type: AddressFamily
Parameter Sets: (All)
Aliases:
Accepted values: IPv4, IPv6

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddressSpace
Specifies the name of an address space.
If you do not specify this parameter, the cmdlet imports the IP addresses into the Default address space.
If you specify this parameter, you must specify the *AddressFamily* parameter.

```yaml
Type: String
Parameter Sets: InventoryImport
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
Runs the cmdlet as a background job. Use this parameter to run commands that take a long time to complete.

The cmdlet immediately returns an object that represents the job and then displays the command prompt.
You can continue to work in the session while the job completes.
To manage the job, use the `*-Job` cmdlets.
To get the job results, use the [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet.

For more information about Windows PowerShell background jobs, see [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251).

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
Runs the cmdlet in a remote session or on a remote computer.
Enter a computer name or a session object, such as the output of a [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) or [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet.
The default is the current session on the local computer.

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
Prompts you for confirmation before running the cmdlet.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -EndIpAddress
Specifies the end address for the IP address block.
If you do not specify this parameter, the cmdlet uses the last IP address of the network that you specify for the *NetworkId* parameter.
If you specify this parameter, you must specify the *StartIPAddress* parameter.

```yaml
Type: IPAddress
Parameter Sets: InventoryImport
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ErrorPath
Specifies the literal path of the error CSV files that IPAM generates if one or more IP address records fail to import.

The file name is generated automatically by the computer that runs the IPAM server by prepending `Error_` and appending the timestamp of the operation to the file name specified in the *Path* parameter.
The default value of this parameter is the **Documents** folder of the user.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Force
Forces the command to run without asking for user confirmation.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagedByService
Specifies the value of the service that manages the IP address range for which you import and update IP addresses.
Specify this parameter and the *ServiceInstance*, *NetworkId*, *StartIpAddress*, and *EndIpAddress* parameters to uniquely identify a range.

```yaml
Type: String
Parameter Sets: InventoryImport
Aliases: MB

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkId
Specifies an IPv4 or IPv6 network prefix, in Classless InterDomain Routing (CIDR) notation.
This parameter specifies the IP subnet of the IP address range for which you import the addresses.

Specify this parameter and the *ManagedByService*, *ServiceInstance*, *StartIpAddress*, and *EndIpAddress* parameters to uniquely identify a range.

```yaml
Type: String
Parameter Sets: InventoryImport
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkType
Specifies an IPv4 or IPv6 network prefix, in Classless InterDomain Routing (CIDR) notation.
This parameter specifies the IP subnet of the IP address range for which to export the addresses.

Specify this parameter and the *ManagedByService*, *ServiceInstance*, *StartIpAddress*, and *EndIpAddress* parameters to uniquely identify an address range.

```yaml
Type: VirtualizationType
Parameter Sets: InventoryImport
Aliases:
Accepted values: NonVirtualized, Provider, Customer

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path
Specifies the literal path and name of the CSV file to import.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ServiceInstance
Specifies the value of the service instance of the IP address range for which you are importing and updating IP addresses.
Specify this parameter and the *ManagedByService*, *NetworkId*, *StartIpAddress*, and *EndIpAddress* parameters to uniquely identify a range.

```yaml
Type: String
Parameter Sets: InventoryImport
Aliases: SI

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StartIpAddress
Specifies the start address for the IP address block.
If you do not specify this parameter, the cmdlet uses the first address of the network that you specify for the *NetworkId* parameter.
If you specify this parameter, you must specify the *EndIpAddress* parameter.

```yaml
Type: IPAddress
Parameter Sets: InventoryImport
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行此cmdlet的最大操作数量。如果省略此参数或输入值`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算一个最优的 throttling（限流）限制。这个限流限制仅适用于当前的cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.String
此cmdlet返回一个字符串，其中包含该cmdlet执行的步骤的详细摘要。返回的消息有以下几种之一：

- Import of \<AddressFamily\> objects is complete.
\<y\> out of \<y\> objects successfully imported.

- Import of \<AddressFamily\> objects is complete.
\<x\> out of \<y\> objects successfully imported.
\<z\> out of \<y\> objects failed to get imported.
Failures recorded in the file: \<ErrorFilename\>

## 备注

## 相关链接

[Export-IpamAddress](./Export-IpamAddress.md)

