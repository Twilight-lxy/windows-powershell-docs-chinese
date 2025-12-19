---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.KpsServer.Administration.dll-Help.xml
Module Name: HgsKeyProtection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgskeyprotection/get-hgskeyprotectionconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-HgsKeyProtectionConfiguration
---

# Get-HgsKeyProtectionConfiguration

## 摘要
获取密钥保护服务的配置信息。

## 语法

```
Get-HgsKeyProtectionConfiguration [<CommonParameters>]
```

## 描述
`Get-HgsKeyProtectionConfiguration` cmdlet 可以获取在本地计算机上运行的 Key Protection Service 的配置信息。该配置包括 Key Protection Service 用于签署服务提供的元数据的通信证书。

## 示例

### 示例 1：获取密钥保护服务的配置信息
```
PS C:\> Get-HgsKeyProtectionConfiguration
```

这个命令用于获取本地计算机上密钥保护服务（Key Protection Service）的配置信息。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无
您无法将输入内容通过管道传递给此cmdlet。

## 输出

### Microsoft.Windows.KpsServer COMMON.Store.Data.ServiceConfiguration
此cmdlet返回在本地计算机上设置的Key Protection Service（密钥保护服务）的配置信息。

## 备注

## 相关链接

[Set-HgsKeyProtectionConfiguration](./Set-HgsKeyProtectionConfiguration.md)

