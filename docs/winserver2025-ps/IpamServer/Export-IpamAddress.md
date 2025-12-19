---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamAddress.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/export-ipamaddress?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-IpamAddress
---

# 导出 IPAM 地址

## 摘要
从 IPAM 中导出 IP 地址。

## 语法

```
Export-IpamAddress -AddressFamily <AddressFamily> [-NetworkType <VirtualizationType>] [-Path <String>]
 [-PassThru] [-Force] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Export-IpamAddress` 这个 cmdlet 可以从 IP 地址管理（IPAM）系统中的某个地址族中导出所有 IP 地址，并将这些地址保存为逗号分隔值（CSV）格式的文件。

此 cmdlet 导出的字段标题名称以及 IP 地址对象的枚举值都采用英语命名，这些英文名称与文化环境无关（即具有普适性），并且不使用服务器所使用的本地化语言。字段标题名称遵循 Windows PowerShell 的属性命名规范。导出对象的日期和时间值的格式采用的是运行 IPAM 服务器的计算机所处的本地化语言设置，而非协调世界时（UTC）。

Windows PowerShell中的IPAM客户端控制台及IPAM服务器cmdlets支持英语版本与本地化版本的CSV文件之间的导入/导出功能互操作性，前提是用于导入/导出IP地址的IPAM服务器所在计算机的语言和区域设置（locale）保持一致。你可以使用IPAM Windows PowerShell导入从运行IPAM客户端界面的计算机导出的本地化CSV文件；同样地，如果你使用的是从运行IPAM客户端的计算机通过IPAM Windows PowerShell导出的英语版本的CSV文件，也是可以的——前提是这两台计算机的语言和区域设置相同。

## 示例

#### 示例 1：导出所有 IPv4 地址
```
PS C:\> Export-IpamAddress -AddressFamily IPv4 -Path "C:\Addresses_v4.csv"
```

该命令会将IPAM服务器中的所有IPv4地址导出到指定的路径。

### 示例 2：导出所有 IPv6 地址
```
PS C:\> Export-IpamAddress -AddressFamily IPv6 -Path "C:\addresses_v6.csv" -Force
```

该命令将IPAM中所有的IPv6地址导出到指定的路径。如果目标文件已经存在，该命令会直接覆盖该文件，而不会提示用户。

### 示例 3：输出所有 IPv4 地址
```
PS C:\> Export-IpamAddress -AddressFamily IPv4 -PassThru
IPAddress       IPAddressState    AssignmentType   ManagedByService    ServiceInstance
---------       --------------    --------------   ----------------    ---------------
172.22.2.15     In-Use            Static           IPAM                Localhost
10.10.0.10      In-Use            Static           IPAM                Localhost
172.17.14.15    Reserved          Dynamic          MS DHCP             s2-infra.contoso.com
192.168.0.1     Reserved          Dynamic          MS DHCP             s2-infra.contoso.com
```

这个命令会输出IPAM中的所有IPv4地址对象。

该命令包含了 *PassThru* 参数，因此它会将结果显示在控制台上。

### 示例 4：输出所有已过期的 IPv4 地址
```
PS C:\> Export-IpamAddress -AddressFamily IPv4 -PassThru | Where-Object -FilterScript { $_.ExpiryStatus -Eq "Expired" }
IPAddress         IPAddressState    AssignmentType   ManagedByService    ServiceInstance
---------         --------------    --------------   ----------------    ---------------
10.155.155.155    In-Use            Static           IPAM                Localhost
```

这个命令会过滤并输出IPAM中所有过期的IPv4地址。

该命令包含了 *PassThru* 参数，因此它会将结果显示在控制台上。

### 示例 5：导出所有已过期的 IPv4 地址
```
PS C:\> Export-IpamAddress -AddressFamily IPv4 -PassThru | Where-Object -FilterScript { $_.ExpiryStatus -Eq "Expired" } | Export-Csv -Path "C:\expired.csv"
```

该命令会过滤并导出 IPAM 中所有已过期的 IPv4 地址到指定的路径。

该命令包含了 *PassThru* 参数，因此它会将结果显示在控制台上。

### 示例 6：导出并输出所有已过期的 IPv4 地址
```
PS C:\> Export-IpamAddress -AddressFamily IPv4 -Path "C:\Addresses.csv" -PassThru
IPAddress       IPAddressState    AssignmentType   ManagedByService    ServiceInstance
---------       --------------    --------------   ----------------    ---------------
172.22.2.15     In-Use            Static           IPAM                Localhost
10.10.0.10      In-Use            Static           IPAM                Localhost
172.17.14.15    Reserved          Dynamic          MS DHCP             s2-infra.contoso.com
192.168.0.1     Reserved          Dynamic          MS DHCP             s2-infra.contoso.com
```

此命令将IPAM中的所有IPv4地址导出到指定的路径，然后输出这些已导出的地址。

该命令包含了 *PassThru* 参数，因此它会将结果显示在控制台上。

## 参数

### -AddressFamily
指定一组IP地址所属的地址族（address family）。该参数的可接受值包括：

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

### -Force
Indicates that the cmdlet overwrites a CSV file that has the same name that you specify for the *Path* parameter.

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
Specifies an IPv4 or IPv6 network prefix, in Classless InterDomain Routing (CIDR) notation.
This parameter specifies the IP subnet of the IP address range for which to import the addresses.

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
Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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
指定导出的 CSV 文件的绝对路径。

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
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最优限制值。此限制仅适用于当前运行的 cmdlet，不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.Windows.Ipamcommands.IpamIPAddressPSObject[]
这个cmdlet返回一个对象数组，其中包含IPAM IP地址。

## 备注

## 相关链接

[导入 Ipam 地址](./Import-IpamAddress.md)

[Add-IpamAddress](./Add-IpamAddress.md)

[Get-IpamAddress](./Get-IpamAddress.md)

[Set-IpamAddress](./Set-IpamAddress.md)

[Remove-IpamAddress](./Remove-IpamAddress.md)

[导入 Ipam 地址](./Import-IpamAddress.md)

