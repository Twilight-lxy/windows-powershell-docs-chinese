---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV6OptionDefinition_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/remove-dhcpserverv6optiondefinition?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DhcpServerv6OptionDefinition
---

# 删除 DHCP Server v6 选项定义

## 摘要
从DHCP服务器服务中删除IPv6选项定义。

## 语法

```
Remove-DhcpServerv6OptionDefinition [-ComputerName <String>] [-OptionId] <UInt32[]> [[-VendorClass] <String>]
 [-Passthru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-DhcpServerv6OptionDefinition` cmdlet 用于从动态主机配置协议（DHCP）服务器服务中删除一个或多个 IPv6 选项定义。如果指定了 `VendorClass` 参数，则只会删除与该供应商类别相关的选项定义。

## 示例

### 示例 1：删除某个 ID 的选项定义
```
PS C:\> Remove-DhcpServerv6OptionDefinition -ComputerName "dhcpserver.contoso.com" -OptionId 21,24
```

这个示例会删除指定选项ID对应的DHCPv6选项定义。

### 示例 2：删除某个供应商类别中某个选项ID对应的选项定义
```
PS C:\> Remove-DhcpServerv6OptionDefinition -ComputerName "dhcpserver.contoso.com" -VendorClass "MyVendorClass" -OptionId 10
```

这个示例会删除指定供应商类别特定选项（vendor-class-specific option）对应的DHCPv6选项定义。

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlet；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
指定运行DHCP服务器服务的目标计算机的DNS名称，或IPv4地址或IPv6地址。

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

### -OptionId
指定一个或多个数字标识符（ID），用于表示那些需要删除其定义的一个或多个选项。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Passthru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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
指定可以同时运行的最大并发操作数量。如果省略此参数或输入 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最优限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -VendorClass
仅针对指定的供应商类别移除选项定义。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6OptionDefinition
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6OptionValue
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6OptionDefinition[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv6OptionDefinition](./Add-DhcpServerv6OptionDefinition.md)

[Get-DhcpServerv6OptionDefinition](./Get-DhcpServerv6OptionDefinition.md)

[Set-DhcpServerv6OptionDefinition](./Set-DhcpServerv6OptionDefinition.md)

