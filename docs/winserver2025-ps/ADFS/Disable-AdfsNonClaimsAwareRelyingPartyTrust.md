---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/disable-adfsnonclaimsawarerelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-AdfsNonClaimsAwareRelyingPartyTrust
---

# 禁用 AdfsNonClaims Aware Relying Party Trust 功能

## 摘要
对于那些不支持索赔处理（claims-aware）的 Web 应用程序或服务，该功能会禁用联邦服务（Federation Service）所提供的依赖方信任机制（relying party trust）。

## 语法

### 标识符Name（默认值）
```
Disable-AdfsNonClaimsAwareRelyingPartyTrust [-PassThru] [-TargetName] <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 标识符
```
Disable-AdfsNonClaimsAwareRelyingPartyTrust [-PassThru] -TargetIdentifier <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 标识符Object
```
Disable-AdfsNonClaimsAwareRelyingPartyTrust [-PassThru]
 -TargetNonClaimsAwareRelyingPartyTrust <NonClaimsAwareRelyingPartyTrust> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Disable-AdfsNonClaimsAwareRelyingPartyTrust` cmdlet 用于禁用联邦服务（Federation Service）中针对那些不支持“非声明性认证”（non-claims-aware）功能的 Web 应用程序或服务的依赖方信任关系。一旦依赖方信任关系被禁用，该应用程序将无法接收任何身份验证请求。对于通过 Web 应用程序代理（Web Application Proxy）发布的、且其依赖方信任关系已被禁用的应用程序而言，这将导致客户端无法正常访问这些应用程序。

“非声明感知型依赖方信任”（non-claims-aware relying party trust）是一种适用于Web应用程序或服务的信任机制。这类应用程序或服务并不直接依赖Active Directory Federation Services (AD FS)来生成令牌，而是通过第三方来获取这些令牌，并将其转换为应用程序能够识别的格式。对于那些不使用AD FS令牌的Web应用程序和服务而言，这种信任机制有助于定义相应的身份验证和授权策略。Web Application Proxy会为来自网络外部的请求请求这些令牌，以便在代理服务器对这些请求进行预身份验证处理之后，将它们传递给目标Web应用程序或服务。

## 示例

### 示例 1：通过使用名称来禁用依赖方信任
```
PS C:\> Disable-AdfsNonClaimsAwareRelyingPartyTrust -TargetName "ExpenseReport"
45495
```

此命令将禁用名为“ExpenseReport”的费用报告依赖方信任（dependency trust）。

### 示例 2：使用标识符禁用报告依赖方的信任关系
```
PS C:\> Disable-AdfsNonClaimsAwareRelyingPartyTrust -TargetIdentifier "https://Contosoexpense/"
```

此命令会禁用依赖方信任（party trust）功能，该功能的标识符为 https://Contosoexpense。

## 参数

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -TargetIdentifier
指定要禁用的、不支持“非声明性依赖方信任”（non-claims-aware relying party trust）机制的依赖方信任的标识符。

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
指定要禁用的、不支持“Claims Awareness”（声明感知）功能的依赖方信任关系的名称。

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
用于指定一个 **NonClaimsAwareRelyingPartyTrust** 对象。该 cmdlet 会禁用您所指定的、不具备“非声明感知”（non-claims-aware）功能的依赖方信任关系。若要获取一个 **NonClaimsAwareRelyingPartyTrust** 对象，请使用 **Get-AdfsNonClaimsAwareRelyingPartyTrust** cmdlet。

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
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[添加 AdfsNonClaimsAwareRelyingPartyTrust](./Add-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Enable-AdfsNonClaimsAwareRelyingPartyTrust](./Enable-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Get-AdfsNonClaimsAwareRelyingPartyTrust](./Get-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Remove-AdfsNonClaimsAwareRelyingPartyTrust](./Remove-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Set-AdfsNonClaimsAwareRelyingPartyTrust](./Set-AdfsNonClaimsAwareRelyingPartyTrust.md)

