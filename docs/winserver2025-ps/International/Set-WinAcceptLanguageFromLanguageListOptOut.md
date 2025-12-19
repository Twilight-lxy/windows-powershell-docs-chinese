---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/set-winacceptlanguagefromlanguagelistoptout?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WinAcceptLanguageFromLanguageListOptOut
---

# 使用 `Set-WinAcceptLanguageFromLanguageListOptOut` 命令来设置 Windows 的语言接受选项

## 摘要
根据当前用户账户的“语言列表”设置（该设置允许用户选择不接收某些语言信息），来决定HTTP请求中应使用的接受语言（Accept Language）。

## 语法

```
Set-WinAcceptLanguageFromLanguageListOptOut [-OptOut] <Boolean> [<CommonParameters>]
```

## 描述
`Set-WinAcceptLanguageFromLanguageListOptOut` cmdlet 用于根据当前用户账户的语言列表设置来修改 HTTP 请求中的 `Accept-Language` 头信息。默认情况下，HTTP 的 `Accept-Language` 头值会自动从该用户账户的语言列表中生成。你可以使用这个 cmdlet 来手动指定 `Accept-Language` 的具体值。

- 如果将此参数设置为 `$True`，则会清除注册表中与 HTTP `Accept-Language` 相关的设置，并阻止后续对语言列表的更改再次影响该设置。
- 如果将此参数设置为 `$False`，则系统会根据当前用户账户的语言列表重新生成并应用相应的 `Accept-Language` 值。

简而言之：这个 cmdlet 允许你手动控制浏览器在发送 HTTP 请求时使用的 `Accept-Language` 头内容。

## 示例

### 示例 1：更新注册表键
```
PS C:\> Set-WinAcceptLanguageFromLanguageListOptOut -OptOut $True
```

这个cmdlet会删除**HTTP Accept Language**注册表键中的当前内容，并根据用户语言列表的变化来阻止对该键的更新。

## 参数

### -OptOut
指定退出（即选择不参与某项服务或活动的）值。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-WinAcceptLanguageFromLanguageListOptOut](./Get-WinAcceptLanguageFromLanguageListOptOut.md)

