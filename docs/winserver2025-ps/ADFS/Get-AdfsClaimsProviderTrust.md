---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsclaimsprovidertrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsClaimsProviderTrust
---

# Get-AdfsClaimsProviderTrust

## 摘要
获取联合服务（Federation Service）中使用的声明提供者信任关系（claims provider trusts）。

## 语法

### ClaimsProviderName（默认值）
```
Get-AdfsClaimsProviderTrust [[-Name] <String[]>] [<CommonParameters>]
```

### TokenSigningCertificates
```
Get-AdfsClaimsProviderTrust [-Certificate] <X509Certificate2[]> [<CommonParameters>]
```

### 标识符
```
Get-AdfsClaimsProviderTrust [-Identifier] <String[]> [<CommonParameters>]
```

## 描述
`Get-AdfsClaimsProviderTrust` cmdlet 用于获取联邦服务（Federation Service）中的声明提供者信任关系（claims provider trusts）。您可以不带任何参数使用此 cmdlet 来获取所有声明提供者信任对象。

## 示例

#### 示例 1：获取声明提供者的信任关系
```
PS C:\> Get-AdfsClaimsProviderTrust -Name "Fabrikam claims provider"
```

此命令用于获取名为“Fabrikam Claims Provider”的声明提供者（claims provider）的属性设置。

## 参数

### -Certificate
指定一个包含声明提供者信任的令牌签名证书的数组，以便获取这些证书。

```yaml
Type: X509Certificate2[]
Parameter Sets: TokenSigningCertificates
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Identifier
指定一个包含唯一ID的数组，这些ID对应于需要获取的声明提供者（claim provider）的信任信息。

```yaml
Type: String[]
Parameter Sets: Identifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name
指定一个数组，其中包含要获取的声明提供者信任关系的显示名称（display names）。

```yaml
Type: String[]
Parameter Sets: ClaimsProviderName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.Security.Cryptography.X509Certificates.X509Certificate.X509Certificate2

`X509Certificate2` 对象是通过 `Certificate` 参数接收到的。

### System.String

字符串对象通过 *Identifier*（标识符）和 *Name*（名称）参数被接收。

## 输出

### MicrosoftIdentityServer.PowerShell.ResourcesClaimsProviderTrust

返回一个或多个ClaimsProviderTrust对象，这些对象表示联邦服务（Federation Service）所使用的声明提供者信任关系（claims provider trusts）。

## 备注
* If you do not specify the *Name* parameter, the cmdlet lists all claims providers. The claims provider collects and authenticates a user's credentials, builds up claims for that user, and packages the claims into security tokens or Information Cards. In other words, a claims provider represents the organization for whose users the claims provider issues security tokens or Information Cards on their behalf. When you configure Active Directory Federation Services (AD FS), the role of the claims provider is to enable its users to access resources that are hosted in a relying party organization by establishing one side of the federation trust relationship. After the federation trust is established, tokens and Information Cards can be presented to the relying party across the trust.

## 相关链接

[Add-AdfsClaimsProviderTrust](./Add-AdfsClaimsProviderTrust.md)

[禁用 AdfsClaimsProviderTrust](./ Disable-AdfsClaimsProviderTrust.md)

[ Enable-AdfsClaimsProviderTrust](./Enable-AdfsClaimsProviderTrust.md)

[Remove-AdfsClaimsProviderTrust](./Remove-AdfsClaimsProviderTrust.md)

[Set-AdfsClaimsProviderTrust](./Set-AdfsClaimsProviderTrust.md)

[更新 AdfsClaimsProviderTrust](./Update-AdfsClaimsProviderTrust.md)

