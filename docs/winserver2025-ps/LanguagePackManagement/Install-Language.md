---
description: `Install-Language` cmdlet 允许您向正在运行的 Windows 系统中添加一种语言支持。
external help file: Microsoft.LanguagePackManagement.Powershell.Commands.dll-Help.xml
Module Name: LanguagePackManagement
ms.date: 08/15/2022
online version: https://learn.microsoft.com/powershell/module/languagepackmanagement/install-language?view=windowsserver2025-ps
schema: 2.0.0
title: Install-Language
---

# 安装语言插件

## 摘要
将一种语言安装到设备上。

## 语法

```
Install-Language [-Language] <String> [-CopyToSettings] [-ExcludeFeatures] [-AsJob] [<CommonParameters>]
```

## 描述

将指定语言的可用语言组件下载并安装到设备上。

您还可以通过使用“International”模块命令（`Set-Win UILanguageOverride <已安装的语言>`）来更改显示语言。

## 示例

### 示例 1：为设备添加一种语言支持

```powershell
Install-Language ja-JP
```

此命令会将日语语言添加到设备中。

## 参数

### -AsJob

如果指定了该参数，语言安装过程将作为[异步PowerShell作业](/powershell/module/microsoft.powershell.core/about/about_jobs)来执行。

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

### -CopyToSettings

如果指定了此参数，它将在安装后将系统和默认设备设置（Windows显示语言、区域和本地化格式）设置为所安装语言对应的设置。

使用此命令添加语言后，你需要重新启动设备或再次登录才能使更改生效。重新登录后，你可以在“设置”应用程序中更改Windows显示语言，从而改变设备的用户界面语言。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: ApplyToSettings, ApplyToInternationalSettings, CopyToInternationalSettings

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExcludeFeatures

如果指定了相关语言，那么按需提供的语言功能将不会被安装。

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

### -Language

您正在安装的语言对应的 bcp47 标签。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft(LanguagePackManagement.PowershellCommands.InstallLanguage + InstallLanguageJob

### System.Collections.Generic.List<Microsoft(LanguagePackManagement.PowershellCommands.InstalledLanguage>

## 相关链接

[UninstallLanguage](uninstall-language.md)
