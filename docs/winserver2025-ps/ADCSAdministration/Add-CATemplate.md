---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Administration.Commands.dll-Help.xml
Module Name: ADCSAdministration
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsadministration/add-catemplate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-CATemplate
---

# 添加-CATemplate

## 摘要
向证书颁发机构（CA）添加一个证书模板。

## 语法

```
Add-CATemplate [-Name] <String> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-CATemplate` cmdlet 可以将证书模板添加到证书颁发机构（CA）中，以便后续用于颁发证书。

证书模板是一份预先配置好的证书设置列表，它让用户和计算机能够在无需创建复杂证书申请的情况下轻松办理证书的申领流程。通过使用证书模板，可以定制由证书颁发机构（CA）颁发的证书内容。该模板定义了诸如加密类型、有效期限及续期规则、以及证书用途等关键参数。

证书模板存储在 Active Directory 域服务（AD DS）中。当安装了 CA 角色服务时，许多默认的证书模板会被添加到 AD DS 中。此 cmdlet 不允许您创建新的模板或复制现有的模板。

## 示例

### 示例 1：添加一个 CA 模板
```
PS C:\> Add-CATemplate -Name "EFS"
```

此命令添加了一个名为“EFS”的CA模板。

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

### -Force
强制命令运行，而不需要用户确认。

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

### -Name
指定证书模板的名称。该名称必须始终是模板本身的名称（即不带空格的简称），而不是模板的显示名称。例如，模板显示名为“Exchange Enrollment Agent (Offline request)”的证书模板，应使用其实际的模板名称“EnrollmentAgentOffline”来标识。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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

### System.String
这个cmdlet只有一个参数，即*Name*（名称），并且每次只能通过字符串形式指定一个模板。

## 输出

### System.Object

## 备注
* To perform this procedure, you must be a member of the Domain Admins group or the Enterprise Admins group in AD DS, or you must have been delegated the appropriate authority. As a security best practice, consider using Run as to perform this procedure.

## 相关链接

[Get-CATemplate](./Get-CATemplate.md)

[Remove-CATemplate](./Remove-CATemplate.md)

