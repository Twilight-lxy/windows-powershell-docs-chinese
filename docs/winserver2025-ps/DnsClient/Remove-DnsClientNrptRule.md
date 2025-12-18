---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsClientNRPTRule_v1.0.0.cdxml-help.xml
Module Name: DnsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsclient/remove-dnsclientnrptrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DnsClientNrptRule
---

# 删除 DNS 客户端 Nrpt 规则

## 摘要
删除指定的DNS客户端NRPT规则。

## 语法

```
Remove-DnsClientNrptRule [-GpoName <String>] [-Name] <String> [-PassThru] [-Server <String>] [-Force]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DnsClientNrptRule` cmdlet 用于删除指定的 DNS 客户端名称解析策略表（NRPT）规则。

## 示例

### 示例 1：从指定的服务器中删除一个 NRPT 规则
```
PS C:\> Remove-DnsClientNrptRule -GpoName "TestGPO" -Name "{1326d9d0-4fb5-4fed-9f67-f53637b85010}" -PassThru -Server "host1.com" -Force
```

这个示例会从名为host1.com的服务器上删除名为{1326d9d0-4fb5-4fed-9f67-f53637b85010}的NRPT规则。

### 示例 2：删除一个 NRPT 规则
```
PS C:\> Remove-DnsClientNrptRule -Name "DA-{274D94E4-E38B-4997-BA9F-84700712C09E}" -PassThru

Confirm
Removing NRPT rule for the namespace nls.corp.contoso.com with
 DAEnable: Enable,
 DnsSecValidationRequired: Disabled,
 NameEncoding: Disable
 NameServers: No
 Do you want to continue?
 [Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y

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

This version of the cmdlet performs the task without user confirmation.
PS C:\> Remove-DnsClientNrptRule -Name "DA-{274D94E4-E38B-4997-BA9F-84700712C09E}" -PassThru -Force

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

这个示例删除了名为 {1326d9d0-4fb5-4fed-9f67-f53637b85010} 的 NRPT 规则。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业的结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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

### -Force
强制命令运行，而无需请求用户确认。

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
指定用于唯一标识某条规则的名称。

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

### -Server
指定包含该组策略对象（GPO）的服务器名称。此参数仅与 *GpoName* 参数配合使用。

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
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsClientNrptRule
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows Management Instrumentation (WMI) 对象。井号（`#`）之后的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsClientNrptRule
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows Management Instrumentation (WMI) 对象。井号（`#`）之后的路径表示底层 WMI 对象的命名空间和类名。


`DnsClientNrptRule` 对象包含了 DNS 客户端 NRPT 规则的所有属性。

## 备注

## 相关链接

[Add-DnsClientNrptRule](./Add-DnsClientNrptRule.md)

[Get-DnsClientNrptGlobal](./Get-DnsClientNrptGlobal.md)

[Get-DnsClientNrptPolicy](./Get-DnsClientNrptPolicy.md)

[Get-DnsClientNrptRule](./Get-DnsClientNrptRule.md)

[Set-DnsClientNrptGlobal](./Set-DnsClientNrptGlobal.md)

[Set-DnsClientNrptRule](./Set-DnsClientNrptRule.md)

