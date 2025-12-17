---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsauthenticationprovider?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsAuthenticationProvider
---

# Get-AdfsAuthenticationProvider

## 摘要
获取 AD FS 中所有身份验证提供程序的列表。

## 语法

```
Get-AdfsAuthenticationProvider [[-Name] <String>] [<CommonParameters>]
```

## 描述
`Get-AdfsAuthenticationProvider` cmdlet 可以获取当前在 Active Directory Federation Services (AD FS) 中注册的所有身份验证提供程序的列表。这个只读列表包括内置的身份验证提供程序和外部身份验证提供程序，以及相关的属性信息。

## 示例

#### 示例 1：获取所有已注册的身份验证提供者
```
PS C:\> Get-AdfsAuthenticationProvider
AdminName                          : Forms Authentication
AllowedForPrimaryExtranet          : True
AllowedForPrimaryIntranet          : True
AllowedForAdditionalAuthentication : False
AuthenticationMethods              : {urn:oasis:names:tc:SAML:1.0:am:password, urn:oasis:names:tc:SAML:2.0:ac:classes:Password, urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport, http://schemas.microsoft.com/ws/2008/06/identity/authenticationmethod/password}
Descriptions                       : {}
DisplayNames                       : {}
Name                               : FormsAuthentication
IdentityClaims                     : {}
IsCustom                           : False
RequiresIdentity                   : False

AdminName                          : Windows Authentication
AllowedForPrimaryExtranet          : False
AllowedForPrimaryIntranet          : True
AllowedForAdditionalAuthentication : False
AuthenticationMethods              : {urn:ietf:rfc:1510, urn:federation:authentication:windows, urn:oasis:names:tc:SAML:2.0:ac:classes:Kerberos, http://schemas.microsoft.com/ws/2008/06/identity/authenticationmethod/kerberos...} Descriptions                       : {}
DisplayNames                       : {}
Name                               : WindowsAuthentication
IdentityClaims                     : {}
IsCustom                           : False
RequiresIdentity                   : False

AdminName                          : Certificate Authentication
AllowedForPrimaryExtranet          : True
AllowedForPrimaryIntranet          : True
AllowedForAdditionalAuthentication : True
AuthenticationMethods              : {urn:ietf:rfc:2246, urn:oasis:names:tc:SAML:1.0:am:X509-PKI, urn:oasis:names:tc:SAML:2.0:ac:classes:TLSClient, urn:oasis:names:tc:SAML:2.0:ac:classes:X509...} Descriptions                       : {}
DisplayNames                       : {}
Name                               : CertificateAuthentication
IdentityClaims                     : {}
IsCustom                           : False
RequiresIdentity                   : False
```

该命令可以获取当前在 AD FS 中注册的所有身份验证提供程序。

## 参数

### -Name
指定要从 Active Directory Federation Services (AD FS) 中检索的认证提供程序的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[注册 AdfsAuthenticationProvider](./Register-AdfsAuthenticationProvider.md)

[Unregister-AdfsAuthenticationProvider](./Unregister-AdfsAuthenticationProvider.md)

