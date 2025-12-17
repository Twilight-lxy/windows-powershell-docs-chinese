---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfsclaimdescription?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsClaimDescription
---

# 添加 AdfsClaimDescription

## 摘要
向联邦服务添加一个声明描述（claim description）。

## 语法

```
Add-AdfsClaimDescription -Name <String> -ClaimType <String> [-ShortName <String>] [-IsAccepted <Boolean>]
 [-IsOffered <Boolean>] [-IsRequired <Boolean>] [-Notes <String>] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-AdfsClaimDescription` cmdlet 用于向联合服务（Federation Service）添加一个声明描述（claim description）。

## 示例

### 示例 1：添加索赔描述
```
PS C:\> Add-AdfsClaimDescription -Name "Role" -ClaimType "https://Fabrikam.com/role"
```

此命令为具有指定声明类型的自定义声明添加一个名为“Role”的声明描述。

## 参数

### -ClaimType
指定声明的类型（即声明的URN或URI）。所有声明描述都必须包含一个有效的URN或URI。

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

### -IsAccepted
该字段用于指示该声明是否被发布在联邦元数据中，并被视为联邦服务所接受的声明类型。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsOffered
该字段用于指示该声明是否作为联邦服务所提供的功能之一，被发布在联邦服务的元数据中。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsRequired
用于指示该声明是否作为联邦服务所要求的声明被发布在联邦元数据中。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个友好的名称，用于添加到声明描述中。

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

### -Notes
用于指定描述该声明用途的文本。此cmdlet会将这些说明添加到声明描述中。

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

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ShortName
指定一个简短的名称。

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

### -Confirm
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.IdentityServer.ManagementResources.ClaimDescription

当指定了*PassThru*参数时，会返回一个新的ClaimDescription对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* Use claim descriptions to configure the list of claims that are available to be offered or accepted by Active Directory Federation Services (AD FS).

## 相关链接

[Get-AdfsClaimDescription](./Get-AdfsClaimDescription.md)

[Remove-AdfsClaimDescription](./Remove-AdfsClaimDescription.md)

[Set-AdfsClaimDescription](./Set-AdfsClaimDescription.md)

