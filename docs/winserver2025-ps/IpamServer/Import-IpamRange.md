---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamRange.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/import-ipamrange?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-IpamRange
---

# 导入IpamRange

## 摘要
从指定的文件中导入一个或多个IP地址范围对象到IPAM服务器中。

## 语法

### 导入（默认设置）
```
Import-IpamRange -Path <String> -AddressFamily <AddressFamily> [-ErrorPath <String>] [-CreateSubnetIfNotFound]
 [-Force] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### InventoryImport
```
Import-IpamRange -Path <String> -AddressFamily <AddressFamily> [-ErrorPath <String>] [-CreateSubnetIfNotFound]
 [-Force] -ManagedByService <String> -ServiceInstance <String> [-AddManagedByService] [-AddServiceInstance]
 [-DeleteMappedAddresses] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Import-IpamRange` cmdlet 用于将来自指定逗号分隔值（.csv）文件的 IP 地址范围对象导入到 IP 地址管理（IPAM）服务器中。不过，IPAM 服务器不支持导入那些 `ServiceInstance` 参数值为 `MS DHCP` 的 IP 地址范围；该参数专门用于标识由 IPAM 服务器从运行 Microsoft DHCP 服务器服务的受管理计算机中自动检测到的动态主机配置协议（DHCP）作用域。在导入过程中任何失败的操作都会被记录到相应的错误日志文件中，以便进一步分析。

此cmdlet支持两种参数设置。默认情况下，该cmdlet会从.csv文件中添加新的IP地址范围对象到IPAM服务器，并根据.csv文件中指定的更新信息来修改现有的地址范围。

第二组参数可用于定期导入并更新所有属于指定组合（即 *ManagedByService* 和 *ServiceInstance* 参数）的 IP 地址范围对象，这些对象存储在 IPAM 服务器中。除了对现有地址范围进行添加和编辑操作外，该导入功能还会从 IPAM 服务器中删除那些与 *ManagedByService* 和 *ServiceInstance* 参数值相同，但未包含在所导入的 .csv 文件中的地址范围。通过使用 *DeleteMappedAddresses* 参数，您可以选择删除在导入过程中被删除的 IP 地址范围对应的 IP 地址。

如果指定的 *ManagedByService* 和 *ServiceInstance* 参数值在导入时已经存在于 IPAM 服务器上，那么导入和更新这些参数值的操作将会成功。如果需要，在导入操作之前，可以使用 *AddManagedByService* 和 *AddServiceInstance* 功能在运行时在 IPAM 服务器中创建相应的参数值。

网络标识符（ID）字段是必需的，用于将IPAM范围导入到.csv文件中。其他与范围相关的基本字段或自定义字段也可以按任意顺序添加到.csv文件中进行导入。可以通过IPAM用户界面（提供多种语言版本）或IPAM Windows PowerShell®（仅提供英文版本）中的导出功能来生成.csv文件的示例格式。

IPAM Windows PowerShell导入功能支持英文格式的.csv文件，同时也支持服务器本地化后的.csv文件。IPAM服务器会通过检测.csv文件中是否存在名为“NetworkId”（不含空格）的字段来判断该文件应使用哪种格式进行处理；如果不存在该字段，则文件将按照服务器本地化的格式进行解析，其中各个字段的名称和枚举值也会相应地进行本地化处理。导入对象的日期和时间值的显示格式始终采用IPAM服务器的本地化设置，而非国际协调时间（UTC）格式。

## 示例

### 示例 1：导入地址范围
```
PS C:\> Import-IpamRange -AddressFamily IPv4 -Path "C:\Rangev4.csv" -Force
```

该命令从名为Rangev4.csv的文件中导入IPv4地址范围，并将其添加到IPAM服务器中。同时，也会对现有的地址范围进行相应的修改。如果出现任何错误，这些错误会被记录在用户文件夹下的Documents文件夹中，并以.csv文件的格式保存。

此命令包含了*Force*参数，因此它会抑制默认的确认消息。

### 示例 2：导入 IPv4 地址范围并记录错误信息
```
PS C:\> Import-IpamRange -AddressFamily IPv4 -Path "C:\Rangev4.csv" -ErrorPath "C:\" -Force
```

此命令将名为 Rangev4.csv 的文件中的 IPv4 地址范围导入到 IPAM 服务器中。新地址范围会被添加进来，现有地址范围也会被相应修改。如果出现任何错误，这些错误会以 .csv 文件格式记录在路径 C:\ 下。

此命令包含了*Force*参数，因此它会抑制默认的确认消息。

### 示例 3：导入和更新地址范围
```
PS C:\> Import-IpamRange -AddressFamily IPv4 -Path "C:\Rangeupdatev4.csv" -ManagedByService "IPAM" -ServiceInstance "localhost"
Confirm

Imports a csv file as an update of all IP address ranges that belong to the specified combination of ManagedByService and ServiceInstance values. Along with adding new ranges and editing existing ranges, this operation also deletes ranges belonging to the specified combination of ManagedByService and ServiceInstance from IPAM database, that are not present in the csv file being imported.
Continue with this operation?

[Y] Yes  [N] No  [?] Help  <default is "Y">:Y
```

此命令从名为 C:\Rangeupdatev4.csv 的文件中导入并更新由 IPAM 服务和 Localhost 服务实例管理的所有 IPv4 地址范围，并将这些信息添加到 IPAM 中。新的地址范围会被添加进来，现有的地址范围会得到相应的修改；而那些同时满足 *ManagedByService* 和 *ServiceInstance* 参数要求（但并未包含在该 .csv 文件中）的地址范围则会从 IPAM 服务器上删除。如果过程中出现任何错误，这些错误信息将会以 .csv 文件格式被记录在用户对应的 “Documents” 文件夹中。

### 示例 4：导入和更新地址范围，并记录错误信息
```
PS C:\> Import-IpamRange -AddressFamily IPv4 -Path "C:\Rangeupdatev4.csv" -ManagedByService "IPAM" -ServiceInstance "localhost" -ErrorPath "C:\" -Force
```

此命令从名为 `C:\Rangeupdatev4.csv` 的文件中，将所有 IPv4 地址范围导入并更新到名为 IPAM 的管理服务以及名为 Localhost 的服务实例中。新的地址范围会被添加到 IPAM 服务器中；现有的地址范围会进行修改；而那些属于 `.csv` 文件中未指定的 `ManagedByService` 和 `ServiceInstance` 参数组合的地址范围，则会从 IPAM 服务器中删除。如果出现任何错误，这些错误会以 `.csv` 文件格式记录在路径 `C:\` 下。

此命令包含了*Force*参数，因此它会抑制默认的确认消息。

### 示例 5：导入、更新和删除地址范围
```
PS C:\> Import-IpamRange -AddressFamily IPv4 -Path "C:\Rangeupdatev4.csv" -ManagedByService "Others" -ServiceInstance "DHCPServer1" -AddServiceInstance -Force
```

此命令会将 DHCPServer1 添加为自定义字段 ServiceInstance 的新值（如果该值在 IPAM 服务器中还不存在的话）。该 cmdlet 会从名为 C:\Rangeupdatev4.csv 的文件中导入所有与 managed service “Others” 和服务实例 DHCPServer1 相关的 IPv4 地址范围，并将这些信息更新到 IPAM 服务器中。新地址范围会被添加到系统中，现有的地址范围会被修改；而那些属于 *ManagedByService* 与 *ServiceInstance* 参数组合但并未包含在该 .csv 文件中的地址范围，则会从 IPAM 服务器中删除。如果出现任何错误，这些错误信息将以 .csv 文件格式记录在用户的 Documents 文件夹中。

此命令包含了*Force*参数，因此它会抑制默认的确认消息。

### 示例 6：添加自定义值并导入地址范围
```
PS C:\> Import-IpamRange -AddressFamily IPv4 -Path "C:\Rangeupdatev4.csv" -ManagedByService "MyDHCPType" -ServiceInstance "DHCPServer1" -AddServiceInstance -AddManagedByService -Force
```

此命令会将 DHCPServer1 添加为自定义字段 ServiceInstance 的新值（如果该值在 IPAM 服务器中还不存在的话）。同时，此 cmdlet 还会将 MyDHCPType 添加为自定义字段 ManagedByService 的新值（如果该值在 IPAM 服务器中还不存在的话）。此外，该 cmdlet 会从名为 C:\rangeupdatev4.csv 的文件中导入所有由管理服务 MyDHCPType 和服务实例 DHCPServer1 管理的 IPv4 地址范围，并更新这些范围信息到 IPAM 服务器中。新地址范围会被添加到系统中，现有的地址范围会被相应修改；而那些属于 *ManagedByService* 与 *ServiceInstance* 参数组合但未包含在该 .csv 文件中的地址范围，则会从 IPAM 服务器中删除。如果出现任何错误，这些错误信息将以 .csv 文件格式被记录在用户的 Documents 文件夹中。

此命令包含了*Force*参数，因此它会抑制默认的确认消息。

## 参数

### -AddManagedByService
表示该 cmdlet 会将指定的 *ManagedByService* 参数值添加到与该参数名称匹配的自定义字段中（如果该字段尚不存在的话）。

```yaml
Type: SwitchParameter
Parameter Sets: InventoryImport
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddServiceInstance
这表示该 cmdlet 会将指定的 *ServiceInstance* 参数值添加到与该参数名称匹配的自定义字段中（如果该字段尚不存在的话）。

```yaml
Type: SwitchParameter
Parameter Sets: InventoryImport
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddressFamily
指定此 cmdlet 导入的记录所属的地址族。

此参数的可接受值为：

- IPv4
- IPv6.

Only one address family at a time can be specified with this cmdlet and the records in the .csv file should match the specified address.

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

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要较长时间才能完成的任务。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
在运行cmdlet之前会提示您进行确认。

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

### -CreateSubnetIfNotFound
表示该 cmdlet 会为这个地址范围创建一个父子子网。如果您指定了此参数，如果不存在父子子网，cmdlet 会自动为此地址范围创建一个父子子网。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DeleteMappedAddresses
这意味着在导入和更新操作期间被删除的所有IP地址范围所包含的、或映射到这些IP地址范围内的所有IP地址，也将被同时删除。

```yaml
Type: SwitchParameter
Parameter Sets: InventoryImport
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ErrorPath
指定错误.csv文件的完整路径（而非文件名）。当一个或多个记录无法导入时，系统会生成这些错误文件。

文件名是由 IPAM 服务器自动生成的：会在文件名前添加 `Error_`，并在文件名后加上操作的时间戳（该时间戳来自 *Path* 参数中指定的路径）。这个参数的默认值是用户的 “Documents” 文件夹。

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
强制命令运行，而无需请求用户确认。

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
指定正在导入和更新的 IP 地址范围的管理服务的值。IPAM 不支持导入 `MS DHCP` 范围。

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

### -Path
指定要导入的.csv文件的完整路径和文件名。

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
指定一个服务实例数组，这些服务实例用于管理要导入的地址范围。

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

### -ThrottleLimit
该参数用于指定可以同时执行的命令（cmdlet）操作的最大数量。如果省略此参数或输入值为`0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算出该命令的最佳执行限制（即并发操作的极限）。此限制仅适用于当前正在执行的命令，而不影响整个会话或整台计算机。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.String
此cmdlet返回一个字符串，其中包含该命令执行的步骤的详细摘要。消息可以是以下内容之一：

- Import of \<AddressFamily\> objects is complete.
\<y\> out of \<y\> objects successfully imported.\<AddressFamily\>\<y\>\<y\>.

- Import of \<AddressFamily\> objects is complete.
\<x\> out of \<y\> objects successfully imported.
\<z\> out of \<y\> objects failed to get imported.
Failures recorded in the file: \<ErrorFilename\> \<AddressFamily\>\<x\>\<y\>\<z\>\<y\>\<ErrorFilename\>

## 备注

## 相关链接

[Export-IpamRange](./Export-IpamRange.md)

