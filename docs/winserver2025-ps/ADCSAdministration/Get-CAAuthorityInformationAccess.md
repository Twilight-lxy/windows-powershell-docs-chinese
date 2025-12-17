---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Administration.Commands.dll-Help.xml
Module Name: ADCSAdministration
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsadministration/get-caauthorityinformationaccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-CAAuthorityInformationAccess
---

# 获取 CA 权限信息访问权限

## 摘要
获取设置在证书颁发机构（CA）属性的“AIA”扩展中的AIA和OCSP URI信息。

## 语法

```
Get-CAAuthorityInformationAccess [<CommonParameters>]
```

## 描述
`Get-CAAuthorityInformationAccess` cmdlet 可以获取证书颁发机构（CA）属性中 AIA（Authority Information Access）扩展部分所设置的 AIA URI 信息以及 OCSP（Online Certificate Status Protocol）URI 信息。

## 示例

### 示例 1：从证书颁发机构（CA）属性的 AIA 扩展中获取 AIA 和 OCSP URI 信息
```
PS C:\> Get-CAAuthorityInformationAccess
```

该命令用于获取当前认证机构的AIA（Autonomous Identity Authority）和OCSP（Online Certificate Status Protocol）设置信息。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要说明的内容）。

## 输出

### Microsoft.CertificateServices ADMINistration Commands.CA.AuthorityInformationAccess
此cmdlet返回一个由Authority Information Access（AIA）对象组成的数组，具体类型为`Microsoft.CertificateServices.Management Cmdlets.CA.AuthorityInformationAccess`。每个对象将包含一个URI以及以下布尔属性：

Name | Type
-----|------
Uri | String
AddToCertificateAia | Boolean
AddtoCertificateOCSP | Boolean

## 备注

## 相关链接

[Add-CAAuthorityInformationAccess](./Add-CAAuthorityInformationAccess.md)

[Remove-CAAuthorityInformationAccess](./Remove-CA AuthorityInformationAccess.md)

