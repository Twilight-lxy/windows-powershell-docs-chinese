---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsclaimdescription?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsClaimDescription
---

# Get-AdfsClaimDescription

## 摘要
从联邦服务（Federation Service）获取索赔描述。

## 语法

### 名称（默认值）
```
Get-AdfsClaimDescription [[-Name] <String[]>] [<CommonParameters>]
```

### 标识符
```
Get-AdfsClaimDescription -ClaimType <String[]> [<CommonParameters>]
```

### ShortName
```
Get-AdfsClaimDescription -ShortName <String[]> [<CommonParameters>]
```

## 描述
`Get-AdfsClaimDescription` cmdlet 用于从联邦服务（Federation Service）中获取声明描述（claim descriptions）。这些声明描述了联邦服务所使用的各种声明类型，同时也说明了这些声明是如何在联邦元数据（federation metadata）中被发布的。您可以不使用任何参数来调用此 cmdlet，从而获取联邦服务中的所有声明描述信息。

## 示例

#### 示例 1：获取索赔描述
```powershell
PS C:\> Get-AdfsClaimDescription | Where-Object {$_.IsOffered}
```

这个命令可以获取联邦服务提供的索赔描述列表。

## 参数

### -ClaimType
指定一个包含声明类型 URI（Uniform Resource Names）或声明本身 URI 的数组。该 cmdlet 会获取您所指定的这些声明的描述信息。

```yaml
Type: String[]
Parameter Sets: Identifier
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name
指定一个需要获取的索赔描述名称数组。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -ShortName
指定用于生成和消费 JWT 令牌的声明描述的唯一简短名称（ID）。

```yaml
Type: String[]
Parameter Sets: ShortName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

`ClaimType`、`Name` 和 `ShortName` 参数接收的是字符串对象。

## 输出

### Microsoft IdentityServer.PowerShell.Resources.ClaimDescription

返回一个或多个ClaimDescription对象，这些对象代表了联邦服务的声明描述资源。

## 备注
* Use claim descriptions to configure the list of claims available to be offered or accepted by Active Directory Federation Services (AD FS).

## 相关链接

[Add-AdfsClaimDescription](./Add-AdfsClaimDescription.md)

[Remove-AdfsClaimDescription](./Remove-AdfsClaimDescription.md)

[Set-AdfsClaimDescription](./Set-AdfsClaimDescription.md)
