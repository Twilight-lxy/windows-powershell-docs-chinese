---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfswebtheme?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsWebTheme
---

# 移除 AdfsWebTheme

## 摘要
移除一个网页主题。

## 语法

### IdentifierName
```
Remove-AdfsWebTheme [-TargetName] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### IdentifierObject
```
Remove-AdfsWebTheme [-TargetWebTheme] <AdfsWebTheme> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-AdfsWebTheme` cmdlet 用于删除一个 `AdfsWebTheme` 对象。您可以通过名称或使用 `Get-AdfsWebTheme` cmdlet 来指定要删除的网页主题。

## 示例

### 示例 1：移除一个已命名的网页主题
```
PS C:\> Remove-AdfsWebTheme -TargetName "Theme01"
```

这个命令会删除名为“Theme01”的网页主题。

### 示例 2：通过指定一个 Web 主题对象来移除该 Web 主题
```
PS C:\> Get-AdfsWebTheme -Name "Theme02" | Remove-AdfsWebTheme
```

该命令使用 **Get-AdfsWebTheme** cmdlet 来获取名为 Theme02 的网页主题，然后通过管道运算符将其传递给当前的 cmdlet。该 cmdlet 会删除这个网页主题。

## 参数

### -TargetName
指定一个名称。该cmdlet会删除按名称指定的主题。

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
用于指定一个 **AdfsWebTheme** 对象。该 cmdlet 会删除您指定的主题。要获取一个 **AdfsWebTheme** 对象，请使用 **Get-AdfsWebTheme** cmdlet。

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
在运行该cmdlet之前，会提示您确认是否要继续执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String; Microsoft.IdentityServer.ManagementResources.AdfsWebTheme

## 输出

## 备注

## 相关链接

[Export-AdfsWebTheme](./Export-AdfsWebTheme.md)

[Get-AdfsWebTheme](./Get-AdfsWebTheme.md)

[New-AdfsWebTheme](./New-AdfsWebTheme.md)

[Set-AdfsWebTheme](./Set-AdfsWebTheme.md)

