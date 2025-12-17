---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 09/19/2017
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsclient?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsClient
---

# Set-AdfsClient

## 摘要
修改通过 AD FS 注册的 OAuth 2.0 客户端的注册设置。

## 语法

### 名称（默认值）
```
Set-AdfsClient [-Force] [-TargetName] <String> [-ClientId <String>] [-Name <String>] [-RedirectUri <String[]>]
 [-Description <String>] [-ADUserPrincipalName <String>] [-JWTSigningCertificate <X509Certificate2[]>]
 [-JWTSigningCertificateRevocationCheck <RevocationSetting>] [-ChangeClientSecret] [-ResetClientSecret]
 [-JWKSUri <Uri>] [-ReloadJWTSigningKeys] [-JWKSFile <String>] [-LogoutUri <String>] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### ClientId
```
Set-AdfsClient [-Force] [-TargetClientId] <String> [-ClientId <String>] [-Name <String>]
 [-RedirectUri <String[]>] [-Description <String>] [-ADUserPrincipalName <String>]
 [-JWTSigningCertificate <X509Certificate2[]>] [-JWTSigningCertificateRevocationCheck <RevocationSetting>]
 [-ChangeClientSecret] [-ResetClientSecret] [-JWKSUri <Uri>] [-ReloadJWTSigningKeys] [-JWKSFile <String>]
 [-LogoutUri <String>] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Set-AdfsClient [-Force] [-TargetClient] <AdfsClient> [-ClientId <String>] [-Name <String>]
 [-RedirectUri <String[]>] [-Description <String>] [-ADUserPrincipalName <String>]
 [-JWTSigningCertificate <X509Certificate2[]>] [-JWTSigningCertificateRevocationCheck <RevocationSetting>]
 [-ChangeClientSecret] [-ResetClientSecret] [-JWKSUri <Uri>] [-ReloadJWTSigningKeys] [-JWKSFile <String>]
 [-LogoutUri <String>] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsClient` cmdlet 用于修改在 Active Directory Federation Services (AD FS) 中注册的 OAuth 2.0 客户端的注册设置。您可以使用此 cmdlet 来更改客户端标识符、重定向 URI、名称或描述等设置，还可以为该 OAuth 2.0 客户端注册额外的重定向 URI。

## 示例

### 示例 1：修改重定向 URI
```
PS C:\> Set-AdfsClient -TargetName "Payroll Application" -RedirectUri "https://localhost"
```

此命令会更改当前在 AD FS 中注册的名为“Payroll Application”的 OAuth 2.0 客户端的重定向 URI。

### 示例 2：重命名一个 OAuth 2.0 客户端
```
PS C:\> Set-AdfsClient -TargetName "Payroll Application" -Name "Payroll Application v2"
```

此命令将当前在 AD FS 中注册的 OAuth 2.0 客户端的名称更改为“Payroll Application”。

## 参数

### -ADUserPrincipalName
指定一个 Active Directory 用户主体名称（User Principal Name）。

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

### -ClientId
指定一个字符串。该cmdlet会使用您指定的标识符来修改OAuth 2.0客户端的注册信息。

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

### -Description
指定一个描述性文字。该cmdlet会根据您提供的描述来修改OAuth 2.0客户端注册信息。

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

### -Force
强制命令运行，而无需请求用户确认。

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
该参数的可接受值为：

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
指定 OAuth 2.0 客户端用于向 AD FS 注册的登出（logout）URI。当 AD FS 启动登出流程时，它会通过在一个 iframe 中显示该 URI 来将客户端用户的用户代理（user-agent）重定向到该 URI。此参数的值必须是一个绝对 URI，可以包含查询组件（query component），但不允许包含片段组件（fragment component）。只有在安装了 Windows Update KB4038801 之后，此参数才可用。

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
用于指定一个名称。该cmdlet会根据您指定的名称来修改OAuth 2.0客户端注册信息。

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
指定一个或多个重定向 URI。此 cmdlet 会根据您指定的重定向 URI 来修改 OAuth 2.0 客户端注册信息。

OAuth 2.0 客户端在请求访问由 AD FS 保护的资源时，会使用重定向 URI。您可以为一个客户端标识符注册多个重定向 URI。重定向 URI 必须是一个有效的 URI。

客户端指定的重定向 URI必须已经注册在 AD FS（Active Directory Federation Services）中，并且必须与该 OAuth 2.0 客户端的标识符相对应，这样才能授权该客户端访问相应的资源。如果客户端 ID 和重定向 URI 对应于一个预先注册的 OAuth 2.0 客户端，并且资源所有者通过提供自己的凭据来授权访问权限，那么 AD FS 将通过将客户端的用户代理（user-agent）重定向到这个重定向 URI 来提供授权代码或访问令牌。

请确保 `RedirectUri` 参数的值与 OAuth 2.0 客户端在请求授权时指定的重定向 URI 完全匹配（包括末尾的斜杠 `/`，如果需要的话）。在指定重定向 URI 时，请使用更安全的协议，例如 https。

对于使用 Windows Web Authentication Broker 进行身份验证的 Windows 应用程序，在注册重定向 URI 时，请使用 ‘ms-app:/’ 方案。例如，`ms-app://s-1-15-2-1101140336-4090662585-1905587327-262951538-2732256205-1306401843-4235927180/` 是一个 Windows 应用程序的重定向 URI。如果您正在开发 Windows 应用程序，可以使用以下代码片段来获取应用程序的重定向 URI：

```csharp
Uri redirectURI = Windows.Security Authentication.Web.WebAuthenticationBrokerGetCurrentApplicationCallbackUri();
```

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

### -TargetClient
指定要修改的已注册的OAuth 2.0客户端。

```yaml
Type: AdfsClient
Parameter Sets: InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetClientId
指定要修改的已注册 OAuth 2.0 客户端的客户端标识符。

```yaml
Type: String
Parameter Sets: ClientId
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetName
指定要修改的已注册的 OAuth 2.0 客户端的名称。

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
在运行cmdlet之前会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被执行。

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

### MicrosoftIdentityServer.Management.Resources.AdfsClient

`AdfsClient` 对象是通过 `*TargetClient*` 参数接收到的。

### System.String

字符串对象通过 *ClientId*、*Description*、*Name*、*RedirectUri*、*TargetClientId* 和 *TargetName* 这些参数被接收。

## 输出

### MicrosoftIdentityServer.Management.Resources.AdfsClient

当指定*PassThru*参数时，该命令会返回更新后的AdfsClient对象。默认情况下，此cmdlet不会生成任何输出。

## 备注

## 相关链接

[Add-AdfsClient](./Add-AdfsClient.md)

[ Disable-AdfsClient](./Disable-AdfsClient.md)

[Enable-AdfsClient](./Enable-AdfsClient.md)

[Get-AdfsClient](./Get-AdfsClient.md)

[Remove-AdfsClient](./Remove-AdfsClient.md)

