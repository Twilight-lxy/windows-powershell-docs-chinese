---
description: `Set-SystemPreferredUILanguage` cmdlet 允许您将已安装的语言设置为正在运行的 Windows 系统中的系统默认用户界面语言。
external help file: Microsoft.LanguagePackManagement.Powershell.Commands.dll-Help.xml
Module Name: LanguagePackManagement
ms.date: 08/15/2022
online version: https://learn.microsoft.com/powershell/module/languagepackmanagement/set-systempreferreduilanguage?view=windowsserver2025-ps
schema: 2.0.0
title: Set-SystemPreferredUILanguage
---

# 设置系统首选的 UI 语言

## 摘要
将提供的语言设置为系统的默认用户界面语言。

## 语法

```
Set-SystemPreferredUILanguage [-Language] <String> [-PassThru] [<CommonParameters>]
```

## 描述

将提供的语言设置为系统的默认用户界面语言。

将某种语言设置为系统首选用户界面语言后，你需要重启设备或重新登录才能使设置生效。在设置系统首选用户界面语言之后创建的新账户将会被配置为使用该新语言。

## 示例

#### 示例 1：在 Windows 系统中设置系统默认的用户界面语言

```powershell
Set-SystemPreferredUILanguage ja-JP
```

此命令将系统默认的用户界面语言设置为日语。

## 参数

### -Language

将语言的 bcp47 标签设置为系统首选的用户界面语言。

```yaml
Type: String
Parameter Sets: (All)
Aliases: LanguageId, LanguageTag

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru

如果指定了该参数，在成功配置系统首选用户界面语言后，它将返回 해당语言的 bcp47 标签。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### SystemVoid

### System.String

## 备注

## 相关链接

[Get-SystemPreferredUILanguage](Set-SystemPreferredUILanguage.md)
