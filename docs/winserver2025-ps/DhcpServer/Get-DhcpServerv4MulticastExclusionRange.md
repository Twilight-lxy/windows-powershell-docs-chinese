---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4MulticastExclusionRange_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv4multicastexclusionrange?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv4MulticastExclusionRange
---

# Get-DhcpServerv4MulticastExclusionRange

## 摘要
检索指定多播范围内的排除范围（即不包含在多播数据中的地址段）。

## 语法

```
Get-DhcpServerv4MulticastExclusionRange [-ComputerName <String>] [[-Name] <String[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv4MulticastExclusionRange` 这个 cmdlet 可以检索指定多播范围内的排除地址范围。通过设置排除地址范围，可以防止动态主机配置协议（DHCP）服务器将这些地址分配给客户端设备。

## 示例

### 示例 1：获取某个作用域的排除范围
```
PS C:\> Get-DhcpServerv4MulticastExclusionRange -ComputerName "DhcpServer01.Contoso.com" -Name "Multicast_AudioConference"
```

此命令用于检索多播范围“Multicast_AudioConference”的排除范围（即不应被包含在传输数据中的IP地址段）。

### 示例 2：检索所有多播作用域的排除范围
```
PS C:\> Get-DhcpServerv4MulticastExclusionRange -ComputerName "DhcpServer01.Contoso.com"
```

该命令会返回名为DhcpServer01.Contoso.com的计算机上所有多播作用域的排除范围（即不允许数据传输的范围）。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -ComputerName
指定运行DHCP服务器服务的目标计算机的DNS名称或IP地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Cn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个多播作用域名称数组，从这些作用域中移除某个排除范围（即不再将该范围应用于数据传输）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的命令行脚本（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM 命令行脚本的数量来计算一个最优的流量限制（throttle limit）。该流量限制仅适用于当前的命令行脚本，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DhcpServerv4MulticastExclusionRange[]

## 备注

## 相关链接

[Add-DhcpServerv4MulticastExclusionRange](./Add-DhcpServerv4MulticastExclusionRange.md)

[Remove-DhcpServerv4MulticastExclusionRange](./Remove-DhcpServerv4MulticastExclusionRange.md)

