---
description: `Uninstall-Language` cmdlet 可以帮助您从正在运行的 Windows 系统中删除某个语言及其相关组件。
external help file: Microsoft.LanguagePackManagement.Powershell.Commands.dll-Help.xml
Module Name: LanguagePackManagement
ms.date: 08/15/2022
online version: https://learn.microsoft.com/powershell/module/languagepackmanagement/uninstall-language?view=windowsserver2025-ps
schema: 2.0.0
title: Uninstall-Language
---

# 卸载指定语言包

## 摘要
从设备中卸载某种语言相关的内容（或应用程序）。

## 语法

```
Uninstall-Language [-Language] <String> [-PassThru] [<CommonParameters>]
```

## 描述

从设备中卸载某种语言及其所有相关组件。此操作为异步执行的。

## 示例

### 示例 1：从设备中删除某种语言设置

```powershell
Uninstall-Language ja-jp
```

此命令会从设备中删除日语相关内容（或：删除与日语相关的设置/数据等）。

## 参数

### -Language

需要安装的语言对应的 bcp47 标签。

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

如果指定了该参数，在成功安装新语言后，它将返回所安装语言对应的 bcp47 标签。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System Void

### System.String

## 备注

## 相关链接

[安装语言](Install-Language.md)
