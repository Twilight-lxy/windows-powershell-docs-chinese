---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfswebtheme?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsWebTheme
---

# 设置 AdfsWeb 主题

## 摘要
修改网页主题的属性。

## 语法

### IdentifierName（默认值）
```
Set-AdfsWebTheme [-StyleSheet <Hashtable[]>] [-RTLStyleSheetPath <String>] [-OnLoadScriptPath <String>]
 [-Logo <Hashtable[]>] [-Illustration <Hashtable[]>] [-AdditionalFileResource <Hashtable[]>] [-PassThru]
 [-TargetName] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### IdentifierObject
```
Set-AdfsWebTheme [-StyleSheet <Hashtable[]>] [-RTLStyleSheetPath <String>] [-OnLoadScriptPath <String>]
 [-Logo <Hashtable[]>] [-Illustration <Hashtable[]>] [-AdditionalFileResource <Hashtable[]>] [-PassThru]
 [-TargetWebTheme] <AdfsWebTheme> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsWebTheme` cmdlet 用于修改 `AdfsWebTheme` 对象的属性。您可以通过名称或使用 `Get-AdfsWebTheme` cmdlet 来指定一个 Web 主题。

## 示例

### 示例 1：修改一个名为 “theme” 的网页
```
PS C:\> Set-AdfsWebTheme -TargetName "Theme01" -Illustration @{Locale="";Path="c:\illustration.png"} -Logo @{Locale="";Path="c:\logo.png"} -RTLStyleSheetPath "C:\StyleSheet.css" -StyleSheet @{Locale="";Path="c:\stylesheet.css"}
```

这个命令用于修改一个名为 Theme01 的网页主题。该命令使用了标准的 Windows PowerShell® 语法来创建哈希表。如需更多信息，请输入 `Get-Help about_Hash_Tables`。该命令为 Theme01 指定了插图图片、Logo 图片、RTL 样式表以及层叠样式表。对于这些参数中的任何一个，命令都没有指定 **Locale** 的值；因此，插图、Logo 和样式表都使用了不变的本地化设置（即不考虑语言或区域设置）。

### 示例 2：指定一个额外的资源
```
PS C:\> Set-AdfsWebTheme -TargetName "Theme02" -AdditionalFileResource @{Uri="/adfs/portal/Background.png";Path="Background.png"}
```

此命令为名为Theme02的网站主题指定了一个额外的文件资源。该命令使得BackGround.png这个资源可以被级联样式表（CSS）或JavaScript应用程序使用。

### 示例 3：使用变量来修改网页主题
```
PS C:\> $Theme = Get-AdfsWebTheme -Name "Theme03"
PS C:\> Set-AdfsWebTheme -TargetWebTheme $Theme -Illustration @{Locale="";Path="C:\Illustration.png"} -Logo @{Locale="";Path="C:\Logo.png"} -RTLStyleSheetPath "C:\StyleSheet.css" -StyleSheet @{Locale="";Path="C:\StyleSheet.css"}
```

第一个命令使用 **Get-AdfsWebTheme** cmdlet 来获取名为 Theme03 的网页主题，然后将其存储在 `$Theme` 变量中。

第二个命令用于修改存储在 `$Theme` 变量中的网页主题。该命令指定了该主题所需的插图图片、标志图片、RTL 样式表以及层叠样式表（Cascading Style Sheets）。

## 参数

### -AdditionalFileResource
该参数用于指定一个 `Hashtable` 对象数组，这些对象通过两个字符串键（`Uri` 和 `Path`）来标识额外的文件资源。有关更多信息，请输入 `Get-Help about_Hash_Tables`。`Uri` 表示资源的相对统一资源标识符（URI）；该 URI 始终以 `/adfs/portal/` 开头。`Path` 表示文件的路径；如果未指定路径，该 cmdlet 将删除与指定 URI 对应的文件资源。

指定此参数，以便将资源（如图片）提供给层叠样式表或JavaScript应用程序使用。

```yaml
Type: Hashtable[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Illustration
指定一个包含 **Hashtable** 对象的数组，这些对象通过两个字符串键（**Locale** 和 **Path**）来标识相应的插图。其中，**Locale** 是一个 **CultureInfo** 对象，而 **Path** 是文件的路径。如果未指定地区设置（locale），则 **Locale** 会默认使用不变的地区设置（invariant locale）。

```yaml
Type: Hashtable[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Logo
指定一个 **Hashtable** 对象数组，这些对象通过两个字符串键（**Locale** 和 **Path**）来表示徽标。其中，**Locale** 是一个 **CultureInfo** 对象，**Path** 是文件路径。如果没有指定区域设置（locale），则 **Locale** 会使用默认的不变区域设置；如果没有指定文件路径，该 cmdlet 会删除与所指定区域设置对应的文件内容。

```yaml
Type: Hashtable[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OnLoadScriptPath
指定此参数，以便将资源（如图片）提供给层叠样式表或JavaScript应用程序使用。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -RTLStyleSheetPath
指定一个运行时库（RTL）样式表的文件路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StyleSheet
指定一个 `Hashtable` 对象数组，这些对象通过两个字符串键（`Locale` 和 `Path`）来标识样式表。`Locale` 是用于表示样式表的 `CultureInfo` 对象；`Path` 则是样式表的文件路径。如果没有指定 `Locale`，则使用不变的默认区域设置（即“不变区域设置”）。如果没有指定 `Path`，该 cmdlet 会删除与该区域设置对应的文件内容。

```yaml
Type: Hashtable[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetName
用于指定一个名称。该 cmdlet 会修改您通过名称指定的主题。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetWebTheme
用于指定一个 **AdfsWebTheme** 对象。该 cmdlet 会修改您所指定的主题。要获取一个 **AdfsWebTheme** 对象，请使用 **Get-AdfsWebTheme** cmdlet。

```yaml
Type: AdfsWebTheme
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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

## 输出

### System_identityServer.ManagementResources.AdfsWebTheme
此cmdlet会生成一个Web自定义对象，即**System.IdentityServer.Management.Resources.AdfsWebTheme**。该对象包含以下属性：

- Name: **System.String**
- IsBuiltinTheme: **System.Boolean**
- StyleSheet: **IDictionary\<string, byte\[\]\>**
- Logo: **IDictionary\<string, byte\[\]\>**
- Illustration: **IDictionary\<string, byte\[\]\>**
- RTLStyleSheet: **byte\[\]**
- AdditionalFileResources: **IDictionary\<string, byte\[\]\>**

## 备注

## 相关链接

[Export-AdfsWebTheme](./Export-AdfsWebTheme.md)

[Get-AdfsWebTheme](./Get-AdfsWebTheme.md)

[New-AdfsWebTheme](./New-AdfsWebTheme.md)

[Remove-AdfsWebTheme](./Remove-AdfsWebTheme.md)

