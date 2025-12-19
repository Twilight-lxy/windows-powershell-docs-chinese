---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamRange.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/export-ipamrange?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-IpamRange
---

# 导出 Ipam 范围

## 摘要
将所有 IP 地址范围导出为一个文件、一个对象数组，或者同时以这两种形式进行导出。

## 语法

```
Export-IpamRange -AddressFamily <AddressFamily> [-NetworkType <VirtualizationType>] [-Path <String>]
 [-PassThru] [-Force] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Export-IpamRange` cmdlet 可以将指定地址族中的所有 IP 地址范围从运行 IP 地址管理（IPAM）服务器的计算机中导出为逗号分隔值（.csv）文件、Windows PowerShell® 对象数组，或者同时以这两种格式进行导出。

在使用该cmdlet时，必须至少指定一个*Path*或*PassThru*参数。通过*PassThru*参数返回的对象数组可以根据需要进行进一步处理（例如使用管道操作进行过滤）。

与从 IPAM 客户端用户界面（UI）导出的本地化对象不同，Windows PowerShell 导出的 IP 地址范围对象的字段标题名称和枚举值名称都是英文的，并不会根据运行 IPAM 服务器的计算机的使用语言进行本地化处理。这些字段标题名称必须遵循 Windows PowerShell 的属性命名规范。

导出对象的日期和时间值的格式采用的是运行 IPAM 服务器的计算机所使用的本地化格式，而不是协调世界时（UTC）格式。

IPAM客户端界面（UI）和IPAM Windows PowerShell支持导入/导出功能的互操作性，无论是英文版本的.csv文件还是本地化版本的.csv文件。这一互操作性的前提是：执行IPAM服务器及相关用户界面的计算机的操作系统语言和区域设置（locale）必须保持一致。换句话说，从IPAM客户端界面导出的本地化.csv文件可以使用IPAM Windows PowerShell进行导入；同样，从IPAM Windows PowerShell导出的英文.csv文件也可以使用IPAM客户端界面进行导入。总之，只要运行IPAM客户端和IPAM服务器的计算机的操作系统语言及区域设置相同，就可以实现文件之间的顺利转换。

## 示例

### 示例 1：将 IPv4 地址范围导出到文件中
```
PS C:\> Export-IpamRange -AddressFamily IPv4 -Path "C:\Ranges_v4.csv"
```

这个命令将所有的IPv4地址范围输出到名为Ranges_v4.csv的文件中。

### 示例 2：将 IPv6 地址范围导出到文件
```
PS C:\> Export-IpamRange -AddressFamily IPv6 -Path "C:\Ranges_v6.csv" -Force
```

该命令会将所有的IPv6地址范围输出到文件Ranges_v6.csv中；如果该文件已经存在，则会覆盖原有的文件内容。

### 示例 3：导出 IPv4 地址范围
```
PS C:\> Export-IpamRange -AddressFamily IPv4 -PassThru
NetworkId       StartIPAddress    EndIPAddress    PercentageUtilized    ManagedByService    ServiceInstance
---------       --------------    ------------    ------------------    ----------------    ---------------
172.22.2.0/24      172.22.2.1      172.22.2.254       20.00                 IPAM                Localhost
10.10.0.0/24       10.10.0.1       10.10.0.254        0.00                  IPAM                Localhost
172.17.14.0/24     172.17.14.1     172.17.14.254      85.00                 MS DHCP             s2-infra.contoso.com
192.168.0.0/16     192.168.0.1     192.168.255.254    48.75                 MS DHCP             s2-infra.contoso.com
```

这个命令会输出所有的 IPv4 地址范围对象。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

### 示例 4：导出被过度使用的 IPv4 地址范围对象
```
PS C:\> Export-IpamRange -AddressFamily IPv4 -PassThru | Where-Object -FilterScript { $_.Utilization -Eq "Over" }
NetworkId       StartIPAddress    EndIPAddress    PercentageUtilized    ManagedByService    ServiceInstance
---------       --------------    ------------    ------------------    ----------------    ---------------
172.17.14.0/24  172.17.14.1       172.17.14.254   85.00                 MS DHCP             s2-infra.contoso.com
```

这个命令会过滤掉所有被过度使用的 IPv4 地址范围对象。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

### 示例 5：将使用过度的 IPv4 地址范围对象导出到文件中
```
PS C:\> Export-IpamRange -AddressFamily IPv4 -PassThru | Where-Object -FilterScript { $_.Utilization -Eq "Over" } | Export-Csv -Path "C:\overutilized.csv"
```

该命令会过滤所有使用过度（即被过度分配或频繁使用的）IPv4地址范围对象，并将这些对象导出到指定的文件中。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

### 示例 6：从文件中导出地址范围
```
PS C:\> Export-IpamRange -AddressFamily IPv4 -Path "C:\Ranges.csv" -PassThru
NetworkId       StartIPAddress    EndIPAddress    PercentageUtilized    ManagedByService    ServiceInstance
---------       --------------    ------------    ------------------    ----------------    ---------------
172.22.2.0/24     172.22.2.1       172.22.2.254       20.00                 IPAM                Localhost
10.10.0.0/24      10.10.0.1        10.10.0.254        0.00                  IPAM                Localhost
172.17.14.0/24    172.17.14.1      172.17.14.254      85.00                 MS DHCP             s2-infra.contoso.com
192.168.0.0/16    192.168.0.1      192.168.255.254    48.75                 MS DHCP             s2-infra.contoso.com
```

该命令会输出名为 C:\Ranges.csv 的文件中所有的 IPv4 地址范围，并同时显示这些被导出的地址范围。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

## 参数

### -AddressFamily
指定要导出的 IP 地址范围对象的地址族。该参数的可接受值为：

- IPv4
- IPv6

This parameter specifies whether the IPv4 or IPv6 records need to be exported.
Only one address family at a time can be specified with this cmdlet.

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
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定通过导出生成的新.csv文件必须覆盖现有的.csv文件（如果存在的话），具体覆盖路径由*Path*参数指定。

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
指定给定IP子网所属的网络类型。

此参数的可接受值为：

- Provider
- Customer
- NonVirtualized

If the address space specified by the *AddressSpace* parameter is Default, specify a value of Provider or NonVirtualized.
If the address space specified by *AddressSpace* parameter is of type Provider, if you specify this parameter, specify a value of Provider.
Specifying any other value for this parameter causes an error.
If the address space specified by the *AddressSpace*  parameter is of type Customer, then, if you specify this parameter, specify a value of Customer.
Specifying any other value for this parameter causes an error.
If you do not specify this parameter, the cmdlet uses a network type NonVirtualized.

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
返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

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
指定在导出过程中生成的.csv文件的路径和名称。

此参数用于将所有IP地址范围对象导出为.csv文件格式。

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
指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.Windows.IpamCommands.IpamIPRangePSObject[]
此cmdlet返回一个对象数组，其中包含IPAM IP地址范围。

## 备注

## 相关链接

[Import-IpamRange](./Import-IpamRange.md)

