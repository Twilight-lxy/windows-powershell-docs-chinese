---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/import-adfswebcontent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-AdfsWebContent
---

# 导入 AdfsWebContent

## 摘要
将资源文件中的属性导入到全局对象以及依赖方的网页内容对象中。

## 语法

```
Import-AdfsWebContent [[-Locale] <CultureInfo>] -FilePath <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Import-AdfsWebContent` cmdlet 用于将 `.resx` 资源文件中的属性导入到全局 Web 内容对象以及依赖方（relying party）的 Web 内容对象中。如果不存在相应的 Web 内容对象，该 cmdlet 会创建一个新的对象。如果您没有指定区域设置（locale），则该 cmdlet 会将 Web 内容导入为与系统默认区域设置一致的格式。

使用此cmdlet来实现Active Directory Federation Services（AD FS）登录体验中自定义消息的本地化。通过使用**Export-AdfsWebContent** cmdlet将网页内容导出为.resx文件，对文件进行本地化处理，然后再导入本地化的.resx文件。

## 示例

### 示例 1：导入适用于不变区域设置（invariant locale）的网页内容
```
PS C:\> Import-AdfsWebContent -FilePath "C:\WebContent\Invariant.resx"
```

该命令从指定的文件中将针对不变区域设置的定制网页内容导入到 AD FS 配置存储中。

### 示例 2：为指定的地区导入网页内容
```
PS C:\> Import-AdfsWebContent -Locale en-us -FilePath "C:\WebContent\EnUs.resx"
```

此命令从指定的文件中将针对 en-us 地区设置的定制网页内容导入到 AD FS 配置存储中。

## 参数

### -FilePath
指定一个文件路径。该 cmdlet 会从您指定的文件中导入属性。

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

### -Locale
指定一个区域设置（locale）。该cmdlet会导入与您指定的区域设置相匹配的网页内容对象的属性。

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

### -Confirm
在运行cmdlet之前会提示您进行确认。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Export-AdfsWebContent](./Export-AdfsWebContent.md)

