---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfslocalclaimsprovidertrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsLocalClaimsProviderTrust
---

# 添加 AdfsLocalClaimsProviderTrust

## 摘要
创建一个本地的声明提供者信任（claims provider trust）。

## 语法

```
Add-AdfsLocalClaimsProviderTrust -Name <String> -Identifier <String> [-AcceptanceTransformRules <String>]
 [-AcceptanceTransformRulesFile <String>] [-Enabled <Boolean>] [-Notes <String>]
 [-OrganizationalAccountSuffix <String[]>] [-Force] [-Type <String>] [-PassThru] [-WhatIf] [-Confirm]
 -LdapServerConnection <LdapServerConnection[]> -UserObjectClass <String> -UserContainer <String>
 -AnchorClaimLdapAttribute <String> -AnchorClaimType <String>
 [-LdapAuthenticationMethod <LdapAuthenticationMethod>]
 [-LdapAttributeToClaimMapping <LdapAttributeToClaimMapping[]>] [<CommonParameters>]
```

## 描述
`Add-AdfsLocalClaimsProviderTrust` cmdlet 用于创建一个本地声明提供者信任关系。该信任关系基于符合轻量级目录访问协议（LDAP）v3标准的目录，而非 Active Directory Federation Services (AD FS) 服务器所属的 Active Directory 域。这些目录可以包括其他不受信任的 Active Directory 林或域、Active Directory 轻量级目录服务（LDAP）目录，以及非 Active Directory 的 LDAP 目录。

## 示例

### 示例 1：创建一个 LDAP 本地声明提供者信任关系
```
PS C:\> $Credential = Get-Credential
PS C:\ > $LdapConn = New-AdfsLdapServerConnection -HostName "DomainContoller03.contoso.com" -Port 389 -SslMode None -AuthenticationMethod Basic -Credential $Credential
PS C:\ > $DisplayName = New-AdfsLdapAttributeToClaimMapping -LdapAttribute "displayName" -ClaimType "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/displayname"
PS C:\> Add-AdfsLocalClaimsProviderTrust -Name "testldap" -Identifier "urn:testldap" -Type ldap -LdapServerConnection $LdapConn -UserObjectClass user -UserContainer "CN=Users,DC=<sub_domain_name>,DC=<domain_name>,DC=com" -LdapAuthenticationMethod Basic -AnchorClaimLdapAttribute userPrincipalName -AnchorClaimType "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn" -AcceptanceTransformRules "c:[] => issue(claim=c);" -Enabled $True -OrganizationalAccountSuffix "TSQA.contoso.com" - LdapAttributeToClaimMapping $DisplayName
```

第一个命令使用 **Get-Credential** cmdlet 来提示用户输入用户名和密码。该命令将结果存储在 `$Credential` 变量中。

第二个命令使用 **New-AdfsLdapServerConnection** cmdlet 创建一个 LDAP 连接。DomainController03.contoso.com 是另一个林中域控制器的完全限定域名（FQDN）。该命令将连接结果存储在 $LdapConn 变量中。

第三个命令使用 **New-AdfsLdapAttributeToClaimMapping** cmdlet 来创建一个映射关系：将 LDAP 目录属性与某种声明类型（claim type）关联起来。

最后一个命令创建了一个LDAP声明提供者信任关系，用于在另一个不受信任的Active Directory林中验证用户身份。

## 参数

### -AcceptanceTransformRules
指定了一组需要在本地声明提供者信任（local claims provider trust）上配置的声明规则。这些规则决定了从由本地声明提供者信任所代表的合作伙伴那里接收哪些信息。

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

### -AcceptanceTransformRulesFile
指定一个文件的完整路径，该文件包含了一组用于配置本地声明提供者信任关系的声明规则。

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

### -AnchorClaimLdapAttribute
指定一个LDAP属性，用户输入的用户名将与之进行匹配，以便在LDAP目录中找到正确的用户账户。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AnchorClaimType
指定 AD FS 中锚定声明（anchor claim）的声明类型。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Enabled
表示是否启用了信任功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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

### -Identifier
指定声明提供者信任关系的ID（以URI的形式表示）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LdapAttributeToClaimMapping
用于指定 LDAP 目录属性与声明类型之间的映射关系。每一种映射都会生成一个 AD FS 声明，该声明具有相应的声明类型和 LDAP 属性值，可供 AD FS 处理规则使用。要获取这种映射关系，请使用 **New-AdfsLdapAttributeToClaimMapping** cmdlet。

```yaml
Type: LdapAttributeToClaimMapping[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LdapAuthenticationMethod
指定本地声明提供者所使用的身份验证方法。在 Windows Server 2016 中，唯一支持的身份验证方法是基本认证（用户名/密码）。

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

### -LdapServerConnection
指定一组LDAP服务器连接信息，这些连接信息将被声明提供者（claim provider）所信任并使用。要获取一个**LdapServerConnection**对象，请使用**New-AdfsLdapServerConnection** cmdlet。

```yaml
Type: LdapServerConnection[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
为本地声明提供程序信任关系指定一个名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Notes
用于指定注释内容。

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

### -OrganizationalAccountSuffix
指定一组组织账户后缀，管理员可以为这些后缀配置相应的信任设置，以便在“家庭领域发现”（Home Realm Discovery, HRD）场景中使用这些后缀与身份提供者进行交互。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不生成任何输出。

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

### -Type
指定声明提供者信任的类型。此参数的可接受值为：ActiveDirectory 和 LDAP。

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

### -UserContainer
指定一个用户容器。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserObjectClass
指定一个用户对象类。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
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
展示了如果运行该cmdlet会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Disable-AdfsLocalClaimsProviderTrust](./Disable-AdfsLocalClaimsProviderTrust.md)

[Enable-AdfsLocalClaimsProviderTrust](./Enable-AdfsLocalClaimsProviderTrust.md)

[Get-AdfsLocalClaimsProviderTrust](./Get-AdfsLocalClaimsProviderTrust.md)

[New-AdfsLdapAttributeToClaimMapping](./New-AdfsLdapAttributeToClaim Mapping.md)

[Remove-AdfsLocalClaimsProviderTrust](./Remove-AdfsLocalClaimsProviderTrust.md)

[Set-AdfsLocalClaimsProviderTrust](./Set-AdfsLocalClaimsProviderTrust.md)

