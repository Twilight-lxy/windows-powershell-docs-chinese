---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Administration.Commands.dll-Help.xml
Module Name: ADCSAdministration
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsadministration/get-catemplate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-CATemplate
---

# Get-CATemplate

## 摘要
获取在证书颁发机构（CA）上设置的用于生成证书的模板列表。

## 语法

```
Get-CATemplate [<CommonParameters>]
```

## 描述
`Get-CATemplate` cmdlet 可以获取证书颁发机构（CA）上用于证书发行的模板列表。

## 示例

### 示例 1：获取用于证书签发的 CA（证书颁发机构）上设置的模板列表
```
PS C:\> Get-CATemplate
```

这个命令会获取一份证书模板条目的列表，每个条目都包含一个模板名称。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.CertificateServices ADMINistration CommandsCommon.CertificateTemplate
此cmdlet返回一个证书模板对象数组，这些对象具有两个属性：（1）对象名称（Object Name）和（2）对象ID（Object ID）。这两个属性均为字符串类型。

## 备注

## 相关链接

[Add-CATemplate](./Add-CATemplate.md)

[Remove-CATemplate](./Remove-CATemplate.md)

