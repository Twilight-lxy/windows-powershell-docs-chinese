---
description: LanguagePackManagement模块包含了一些cmdlet（命令行工具），可以帮助您轻松地管理和配置正在运行的Windows系统中的语言设置。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.1
Locale: en-US
Module Guid: f42dbdd4-4358-4067-8155-a4567a0aaee5
Module Name: LanguagePackManagement
ms.date: 08/15/2022
title: LanguagePackManagement module
---

# 语言包管理模块
## 描述

该模块可以轻松地用于[添加语言](/windows-hardware/manufacturedesktop/available-language-packs-for-windows)和[相关的语言功能](/windows-hardware/manufacture/desktop/features-on-demand-language-fod)，并通过新的cmdlet来管理诸如“系统首选UI语言”、“系统区域设置”、“输入法（键盘）”、“区域设置”、“语音识别器”以及“用户首选语言列表”等设置。

> [!注意] > - 这些cmdlets仅支持在客户端操作系统上使用。  
> - 要运行`Install-Language`和`Set-Language` cmdlets，您必须以管理员身份运行PowerShell（右键点击PowerShell图标）。  
> - 这些cmdlets与[International模块](/powershell/module/international/)配合使用，该模块允许用户控制用户界面（UI）中各种元素所用的语言。  
> - `Install-Language` cmdlet仅能安装适用于[语言包语言](/windows-hardware/manufacture/desktop/available-language-packs-for-windows)的Windows显示语言资源。

## LanguagePackManagementCmdlets
### [Get-InstalledLanguage](Get-InstalledLanguage.md)
返回有关设备上已安装语言的信息。

### [Get-SystemPreferredUILanguage](Get-SystemPreferredUILanguage.md)
返回当前系统的首选语言。

### [安装语言](Install-Language.md)
将一种语言安装到设备上。

### [Set-SystemPreferredUILanguage](Set-SystemPreferredUILanguage.md)
将提供的语言设置为系统首选的用户界面语言。

### [卸载语言相关文档](Uninstall-Language.md)
从设备中移除某种语言设置（或相关功能）。
