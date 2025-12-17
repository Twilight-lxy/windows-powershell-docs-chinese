---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsrelyingpartywebcontent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsRelyingPartyWebContent
---

# 获取 AdfsRelyingPartyWebContent 的内容

## 摘要
为依赖方获取网页内容对象。

## 语法

```
Get-AdfsRelyingPartyWebContent [-Locale <CultureInfo>] [-RelyingPartyName <String[]>] [<CommonParameters>]
```

## 描述
`Get-AdfsRelyingPartyWebContent` 这个 cmdlet 可以获取依赖方的网页内容对象。你需要通过名称来指定具体的依赖方；如果未指定名称，该 cmdlet 会获取所有依赖方的网页内容对象。另外，如果你没有指定区域设置（locale），它将获取适用于所有区域的网页内容。

## 示例

### 示例 1：获取所有网页内容对象
```
PS C:\> Get-AdfsRelyingPartyWebContent
```

这个命令会获取所有依赖方和地区的网页内容对象。

### 示例 2：获取指定依赖方的网页内容对象
```
PS C:\> Get-AdfsRelyingPartyWebContent -Name "RelyingParty01"
```

这个命令会为名为“RelyingParty01”的依赖方获取所有语言环境（locales）下的网页内容对象。

### 示例 3：获取指定依赖方和区域的网页内容对象
```
PS C:\> Get-AdfsRelyingPartyWebContent -Locale en-us -Name "RelyingParty01"
```

此命令会为名为“RelyingParty01”的依赖方获取指定语言环境（locale）下的网页内容对象。

## 参数

### -Locale
用于指定一个区域设置（locale）。该 cmdlet 会获取与你指定的区域设置相对应的相关方网站内容（web content）。

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

### -RelyingPartyName
指定一个依赖方名称数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: Name

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.IdentityServerManagement.Resources.AdfsRelyingPartyWebContent

### MicrosoftIdentityServer.ManagementResources.AdfsRelyingPartyWebContent[]

此cmdlet生成一个**System.IdentityServer.ManagementResources.AdfsRelyingPartyWebContent**对象，该对象表示依赖方的网页内容；或者生成这样一个对象的数组。该对象包含以下属性：

- Locale: **System.Globalization.CultureInfo**
- Name: **System.String**
- ErrorPageGenericErrorMessage: **System.String**
- ErrorPageAuthorizationErrorMessage: **System.String**
- ErrorPageDeviceAuthenticationErrorMessage: **System.String**

## 备注

## 相关链接

[Remove-AdfsRelyingPartyWebContent](./Remove-AdfsRelyingPartyWebContent.md)

[Set-AdfsRelyingPartyWebContent](./Set-AdfsRelyingPartyWebContent.md)
