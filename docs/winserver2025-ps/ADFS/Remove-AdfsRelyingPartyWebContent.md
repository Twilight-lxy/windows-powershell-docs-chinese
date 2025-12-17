---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsrelyingpartywebcontent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsRelyingPartyWebContent
---

# 删除依赖 AdFS 的相关 Web 内容

## 摘要
删除一个依赖方（relying party）的网络内容对象。

## 语法

### IdentifierName（默认值）
```
Remove-AdfsRelyingPartyWebContent [[-Locale] <CultureInfo>] -TargetRelyingPartyName <String> [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### IdentifierObject
```
Remove-AdfsRelyingPartyWebContent [-TargetRelyingPartyWebContent] <AdfsRelyingPartyWebContent> [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-AdfsRelyingPartyWebContent` cmdlet 用于删除依赖方网页内容对象。您可以通过指定名称和区域设置（locale）来定位所需的依赖方网页内容对象，或者先使用 `Get-AdfsRelyingPartyWebContent` cmdlet 获取该对象的信息。如果您未指定区域设置，cmdlet 将使用默认的不变区域设置（invariant locale）。

## 示例

### 示例 1：移除与不变本地化设置相关的网络内容对象
```
PS C:\> Remove-AdfsRelyingPartyWebContent -TargetRelyingPartyName "RelyingParty01"
```

此命令会删除名为 RelyingParty01 的依赖方的 Web 内容对象（该对象的不变本地化为 “invariant locale”）。

### 示例 2：删除指定区域设置（locale）下的网页内容对象
```
PS C:\> Remove-AdfsRelyingPartyWebContent -Locale en-us -TargetRelyingPartyName "RelyingParty01"
```

此命令会删除指定区域设置下、名为 RelyingParty01 的依赖方对应的 Web 内容对象。

## 参数

### -Locale
用于指定一个区域设置（locale）。该cmdlet会删除与该区域设置相关联的依赖方网页内容。如果您没有指定区域设置，那么该cmdlet将删除与“不变区域设置”（invariant locale）相关联的依赖方网页内容。

```yaml
Type: CultureInfo
Parameter Sets: IdentifierName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetRelyingPartyName
指定需要从中删除网页内容的依赖方的名称。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases: Name

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetRelyingPartyWebContent
指定要从依赖方中移除的网页内容。

```yaml
Type: AdfsRelyingPartyWebContent
Parameter Sets: IdentifierObject
Aliases: TargetWebContent

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
展示了如果运行该cmdlet会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

[Get-AdfsRelyingPartyWebContent](./Get-AdfsRelyingPartyWebContent.md)

[Set-AdfsRelyingPartyWebContent](./Set-AdfsRelyingPartyWebContent.md)

