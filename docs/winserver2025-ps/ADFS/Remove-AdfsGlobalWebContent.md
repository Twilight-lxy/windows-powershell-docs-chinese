---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsglobalwebcontent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsGlobalWebContent
---

# 移除 AdfsGlobalWebContent

## 摘要
删除一个全局性的网页内容对象。

## 语法

### IdentifierName（默认值）
```
Remove-AdfsGlobalWebContent [[-Locale] <CultureInfo>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### IdentifierObject
```
Remove-AdfsGlobalWebContent [-TargetWebContent] <AdfsGlobalWebContent> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-AdfsGlobalWebContent` cmdlet 用于删除与某个区域设置（locale）相对应的全局网页内容对象。如果您不指定 `Locale` 参数，该 cmdlet 将删除与默认区域设置相关的全局网页内容对象。当所有全局网页内容对象都被删除后，Active Directory Federation Services (AD FS) 会恢复到其默认配置。

## 示例

### 示例 1：移除与不变区域设置（invariant locale）相关的全局网页内容
```
PS C:\> Remove-AdfsGlobalWebContent
```

此命令会删除与不变区域设置（invariant locale）相对应的全局网页内容对象。

### 示例 2：移除特定语言环境下的全局网页内容
```
PS C:\> Remove-AdfsGlobalWebContent -Locale en-us
```

此命令会删除与“en-us”区域设置相对应的全局Web内容对象。

## 参数

### -Locale
用于指定一个区域设置（locale）。该cmdlet会删除与该区域设置相对应的全局网页内容。

```yaml
Type: CultureInfo
Parameter Sets: IdentifierName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetWebContent
指定要删除的 **AdfsGlobalWebContent** 对象。若要获取一个 **AdfsGlobalWebContent** 对象，请使用 **Get-AdfsGlobalWebContent** cmdlet。

```yaml
Type: AdfsGlobalWebContent
Parameter Sets: IdentifierObject
Aliases:

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-AdfsGlobalWebContent](./Get-AdfsGlobalWebContent.md)

[Set-AdfsGlobalWebContent](./Set-AdfsGlobalWebContent.md)

[Remove-AdfsGlobalWebContent](./Remove-AdfsGlobalWebContent.md)

