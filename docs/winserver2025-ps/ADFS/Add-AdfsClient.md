---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 09/19/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfsclient?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsClient
---

# 添加 AdfsClient

## 摘要
将一个 OAuth 2.0 客户端注册到 AD FS（Active Directory Federation Services）中。

## 语法

```
Add-AdfsClient [-ClientId] <String> [-Name] <String> [[-RedirectUri] <String[]>] [-Description <String>]
 [-ClientType <ClientType>] [-ADUserPrincipalName <String>] [-JWTSigningCertificate <X509Certificate2[]>]
 [-JWTSigningCertificateRevocationCheck <RevocationSetting>] [-JWKSUri <Uri>] [-JWKSFile <String>]
 [-LogoutUri <String>] [-GenerateClientSecret] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-AdfsClient` cmdlet 用于将 OAuth 客户端注册到 Active Directory Federation Services (AD FS) 中。为了让 OAuth 客户端能够访问由 AD FS 保护的资源，您需要使用此 cmdlet 将该客户端注册到 AD FS。

当您使用 AD FS 注册一个 OAuth 2.0 客户端时，必须为该客户端指定一个客户端标识符（client identifier）和重定向 URI（redirection URI），以及一个友好的名称（friendly name）和描述（description）。当 OAuth 客户端使用 OAuth 2.0 协议请求访问某个资源时，根据 [RFC 6749](https://tools.ietf.org/html/rfc6749) 的规定，客户端必须向 AD FS 提供相应的客户端标识符和重定向 URI。AD FS 不会允许那些指定的客户端标识符或重定向 URI 未在 AD FS 中注册的客户端访问该资源。

## 示例

#### 示例 1：添加一个客户端
```
PS C:\> Add-AdfsClient -Name "Payroll Application" -ClientId "ab762716-544d-4aeb-a526-687b73838a33" -RedirectUri "ms-app://s-1-15-2-2205112887-4282980309-3272664163-2407253042-283898840-27493891-3661245662/" -Description "OAuth 2.0 client for our Payroll application"
```

此命令使用客户端标识符、重定向URI、名称和描述，在AD FS中注册一个OAuth 2.0客户端。

### 示例 2：添加一个具有多个重定向 URI 的客户端
```
PS C:\> Add-AdfsClient -Name "Payroll Application" -ClientId "ab762716-544d-4aeb-a526-687b73838a33" -RedirectUri @("ms-app://s-1-15-2-2205112887-4282980309-3272664163-2407253042-283898840-27493891-3661245662/", "https://Contosopayrollapplication/oauthclient/") -Description "OAuth 2.0 client for our Payroll application"
```

这个命令用于在 AD FS（Active Directory Federation Services）中注册一个 OAuth 2.0 客户端。该客户端需要提供客户端标识符、两个重定向 URI（Redirect URI），以及相应的名称和描述信息。通过使用这两个不同的重定向 URI，可以表示应用程序的多种版本；这些不同版本的应用程序可能需要使用不同的重定向路径来进行身份验证或数据交换。

## 参数

### -ADUserPrincipalName
指定一个 Active Directory 用户主体名称。

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

### -ClientId
指定客户端ID。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ClientType
指定客户端类型。该参数的可接受值为：

- Public
- Confidential

```yaml
Type: ClientType
Parameter Sets: (All)
Aliases:
Accepted values: Public, Confidential

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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
表示是否生成客户端密钥。

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

### -JWKSFile
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
此参数的可接受值为：

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
指定 OAuth 2.0 客户端用于向 AD FS 注册的登出（logout）URI。当 AD FS 启动登出流程时，它会通过在一个 iframe 中显示该 URI 来将客户端用户代理（user-agent）重定向到此 URI。此参数的值必须是一个绝对 URI，可以包含查询组件（query component），但不能包含片段组件（fragment component）。只有在安装了 Windows Update KB4038801 之后，才能使用此参数。

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
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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
指定一个或多个重定向 URI。该 cmdlet 会根据您指定的重定向 URI 修改 OAuth 2.0 客户端注册信息。

OAuth 2.0 客户端在请求授权以访问由 AD FS 保护的资源时，会使用重定向 URI。您可以为一个客户端标识符注册多个重定向 URI。重定向 URI 必须是一个有效的 URI。

客户端指定的重定向URI必须已经在AD FS中注册，并且必须与该OAuth 2.0客户端的标识符相对应，这样才能授权该客户端访问资源。如果客户端ID和重定向URI对应于一个预先注册的OAuth 2.0客户端，并且资源所有者通过提供其凭据来授权访问，那么AD FS将通过将客户端用户代理重定向回这个重定向URI来提供授权码或访问令牌。

请确保 `RedirectUri` 参数的值与 OAuth 2.0 客户端在请求授权时指定的重定向 URI 完全匹配，包括可能存在的尾随斜杠（/）。在指定重定向 URI 时，请使用更安全的传输协议，例如 HTTPS。

对于使用 Windows Web Authentication Broker 进行身份验证的 Windows 应用程序，在注册重定向 URI 时，请使用 ‘ms-app://’ 格式。例如，`ms-app://s-1-15-2-1101140336-4090662585-1905587327-262951538-2732256205-1306401843-4235927180/` 是一个 Windows 应用程序的重定向 URI。如果您正在开发 Windows 应用程序，可以使用以下代码片段来获取您的应用程序的重定向 URI：

```csharp
Uri redirectURI = Windows.Security Authentication.Web.WebAuthenticationBroker.GetCurrentApplicationCallbackUri();
```

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

字符串对象通过 *ClientId*、*Description*、*Name* 和 *RedirectUri* 参数传递进来。

## 输出

### MicrosoftIdentityServer.Management.Resources.AdfsClient

当指定*PassThru*参数时，该命令会返回一个新的AdfsClient对象。默认情况下，此cmdlet不会生成任何输出。

## 备注

## 相关链接

[Disable-AdfsClient](./Disable-AdfsClient.md)

[Enable-AdfsClient](./Enable-AdfsClient.md)

[Get-AdfsClient](./Get-AdfsClient.md)

[Remove-AdfsClient](./Remove-AdfsClient.md)

[Set-AdfsClient](./Set-AdfsClient.md)

