---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4ExclusionRange_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/remove-dhcpserverv4exclusionrange?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DhcpServerv4ExclusionRange
---

# 删除 DHCP 服务器 v4 的排除范围

## 摘要
删除之前被从某个 IPv4 范围中排除掉的一系列 IPv4 地址。

## 语法

```
Remove-DhcpServerv4ExclusionRange [-ComputerName <String>] [-ScopeId] <IPAddress> [[-StartRange] <IPAddress>]
 [[-EndRange] <IPAddress>] [-Passthru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
**Remove-DhcpServerv4ExclusionRange** cmdlet 用于删除之前从某个 IPv4 范围中排除掉的 IPv4 地址段。如果指定了 *StartRange* 和 *EndRange* 参数，那么就会删除该指定起始范围和结束范围的排除段；如果只指定了 *StartRange* 参数，则删除仅包含指定起始范围的排除段；如果只指定了 *EndRange* 参数，则删除仅包含指定结束范围的排除段；如果两者都没有指定，则会删除该范围内所有的排除段。

## 示例

### 示例 1：删除所有被排除在外的地址范围
```
PS C:\> Remove-DhcpServerv4ExclusionRange -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0
```

这个示例会删除指定DHCP服务器服务上所有被排除的IPv4地址范围。

### 示例 2：删除指定的排除地址范围
```
PS C:\> Remove-DhcpServerv4ExclusionRange -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -StartRange 10.10.10.1 -EndRange 10.10.10.10
```

这个示例会从指定的DHCP服务器服务中指定的范围内删除被排除的IPv4地址范围（即从10.10.10.1到10.10.10.10）。

### 示例 3：删除以指定地址开头的被排除的地址范围
```
PS C:\> Remove-DhcpServerv4ExclusionRange -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -StartRange 10.10.10.1
```

这个示例会从指定的DHCP服务器服务中，删除以IPv4地址10.10.10.1开头、属于被排除范围内的IPv4地址段。

### 示例 4：删除以指定地址结尾的被排除地址范围
```
PS C:\> Remove-DhcpServerv4ExclusionRange -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -EndRange 10.10.10.10
```

这个示例会从指定的DHCP服务器服务中，删除以IPv4地址10.10.10.10结尾的被排除的IPv4地址范围。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定目标计算机的DNS名称，或者其IPv4或IPv6地址。该目标计算机上运行着动态主机配置协议（DHCP）服务器服务。

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

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -EndRange
指定要删除的被排除 IP 范围的结束 IPv4 地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Passthru
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

### -ScopeId
指定排除范围将要从中被删除的范围标识符（ID），该标识符采用IPv4地址格式。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StartRange
指定要删除的被排除IP范围内的起始IPv4地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值（即并发操作的数量）。该限制仅适用于当前的 cmdlet，而不影响整个会话或计算机本身。

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

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4ExclusionRange
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）之后的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4ExclusionRange[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）之后的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv4ExclusionRange](./Add-DhcpServerv4ExclusionRange.md)

[Get-DhcpServerv4ExclusionRange](./Get-DhcpServerv4ExclusionRange.md)

