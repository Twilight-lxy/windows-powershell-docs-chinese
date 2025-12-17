---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/new-adfsorganization?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AdfsOrganization
---

# 新的 AdFS 组织

## 摘要
创建一个新的组织信息对象。

## 语法

```
New-AdfsOrganization -DisplayName <String> -OrganizationUrl <Uri> [-Name <String>] [<CommonParameters>]
```

## 描述
`New-AdfsOrganization` cmdlet 用于为 Active Directory Federation Services (AD FS) 2.0 中的一个组织创建一个信息对象。

## 示例

### 示例 1：创建一个新的组织
```
PS C:\> New-AdfsOrganization -DisplayName "Fabrikam" -OrganizationUrl https://fabrikam.com
```

此命令会在 AD FS 中添加一个名为 Fabrikam 的新组织。

## 参数

### -DisplayName
指定组织的显示名称。

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

### -Name
指定组织的名称。

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

### -OrganizationUrl
指定该组织的网址。

```yaml
Type: Uri
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.IdentityServer.PowerShell.ResourcesOrganization
此cmdlet生成一个类结构，用于表示AD FS中的组织对象。

## 备注
* You can publish this information by using the **Set-AdfsProperties** cmdlet.

## 相关链接

[Get-AdfsProperties](./Get-AdfsProperties.md)

[Set-AdfsProperties](./Set-AdfsProperties.md)

