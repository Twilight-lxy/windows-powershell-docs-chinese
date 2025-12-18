---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsClientNRPTRule_v1.0.0.cdxml-help.xml
Module Name: DnsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsclient/get-dnsclientnrptrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsClientNrptRule
---

# Get-DnsClientNrptRule

## 摘要
检索DNS客户端的相关NRPT规则。

## 语法

```
Get-DnsClientNrptRule [-GpoName <String>] [[-Name] <String[]>] [-Server <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsClientNrptRule` cmdlet 可以检索 DNS 客户端的名称解析策略表（Name Resolution Policy Table，简称 NRPT）规则，并提供以下详细信息：

- DNS client name setting.
- DNS client version setting.
- DNS client namespace setting.
- DNS client IPsec Certification Authority (CA) restriction setting.
- Direct Access (DA) DNS servers setting.
- DA enabled setting.
- DA proxy type setting.
- DA proxy name setting.
- DA query IPsec encryption setting.
- DA query IPsec required setting.
- DNS client name servers setting.
- DNS security enabled setting.
- DNS security query IPsec encryption setting.
- DNS security query IPsec required setting.
- DNS security validation required setting.
- DNS client name encoding setting.
- DNS client display name setting.
- DNS client comment setting.

## 示例

### 示例 1：获取指定 GPO 的 NRPT 规则
```
PS C:\> Get-DnsClientNrptRule -GpoName "corp.contoso.com\DirectAccess Client Settings"

Name                             : DA-{FD4B6054-F8C8-4868-94E6-8132AC707DBD}
Version                          : 1
Namespace                        : {.corp.contoso.com}
IPsecCARestriction               :
DirectAccessDnsServers           : {2001:db8:1::2, 2001:db8:2::20, 2001:db8:6::6}
DirectAccessEnabled              : True
DirectAccessProxyType            : NoProxy
DirectAccessProxyName            :
DirectAccessQueryIPsecEncryption :
DirectAccessQueryIPsecRequired   : False
NameServers                      :
DnsSecEnabled                    : False
DnsSecQueryIPsecEncryption       :
DnsSecQueryIPsecRequired         :
DnsSecValidationRequired         :
NameEncoding                     : Disable
DisplayName                      :
Comment                          :

Name                             : DA-{274D94E4-E38B-4997-BA9F-84700712C09E}
Version                          : 1
Namespace                        : {nls.corp.contoso.com}
IPsecCARestriction               :
DirectAccessDnsServers           :
DirectAccessEnabled              : True
DirectAccessProxyType            : UseDefault
DirectAccessProxyName            :
DirectAccessQueryIPsecEncryption :
DirectAccessQueryIPsecRequired   : False
NameServers                      :
DnsSecEnabled                    : False
DnsSecQueryIPsecEncryption       :
DnsSecQueryIPsecRequired         :
DnsSecValidationRequired         :
NameEncoding                     : Disable
DisplayName                      :
Comment                          :
```

此示例用于检索指定 GPO 的 NRPT 规则。

### 示例 2：获取指定服务器上的 NRPT 规则
```
PS C:\> Get-DnsClientNrptRule -GpoName "corp.contoso.com\DirectAccess Client Settings" -Server "dc1"

Name                             : DA-{FD4B6054-F8C8-4868-94E6-8132AC707DBD}
Version                          : 1
Namespace                        : {.corp.contoso.com}
IPsecCARestriction               :
DirectAccessDnsServers           : {2001:db8:1::2, 2001:db8:2::20, 2001:db8:6::6}
DirectAccessEnabled              : True
DirectAccessProxyType            : NoProxy
DirectAccessProxyName            :
DirectAccessQueryIPsecEncryption :
DirectAccessQueryIPsecRequired   : False
NameServers                      :
DnsSecEnabled                    : False
DnsSecQueryIPsecEncryption       :
DnsSecQueryIPsecRequired         :
DnsSecValidationRequired         :
NameEncoding                     : Disable
DisplayName                      :
Comment                          :

Name                             : DA-{274D94E4-E38B-4997-BA9F-84700712C09E}
Version                          : 1
Namespace                        : {nls.corp.contoso.com}
IPsecCARestriction               :
DirectAccessDnsServers           :
DirectAccessEnabled              : True
DirectAccessProxyType            : UseDefault
DirectAccessProxyName            :
DirectAccessQueryIPsecEncryption :
DirectAccessQueryIPsecRequired   : False
NameServers                      :
DnsSecEnabled                    : False
DnsSecQueryIPsecEncryption       :
DnsSecQueryIPsecRequired         :
DnsSecValidationRequired         :
NameEncoding                     : Disable
DisplayName                      :
Comment                          :
```

这个示例从指定的服务器上检索与指定GPO相关联的NRPT规则。

### 示例 3：从远程计算机获取 NRPT 规则
```
PS C:\> Get-DnsClientNrptRule -GpoName "corp.contoso.com\DirectAccess Client Settings" -CimSession 2-dc1.corp2.corp.contoso.com
```

这个示例用于从名为 2-dc1.corp2.corp.contoso.com 的远程计算机上检索 NRPT 规则。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -GpoName
指定组策略对象（GPO）的名称。

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

### -Name
指定用于唯一标识规则的名称。如果未指定此参数，则会检索所有可用的NRPT规则。

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

### -Server
指定托管组策略对象（GPO）的服务器。此参数仅与 *GpoName* 参数一起使用时有效。

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
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsClientNrptRule[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsClientNrptRule[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

`DnsClientNrptRule` 对象包含了 DNS 客户端 NRPT 规则的所有属性。

## 备注

## 相关链接

[Add-DnsClientNrptRule](./Add-DnsClientNrptRule.md)

[Get-DnsClientNrptGlobal](./Get-DnsClientNrptGlobal.md)

[Get-DnsClientNrptPolicy](./Get-DnsClientNrptPolicy.md)

[Remove-DnsClientNrptRule](./Remove-DnsClientNrptRule.md)

[Set-DnsClientNrptGlobal](./Set-DnsClientNrptGlobal.md)

[Set-DnsClientNrptRule](./Set-DnsClientNrptRule.md)

