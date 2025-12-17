---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsrelyingpartywebtheme?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsRelyingPartyWebTheme
---

# 移除依赖 AdFS 的 Party Web 主题

## 摘要
将某个网页主题从依赖该主题的第三方系统中移除。

## 语法

### IdentifierName
```
Remove-AdfsRelyingPartyWebTheme [-TargetRelyingPartyName] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### IdentifierObject
```
Remove-AdfsRelyingPartyWebTheme [-TargetRelyingPartyWebTheme] <AdfsRelyingPartyWebTheme> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-AdfsRelyingPartyWebTheme` cmdlet 用于删除依赖方的网页主题。

## 示例

#### 示例 1：移除网页主题
```
PS C:\> Remove-AdfsRelyingPartyWebTheme -TargetRelyingPartyName "urn:app1"
```

此命令会删除名为 urn:app1 的依赖方的 Web 主题。

## 参数

### -TargetRelyingPartyName
指定要为其删除网页主题的目标依赖方的名称。

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
指定要为其删除网页主题的目标依赖方（relying party）。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-AdfsRelyingPartyWebTheme](./Get-AdfsRelyingPartyWebTheme.md)

[Set-AdfsRelyingPartyWebTheme](./Set-AdfsRelyingPartyWebTheme.md)

