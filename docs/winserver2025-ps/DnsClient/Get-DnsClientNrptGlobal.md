---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsClientNRPTGlobal_v1.0.0.cdxml-help.xml
Module Name: DnsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsclient/get-dnsclientnrptglobal?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsClientNrptGlobal
---

# Get-DnsClientNrptGlobal

## 摘要
获取NRPT全局设置。

## 语法

```
Get-DnsClientNrptGlobal [-Server <String>] [-GpoName <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsClientNrptGlobal` cmdlet 可以获取以下名称解析策略表（NRPT）的相关详细信息：

- DirectAccess (DA) settings.
- DNS client query policy.
- DNS client name resolution fallback policy.

## 示例

#### 示例 1：获取全局 NRPT 设置
```
PS C:\> Get-DnsClientNrptGlobal

EnableDAForAllNetworks                  QueryPolicy                             SecureNameQueryFallback
----------------------                  -----------                             -----------------------
Disable                                 Disable                                 Disable
```

这个示例用于检索全局的NRPT设置。

### 示例 2：获取与 GPO 相关联的全局 NRPT 设置
```
PS C:\> Get-DnsClientNrptGlobal -GpoName "corp.contoso.com\DirectAccess Client Settings"
```

此示例用于检索与 corp.contoso.com 关联的名为“DirectAccess Client Settings”的 GPO（组策略对象）所配置的全局 NRPT（网络注册表协议）设置。

### 示例 3：获取指定 GPO 和服务器的全局 NRTP 设置
```
PS C:\> Get-DnsClientNrptGlobal -GpoName "corp.contoso.com\DirectAccess Client Settings" -Server "dc1"
```

这个示例用于检索名为“DirectAccess Client Settings”的GPO的全局NRPT设置。该GPO链接到了服务器dc1上的corp.contoso.com。

### 示例 4：获取指定 CIM 会话的全局 NRPT 设置
```
PS C:\> Get-DnsClientNrptGlobal -GpoName "corp.contoso.com\DirectAccess Client Settings" -CimSession 2-dc1.corp2.corp.contoso.com
```

这个示例用于检索名为“DirectAccess Client Settings”的GPO的全局NRPT设置。该GPO链接到了corp.contoso.com，并应用于名为2-dc1.corp2.corp.contoso.com的远程计算机上。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在该作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定组策略对象（GPO）的名称。如果未指定此参数，则会获取默认的NRPT设置。

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

### -Server
指定托管该组策略对象（GPO）的服务器。此参数仅与 *GpoName* 参数一起使用时才有效。

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
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIMcmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsClientNrptGlobal
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

`DnsClientNrptGlobal` 对象包含了 DNS 客户端 NRPT（Name Resolution Protocol Translation）全局设置的所有属性。

## 备注

## 相关链接

[Add-DnsClientNrptRule](./Add-DnsClientNrptRule.md)

[Get-DnsClientNrptPolicy](./Get-DnsClientNrptPolicy.md)

[Get-DnsClientNrptRule](./Get-DnsClientNrptRule.md)

[Remove-DnsClientNrptRule](./Remove-DnsClientNrptRule.md)

[Set-DnsClientNrptGlobal](./Set-DnsClientNrptGlobal.md)

[Set-DnsClientNrptRule](./Set-DnsClientNrptRule.md)

