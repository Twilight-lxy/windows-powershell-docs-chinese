---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4Superscope_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/rename-dhcpserverv4superscope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Rename-DhcpServerv4Superscope
---

# 重命名 DHCPServerv4 的超范围（SuperScope）配置

## 摘要
重命名一个超范围（superscope）对象。

## 语法

```
Rename-DhcpServerv4Superscope [-ComputerName <String>] [-Name] <String> [-NewName] <String> [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
` Rename-DhcpServerv4Superscope` 这个 cmdlet 用于重命名一个超级范围（superscope）。超级范围是动态主机配置协议（DHCP）服务器的一项管理功能，它可以将多个范围组合成一个单独的管理实体。

## 示例

### 示例 1：重命名一个超范围（superscope）
```
PS C:\> Rename-DhcpServerv4Superscope -Name "Expanded B3 Network" -NewName "Expanded B3-1 Network" -ComputerName "DhcpServer01.Contoso.com"
```

此命令将名为“Expanded B3 Network”的超范围（superscope）重命名为“Expanded B3-1 Network”，该操作是在名为DhcpServer01.Contoso.com的DHCP服务器上执行的。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
Aliases:

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

### -Name
指定一个超范围的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NewName
指定超范围（superscope）的新名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
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

### -ThrottleLimit
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算一个最佳的并发限制。这个并发限制仅适用于当前的 cmdlet，而不适用于整个会话或整个计算机。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DhcpServerv4Superscope

## 备注

## 相关链接

[Get-DhcpServerv4Superscope](./Get-DhcpServerv4Superscope.md)

[Add-DhcpServerv4Superscope](./Add-DhcpServerv4Superscope.md)

[Remove-DhcpServerv4Superscope](./Remove-DhcpServerv4Superscope.md)

[Get-DhcpServerv4SuperscopeStatistics](./Get-DhcpServerv4SuperscopeStatistics.md)

