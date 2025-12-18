---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsClientNRPTRule_v1.0.0.cdxml-help.xml
Module Name: DnsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsclient/add-dnsclientnrptrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsClientNrptRule
---

# Add-DnsClientNrptRule

## 摘要
向NRPT中添加一条规则。

## 语法

```
Add-DnsClientNrptRule [-GpoName <String>] [-DANameServers <String[]>] [-DAIPsecRequired]
 [-DAIPsecEncryptionType <String>] [-DAProxyServerName <String>] [-DnsSecEnable] [-DnsSecIPsecRequired]
 [-DnsSecIPsecEncryptionType <String>] [-NameServers <String[]>] [-NameEncoding <String>]
 [-Namespace] <String[]> [-Server <String>] [-DAProxyType <String>] [-DnsSecValidationRequired] [-DAEnable]
 [-IPsecTrustAuthority <String>] [-Comment <String>] [-DisplayName <String>] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DnsClientNrptRule` cmdlet 为指定的命名空间添加一条名称解析策略表（Name Resolution Policy Table，简称 NRPT）规则。

## 示例

#### 示例 1：将 NRPT 规则添加到 GPO 中
```
PS C:\> Add-DnsClientNrptRule -GpoName "TestGPO" -DANameServers "10.0.0.1" -DAIPsecRequired -DAIPsecEncryptionType "High" -DAProxyServerName "DaServer.com:6666" -DnsSecEnable -PassThru -DAProxyType "UseProxyName" -DnsSecValidationRequired -DAEnable -IPsecTrustAuthority "RootCA" -Comment "Sample NRPT Rule" -DisplayName "Sample" -DnsSecIPsecRequired -DnsSecIPsecEncryptionType "Medium" -NameServers "10.0.0.1" -NameEncoding "Punycode" -Namespace "dnsnrpt.com" -Server "host1.com"
```

此命令在服务器host1.com上的TestGPO中为命名空间dnsnrpt.com添加一条NRPT规则。

### 示例 2：添加一条 NRPT 规则来配置服务器
```
PS C:\> Add-DnsClientNrptRule -Namespace "pqr.com" -NameServers "10.0.0.1"
```

此命令添加了一条NRPT规则，用于将名为10.0.0.1的服务器配置为域名pqr.com的DNS服务器。

### 示例 3：添加一条 NRPT 规则以启用 DNSSEC 查询
```
PS C:\> Add-DnsClientNrptRule -Namespace "pqr.com" -DnsSecEnable
```

此命令添加了一条 NRPT 规则，使得可以为域名 pqr.com 发送 DNSSEC 查询。

#### 示例 4：添加一条 NRPT 规则，以允许对指定的命名空间执行 DNSSEC 查询
```
PS C:\> Add-DnsClientNrptRule -Namespace "pqr.com" -DnsSecEnable -NameServers "10.0.0.1"
```

此命令添加了一条NRPT规则，允许针对命名空间pqr.com的DNSSEC查询发送到名为10.0.0.1的DNS服务器。

### 示例 5：添加一条 NRPT 规则以发送 Punycode 格式的 DNS 查询
```
PS C:\> Add-DnsClientNrptRule -Namespace "pqr.com" -NameEncoding "Punycode" -NameServers "10.1.1.1" -PassThru

Name                             : {6a78d8d1-231d-4d1e-bc23-fb593e11a53d}
Version                          : 2
Namespace                        : {pqr.com}
IPsecCARestriction               :
DirectAccessDnsServers           :
DirectAccessEnabled              : False
DirectAccessProxyType            :
DirectAccessProxyName            :
DirectAccessQueryIPsecEncryption :
DirectAccessQueryIPsecRequired   :
NameServers                      : 10.1.1.1
DnsSecEnabled                    : False
DnsSecQueryIPsecEncryption       :
DnsSecQueryIPsecRequired         :
DnsSecValidationRequired         :
NameEncoding                     : Punycode
DisplayName                      :
Comment                          :
```

此命令添加了一条NRPT规则，用于将使用Punycode编码的DNS查询发送到名为10.1.1.1的DNS服务器，以查询名为pqr.com的命名空间。

## 参数

### -AsJob
以后台作业的形式运行该 cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业的结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
用于存储管理员的备注信息。

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

### -DAEnable
表示 DirectAccess 的规则状态。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: DirectAccessEnabled

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DAIPsecEncryptionType
指定 DirectAccess 的互联网协议安全（IPsec）加密设置。该参数的可接受值为：

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
Indicates that IPsec is required for DirectAccess.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: DirectAccessQueryIPsecRequired

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DANameServers
Specifies an array of DNS servers to query when DirectAccess is enabled.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: DirectAccessDnsServers

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DAProxyServerName
Specifies the proxy server to use when connecting to the Internet.
This parameter is only applicable if the *DAProxyType* parameter is set to UseProxyName.

Acceptable formats are:

- hostname:port
- IPv4 address:port
- IPv6 address:port

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
Enables Domain Name System Security Extensions (DNSSEC) on the rule.

```yaml
Type: SwitchParameter
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
Indicates the DNS client must set up an IPsec connection to the DNS server.

```yaml
Type: SwitchParameter
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
Type: SwitchParameter
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
Specifies the certification authority to validate the IPsec channel.

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
Specifies the DNS servers to which the DNS query is sent when DirectAccess is disabled.

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

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
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
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet被运行会会发生什么情况。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsClientNrptRule
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsClientNrptRule
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

`DnsClientNrptRule`对象包含了DNS客户端NRPT规则的所有属性。

## 备注

## 相关链接

[Get-DnsClientNrptGlobal](./Get-DnsClientNrptGlobal.md)

[Get-DnsClientNrptPolicy](./Get-DnsClientNrptPolicy.md)

[Get-DnsClientNrptRule](./Get-DnsClientNrptRule.md)

[Remove-DnsClientNrptRule](./Remove-DnsClientNrptRule.md)

[Set-DnsClientNrptGlobal](./Set-DnsClientNrptGlobal.md)

[Set-DnsClientNrptRule](./Set-DnsClientNrptRule.md)

