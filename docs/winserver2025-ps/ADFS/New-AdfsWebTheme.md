---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/new-adfswebtheme?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AdfsWebTheme
---

# 新 AdfsWeb 主题

## 摘要
创建一个 AD FS 网页主题。

## 语法

```
New-AdfsWebTheme -Name <String> [-SourceName <String>] [-StyleSheet <Hashtable[]>]
 [-RTLStyleSheetPath <String>] [-OnLoadScriptPath <String>] [-Logo <Hashtable[]>] [-Illustration <Hashtable[]>]
 [-AdditionalFileResource <Hashtable[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-AdfsWebTheme` cmdlet 用于创建 Active Directory Federation Services (AD FS) 网页主题。您可以创建一个空的 `AdfsWebTheme` 对象，或者基于现有主题来创建一个新的 `AdfsWebTheme` 对象。如果使用现有主题作为起点，该 cmdlet 会将其属性复制到新对象中；同时，您也可以为 AD FS 网页主题指定额外的属性。

## 示例

#### 示例 1：创建一个主题
```
PS C:\> New-AdfsWebTheme -Name "Theme01" -AdditionalFileResource @{Uri="/adfs/portal/Background.png";Path="C:\Background.png"} -Illustration @{Locale="";Path="C:\Illustration.png"} -Logo @{Locale="";Path="C:\Logo.png"} -RTLStyleSheetPath "C:\StyleSheet.css" -StyleSheet @{Locale="";Path="C:\StyleSheet.css"}
```

此命令创建了一个名为“Theme01”的主题，该主题提供了自定义的登录体验。该命令使用标准的 Windows PowerShell® 语法来创建哈希表。有关更多信息，请输入 `Get-Help about_Hash_Tables`。该命令还指定了一个额外的文件资源、一张插图图片、一个徽标以及一个层叠样式表。对于这些参数中的任何一个，该命令都没有为 **Locale** 参数指定值；因此，插图、徽标和样式表都使用不变的本地化设置（即不进行任何本地化处理）。

### 示例 2：复制一个主题
```
PS C:\> New-AdfsWebTheme -Name "Theme02" -SourceName "Default"
```

这个命令会创建一个名为“Theme02”的主题，并将现有的默认主题复制到新的主题中。你可以使用 `Export-AdfsWebTheme` 或 `Set-AdfsWebTheme` cmdlet 来修改新主题。

### 示例 3：创建和修改主题
```
PS C:\> New-AdfsWebTheme -Name "Theme03" -AdditionalFileResource @{Uri="/adfs/portal/Background.png";Path="C:\Background.png"} -Illustration @{Locale="en-us";Path="c:\Illustration.png"} -Logo @{Locale="en-us";Path="C:\Logo.png"} -RTLStyleSheetPath "C:\StyleSheet.css" -SourceName "Default" -StyleSheet @{Locale="en-us";Path="C:\StyleSheet.css"}
```

这个命令基于一个名为“Default”的现有主题，创建了一个名为“Theme03”的新主题。该命令指定了额外的文件资源（包括一张插图图片、一个徽标以及一个层叠样式表）。对于这些资源（插图、徽标和样式表），cmdlet将**Locale**属性的值设置为“en-us”。

## 参数

### -AdditionalFileResource
该参数用于指定一个 `Hashtable` 对象数组，这些对象通过两个字符串键（`Uri` 和 `Path`）来标识额外的文件资源。有关更多详细信息，请输入 `Get-Help about_Hash_Tables`。  
- `Uri` 是资源的相对统一资源标识符（URI）字符串；所有 URI 都以 `/adfs/portal/` 开头。  
- `Path` 是资源的文件路径；如果未指定路径，该 cmdlet 会删除与指定 URI 对应的文件资源。

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
指定一个由 **Hashtable** 对象组成的数组，这些对象通过两个字符串键（**Locale** 和 **Path**）来标识相应的插图。其中，**Locale** 是一个 **CultureInfo** 对象，**Path** 是文件路径。如果未指定区域设置（locale），则 **Locale** 会使用不变的默认区域设置（invariant locale）。

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
指定一个包含 **Hashtable** 对象的数组，这些对象使用两个字符串键（**Locale** 和 **Path**）来标识相应的日志文件。其中，**Locale** 是一个 **CultureInfo** 对象，而 **Path** 是文件的路径。如果不指定 **Locale**，则系统会使用默认的不变区域设置（invariant locale）。如果不指定 **Path**，该 cmdlet 会删除与该区域设置对应的文件内容。

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

### -Name
指定一个名称。该cmdlet会将您指定的名称分配给新的主题。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
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

### -RTLStyleSheetPath
指定一个指向从右到左（RTL）样式表的文件路径。

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

### -SourceName
用于指定一个现有主题的名称。该cmdlet会以您指定的主题为基础来创建新的主题。

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
该参数指定一个 **Hashtable** 对象数组，这些对象通过两个字符串键（**Locale** 和 **Path**）来标识样式表。其中，**Locale** 是对应样式表的 **CultureInfo** 对象；**Path** 则是样式表的文件路径。如果未指定 **Locale**，则使用默认的不变区域设置（invariant locale）；如果未指定文件路径，该 cmdlet 会删除与该区域设置对应的样式表内容。

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

### -Confirm
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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
展示了如果该cmdlet被运行会发生的情景。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### MicrosoftIdentityServer.Management.Resources.AdfsWebTheme
此cmdlet生成一个Web自定义对象，即**SystemIdentityServer.Management.Resources.AdfsWebTheme**。该对象包含以下属性：

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

[Remove-AdfsWebTheme](./Remove-AdfsWebTheme.md)

[Set-AdfsWebTheme](./Set-AdfsWebTheme.md)

