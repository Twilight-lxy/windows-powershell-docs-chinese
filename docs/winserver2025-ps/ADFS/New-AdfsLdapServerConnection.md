---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/new-adfsldapserverconnection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AdfsLdapServerConnection
---

# 新的 AdfsLdapServer 连接

## 摘要
创建一个连接对象。

## 语法

```
New-AdfsLdapServerConnection [-HostName] <String> [-Port <Int32>] [-SslMode <LdapSslMode>]
 [-AuthenticationMethod <LdapAuthenticationMethod>] [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`New-AdfsLdapServerConnection` cmdlet 创建一个连接对象，该对象代表用于充当声明提供者信任的轻量级目录访问协议（LDAP）文件夹。连接对象包含主机名、端口和身份验证凭据。

## 示例

### 示例 1：创建一个 LDAP 连接
```
PS C:\> $Credential = Get-Credential
PS C:\ > $LdapConn = New-AdfsLdapServerConnection -HostName "DomainContoller03.contoso.com" -Port 389 -SslMode None -AuthenticationMethod Basic -Credential $Credential
```

第一个命令使用 `Get-Credential` cmdlet 来提示用户输入用户名和密码，并将结果存储在 `$Credential` 变量中。

第二个命令用于创建一个LDAP连接。DomainController03.contoso.com是另一个森林（forest）中某个域控制器的完全限定域名（fully qualified domain name）。该命令将连接结果存储在$LdapConn变量中。

要了解此 cmdlet 是如何用于创建 LDAP 本地声明提供程序信任关系的，请参阅 **Add-AdfsLocalClaimsProviderTrust** cmdlet。

## 参数

### -AuthenticationMethod
指定本地声明提供者所信任的身份验证方法。在 Windows Server 2016 中，唯一支持的方法是基本身份验证（用户名/密码）。

```yaml
Type: LdapAuthenticationMethod
Parameter Sets: (All)
Aliases:
Accepted values: Basic, Kerberos, Negotiate

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定用于连接 LDAP 主机的凭据。要获取一个 **PSCredential** 对象，请使用 **Get-Credential** cmdlet。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HostName
指定托管LDAP文件夹的服务器的完全限定域名。Active Directory Federation Services（AD FS）会连接到该服务器以发送身份验证请求。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Port
指定 AD FS 用于连接到 LDAP 主机的端口。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SslMode
指定连接的 SSL 设置。该参数的可接受值为：

- None
- Ssl
- Tls

```yaml
Type: LdapSslMode
Parameter Sets: (All)
Aliases:
Accepted values: None, Ssl, Tls

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AdfsLocalClaimsProviderTrust](./Add-AdfsLocalClaimsProviderTrust.md)

