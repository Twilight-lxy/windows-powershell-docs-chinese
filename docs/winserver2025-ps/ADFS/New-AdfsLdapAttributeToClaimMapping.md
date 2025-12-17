---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/new-adfsldapattributetoclaimmapping?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AdfsLdapAttributeToClaimMapping
---

# 新的 AdfsLdapAttributeToClaimMapping 映射关系

## 摘要
创建一个映射关系，将LDAP文件夹中的属性与AD FS（Active Directory Federation Services）声明类型关联起来。

## 语法

```
New-AdfsLdapAttributeToClaimMapping [-LdapAttribute] <String> [[-ClaimType] <String>] [<CommonParameters>]
```

## 描述
`New-AdfsLdapAttributeToClaimMapping` cmdlet 可以在轻量级目录访问协议（LDAP）文件夹的属性与活动目录联合服务（AD FS）的声明类型之间建立映射关系。这种映射使得 LDAP 属性能够在 AD FS 中被用于声明规则的处理过程。

## 示例

### 示例 1：创建一个 LDAP 目录属性的映射关系
```
PS C:\> $DisplayName = New-AdfsLdapAttributeToClaimMapping -LdapAttribute "displayName" -ClaimType "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/displayname"
```

此命令创建了一个将LDAP目录属性与声明类型（claim type）关联起来的映射关系。该命令会将这种映射关系存储在 `$DisplayName` 变量中，以便在其他cmdlet中使用。

要了解此 cmdlet 是如何用于创建 LDAP 本地声明提供者信任关系的，请参阅 **Add-AdfsLocalClaimsProviderTrust** cmdlet。

## 参数

### -ClaimType
指定要分配给包含 LDAP 属性值的 AD FS 主张（claim）的主张类型。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LdapAttribute
指定LDAP文件夹中用于映射声明类型的属性。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AdfsLocalClaimsProviderTrust](./Add-AdfsLocalClaimsProviderTrust.md)

