---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsclaimsprovidertrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsClaimsProviderTrust
---

# 删除 AdfsClaimsProviderTrust

## 摘要
从联合服务（Federation Service）中移除某个声明提供者（claims provider）的信任关系。

## 语法

### 标识符Object
```
Remove-AdfsClaimsProviderTrust -TargetClaimsProviderTrust <ClaimsProviderTrust> [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### TokenSigningCertificates
```
Remove-AdfsClaimsProviderTrust -TargetCertificate <X509Certificate2> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 标识符
```
Remove-AdfsClaimsProviderTrust -TargetIdentifier <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符Name
```
Remove-AdfsClaimsProviderTrust -TargetName <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-AdfsClaimsProviderTrust` cmdlet 用于从联邦服务中删除某个声明提供者信任关系（claims provider trust）。

## 示例

### 示例 1：移除对某个声明提供者（claims provider）的信任
```
PS C:\> Remove-AdfsClaimsProviderTrust -TargetName "Fabrikam claims provider"
```

这个命令会删除名为“Fabrikam claims provider”的声明提供者信任关系。

## 参数

### -PassThru
返回一个对象，该对象表示您正在操作的项。默认情况下，此 cmdlet 不生成任何输出。

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

### -TargetCertificate
指定要移除的声明提供者信任（claims provider trust）所使用的令牌签名证书（token-signing certificate）。

```yaml
Type: X509Certificate2
Parameter Sets: TokenSigningCertificates
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetClaimsProviderTrust
用于指定一个 **ClaimsProviderTrust** 对象。该 cmdlet 可以实现您所指定的声明提供者信任关系。若要获取一个 **ClaimsProviderTrust** 对象，请使用 **Get-AdfsClaimsProviderTrust** cmdlet。

```yaml
Type: ClaimsProviderTrust
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetIdentifier
指定要删除的声明提供者信任（claims provider trust）的标识符。

```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetName
指定要删除的声明提供者信任（claims provider trust）的名称。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前会提示您进行确认。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.securityCRYPTography.X509Certificates.X509Certificate.X509Certificate2

`X509Certificate2` 对象是通过 `TargetCertificate` 参数接收到的。

### Microsoft_identityServer.PowerShellResourcesClaimsProviderTrust

`ClaimsProviderTrust` 对象是通过 `TargetClaimsProviderTrust` 参数接收到的。

### System.String

字符串对象通过 *TargetIdentifier* 和 *TargetName* 参数被接收。

## 输出

### Microsoft_identityServer.PowerShellResourcesClaimsProviderTrust

当指定*PassThru*参数时，会返回被移除的ClaimsProviderTrust对象。默认情况下，此cmdlet不会生成任何输出。


## 备注
* The claims provider collects and authenticates a user's credentials, builds up claims for that user, and packages the claims into security tokens or Information Cards. In other words, a claims provider represents the organization for whose users the claims provider issues security tokens or Information Cards on their behalf. When you configure Active Directory Federation Services (AD FS), the role of the claims provider is to enable its users to access resources that are hosted in a relying party organization by establishing one side of a federation trust relationship. After the trust is established, tokens and Information Cards can be presented to a relying party across the federation trust.

## 相关链接

[Add-AdfsClaimsProviderTrust](./Add-AdfsClaimsProviderTrust.md)

[禁用 AdfsClaimsProviderTrust](./Disable-AdfsClaimsProviderTrust.md)

[Enable-AdfsClaimsProviderTrust](./Enable-AdfsClaimsProviderTrust.md)

[Get-AdfsClaimsProviderTrust](./Get-AdfsClaimsProviderTrust.md)

[Set-AdfsClaimsProviderTrust](./Set-AdfsClaimsProviderTrust.md)

[更新 AdfsClaimsProviderTrust](./Update-AdfsClaimsProviderTrust.md)

