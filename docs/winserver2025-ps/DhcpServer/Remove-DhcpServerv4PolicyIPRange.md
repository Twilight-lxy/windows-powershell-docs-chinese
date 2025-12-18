---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4PolicyIPRange_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/remove-dhcpserverv4policyiprange?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DhcpServerv4PolicyIPRange
---

# 删除 DHCPServerv4PolicyIPRange

## 摘要
在范围级别上，从现有的策略中删除一个IP地址范围。

## 语法

```
Remove-DhcpServerv4PolicyIPRange [-Name] <String> [-ScopeId] <IPAddress> [[-StartRange] <IPAddress>]
 [[-EndRange] <IPAddress>] [-PassThru] [-ComputerName <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DhcpServerv4PolicyIPRange` cmdlet 用于从现有策略中删除指定的 IP 范围。该操作在策略的范围内进行（即在该策略所关联的所有服务器或设备上同时生效）。

如果您既没有指定*StartRange*参数，也没有指定*EndRange*参数，那么与该策略关联的所有IP地址范围都会被删除。

如果您仅指定了 *StartRange* 参数，那么系统会删除包含该指定起始地址的策略 IP 地址范围。

如果您只指定了 *EndRange* 参数，那么系统中具有该指定结束地址的策略IP地址范围将被删除。

## 示例

### 示例 1：从策略中删除一个 IP 地址范围
```
PS C:\> Remove-DhcpServerv4PolicyIPRange -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -Name "HyperVPolicy" -StartRange 10.10.10.10 -EndRange 10.10.10.20
```

这个示例会删除IP地址范围（从10.10.10.10到10.10.10.20），该地址范围与名为“HyperVPolicy”的策略相关联，且位于作用域10.10.10.0内。

### 示例 2：从策略中删除所有 IP 地址范围
```
PS C:\> Remove-DhcpServerv4PolicyIPRange -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -Name "HyperVPolicy"
```

这个示例会删除与名为“HyperVPolicy”的策略关联的所有IP地址范围，这些地址范围位于10.10.10.0范围内的网络中。

### 示例 3：通过指定起始地址来删除一个范围
```
PS C:\> Remove-DhcpServerv4PolicyIPRange -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -Name "HyperVPolicy" -StartRange 10.10.10.10
```

这个示例会删除从 10.10.10.10 开始的 IP 地址范围，该地址范围与名为 HyperVPolicy 的策略关联，并且位于 10.10.10.0 范围内。

### 示例 4：通过指定结束地址来删除一个数据范围
```
PS C:\> Remove-DhcpServerv4PolicyIPRange -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -Name "HyperVPolicy" -EndRange 10.10.10.20
```

这个示例会删除地址范围为 10.10.10.0.0 至 10.10.10.10 的 IP 地址段。该地址段与名为 HyperVPolicy 的策略相关联，且位于范围 10.10.10.0 内。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlet；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定运行动态主机配置协议（DHCP）服务器服务的目标计算机的DNS名称，或IPv4或IPv6地址。

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
在运行cmdlet之前，会提示您确认是否要继续执行该操作。

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
指定要从策略中删除的IP地址范围的结束IP地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定要删除一个或多个关联IP地址范围的策略名称。

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

### -PassThru
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

### -ScopeId
指定范围标识符（ID），采用IPv4地址格式，其中包含所指定的策略。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StartRange
指定要从策略中删除的 IP 地址范围的起始 IP 地址。

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

### -ThrottleLimit
该参数用于指定可以同时进行的操作的最大数量，以便运行相应的 cmdlet。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前执行的 cmdlet，而不影响整个会话或整个计算机。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Policy
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4PolicyIPRange
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4PolicyIPRange[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv4PolicyIPRange](./Add-DhcpServerv4PolicyIPRange.md)

[Get-DhcpServerv4PolicyIPRange](./Get-DhcpServerv4PolicyIPRange.md)

