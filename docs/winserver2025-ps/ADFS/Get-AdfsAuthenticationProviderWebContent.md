---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsauthenticationproviderwebcontent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsAuthenticationProviderWebContent
---

# 获取 AdfsAuthenticationProviderWebContent 的内容

## 摘要
为身份验证提供程序检索网页内容对象。

## 语法

```
Get-AdfsAuthenticationProviderWebContent [-Locale <CultureInfo>] [-Name <String[]>] [<CommonParameters>]
```

## 描述
`Get-AdfsAuthenticationProviderWebContent` 这个 cmdlet 可以检索所有身份验证提供程序的网页内容对象，或者特定身份验证提供程序在指定区域设置（locale）下的网页内容。您可以通过名称来指定身份验证提供程序；如果不提供身份验证提供程序的名称，该 cmdlet 会检索所有身份验证提供程序的网页内容对象。如果您没有指定区域设置，它将检索所有区域的网页内容。另外，如果您没有使用 `Set-AdfsAuthenticationProviderWebContent` cmdlet 来自定义身份验证提供程序的网页内容，那么这个 cmdlet 将不会返回任何信息。

## 示例

## 参数

### -Locale
用于指定一个区域设置（locale）。该cmdlet会获取与您指定的区域设置相关联的提供者网络内容（provider web content）。

```yaml
Type: CultureInfo
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定一个名称数组。此 cmdlet 会获取与您指定的名称关联的提供程序网页内容。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Remove-AdfsAuthenticationProviderWebContent](./Remove-AdfsAuthenticationProviderWebContent.md)

[Set-AdfsAuthenticationProviderWebContent](./Set-AdfsAuthenticationProviderWebContent.md)

