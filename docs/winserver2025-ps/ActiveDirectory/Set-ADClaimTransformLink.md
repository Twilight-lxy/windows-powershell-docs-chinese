---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adclaimtransformlink?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADClaimTransformLink
---

# Set-ADClaimTransformLink

## 摘要
将声明转换（claims transformation）应用于 Active Directory 中的一个或多个跨林信任关系（cross-forest trust relationships）。

## 语法

```
Set-ADClaimTransformLink [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADTrust> [-PassThru] [-Policy] <ADClaimTransformPolicy> [-Server <String>]
 -TrustRole <ADTrustRole> [<CommonParameters>]
```

## 描述
`Set-ADClaimTransformLink` cmdlet 可用于对 Active Directory 中的一个或多个跨林信任关系应用声明转换（claims transformation）。

## 示例

### 示例 1：在 Active Directory 中设置一个声明转换策略以实现跨林信任关系
```
PS C:\> New-ADClaimTransformPolicy -Identity DenyAllPolicy -DenyAll
PS C:\> Set-ADClaimTransformLink "corp.contoso.com" -Policy DenyAllPolicy -TrustRole Trusted
PS C:\> Set-ADClaimTransformLink "corp.contoso.com" -Policy DenyAllPolicy -TrustRole Trusting
```

此命令将声明转换策略 `DenyAllPolicy` 应用于域 `corp.contoso.com`。该规则适用于在该域同时充当受信任域和信任方域的情况下的所有场景。实际上，该规则既适用于从该域的信任伙伴传入的声明，也适用于从该域传出至其信任伙伴的声明。

由于指定的转换规则拒绝了所有发送或接收请求的尝试，因此该域名现在将拒绝来自另一个域名（即信任伙伴）的所有发送或接收请求。

### 示例 2：在 Active Directory 中为跨林信任关系设置声明转换策略
```
PS C:\> New-ADClaimTransformPolicy -Identity AllowAllExceptCompanyAndDepartmentPolicy -AllowAllExcept Company,Department
PS C:\> Get-ADTrust "corp.contoso.com" | Set-ADClaimTransformLink -Policy AllowAllExceptCompanyAndDepartmentPolicy -TrustRole Trusted
```

此命令将“AllowAllExceptCompanyAndDepartmentPolicy”这一声明转换策略应用于trustcorp.contoso.com域名。该规则适用于当该域名在信任关系中充当受信任域时的情况，即适用于从该域名流出并发送给其信任伙伴的声明（claims）。

由于指定的转换规则允许发送或接收所有类型的声明（除了“公司”和“部门”这两类声明），因此该域名现在也将允许向另一个域（即信任合作伙伴）发送除这两类声明之外的所有类型声明。

### 示例 3：在 Active Directory 中为跨林信任关系设置声明转换策略
```
PS C:\> New-ADClaimTransformPolicy -Identity HumanResourcesToHrPolicy -Rule 'C1:[Type=="ad://ext/Department:88ce6e1cc00e9524", Value=="Human Resources", ValueType=="string"] => issue(Type=C1.Type, Value="HR", ValueType=C1.ValueType);';
PS C:\> Set-ADClaimTransformLink -Identity "corp.contoso.com" -Policy HumanResourcesToHrPolicy -TrustRole Trusting
```

此命令将声明转换策略 `HumanResourcesToHrPolicy` 应用于域 `corp.contoso.com`。该规则适用于该域在信任关系中充当“受信任方”角色的情况，也就是说，该规则会应用于从该域的信任伙伴发送到该域的所有声明（claims）。

由于指定的转换规则将声明广告中的值 “Human Resources” 转换为 “HR”（地址：ad://ext/Department:88ce6e1cc00e9524），因此该域名现在也会将从另一个域名（即信任合作伙伴）接收到的声明值中的 “Human Resources” 转换为 “HR”。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。

基本身份验证方法需要使用安全套接字层（SSL）连接。

```yaml
Type: ADAuthType
Parameter Sets: (All)
Aliases:
Accepted values: Negotiate, Basic

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从此类驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果该执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

### -Identity
通过提供以下值之一来指定一个 Active Directory 组对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

```yaml
Type: ADTrust
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
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

### -Policy
指定要应用于跨林信任关系的声明转换策略。此参数不接收管道输入数据。

```yaml
Type: ADClaimTransformPolicy
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此需要提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务、Active Directory 域服务或 Active Directory 快照实例。

以下是指定 Active Directory 域服务实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain Services Windows PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

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

### -TrustRole
指定一个信任角色（以链接类型的枚举形式表示）。该参数用于说明声明转换适用于哪些信任关系中的链接。此参数的可接受值包括：

- Trusted
- Trusting

```yaml
Type: ADTrustRole
Parameter Sets: (All)
Aliases:
Accepted values: Trusted, Trusting

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ActiveDirectory.Management.ADTrust
一个信任对象通过*Identity*参数被接收。

## 输出

### 无或 Microsoft.ActiveDirectory.Management.ADTrust

## 备注

## 相关链接

[Clear-ADClaimTransformLink](./Clear-ADClaimTransformLink.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

