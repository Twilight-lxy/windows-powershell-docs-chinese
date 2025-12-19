---
author: erik0686
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
manager: aandrejs
ms.author: ertorres
ms.date: 09/08/2021
Module Name: International
online version: https://learn.microsoft.com/powershell/module/international/copy-userinternationalsettingstosystem?view=windowsserver2022-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Copy-UserInternationalSettingsToSystem
---

# 将用户国际设置复制到系统

## 摘要
将当前用户的国际设置（Windows显示语言、输入语言、区域格式/区域设置以及位置信息/地理标识符）复制到以下一个或两个目标：  
* 欢迎屏幕和系统账户  
* 新用户账户

**重要提示：**请注意，此 PowerShell 命令仅适用于 Windows 11 及更高版本的系统。

这是一个系统设置。只有具有管理员权限的用户才能对其进行更改。更改会在计算机重新启动后生效。

## 语法

```
Copy-UserInternationalSettingsToSystem [-WelcomeScreen <Boolean>] [-NewUser <Boolean>] [<CommonParameters>]
```

## 描述
`Copy-UserInternationalSettingsToSystem` cmdlet 用于从当前用户那里获取国际设置。你可以选择将这些设置复制到“欢迎屏幕”和系统账户中，或者复制到新用户账户中，也可以同时复制到两者中。

这个cmdlet接受两个参数：**-WelcomeScreen** 和 **-NewUser**。

当任何参数被设置为 `$True` 时，此 cmdlet 会从当前用户那里获取相应的值，并根据这些被设置为 `$True` 的参数，将这些值复制到所选选项的系统设置中。

## 示例

### 示例 1：将设置复制到欢迎屏幕、系统账户以及新用户账户中
```
PS C:\> Copy-UserInternationalSettingsToSystem -WelcomeScreen $True -NewUser $True
```

这个示例将 Windows 的显示语言、输入语言、区域设置（Regional Format/Locale）以及位置信息（Location/GeoID）复制到欢迎屏幕、系统账户和新用户账户中。


### 示例 2：仅将设置复制到欢迎屏幕和系统账户中
```
PS C:\> Copy-UserInternationalSettingsToSystem -WelcomeScreen $True -NewUser $False
```

这个示例仅将 Windows 的显示语言、输入语言、区域设置（Format/locale）以及地区位置/地理标识符（Regional Location/GeoID）复制到欢迎屏幕和系统账户中。


## 参数

### -WelcomeScreen
将这些设置复制到欢迎屏幕和系统账户中。

```yaml
Type: Boolean
Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewUser
将这些设置复制到新的用户账户中。

```yaml
Type: Boolean
Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接
