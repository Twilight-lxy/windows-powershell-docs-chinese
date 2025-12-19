---
description: 使用此主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/get-msmqcertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MsmqCertificate
---

# 获取 MSMQ 证书

## 摘要
用于将证书注册到 Active Directory 域服务中。

## 语法

```
Get-MsmqCertificate [[-ComputerName] <String>] [<CommonParameters>]
```

## 描述
`Get-MsmqCertificate` cmdlet 会获取一个 `System.security cryptography.X509Certificates.X509Certificate` 对象数组。每个对象代表一个当前在 Active Directory® 域服务中注册的个人证书。

## 示例

### 示例 1：获取当前用户的所有证书
```
PS C:\> Get-MsmqCertificate
```

这个命令可以获取当前用户所有主机或虚拟服务器的证书。

### 示例 2：获取当前用户针对某个主机或虚拟服务器的证书
```
PS C:\> Get-MsmqCertificate -ComputerName "Contoso27"
```

这个命令会获取当前用户针对名为“Contoso27”的主机或虚拟服务器所拥有的证书。

## 参数

### -ComputerName
用于指定主机或虚拟服务器的名称。此cmdlet会获取当前用户为该指定主机或虚拟服务器所拥有的证书。如果您未指定此参数，那么此cmdlet将获取当前用户拥有的所有主机或虚拟服务器的证书。

```yaml
Type: String
Parameter Sets: (All)
Aliases: cn

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Enable-MsmqCertificate](./Enable-MsmqCertificate.md)

[Remove-MsmqCertificate](./Remove-MsmqCertificate.md)

