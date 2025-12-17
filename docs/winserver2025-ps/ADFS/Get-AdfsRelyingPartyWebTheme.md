---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsrelyingpartywebtheme?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsRelyingPartyWebTheme
---

# Get-AdfsRelyingPartyWebTheme

## 摘要
获取应用于依赖方信任（relying party trusts）的网页主题的相关属性。

## 语法

```
Get-AdfsRelyingPartyWebTheme [-RelyingPartyName <String[]>] [<CommonParameters>]
```

## 描述
`Get-AdfsRelyingPartyWebTheme` cmdlet 可以获取应用于依赖方信任关系的任何网页主题的属性，以及这些主题所应用的信任关系的名称。

## 示例

### 示例 1：获取一个网页主题
```
PS C:\> Get-AdfsRelyingPartyWebTheme -TargetRelyingPartyName "urn:app1"
```

此命令用于获取名为“urn:app1”的依赖方的网页主题。

## 参数

### -RelyingPartyName
指定一个依赖方名称数组，用于获取相应的网页主题（web themes）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: Name

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Remove-AdfsRelyingPartyWebTheme](./Remove-AdfsRelyingPartyWebTheme.md)

[Set-AdfsRelyingPartyWebTheme](./Set-AdfsRelyingPartyWebTheme.md)

