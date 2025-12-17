---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 09/19/2017
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsserverapplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsServerApplication
---

# 设置 AdfsServerApplication

## 摘要
修改 AD FS 中应用程序的服务器应用角色的配置设置。

## 语法

### 标识符（默认值）
```
Set-AdfsServerApplication [-TargetIdentifier] <String> [-Identifier <String>] [-Name <String>]
 [-RedirectUri <String[]>] [-Description <String>] [-ADUserPrincipalName <String>]
 [-JWTSigningCertificate <X509Certificate2[]>] [-JWTSigningCertificateRevocationCheck <RevocationSetting>]
 [-ChangeClientSecret] [-ResetClientSecret] [-JWKSUri <Uri>] [-ReloadJWTSigningKeys] [-JWKSFile <String>]
 [-LogoutUri <String>] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 名称
```
Set-AdfsServerApplication [-TargetName] <String> [-Identifier <String>] [-Name <String>]
 [-RedirectUri <String[]>] [-Description <String>] [-ADUserPrincipalName <String>]
 [-JWTSigningCertificate <X509Certificate2[]>] [-JWTSigningCertificateRevocationCheck <RevocationSetting>]
 [-ChangeClientSecret] [-ResetClientSecret] [-JWKSUri <Uri>] [-ReloadJWTSigningKeys] [-JWKSFile <String>]
 [-LogoutUri <String>] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ApplicationObject
```
Set-AdfsServerApplication [-TargetApplication] <ServerApplication> [-Identifier <String>] [-Name <String>]
 [-RedirectUri <String[]>] [-Description <String>] [-ADUserPrincipalName <String>]
 [-JWTSigningCertificate <X509Certificate2[]>] [-JWTSigningCertificateRevocationCheck <RevocationSetting>]
 [-ChangeClientSecret] [-ResetClientSecret] [-JWKSUri <Uri>] [-ReloadJWTSigningKeys] [-JWKSFile <String>]
 [-LogoutUri <String>] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsServerApplication` cmdlet 用于修改 Active Directory Federation Services (AD FS) 中应用程序的服务器应用角色的配置设置。

## 示例

## 参数

### -ADUserPrincipalName
指定与已注册的机密客户端相对应的 Active Directory 账户。对于 Active Directory 账户而言，唯一可用的客户端身份验证方法是 Windows 统一身份验证（Windows Integrated Authentication，简称 WIA）。

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

### -ChangeClientSecret
表示此cmdlet会更改客户端密钥的值。

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

### -Description
指定一个描述。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Identifier
指定一个ID。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -JWKSFile
指定一个包含 JSON Web Token（JWT）的文件。

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

### -JWKSUri
指定一个 JWT 的 URI（统一资源标识符）。

```yaml
Type: Uri
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -JWTSigningCertificate
用于指定JWT签名证书的数组。该公钥证书用于验证由本客户端发布的JWT的签名，以便通过使用私钥的JWT客户端认证方法在AD FS中进行身份验证。

```yaml
Type: X509Certificate2[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -JWTSigningCertificateRevocationCheck
用于指定需要对由受信任客户端发送的 JWT 签名进行的撤销检查（即验证签名是否有效）。该参数的可接受值包括：

- None
- CheckEndCert
- CheckEndCertCacheOnly
- CheckChain
- CheckChainCacheOnly
- CheckChainExcludeRoot
- CheckChainExcludeRootCacheOnly

```yaml
Type: RevocationSetting
Parameter Sets: (All)
Aliases:
Accepted values: None, CheckEndCert, CheckEndCertCacheOnly, CheckChain, CheckChainCacheOnly, CheckChainExcludeRoot, CheckChainExcludeRootCacheOnly

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogoutUri
指定 OAuth 2.0 客户端用于向 AD FS 注册的登出（logout）URI。当 AD FS 启动登出流程时，它会通过在一个 iframe 中显示该 URI 来将客户端的用户代理（user-agent）重定向到此 URI。此参数的值必须是一个绝对 URI，可以包含查询组件（query component），但不能包含片段组件（fragment component）。只有在安装了 Windows Update KB4038801 之后，才能使用此参数。

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

### -Name
指定一个名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -RedirectUri
指定一个重定向URI数组，用于OAuth 2.0客户端在AD FS（Active Directory Federation Services）中注册。当OAuth 2.0客户端请求访问AD FS中的资源时，需要提供该重定向URI以完成授权流程。

客户端指定的重定向URI必须已经注册在AD FS中，并且必须与该OAuth 2.0客户端的标识符相对应。如果客户端ID和重定向URI对应于一个预先注册的OAuth 2.0客户端，并且资源所有者通过提供自己的凭据授权访问，那么AD FS会通过将客户端的用户代理重定向到该重定向URI来交付授权码或访问令牌。

此参数的值必须与 OAuth 2.0 客户端在请求授权时指定的重定向 URI 完全匹配。这包括末尾的分号（/），如果需要的话。我们建议在重定向 URI 中使用更安全的协议，例如 HTTPS。

对于使用 Windows Web Authentication Broker 进行身份验证的 Windows 应用程序，应使用 `ms-app://` 方式来指定重定向 URI。如果您正在开发 Windows 应用程序，请使用以下代码片段来获取该应用程序的重定向 URI：

`Uri redirectURI = Windows SECURITY Authentication.Web.WebAuthenticationBroker GetCurrentApplicationCallbackUri();`

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReloadJWTSigningKeys
表示此 cmdlet 会重新加载用于生成 JWT 签名的密钥。

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

### -ResetClientSecret
表示此 cmdlet 会重置客户端密钥的值。

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

### -TargetApplication
指定服务器应用程序。

```yaml
Type: ServerApplication
Parameter Sets: ApplicationObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetIdentifier
指定服务器应用程序的ID。

```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetName
指定服务器应用程序的名称。

```yaml
Type: String
Parameter Sets: Name
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AdfsServerApplication](./Add-AdfsServerApplication.md)

[Get-AdfsServerApplication](./Get-AdfsServerApplication.md)

[Remove-AdfsServerApplication](./Remove-AdfsServerApplication.md)

