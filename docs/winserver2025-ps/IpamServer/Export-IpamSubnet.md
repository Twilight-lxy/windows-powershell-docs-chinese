---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamSubnet.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/export-ipamsubnet?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-IpamSubnet
---

# 导出 Ipam 子网

## 摘要
在运行 IPAM 的计算机上，导出该地址家族中的 IP 地址子网信息。

## 语法

```
Export-IpamSubnet -AddressFamily <AddressFamily> [-NetworkType <VirtualizationType>] [-Path <String>]
 [-PassThru] [-Force] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Export-IpamSubnet` cmdlet 可以导出运行 IP 地址管理（IPAM）的计算机上所有属于某个地址族的 IP 地址子网。输出结果可以是逗号分隔的值文件（.csv 格式），也可以是 Windows PowerShell 对象数组，或者同时包含两者。该 cmdlet 既可用于导出非虚拟化的地址子网，也可用于导出虚拟化的地址子网。

你必须指定 *Path* 参数或 *PassThru* 参数之一。当使用 *PassThru* 参数时，返回的对象数组可以用于进一步的过滤操作（即通过管道传递进行处理）。*Force* 参数可用于覆盖与 *Path* 参数中指定的名称相同的现有 .csv 文件。

与通过运行 IPAM 客户端用户界面的计算机进行本地化对象导出不同，Windows PowerShell 导出的 IP 地址子网对象的字段标题名称和枚举值名称都是英文版本，并不会根据服务器所使用的语言进行本地化处理。这些字段标题名称遵循 Windows PowerShell 的属性命名规范。

该cmdlet以运行IPAM的计算机的本地化格式输出导出对象的日期和时间值，而不是UTC格式。

## 示例

#### 示例 1：导出所有 IPv4 地址子网
```
PS C:\> Export-IpamSubnet -AddressFamily IPv4 -AddressSpace Default -Path "C:\Subnets_v4.csv"
```

此命令将所有属于默认地址空间的 IPv4 地址子网导出到文件 C:\subnets_v4.csv 中。

### 示例 2：导出所有 IPv6 地址子网
```
PS C:\> Export-IpamRange -AddressFamily IPv6 -Path "C:\Ranges_v6.csv" -Force
```

该命令将所有IPv6地址范围导出到文件Ranges_v6.csv中；如果该文件已经存在，则会覆盖该文件的内容。

### 示例 3：导出某个地址空间中的所有 IPv4 地址子网
```
PS C:\> Export-IpamSubnet -AddressFamily IPv4 -AddressSpace ContosoDataCenter -NetworkType Provider -Path "C:\Subnets_v4.csv"
```

这个命令会导出属于 ContosoDataCenter 地址空间的所有网络类型为“Provider”的 IPv4 地址子网。该 cmdlet 将输出结果写入文件 C:\subnets_v4.csv 中。

## 参数

### -AddressFamily
指定此cmdlet获取的IP地址范围对象所属的地址族。该参数的可接受值为：

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

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -NetworkType
指定给定 IP 子网所使用的网络类型。

此参数的可接受值为：

- Provider
 --  Customer
 --  NonVirtualized

如果 *AddressSpace* 参数的值为 “Default”，那么该参数可以取 “Provider” 或 “NonVirtualized” 作为值。如果 *AddressSpace* 参数的值为 “Provider”，那么必须指定 “Provider” 作为该参数的值；否则将会导致错误。同样地，如果 *AddressSpace* 参数的值为 “Customer”，那么也必须指定 “Customer” 作为该参数的值；否则也会导致错误。

如果您指定了 *NetworkType* 参数但没有指定 *AddressSpace* 参数，该 cmdlet 将返回给定网络类型的所有 IP 地址范围。

```yaml
Type: VirtualizationType
Parameter Sets: (All)
Aliases:
Accepted values: NonVirtualized, Provider, Customer

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -Path
指定此 cmdlet 所创建文件的完全限定路径和名称。使用此参数可以将所有 IP 地址子网对象导出为.csv 文件格式。

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

### -ThrottleLimit
该参数用于指定可以同时执行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算该命令的最佳限制值。此限制仅适用于当前正在执行的命令，而不适用于整个会话或计算机本身。

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

### CommonParameters
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### CimInstance#ROOT/microsoft/ipam/MSFT_IPAM/Subnet
此cmdlet返回一个对象，该对象代表IPAM数据存储中的一组IP子网。

## 备注

## 相关链接

[Export-IpamSubnet](./Export-IpamSubnet.md)

[Get-IpamSubnet](./Get-IpamSubnet.md)

[Import-IpamSubnet](./Import-IpamSubnet.md)

[Remove-IpamSubnet](./Remove-IpamSubnet.md)

[Set-IpamSubnet](./Set-IpamSubnet.md)

