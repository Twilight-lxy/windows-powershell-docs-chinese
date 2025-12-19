---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/remove-msmqcertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-MsmqCertificate
---

# 删除 MSMQ 证书

## 摘要
删除个人证书。

## 语法

```
Remove-MsmqCertificate -InputObject <X509Certificate2[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-MsmqCertificate` cmdlet 用于从 Active Directory® 域服务中删除个人证书。此 cmdlet 会返回被删除的消息队列（也称为 MSMQ）证书。

## 示例

### 示例 1：删除当前用户的所有证书
```
PS C:\> Get-MsmqCertificate | Remove-MsmqCertificate
```

该命令使用 **Get-MsmqCertificate** cmdlet 获取当前用户所有主机或虚拟服务器的证书，并通过管道运算符将这些证书传递给后续的 cmdlet。最后，这个命令会删除这些证书。

## 参数

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

### -InputObject
指定一个证书对象数组，这些证书表示该cmdlet将从Active Directory域服务中删除的证书。此参数支持管道输入（pipeline input）。

```yaml
Type: X509Certificate2[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

### System.security.Cryptography.X509Certificates.X509Certificate2[]

## 输出

### System.Object

## 备注

## 相关链接

[Get-MsmqCertificate](./Get-MSMQCertificate.md)

[Enable-MsmqCertificate](./Enable-MSMQCertificate.md)

