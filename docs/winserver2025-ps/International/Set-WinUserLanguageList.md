---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/set-winuserlanguagelist?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WinUserLanguageList
---

# Set-WinUserLanguageList

## 摘要
为当前用户账户设置语言列表及相关属性。

## 语法

```
Set-WinUserLanguageList
 [-LanguageList] <System.Collections.Generic.List`1[Microsoft.InternationalSettings.Commands.WinUserLanguage]>
 [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-WinUserLanguageList` cmdlet 用于设置当前用户的语言设置。这些设置包括输入法、拼写设置、文本预测设置以及手写输入模式等。有关更多信息，请参阅 [CultureInfo 类](https://go.microsoft.com/fwlink/?LinkID=242306) 和 [可配置的语言和文化设置](https://go.microsoft.com/fwlink/?LinkID=242307)。

## 示例

### 示例 1：向现有的语言列表中添加一种新语言
```
PS C:\> $OldList = Get-WinUserLanguageList
PS C:\> $OldList.Add("fr-FR")
PS C:\> Set-WinUserLanguageList -LanguageList $OldList
```

这个示例将法语（法国）添加到用户的语言列表中。

第一个命令使用 `Get-WinUserLanguageList` cmdlet 来获取用户的语言列表，并将结果存储在 `$OldList` 变量中。

第二个命令会将某种语言添加到 `$OldList` 中的对象中。

最后一条命令将当前用户的语言列表设置为修改后的值 `$OldList`。

### 示例 2：修改某种语言中的某个值
```
PS C:\> $UserLanguageList = New-WinUserLanguageList -Language en-US
PS C:\> $UserLanguageList[0].Handwriting = $True
PS C:\> Set-WinUserLanguageList -LanguageList $UserLanguageList
```

这个示例会更改用户语言列表中某种语言的手写输入设置。

第一个命令为美式英语创建了一个语言列表，并为其设置了默认值，随后将该列表存储在 `$UserLanguageList` 变量中。

第二个命令会修改 `$UserLanguageList` 中的语言列表中第一个元素的 **Handwriting**（手写）属性。

最后一条命令将当前用户的语言列表设置为修改后的值 $UserLanguageList。

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

### -LanguageList
用于指定一个语言列表。

```yaml
Type: System.Collections.Generic.List`1[Microsoft.InternationalSettings.Commands.WinUserLanguage]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.Collections.Generic.List<Microsoft.InternationalSettingscommands.WinUserLanguage>
你可以将一系列 **WinUserLanguage** 对象通过管道（pipe）传输过来，这些对象包含一种或多种语言以及相关属性，这些信息来源于当前用户账户的语言列表。每个语言对象都包含以下属性：

- **BCP-47** (READ).
A standard language tag that is used to identify languages.
For more information, see the [Internet Engineering Task Force (IETF) BCP 47 RFC](https://go.microsoft.com/fwlink/?LinkID=242207).
- **Autonym** (LP database) (READ).
The name of the language in the language itself.
- **English name** (LP database) (READ).
The name of the language in English.
- **Localized name** (LP database) (READ).
The name of the language in the current Windows display language.
- **Script** (LP database) (READ).
The writing system of the language.
- **Input methods** (READ/WRITE).
A list of input method Tablet Input Panel (TIP) strings that are enabled for this language.
The enabled input methods are listed in the format `Language ID:Keyboard layout ID`. See [Default input profiles (input locales) in Windows](/windows-hardware/manufacture/desktop/default-input-locales-for-windows-language-packs).
- **Handwriting recognition input mode** (READ/WRITE).
This value is either 0 (freehand) or 1 (write each character separately).

## 输出

## 备注

## 相关链接

[Get-WinUserLanguageList](./Get-WinUserLanguageList.md)

[New-WinUserLanguageList](./New-WinUserLanguageList.md)

