---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/set-winuilanguageoverride?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WinUILanguageOverride
---

# Set-WinUILanguageOverride

## 摘要
设置当前用户账户的Windows UI语言覆盖选项。

## 语法

```
Set-WinUILanguageOverride [[-Language] <CultureInfo>] [<CommonParameters>]
```

## 描述
`Set-WinUILanguageOverride` cmdlet 可以设置用户偏好的显示语言，用于 Windows 用户界面（UI）。如果没有使用任何覆盖设置，显示语言将动态地从用户的语言列表中确定。要使更改生效，需要先注销账户再重新登录。

有关更多信息，请参阅 **Get-WinUserLanguageList** 和 **Set-WinUserLanguageList** cmdlet。

## 示例

### 示例 1：设置语言覆盖规则
```
PS C:\> Set-WinUILanguageOverride -Language de-DE
```

此命令将当前用户账户的 Windows 用户界面语言设置为德语（德国）。

### 示例 2：将语言覆盖值设置为 null
```
PS C:\> Set-WinUILanguageOverride
```

该命令将当前用户账户的 Windows 用户界面语言设置重写值设置为 null（空）。


## 参数

### -Language
指定一种语言。

```yaml
Type: CultureInfo
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### CultureInfo
你可以将一个包含当前用户账户的Windows UI语言设置信息的对象传递给相应的处理函数。有关`CultureInfo`对象的更多信息，请参阅[CultureInfo类](https://go.microsoft.com/fwlink/?LinkID=242306)。

## 输出

## 备注

## 相关链接

[Get-Win UILanguageOverride](./Get-WinUILanguageOverride.md)

[Get-WinUserLanguageList](./Get-WinUserLanguageList.md)

[Set-WinUserLanguageList](./Set-WinUserLanguageList.md)
