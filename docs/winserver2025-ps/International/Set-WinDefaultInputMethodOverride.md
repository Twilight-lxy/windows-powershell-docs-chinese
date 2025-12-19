---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/set-windefaultinputmethodoverride?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WinDefaultInputMethodOverride
---

# Set-WinDefaultInputMethodOverride

## 摘要
为当前用户账户设置默认的输入方法覆盖选项（即是否允许更改系统的默认输入方法）。

## 语法

```
Set-WinDefaultInputMethodOverride [[-InputTip] <String>] [<CommonParameters>]
```

## 描述
`Set-WinDefaultInputMethodOverride` cmdlet 用于设置默认的输入法覆盖选项，该选项为当前用户账户指定一个默认的输入法。如果没有使用任何覆盖设置，输入法将动态地从当前用户账户的语言列表中确定。有关更多信息，请参阅 `Get-WinUserLanguageList` 和 `Set-WinUserLanguageList` cmdlets。

## 示例

### 示例 1：设置默认输入方法的覆盖值
```
PS C:\> Set-WinDefaultInputMethodOverride -InputTip "0409:00000409"
```

此命令将默认的输入方法设置为“英语（美国）- US”。

## 参数

### -InputTip
用于指定输入提示信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 输入提示（InputTip）
你可以将一个地区代码（locale ID）和一个键盘语言代码（keyboard language ID，简称 KLID）通过管道传递。详情请参阅 [Windows 中的默认输入配置文件（输入地区设置）](/windows-hardware/manufacture/desktop/default-input-locales-for-windows-language-packs)。

## 输出

## 备注

## 相关链接

[Get-WinDefaultInputMethodOverride](./Get-WinDefaultInputMethodOverride.md)
