---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsnonclaimsawarerelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsNonClaimsAwareRelyingPartyTrust
---

# 移除不支持 AdFS 非声明性信任机制的依赖方（Relaying Party）

## 摘要
从联合服务（Federation Service）中移除对非声明感知型（non-claims-aware）Web应用程序或服务的依赖方信任（relying party trust）。

## 语法

### 标识符Name（默认值）
```
Remove-AdfsNonClaimsAwareRelyingPartyTrust [-TargetName] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符
```
Remove-AdfsNonClaimsAwareRelyingPartyTrust -TargetIdentifier <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符Object
```
Remove-AdfsNonClaimsAwareRelyingPartyTrust
 -TargetNonClaimsAwareRelyingPartyTrust <NonClaimsAwareRelyingPartyTrust> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-AdfsNonClaimsAwareRelyingPartyTrust` 这个 cmdlet 会从联合服务（Federation Service）中删除那些不支持处理身份声明（claims）的非身份声明感知型（non-claims-aware）Web 应用程序或服务的依赖方信任关系（relying party trust）。

一种“不支持 claims 功能的依赖方信任”（non-claims-aware relying party trust）适用于那些不直接依赖 Active Directory Federation Services (AD FS) 来生成令牌的应用程序或服务。这类应用程序或服务会借助第三方来获取令牌，并将其转换成应用程序能够识别的格式。这种信任机制对于为不使用 AD FS 令牌的 Web 应用程序和服务定义身份验证与授权策略非常有用。Web 应用程序代理（Web Application Proxy）会为来自网络外部的请求，在进行预身份验证时向这些具有相应“不支持 claims 功能的依赖方信任”配置的应用程序或服务请求所需的令牌。

## 示例

### 示例 1：通过使用名称来移除一个不支持声明验证（claims-aware）的依赖方信任关系
```
PS C:\> Remove-AdfsNonClaimsAwareRelyingPartyTrust -TargetName "ExpenseReport"
```

此命令会删除名为ExpenseReport的应用程序所依赖的、不支持声明验证（claim verification）的第三方信任关系（relying party trust）。

### 示例 2：使用标识符移除一个不支持声明（claims）功能的依赖方信任关系
```
PS C:\> Remove-AdfsNonClaimsAwareRelyingPartyTrust -TargetIdentifier "https://Contosoexpense/"
```

此命令会删除 expense report 应用程序中那些不支持 Claim Awareness（声明感知）功能的依赖方信任关系。该应用程序的标识符为 https://Contoso.expense。

## 参数

### -TargetIdentifier
指定要删除的、不支持“非声明感知”（non-claims-aware）依赖方信任机制的标识符。

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
指定要删除的、不支持“声明感知”（claim-aware）功能的依赖方信任（relying party trust）的名称。

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
用于指定一个 **NonClaimsAwareRelyingPartyTrust** 对象。该cmdlet会删除您指定的、不支持处理身份声明（claims）的依赖方信任关系（relying party trust）。若需获取一个 **NonClaimsAwareRelyingPartyTrust** 对象，请使用 **Get-AdfsNonClaimsAwareRelyingPartyTrust** cmdlet。

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
在运行 cmdlet 之前会提示您进行确认。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[添加 AdfsNonClaimsAwareRelyingPartyTrust](./Add-AdfsNonClaimsAwareRelyingPartyTrust.md)

[禁用 AdfsNonClaimsAwareRelyingPartyTrust 功能](./ Disable-AdfsNonClaims AwareRelyingPartyTrust.md)

[Enable-AdfsNonClaimsAwareRelyingPartyTrust](./Enable-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Get-AdfsNonClaimsAwareRelyingPartyTrust](./Get-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Set-AdfsNonClaimsAwareRelyingPartyTrust](./Set-AdfsNonClaimsAwareRelyingPartyTrust.md)

