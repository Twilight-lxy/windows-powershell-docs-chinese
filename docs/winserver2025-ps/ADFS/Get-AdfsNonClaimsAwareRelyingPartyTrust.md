---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsnonclaimsawarerelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsNonClaimsAwareRelyingPartyTrust
---

# 获取不支持AdFS非声明性身份验证（Nonclaims Aware）的依赖方信任关系（Relaying Party Trust）信息

## 摘要
获取非声明感知型 Web 应用程序或服务的依赖方信任（relying party trust）的相关属性。

## 语法

### __AllParameterSets（默认值）
```
Get-AdfsNonClaimsAwareRelyingPartyTrust [<CommonParameters>]
```

### 标识符
```
Get-AdfsNonClaimsAwareRelyingPartyTrust -TargetIdentifier <String> [<CommonParameters>]
```

### 标识符Name
```
Get-AdfsNonClaimsAwareRelyingPartyTrust [-TargetName] <String> [<CommonParameters>]
```

### 标识符Object
```
Get-AdfsNonClaimsAwareRelyingPartyTrust
 -TargetNonClaimsAwareRelyingPartyTrust <NonClaimsAwareRelyingPartyTrust> [<CommonParameters>]
```

## 描述
`Get-AdfsNonClaimsAwareRelyingPartyTrust` cmdlet 可用于获取非声明感知（non-claims-aware）Web应用程序或服务的依赖方信任（relying party trust）的相关属性。

一种“不关注声明内容”的依赖方信任（non-claims-aware relying party trust）适用于那些不直接依赖 Active Directory Federation Services (AD FS) 来生成令牌的 Web 应用程序或服务。这类应用程序或服务会依赖于第三方来获取这些令牌，并将这些令牌转换成它们能够理解的形式。这种信任机制对于为不使用 AD FS 令牌的 Web 应用程序和服务定义身份验证和授权策略非常有用。Web Application Proxy 会为来自网络外部的请求请求相应的令牌，以便对这些请求进行预身份验证。

## 示例

### 示例 1：通过名称获取一个不支持“Claims Awareness”（声明感知）功能的依赖方信任的属性
```
PS C:\> Get-AdfsNonClaimsAwareRelyingPartyTrust -TargetName "ExpenseReport"
```

此命令用于获取名为ExpenseReport的应用程序所使用的、不支持声明验证（non-claims-aware）的依赖方信任（relying party trust）的相关属性。

### 示例 2：使用标识符获取不支持 claims（声明性安全模型）的依赖方信任关系的属性
```
PS C:\> Get-AdfsNonClaimsAwareRelyingPartTrust -TargetIdentifier "https://Contosoexpense/"
```

此命令用于获取标识符为https://Contosoexpense的费用报告应用程序所使用的、不具备“声明感知”（claim-aware）功能的依赖方信任关系的相关属性。

## 参数

### -TargetIdentifier
指定要获取的、不支持声明处理的依赖方信任（relying party trust）的标识符。

```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetName
指定要获取的、不支持索赔识别的依赖方信任（relying party trust）的名称。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetNonClaimsAwareRelyingPartyTrust
用于指定一个 **NonClaimsAwareRelyingPartyTrust** 对象。该 cmdlet 可以实现您所指定的“不关注身份声明（claims）的依赖方信任”功能。若要获取一个 **NonClaimsAwareRelyingPartyTrust**，请使用 **Get-AdfsNonClaimsAwareRelyingPartyTrust** cmdlet。

```yaml
Type: NonClaimsAwareRelyingPartyTrust
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[添加 AdfsNonClaimsAwareRelyingPartyTrust](./Add-AdfsNonClaimsAwareRelyingPartyTrust.md)

[ Disable-AdfsNonClaimsAwareRelyingPartyTrust](./disable-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Enable-AdfsNonClaimsAwareRelyingPartyTrust](./Enable-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Remove-AdfsNonClaimsAwareRelyingPartyTrust](./Remove-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Set-AdfsNonClaimsAwareRelyingPartyTrust](./Set-AdfsNonClaimsAwareRelyingPartyTrust.md)

