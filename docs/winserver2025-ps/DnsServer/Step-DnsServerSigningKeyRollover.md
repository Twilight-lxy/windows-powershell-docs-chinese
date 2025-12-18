---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerSigningKeyRollover_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/step-dnsserversigningkeyrollover?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Step-DnsServerSigningKeyRollover
---

# Step-DnsServerSigningKeyRollover

## 摘要

它覆盖了一个正在等待父DS更新的KSK（Key Signing Key）。

## 语法

```
Step-DnsServerSigningKeyRollover [-ZoneName] <String> [-KeyId] <Guid> [-Force] [-PassThru]
 [-ComputerName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Step-DnsServerSigningKeyRollover` cmdlet 用于更新那些正在等待来自父级委托签名者（DS）更新的密钥签名键（KSK）。如果某个托管了安全委托区域的域名系统（DNS）服务器无法检查其父级记录是否已更新，可以使用此 cmdlet 强制执行密钥的更新操作。

重要提示：在运行此cmdlet之前，你必须手动更新父目录中的DS记录。

## 示例

#### 示例 1：强制进行密钥签名密钥的轮换

这个示例获取已签名区域的密钥信息，然后强制对该区域中某个密钥进行KSK（Key Signing Key）的轮换操作。

第一个命令使用了 **Get-DnsServerSigningKey** cmdlet 来获取已签名区域 Sec.Contoso.com 的相关密钥。

```powershell
Get-DnsServerSigningKey -ZoneName "Sec.Contoso.com"
```

```Output
KeyId                                  KeyType         CryptoAlgorithm    KeyLength  StoreKeysInAD   IsRolloverEnabled
-----                                  -------         ---------------    ---------  -------------   -----------------
5fe47b29-6bf8-457a-b457-e640893ebd53   KeySigningKey   RsaSha256          2048       True            True
aaf3301e-feb2-4ba7-8ac6-273c6bda75af   KeySigningKey   RsaSha1NSec3       2048       True            True
fbf3116f-b0ba-4bf8-bf35-68dab6d4765b   ZoneSigningKey  RsaSha1NSec3       1024       True            True
f760fcb5-577b-4237-b0b2-513e1f68ec72   ZoneSigningKey  RsaSha256          1024       True            True
```

```powershell
Step-DnsServerSigningKeyRollover -KeyId 5fe47b29-6bf8-457a-b457-e640893ebd53 -ZoneName "Sec.Contoso.com" -Force
```

最后一条命令会强制执行KSK（Key Signing Key）的更新过程，该过程正在等待Contoso.com上的父DS（Domain Controller）进行更新。这条命令会针对名为Sec.Contoso.com的区域中指定的密钥来执行KSK更新操作。

## 参数

### -AsJob

将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，随后再显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

指定一个远程DNS服务器。请提供该DNS服务器的IP地址，或者任何可以解析为IP地址的字符串，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

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

### -KeyId

指定要执行KSK轮换操作的密钥的ID。

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru

返回一个表示您正在操作的项目的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

展示了如果运行该cmdlet会发生什么情况。不过实际上并没有运行这个cmdlet。

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

### -ZoneName

指定该 cmdlet 执行 KSK 更换操作的 DNS 区域的名称。

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

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerSigningKey[]

输出对象包含以下字段：

- ActiveKey
- CryptoAlgorithm
- CurrentRolloverStatusCurrentState
- DnsKeySignatureValidityPeriod
- DSSignatureValidityPeriodInitialRolloverOffset
- KeyId
- KeyLengthKeyStorageProvider
- KeyType
- LastRolloverTime
- NextKey
- NextRolloverAction
- NextRolloverTime
- RolloverPeriod
- RolloverType
- StandbyKey
- StoreKeysInAD
- ZoneName
- ZoneSignatureValidityPeriod

## 备注

## 相关链接

[Enable-DnsServerSigningKeyRollover](./Enable-DnsServer SigningKeyRollover.md)

[Invoke-DnsServerSigningKeyRollover](./Invoke-DnsServerSigningKeyRollover.md)

[ Disable-DnsServerSigningKeyRollover](./Disable-DnsServerSigningKeyRollover.md)
