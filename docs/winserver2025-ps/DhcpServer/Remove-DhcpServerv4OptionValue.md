---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4OptionValue_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/remove-dhcpserverv4optionvalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DhcpServerv4OptionValue
---

# 移除 DHCP Server v4 选项值

## 摘要
在服务器、作用域或预留级别上删除一个或多个 IPv4 选项值，这些选项值可以属于标准的 IPv4 选项，也可以属于指定的供应商或用户类别。

## 语法

```
Remove-DhcpServerv4OptionValue [-VendorClass <String>] [-ComputerName <String>] [-OptionId] <UInt32[]>
 [-UserClass <String>] [[-ScopeId] <IPAddress>] [-ReservedIP <IPAddress>] [-PassThru] [-PolicyName <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DhcpServerv4OptionValue` cmdlet 可以在服务器、作用域或预留级别上删除一个或多个 IPv4 选项值，这些选项值既可以适用于标准的 IPv4 选项，也可以适用于指定的供应商或用户类别。

如果您只指定了 *ReservedIP* 参数，那么在预留级别设置的选项值将被删除；如果您只指定了 *ScopeId* 参数，那么在范围级别设置的选项值将被删除；如果您既没有指定 *ScopeId* 也没有指定 *ReservedIP* 参数，那么在服务器级别设置的选项值将被删除。*ScopeId* 和 *ReservedIP* 这两个参数不能同时被指定。

不能同时指定 *UserClass* 和 *PolicyName* 参数。

## 示例

### 示例 1：删除某个作用域内的选项值
```
PS C:\> Remove-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -OptionId 23
```

这个示例会删除在指定范围内为指定的选项ID配置的DHCPv4选项值。

### 示例 2：删除供应商类别的一个选项值
```
PS C:\> Remove-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -VendorClass "MSUCClient" -OptionId 5
```

这个示例会删除在指定范围内为名为“MSUCClient”的供应商类别配置的DHCPv4选项值。该选项使用的是特定的编号（选项5）。

#### 示例 3：通过使用选项 ID 来删除一个选项值
```
PS C:\> Remove-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -PolicyName "SmartPhonePolicy" -OptionId 252
```

这个示例会删除在范围 10.10.10.0 内为指定策略配置的、选项 ID 为 252 的 DHCPv4 选项值。

### 示例 4：删除某个作用域内用户类的选项值
```
PS C:\> Remove-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -UserClass "LabComputer" -OptionId 252
```

这个示例会删除在范围 10.10.10.0 内为指定用户类配置的、选项 ID 为 252 的 DHCPv4 选项值。

### 示例 5：在服务器端删除一个选项值
```
PS C:\> Remove-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -OptionId 23
```

这个示例会删除在服务器级别或整个服务器范围内为指定的选项ID配置的DHCPv4选项值。

### 示例 6：在服务器级别删除某个供应商类的选项值
```
PS C:\> Remove-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -VendorClass "MSUCClient" -OptionId 5
```

这个示例会删除在服务器级别或整个服务器范围内为指定的供应商类别（名为MSUCClient）配置的DHCPv4选项值。该供应商类别使用了特定的选项5。

### 示例 7：通过使用选项 ID 在服务器级别删除一个选项值
```
PS C:\> Remove-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -PolicyName "SmartPhonePolicy" -OptionId 252
```

这个示例会删除在服务器级别或整个服务器范围内为指定策略配置的、选项ID为252的DHCPv4选项值。

### 示例 8：通过使用用户类的选项ID来删除一个选项值
```
PS C:\> Remove-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -UserClass "LabComputer" -OptionId 252
```

这个示例会删除在服务器级别或整个服务器范围内为指定用户类别配置的、选项ID为252的DHCPv4选项值。

### 示例 9：删除预订中的选项值
```
PS C:\> Remove-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ReservedIP 10.10.10.5 -OptionId 23
```

此示例会删除在指定预留资源上为指定的选项ID配置的DHCPv4选项值。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定运行动态主机配置协议（DHCP）服务器服务的目标计算机的DNS名称，或IPv4地址或IPv6地址。

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
在运行该cmdlet之前，会提示您确认是否要继续执行。

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
指定一个或多个用于标识要删除的选项的数字标识符（ID）。

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

### -PolicyName
指定要从中删除选项值的策略的名称。

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

### -ReservedIP
指定用于删除选项值的预留资源的 IPv4 地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases: IPAddress

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScopeId
指定删除选项值的范围ID（采用IPv4地址格式）。

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
该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略此参数或输入值为`0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算该命令的最佳限制值。这个限制仅适用于当前执行的命令，而不涉及整个会话或计算机本身。

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

### -UserClass
指定删除指定用户类的选项值。

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

### -VendorClass
指定删除指定供应商类别的选项值。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4OptionValue
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于展示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4OptionValue[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于展示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerv4OptionValue](./Get-DhcpServerv4OptionValue.md)

[Set-DhcpServerv4OptionValue](./Set-DhcpServerv4OptionValue.md)

