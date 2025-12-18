---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsClientNrptPolicy_v1.0.0.cdxml-help.xml
Module Name: DnsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsclient/get-dnsclientnrptpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsClientNrptPolicy
---

# Get-DnsClientNrptPolicy

## 摘要
获取计算机上配置的NRPT信息。

## 语法

```
Get-DnsClientNrptPolicy [-Effective] [[-Namespace] <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsClientNrptPolicy` cmdlet 为每个命名空间获取以下名称解析策略表（NRPT）的详细信息。

- DNS client name resolution fallback policy.
- DNS client secure name query fallback setting.
- Direct Access (DA) IPsec Certification Authority (CA) restriction setting.
- DA proxy name setting.
- DA DNS servers setting.
- DA enabled setting.
- DA proxy type setting.
- DA Query IPsec encryption setting.
- DA Query IPsec required setting.
- DNS client name servers setting.
- DNS security IPsec CA restriction setting.
- DNS security query IPsec encryption setting.
- DNS security query IPsec required setting.
- DNS security validation required setting.
- DNS client name encoding setting.

## 示例

### 示例 1：获取 NRPT 策略
```
PS C:\> Get-DnsClientNrptPolicy

Namespace                        : nls.corp.contoso.com
QueryPolicy                      :
SecureNameQueryFallback          :
DirectAccessIPsecCARestriction   :
DirectAccessProxyName            :
DirectAccessDnsServers           :
DirectAccessEnabled              :
DirectAccessProxyType            : UseDefault
DirectAccessQueryIPsecEncryption :
DirectAccessQueryIPsecRequired   : False
NameServers                      :
DnsSecIPsecCARestriction         :
DnsSecQueryIPsecEncryption       :
DnsSecQueryIPsecRequired         : False
DnsSecValidationRequired         : False
NameEncoding                     : Utf8WithoutMapping

Namespace                        : .corp.contoso.com
QueryPolicy                      :
SecureNameQueryFallback          :
DirectAccessIPsecCARestriction   :
DirectAccessProxyName            :
DirectAccessDnsServers           : {2001:db8:1::2, 2001:db8:2::20,
                                   2001:db8:6::6}
DirectAccessEnabled              :
DirectAccessProxyType            : NoProxy
DirectAccessQueryIPsecEncryption :
DirectAccessQueryIPsecRequired   : False
NameServers                      :
DnsSecIPsecCARestriction         :
DnsSecQueryIPsecEncryption       :
DnsSecQueryIPsecRequired         : False
DnsSecValidationRequired         : False
NameEncoding                     : Utf8WithoutMapping
```

这个示例用于获取计算机上的NRPT策略。

### 示例 2：获取有效的 NRPT 策略
```
PS C:\> Get-DnsClientNrptPolicy -Effective

Namespace                        : nls.corp.contoso.com
QueryPolicy                      : QueryIPv6Only
SecureNameQueryFallback          : FallbackPrivate
DirectAccessIPsecCARestriction   :
DirectAccessProxyName            :
DirectAccessDnsServers           :
DirectAccessEnabled              : True
DirectAccessProxyType            : UseDefault
DirectAccessQueryIPsecEncryption :
DirectAccessQueryIPsecRequired   : False
NameServers                      :
DnsSecIPsecCARestriction         :
DnsSecQueryIPsecEncryption       :
DnsSecQueryIPsecRequired         :
DnsSecValidationRequired         :
NameEncoding                     :

Namespace                        : .corp.contoso.com
QueryPolicy                      : QueryIPv6Only
SecureNameQueryFallback          : FallbackPrivate
DirectAccessIPsecCARestriction   :
DirectAccessProxyName            :
DirectAccessDnsServers           : {2001:db8:1::2, 2001:db8:2::20,
                                   2001:db8:6::6}
DirectAccessEnabled              : True
DirectAccessProxyType            : NoProxy
DirectAccessQueryIPsecEncryption :
DirectAccessQueryIPsecRequired   : False
NameServers                      :
DnsSecIPsecCARestriction         :
DnsSecQueryIPsecEncryption       :
DnsSecQueryIPsecRequired         :
DnsSecValidationRequired         :
NameEncoding                     :
```

这个示例用于获取计算机上有效的NRPT（Network Resource Protection Table）策略。

### 示例 3：获取指定命名空间的有效 NRPT 策略
```
PS C:\> Get-DnsClientNrptPolicy -Effective -Namespace "nls.corp.contoso.com"

Namespace                        : nls.corp.contoso.com
QueryPolicy                      : QueryIPv6Only
SecureNameQueryFallback          : FallbackPrivate
DirectAccessIPsecCARestriction   :
DirectAccessProxyName            :
DirectAccessDnsServers           :
DirectAccessEnabled              : True
DirectAccessProxyType            : UseDefault
DirectAccessQueryIPsecEncryption :
DirectAccessQueryIPsecRequired   : False
NameServers                      :
DnsSecIPsecCARestriction         :
DnsSecQueryIPsecEncryption       :
DnsSecQueryIPsecRequired         :
DnsSecValidationRequired         :
NameEncoding                     :
```

这个示例为命名空间 nls.corp.contoso.com 获取了一个有效的 NRPT（Network Routing Policy）策略。

## 参数

### -AsJob
以后台作业的形式运行该 cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后会显示命令提示符。在该作业完成之前，您可以继续在当前会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Effective
表示返回了有效的NRPT策略。

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

### -Namespace
指定用于获取策略的 DNS 命名空间。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsClientPolicyConfiguration[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

`DnsClientPolicyConfiguration` 对象包含了 DNS 客户端 NRPT（Name Resolution Protocol Translation）策略的所有属性。如果指定了 `Effective` 参数，那么只会检索有效策略的内容。

## 备注

## 相关链接

[Add-DnsClientNrptRule](./Add-DnsClientNrptRule.md)

[Get-DnsClientNrptGlobal](./Get-DnsClientNrptGlobal.md)

[Get-DnsClientNrptPolicy](./Get-DnsClientNrptPolicy.md)

[Get-DnsClientNrptRule](./Get-DnsClientNrptRule.md)

[Remove-DnsClientNrptRule](./Remove-DnsClientNrptRule.md)

[Set-DnsClientNrptGlobal](./Set-DnsClientNrptGlobal.md)

[Set-DnsClientNrptRule](./Set-DnsClientNrptRule.md)

