---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsrelyingpartywebtheme?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsRelyingPartyWebTheme
---

# 设置 AdfsRelyingPartyWebTheme

## 摘要
将一个网页主题应用于依赖方（即使用该主题的网站或应用程序）。

## 语法

### IdentifierName（默认值）
```
Set-AdfsRelyingPartyWebTheme [-StyleSheet <Hashtable[]>] [-RTLStyleSheetPath <String>]
 [-OnLoadScriptPath <String>] [-Logo <Hashtable[]>] [-Illustration <Hashtable[]>]
 [-SourceWebThemeName <String>] [-SourceRelyingPartyName <String>] [-TargetRelyingPartyName] <String> [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### IdentifierObject
```
Set-AdfsRelyingPartyWebTheme [-StyleSheet <Hashtable[]>] [-RTLStyleSheetPath <String>]
 [-OnLoadScriptPath <String>] [-Logo <Hashtable[]>] [-Illustration <Hashtable[]>]
 [-SourceWebThemeName <String>] [-SourceRelyingPartyName <String>]
 [-TargetRelyingPartyWebTheme] <AdfsRelyingPartyWebTheme> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsRelyingPartyWebTheme` cmdlet 用于将一个网页主题应用于依赖方（relying party）。该网页主题包含徽标、插图、样式表以及自定义的 `onload.js` 文件。

## 示例

### 示例 1：创建一个自定义主题，并将其分配给依赖 Office 365 的第三方信任方
```
PS C:\> New-AdfsWebTheme -Name "Office365Theme" -SourceName "default"
PS C:\> Set-AdfsWebTheme -TargetName "Office365Theme" -Illustration @{Path="C:\localpath\illustration22.jpg"}
PS C:\> Set-AdfsRelyingPartyWebTheme -TargetRelyingPartyName "Microsoft Office 365 Identity Platform" -SourceWebThemeName "Office365Theme"
```

第一个命令使用 `New-AdfsWebTheme` cmdlet 创建了一个 AD FS 网页主题，该主题的名称为 Office365Theme。

第二个命令使用 **Set-AdfsWebTheme** cmdlet 来修改 Office365Theme。

最后一条命令将自定义主题应用于 Office 365 的依赖方信任设置中。

### 示例 2：为每个应用程序创建一个高级的自定义主题，并将其分配给依赖方
```
PS C:\> New-AdfsWebTheme -Name "AppSpecificTheme" -SourceName "default"
PS C:\> Export-AdfsWebTheme -Name "AppSpecificTheme" -DirectoryPath "C:\AppSpecificTheme"
PS C:\> Set-AdfsWebTheme -TargetName "AppSpecificTheme" -AdditionalFileResource @{Uri='/adfs/portal/script/onload.js';Path="C:\AppSpecificTheme\script\onload.js"}
PS C:\> Set-AdfsRelyingPartyWebTheme -TargetRelyingPartyName "urn:app1" -SourceWebThemeName "AppSpecificTheme"
```

第一个命令使用 `New-AdfsWebTheme` 创建一个主题，该主题是 Active Directory Federation Services (AD FS) 中默认全局主题的副本。

第二个命令使用 **Export-AdfsWebTheme** cmdlet 将主题导出以便进行自定义。

第三个命令通过使用 `Set-AdfsWebTheme` 来指定文件，从而自定义主题。

最后一条命令将自定义的主题应用到依赖方（relying party）上。

## 参数

### -Illustration
将一幅插图表示为一个哈希表。

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
通过哈希表的形式指定一个标志（logo）。

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
指定一个加载脚本（onload script）的路径。

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
指定 RTL 样式表的路径。

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

### -SourceRelyingPartyName
指定依赖方的名称（即提供信息的来源方）。

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

### -SourceWebThemeName
指定源网页主题的名称。

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
将样式表指定为一个哈希表（hash table）。

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

### -TargetRelyingPartyName
指定目标依赖方的名称。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases: Name

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetRelyingPartyWebTheme
指定目标网页主题的名称。

```yaml
Type: AdfsRelyingPartyWebTheme
Parameter Sets: IdentifierObject
Aliases: TargetWebTheme

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

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

## 备注

## 相关链接

[Export-AdfsWebTheme](./Export-AdfsWebTheme.md)

[Get-AdfsRelyingPartyWebTheme](./Get-AdfsRelyingPartyWebTheme.md)

[New-AdfsWebTheme](./New-AdfsWebTheme.md)

[Remove-AdfsRelyingPartyWebTheme](./Remove-AdfsRelyingPartyWebTheme.md)

[Set-AdfsWebTheme](./Set-AdfsWebTheme.md)

