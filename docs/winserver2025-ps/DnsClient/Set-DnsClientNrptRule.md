---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsClientNRPTRule_v1.0.0.cdxml-help.xml
Module Name: DnsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsclient/set-dnsclientnrptrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsClientNrptRule
---

# Set-DnsClientNrptRule

## 摘要
修改指定命名空间的DNS客户端名称解析策略表（NRPT）规则。

## 语法

```
Set-DnsClientNrptRule [-DAEnable <Boolean>] [-DAIPsecEncryptionType <String>] [-DAIPsecRequired <Boolean>]
 [-DANameServers <String[]>] [-DAProxyServerName <String>] [-DAProxyType <String>] [-Comment <String>]
 [-DnsSecEnable <Boolean>] [-DnsSecIPsecEncryptionType <String>] [-DnsSecIPsecRequired <Boolean>]
 [-DnsSecValidationRequired <Boolean>] [-GpoName <String>] [-IPsecTrustAuthority <String>] [-Name] <String>
 [-NameEncoding <String>] [-NameServers <String[]>] [-Namespace <String[]>] [-Server <String>]
 [-DisplayName <String>] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsClientNrptRule` cmdlet 用于修改指定的 DNS 客户端名称解析策略表（Name Resolution Policy Table，简称 NRPT）规则。

## 示例

### 示例 1：修改 NRPT 规则
```
PS C:\> Set-DnsClientNrptRule  -DAEnable $True -DAIPsecEncryptionType "High" -DAIPsecRequired $True -DANameServers "10.0.0.1" -DAProxyServerName "DaServer.com:6666" -DAProxyType "UseProxyName" -DisplayName "Sample" -PassThru -IPsecTrustAuthority "RootCA" -Name "{1326d9d0-4fb5-4fed-9f67-f53637b85010}" -NameEncoding "Punycode" -NameServers "10.0.0.1" -Namespace "dnsnrpt.com" -Server "host1.com" -Comment "Sample NRPT Rule" -DnsSecEnable $True -DnsSecIPsecEncryptionType "Medium" -DnsSecIPsecRequired $True -DnsSecValidationRequired $True -GpoName "TestGPO"
```

这个示例修改了位于 host1.com 服务器上的名为 TestGPO 的组策略对象（GPO）中的 NRPT 规则，该组策略对象应用于 dnsnrpt.com 域名。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在当前会话中执行其他操作。要管理这个作业，请使用`*-Job`系列的cmdlets；要获取作业的结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -Comment
存储管理员的评论。

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

### -Confirm
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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

### -DAEnable
表示DirectAccess（DA）的规则状态。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: DirectAccessEnabled

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DAIPsecEncryptionType
指定用于数据访问（DA）的IPsec加密类型。该参数的可接受值为：

- None
- Low
- Medium
- High

```yaml
Type: String
Parameter Sets: (All)
Aliases: DirectAccessQueryIPSSECEncryption
Accepted values: , None, Low, Medium, High

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DAIPsecRequired
Indicates whether IPsec is required.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: DirectAccessQueryIPsecRequired

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DANameServers
Specifies the DNS servers which will be queried when DA is enabled.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: DirectAccessDNSServers

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DAProxyServerName
Specifies the proxy server to be used when connecting to the Internet.

This parameter is only applicable when the *DAProxyType* parameter is set to UseProxyName.

```yaml
Type: String
Parameter Sets: (All)
Aliases: DirectAccessProxyName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DAProxyType
Specifies the proxy server type to be used when connecting to the Internet.
The acceptable values for this parameter are:

- NoProxy
- UseDefault
- UseProxyName

```yaml
Type: String
Parameter Sets: (All)
Aliases: DirectAccessProxyType
Accepted values: , NoProxy, UseDefault, UseProxyName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DisplayName
Specifies an optional friendly name for the NRPT rule.

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

### -DnsSecEnable
Indicates whether DNSSEC is enabled on the rule.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: DnsSecEnabled

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DnsSecIPsecEncryptionType
Specifies the IPsec tunnel encryption settings.
The acceptable values for this parameter are:

- None
- Low
- Medium
- High

```yaml
Type: String
Parameter Sets: (All)
Aliases: DnsSecQueryIPsecEncryption
Accepted values: , None, Low, Medium, High

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DnsSecIPsecRequired
Indicates that the DNS client must set up an IPsec connection to the DNS server.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: DnsSecQueryIPsecRequired

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DnsSecValidationRequired
Indicates that DNSSEC validation is required.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GpoName
Specifies the name of the Group Policy Object (GPO).

- If this parameter and the *Server* parameter are specified, then the NRPT rule is added in the GPO of domain.
The *Server* parameter specifies the domain controller (DC).
- If neither this parameter nor the *Server* parameter is specified, then the NRPT rule is added for local client computer.
- If this parameter is specified and the *Server* parameter is not specified, then the DC of the domain specified by this parameter value is found and NRPT rule is added to the GPO.
- If this parameter is not specified and the *Server* parameter is specified, then an error is displayed.

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

### -IPsecTrustAuthority
Specifies the Certification Authority (CA) to validate the IPsec channel for DA.

```yaml
Type: String
Parameter Sets: (All)
Aliases: IPsecCARestriction

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
Specifies the name which uniquely identifies a rule.

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

### -NameEncoding
Specifies the encoding format for host names in the DNS query.
The acceptable values for this parameter are:

- Disable
- Utf8WithMapping
- Utf8WithoutMapping
- Punycode

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Disable, Utf8WithMapping, Utf8WithoutMapping, Punycode

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NameServers
Specifies the DNS servers to which the DNS query is sent when DA is disabled.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Namespace
Specifies the DNS namespace.
The acceptable values for this parameter are:

- Suffix
- Prefix
- FQDN
- Subnet
- Any

If this parameter is set to Any, then the parameter value must be specified in dot-notation.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

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

### -Server
Specifies the server hosting the GPO.
This parameter is only applicable with the *GpoName* parameter.

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
该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或整个计算机。

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
展示了如果该 cmdlet 被运行时会发生什么情况。但实际上，这个 cmdlet 并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsClientNrptRule
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名称。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsClientNrptRule
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名称。

`DnsClientNrptRule` 对象包含了 DNS 客户端 NRPT 规则的所有属性。

## 备注

## 相关链接

[Add-DnsClientNrptRule](./Add-DnsClientNrptRule.md)

[Get-DnsClientNrptGlobal](./Get-DnsClientNrptGlobal.md)

[Get-DnsClientNrptPolicy](./Get-DnsClientNrptPolicy.md)

[Get-DnsClientNrptRule](./Get-DnsClientNrptRule.md)

[Remove-DnsClientNrptRule](./Remove-DnsClientNrptRule.md)

[Set-DnsClientNrptGlobal](./Set-DnsClientNrptGlobal.md)

