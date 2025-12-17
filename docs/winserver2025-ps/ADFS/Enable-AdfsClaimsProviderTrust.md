---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/enable-adfsclaimsprovidertrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-AdfsClaimsProviderTrust
---

# 启用 AdfsClaimsProviderTrust

## 摘要
使声明提供者（claims provider）对联邦服务（Federation Service）充满信任。

## 语法

### 标识符Object
```
Enable-AdfsClaimsProviderTrust -TargetClaimsProviderTrust <ClaimsProviderTrust> [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### TokenSigningCertificates
```
Enable-AdfsClaimsProviderTrust -TargetCertificate <X509Certificate2> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 标识符
```
Enable-AdfsClaimsProviderTrust -TargetIdentifier <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符Name
```
Enable-AdfsClaimsProviderTrust -TargetName <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-AdfsClaimsProviderTrust` cmdlet 可以在联邦服务（Federation Service）中启用对某个声明提供者（claims provider）的信任关系。

## 示例

### 示例 1：启用对索赔提供者的信任
```
PS C:\> Enable-AdfsClaimsProviderTrust -TargetName "Fabrikam claims provider"
```

此命令用于启用名为“Fabrikam Claims Provider”的声明提供者信任关系。

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

### -TargetCertificate
指定要启用的声明提供者信任（claims provider trust）的令牌签名证书（token-signing certificate）。

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
用于指定一个 **ClaimsProviderTrust** 对象。此 cmdlet 可以启用您所指定的声明提供者信任关系。要获取一个 **ClaimsProviderTrust** 对象，请使用 **Get-AdfsClaimsProviderTrust** cmdlet。

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
指定要启用的声明提供者信任（claims provider trust）的标识符。

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
指定要启用的声明提供者信任（claims provider trust）的名称。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System SECURITY Cryptography.X509Certificates.X509Certificate.X509Certificate2

`X509Certificate2` 对象通过 `TargetCertificate` 参数被接收。

### Microsoft.IdentityServer.PowerShellResources ClaimsProviderTrust

`ClaimsProviderTrust` 对象是通过 `TargetClaimsProviderTrust` 参数接收到的。

### System.String

字符串对象通过 *TargetIdentifier* 和 *TargetName* 参数被接收。

## 输出

### Microsoft.IdentityServer.PowerShellResources ClaimsProviderTrust

当指定*PassThru*参数时，会返回一个禁用的ClaimsProviderTrust对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* A relying party in Active Directory Federation Services (AD FS) is an organization in which web servers that host one or more web-based applications reside. Tokens and Information Cards that originate from a claims provider can then be presented and ultimately accessed by the web-based resources that are located in the relying party organization. When AD FS is configured in the role of the relying party, it acts as a partner that trusts a claims provider to authenticate users. Therefore, the relying party accesses the claims that are packaged in security tokens that come from users in the claims provider. In other words, a relying party is the organization whose web servers are protected by the resource-side federation server. The federation server in the relying party uses the security tokens that the claims provider produces to issue tokens to the web servers that are located in the relying party.

## 相关链接

[Add-AdfsClaimsProviderTrust](./Add-AdfsClaimsProviderTrust.md)

[ Disable-AdfsClaimsProviderTrust](./Disable-AdfsClaimsProviderTrust.md)

[Get-AdfsClaimsProviderTrust](./Get-AdfsClaimsProviderTrust.md)

[Remove-AdfsClaimsProviderTrust](./Remove-AdfsClaimsProviderTrust.md)

[Set-AdfsClaimsProviderTrust](./Set-AdfsClaimsProviderTrust.md)

[更新 AdfsClaimsProviderTrust](./Update-AdfsClaimsProviderTrust.md)

