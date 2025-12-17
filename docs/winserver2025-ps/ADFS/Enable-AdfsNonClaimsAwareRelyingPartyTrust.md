---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/enable-adfsnonclaimsawarerelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-AdfsNonClaimsAwareRelyingPartyTrust
---

# 启用 AdfsNonClaimsAwareRelyingPartyTrust 功能

## 摘要
它使依赖方能够信任来自联邦服务的、不对索赔信息进行处理（即不识别或处理任何与索赔相关的数据）的Web应用程序或服务。

## 语法

### 标识符Name（默认值）
```
Enable-AdfsNonClaimsAwareRelyingPartyTrust [-PassThru] [-TargetName] <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 标识符
```
Enable-AdfsNonClaimsAwareRelyingPartyTrust [-PassThru] -TargetIdentifier <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 标识符Object
```
Enable-AdfsNonClaimsAwareRelyingPartyTrust [-PassThru]
 -TargetNonClaimsAwareRelyingPartyTrust <NonClaimsAwareRelyingPartyTrust> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
**Enable-AdfsNonClaimsAwareRelyingPartyTrust** cmdlet 用于为那些不支持处理身份声明（claims）的 Web 应用程序或服务启用依赖方信任（relying party trust）功能。当该信任被禁用后，将不允许任何身份验证操作的发生。对于通过 Web 应用程序代理（Web Application Proxy）发布的应用程序而言，必须启用相应的依赖方信任设置，才能允许网络外部的客户端通过代理访问这些应用程序。

一种“不关注声明内容”的依赖方信任（non-claims-aware relying party trust）适用于那些不直接依赖于 Active Directory Federation Services (AD FS) 来生成令牌的 Web 应用程序或服务。这类服务会借助第三方来获取这些令牌，并将它们转换成应用程序能够识别的格式。这种信任机制对于为不使用 AD FS 令牌的 Web 应用程序和服务定义身份验证与授权策略非常有用。Web 应用程序代理（Web Application Proxy）会为来自网络外部的请求请求这些令牌，以便在对这些请求进行预身份验证时使用相应的“不关注声明内容”的依赖方信任机制。

## 示例

### 示例 1：通过使用一个名称来启用一个不具备“声明意识”（即不理解或处理相关声明）的依赖方信任
```
PS C:\> Enable-AdfsNonClaimsAwareRelyingPartyTrust -TargetName "ExpenseReport"
```

此命令使名为ExpenseReport的应用程序能够获得那些不关心（或不理解）“非声明性信任”概念的依赖方的信任。

### 示例 2：通过使用标识符来启用一个不关注索赔信息的依赖方信任机制
```
PS C:\> Enable-AdfsNonClaimsAwareRelyingPartyTrust -TargetIdentifier "https://Contosoexpense/"
```

此命令使得那些不关注索赔细节的依赖方（relying parties）能够信任该费用报告应用程序；该应用程序的标识符为 https://Contosoexpense。

## 参数

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不生成任何输出。

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
指定要启用的、不支持“声明处理”（claims-aware）功能的依赖方信任（relying party trust）的标识符。

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
指定要启用的、不支持声明（claims）处理的依赖方信任（relying party trust）的名称。

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
指定一个 **NonClaimsAwareRelyingPartyTrust** 对象。该 cmdlet 可以实现您所指定的“不关注声明信息”的依赖方信任机制（即依赖方无需处理与身份验证相关的声明信息）。要获取一个 **NonClaimsAwareRelyingPartyTrust** 对象，请使用 **Get-AdfsNonClaimsAwareRelyingPartyTrust** cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AdfsNonClaimsAwareRelyingPartyTrust](./Add-AdfsNonClaimsAwareRelyingPartyTrust.md)

[禁用 AdfsNonClaimsAwareRelyingPartyTrust](./Disable-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Get-AdfsNonClaimsAwareRelyingPartyTrust](./Get-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Remove-AdfsNonClaimsAwareRelyingPartyTrust](./Remove-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Set-AdfsNonClaimsAwareRelyingPartyTrust](./Set-AdfsNonClaimsAwareRelyingPartyTrust.md)

