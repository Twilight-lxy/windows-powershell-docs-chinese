---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 09/19/2017
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfsserverapplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsServerApplication
---

# 添加 AdFS 服务器应用程序

## 摘要
将一个服务器应用程序角色添加到 AD FS 中的应用程序中。

## 语法

### ApplicationGroupIdentifier（默认值）
```
Add-AdfsServerApplication [-ApplicationGroupIdentifier] <String> [-Name] <String> [-Identifier] <String>
 [[-RedirectUri] <String[]>] [-Description <String>] [-ADUserPrincipalName <String>]
 [-JWTSigningCertificate <X509Certificate2[]>] [-JWTSigningCertificateRevocationCheck <RevocationSetting>]
 [-JWKSUri <Uri>] [-LogoutUri <String>] [-JWKSFile <String>] [-GenerateClientSecret] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### ApplicationGroupObject
```
Add-AdfsServerApplication [-ApplicationGroup] <ApplicationGroup> [-Name] <String> [-Identifier] <String>
 [[-RedirectUri] <String[]>] [-Description <String>] [-ADUserPrincipalName <String>]
 [-JWTSigningCertificate <X509Certificate2[]>] [-JWTSigningCertificateRevocationCheck <RevocationSetting>]
 [-JWKSUri <Uri>] [-LogoutUri <String>] [-JWKSFile <String>] [-GenerateClientSecret] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Add-AdfsServerApplication` cmdlet 可以将服务器应用程序角色添加到 Active Directory Federation Services (AD FS) 中的某个应用程序中。

## 示例

## 参数

### -ADUserPrincipalName
指定与已注册的机密客户端对应的 Active Directory 账户。对于 Active Directory 账户而言，唯一可用的客户端身份验证方法是 Windows 集成身份验证（Windows Integrated Authentication，简称 WIA）。

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

### -ApplicationGroup
指定一个应用程序组。

```yaml
Type: ApplicationGroup
Parameter Sets: ApplicationGroupObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ApplicationGroupIdentifier
指定一个应用程序组ID。

```yaml
Type: String
Parameter Sets: ApplicationGroupIdentifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Description
指定一个描述信息。

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

### -GenerateClientSecret
表示此cmdlet会为客户生成一个秘密值。

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

### -Identifier
指定一个ID。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
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
指定一个 JWT 的 URI。

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
用于指定JWT签名证书的数组。该公钥证书用于验证由本客户端发布的JWT签名，以便通过使用私钥的JWT客户端认证方法在AD FS中进行身份验证。

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
指定需要对由机密客户端发送的 JWT 签名执行的撤销检查（revocation checks）。该参数的可接受值包括：

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
指定 OAuth 2.0 客户端用于向 AD FS 注册的登出（logout）URI。当 AD FS 启动登出流程时，它会通过在一个 iframe 中显示该 URI 来将客户端用户的用户代理重定向到此 URI。此参数的值必须是一个绝对 URI，可以包含查询组件，但不允许包含片段组件。只有在安装了 Windows 更新 KB4038801 之后，才能使用此参数。

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

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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
指定一组用于OAuth 2.0客户端在AD FS中注册的重定向URL。当OAuth 2.0客户端请求访问AD FS中的资源时，需要提供这些重定向URL。

客户端指定的重定向 URI 必须已经注册在 AD FS（Active Directory Federation Services）中，并且必须与该 OAuth 2.0 客户端的标识符相匹配。如果客户端 ID 和重定向 URI 对应于一个预先注册的 OAuth 2.0 客户端，并且资源所有者通过提供自己的凭据授权了访问权限，那么 AD FS 会通过将客户端的用户代理（user-agent）重定向到该重定向 URI 来颁发授权码或访问令牌。

此参数的值必须与OAuth 2.0客户端在请求授权时指定的重定向URI完全匹配。如果需要的话，还包括末尾的斜杠（/）。我们建议在重定向URI中使用更安全的协议，例如https。

对于使用 Windows Web Authentication Broker 进行身份验证的 Windows 应用程序，请使用 `ms-app://` 方案作为重定向 URI。如果您正在开发 Windows 应用程序，可以通过以下代码片段获取应用程序的重定向 URI：

```csharp
Uri redirectURI = Windows.Security Authentication.Web.WebAuthenticationBroker.GetCurrentApplicationCallbackUri();
```

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-AdfsServerApplication](./Get-AdfsServerApplication.md)

[Remove-AdfsServerApplication](./Remove-AdfsServerApplication.md)

[Set-AdfsServerApplication](./Set-AdfsServerApplication.md)

