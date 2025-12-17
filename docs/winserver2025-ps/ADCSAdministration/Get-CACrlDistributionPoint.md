---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Administration.Commands.dll-Help.xml
Module Name: ADCSAdministration
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsadministration/get-cacrldistributionpoint?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-CACrlDistributionPoint
---

# 获取 CACRL 分发点

## 摘要
获取CA属性中CDP扩展所设置的所有位置信息。

## 语法

```
Get-CACrlDistributionPoint [<CommonParameters>]
```

## 描述
`Get-CACRLDistributionPoint` cmdlet 可以获取证书颁发机构（CA）属性中与 CRL 分发点（CDP）扩展相关设置的所有信息。

## 示例

### 示例 1：获取 CA 证书撤销列表分发点对象
```
PS C:\> Get-CACrlDistributionPoint
```

该命令获取一个CA证书吊销列表（CRL）分发点（CDP）类型对象，其中包含与当前CA对应的配置信息以及统一资源标识符（URI）。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.CertificateServices.AdministrationCommands.CA.CrlDistributionPoint
此cmdlet返回一个由`Microsoft.CertificateServices.Management Cmdlets.CA.CrlDistributionPoint`对象组成的数组。每个对象包含一个URI以及以下不同的布尔属性：

Name | Type
-----|------
PublishToServer | Boolean
PublishDeltaToServer | Boolean
AddToCertificateCdp | Boolean
AddToFreshestCrl | Boolean
AddToCrlCdp | Boolean
AddToCrlIdp | Boolean
Uri | String

## 备注

## 相关链接

[Add-CACrlDistributionPoint](./Add-CACrlDistributionPoint.md)

[Remove-CACrlDistributionPoint](./Remove-CACrlDistributionPoint.md)

