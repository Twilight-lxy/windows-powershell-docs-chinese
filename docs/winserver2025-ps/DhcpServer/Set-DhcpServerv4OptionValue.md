---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4OptionValue_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/set-dhcpserverv4optionvalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DhcpServerv4OptionValue
---

# Set-DhcpServerv4OptionValue

## 摘要
在服务器、范围或预留级别设置一个IPv4选项值。

## 语法

### OptionIds（默认值）
```
Set-DhcpServerv4OptionValue [-PolicyName <String>] [-PassThru] [-Force] [-ReservedIP <IPAddress>]
 [[-ScopeId] <IPAddress>] [-UserClass <String>] [-ComputerName <String>] [-VendorClass <String>]
 [-Value] <String[]> [-OptionId] <UInt32> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### CommonOptions
```
Set-DhcpServerv4OptionValue [-PolicyName <String>] [-PassThru] [-Force] [-DnsDomain <String>]
 [-DnsServer <IPAddress[]>] [-ReservedIP <IPAddress>] [-Router <IPAddress[]>] [[-ScopeId] <IPAddress>]
 [-UserClass <String>] [-WinsServer <IPAddress[]>] [-Wpad <String>] [-ComputerName <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DhcpServerv4OptionValue` cmdlet 可以在服务器、作用域或预留级别设置 IPv4 选项的值。该选项的定义必须已经存在。如果动态主机配置协议（DHCP）服务器服务中不存在该选项的定义，此 cmdlet 将会失败。

如果您只指定了*ReservedIP*参数，那么选项值将在预留级别进行设置；如果您只指定了*ScopeId*参数，那么选项值将在范围级别进行设置。

如果您既没有指定 *ScopeId* 参数，也没有指定 *ReservedIP* 参数，那么这些选项的值将在服务器层面进行设置。如果您指定了 *VendorClass* 参数，那么该选项的值将会针对所指定的供应商类别进行设置。

如果您指定了 *UserClass* 参数，那么该选项的值就会设置为对应的用户类。

如果您指定了 *PolicyName* 参数，那么该参数对应的选项值将被设置。*UserClass* 和 *PolicyName* 这两个参数不能同时被指定。同理，*ScopeId* 和 *ReservedIP* 这两个参数也不能同时被指定。

*PolicyName* 和 *ReservedIP* 参数不能同时被指定。

策略的选项值仅能用于在 Windows Server® 2012 及更高版本的 Windows 操作系统上运行的 DHCP 服务器服务。为在 Windows Server 2012 及更高版本上运行的 DHCP 服务器服务设置用户类选项时，会生成一个策略，该策略的名称将与所设置的用户类名称相同。而对于在 firstref_server_7 或更低版本上运行的 DHCP 服务器服务，只能设置基于用户类的选项值。

要基于传统的用户类别来设置选项，必须指定 *UserClass* 参数。

## 示例

### 示例 1：设置服务器级别的选项值
```
PS C:\> Set-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -DnsServer 192.168.1.2 -WinsServer 192.168.1.3 -DnsDomain "contoso.com" -Router 192.168.1.1 -Wpad "http://proxy.contoso.com/wpad.dat"
```

这个示例设置了服务器级别的选项值，包括DNS服务器、WINS服务器、DNS域、路由器和WPAD的相关配置。

### 示例 2：为某个范围设置选项值
```
PS C:\> Set-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -DnsServer 192.168.1.2 -WinsServer 192.168.1.3 -DnsDomain "contoso.com" -Router 192.168.1.1 -Wpad "http://proxy.contoso.com/wpad.dat"
```

这个示例为作用域 10.10.10.0 设置了 DNS 服务器、WINS 服务器、DNS 域名、路由器和 WPAD 的相关选项值。

### 示例 3：为地址设置选项值
```
PS C:\> Set-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ReservedIP 10.10.10.5 -DnsServer 192.168.1.2 -WinsServer 192.168.1.3 -DnsDomain "contoso.com" -Router 192.168.1.1 -Wpad "http://proxy.contoso.com/wpad.dat"
```

这个示例为保留的IP地址10.10.10.5设置了DNS服务器、WINS服务器、DNS域名、路由器以及WPAD的相关选项值。

### 示例 4：为策略设置选项值
```
PS C:\> Set-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -PolicyName "LabComputers" -DnsServer 192.168.1.2 -WinsServer 192.168.1.3 -DnsDomain "contoso.com" -Router 192.168.1.1 -Wpad "http://proxy.contoso.com/wpad.dat"
```

这个示例为名为“LabComputers”的策略设置了DNS服务器、WINS服务器、DNS域名、路由器和WPAD的选项值，该策略的作用域是10.10.10.0。

### 示例 5：为 DNS 服务器设置全服务范围内的选项值
```
PS C:\> Set-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -OptionId 6 -Value "192.168.1.1"
```

这个示例为服务器范围内的DHCPv4选项设置了选项ID为6（即DNS服务器）的选项值。

### 示例 6：为某个作用域设置 DNS 服务器的选项值
```
PS C:\> Set-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -OptionId 6 -Value "192.168.1.1"
```

这个示例为范围 10.10.10.0 设置了 DHCPv4 选项的值，该选项的 ID 为 6，对应的选项是 DNS 服务器。

### 示例 7：为预订设置 DNS 服务器的选项值
```
PS C:\> Set-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ReservedIP 10.10.10.5 -OptionId 6 -Value "192.168.1.1"
```

这个示例为指定的预留资源设置了DHCPv4选项的值，该选项的ID为6（即DNS服务器）。

### 示例 8：设置特定于供应商类的选项值
```
PS C:\> Set-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -VendorClass "MSUCClient" -OptionId 5 -Value ([System.Text.Encoding]::ASCII.GetBytes("/CertProv/CertProvisioningService.svc"))
```

这个示例为名为 MSUCClient 的指定供应商类，在指定的作用域内，设置了供应商类别特定的 DHCPv4 选项值（选项 ID 为 5）。

### 示例 9：为策略设置 DNS 服务器的选项值
```
PS C:\> Set-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -PolicyName "PrinterPolicy" -OptionId 6 -Value "192.168.1.10"
```

这个示例为指定的策略，在指定的作用域内，设置了 DHCPv4 选项的值（对应于选项 ID 6，即 DNS 服务器）。

### 示例 10：为 DNS 服务器设置特定于用户类的选项值
```
PS C:\> Set-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -UserClass "LabComputer" -OptionId 6 -Value "192.168.1.10"
```

这个示例为指定的用户类，在指定的作用域内，设置与用户类别相关的DHCPv4选项值（即选项ID为6的选项，该选项用于配置DNS服务器）。

### 示例 11：为某个作用域设置特定于供应商类的选项值
```
PS C:\> Set-DhcpServerv4OptionValue -ScopeId 10.10.10.0 -OptionId 43 -Value "241","08","33","255","132","10","33","255","133"
```

这个示例为指定的作用域设置了供应商类特定的DHCPv4选项值（选项ID为43），即那些嵌入的、与特定供应商相关的选项。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定运行DHCP服务器服务的目标计算机的DNS名称，或IPv4或IPv6地址。

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

### -DnsDomain
指定DNS域名选项的值。

```yaml
Type: String
Parameter Sets: CommonOptions
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DnsServer
为DNS服务器选项指定一个或多个值，这些值采用IPv4地址格式表示。

```yaml
Type: IPAddress[]
Parameter Sets: CommonOptions
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Force
指定跳过DNS服务器验证步骤。此参数仅在指定了*DnsServer*参数的情况下才适用。

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

### -OptionId
指定某个选项的数值标识符（ID），该选项已设置了一个或多个值。

```yaml
Type: UInt32
Parameter Sets: OptionIds
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
指定要为其设置一个或多个选项值的策略的名称。

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
指定已设置一个或多个选项值的预留资源的IPv4地址。

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

### -Router
为“路由器”或“默认网关”选项指定一个或多个值，这些值需采用 IPv4 地址格式表示。

```yaml
Type: IPAddress[]
Parameter Sets: CommonOptions
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScopeId
指定一个范围ID（采用IPv4地址格式），为一个或多个选项值设置相应的值。

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
指定可以同时运行的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机。

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
为指定的用户类别设置选项值。

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

### -Value
指定一个或多个要为该选项设置的值。使用以下格式：

- Byte, Word, DWord, DWordDword.
Specify as decimal or hexadecimal strings.
- IPAddress, IPv6Address.
Specify as strings.
- String.
Specify as strings.
- BinaryData, EncapsulatedData.
Specify as hexadecimal strings.

```yaml
Type: String[]
Parameter Sets: OptionIds
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VendorClass
为指定的供应商类别设置选项值。

```yaml
Type: String
Parameter Sets: OptionIds
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

### -WinsServer
指定 WINS 服务器选项的值，采用 IPv4 地址格式。

```yaml
Type: IPAddress[]
Parameter Sets: CommonOptions
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Wpad
用于指定网页代理自动检测选项的值。该选项的值以URL的形式进行设置。

```yaml
Type: String
Parameter Sets: CommonOptions
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4OptionDefinition
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4OptionValue
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4OptionValue
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerv4OptionValue](./Get-DhcpServerv4OptionValue.md)

[Remove-DhcpServerv4OptionValue](./Remove-DhcpServerv4OptionValue.md)

