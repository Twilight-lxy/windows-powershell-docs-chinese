---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adfinegrainedpasswordpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADFineGrainedPasswordPolicy
---

# 移除 AD FineGrainedPasswordPolicy

## 摘要
删除一个Active Directory的细粒度密码策略。

## 语法

```
Remove-ADFineGrainedPasswordPolicy [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADFineGrainedPasswordPolicy> [-Server <String>] [<CommonParameters>]
```

## 描述
`Remove-ADFineGrainedPasswordPolicy` cmdlet 用于删除 Active Directory 中的细粒度密码策略。

`Identity` 参数用于指定要删除的 Active Directory 细粒度密码策略。您可以通过其 distinguished name（唯一名称）或 GUID 来识别某个细粒度密码策略。此外，您还可以将 `Identity` 参数设置为一个细粒度密码策略对象变量（例如 `$<localFineGrainedPasswordPolicyObject>`），或者通过管道将该细粒度密码策略对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADFineGrainedPasswordPolicy` cmdlet 获取一个细粒度密码策略对象，然后通过管道操作符将其传递给 `Remove-ADFineGrainedPasswordPolicy` cmdlet。

## 示例

### 示例 1：按名称删除一个细粒度的密码策略对象
```
PS C:\> Remove-ADFineGrainedPasswordPolicy -Identity MyPolicy
```

这个命令会删除名为“MyPolicy”的细粒度密码策略对象。

### 示例 2：通过区分名称删除细粒度的密码策略对象
```
PS C:\> Remove-ADFineGrainedPasswordPolicy -Identity 'CN=MyPolicy,CN=Password Settings Container,CN=System,DC=USER01,DC=COM'
```

此命令会删除名为 “DistinguishedName CN=MyPolicy,CN=Password Settings Container,CN=System,DC=USER01,DC=COM” 的细粒度密码策略对象。

### 示例 3：移除包含指定字符串的细粒度密码策略对象
```
PS C:\> Get-ADFineGrainedPasswordPolicy -Filter "Name -like '*user*'" | Remove-ADFineGrainedPasswordPolicy
```

该命令会删除所有名称中包含用户信息的细粒度密码策略对象。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值包括：

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

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认凭据将是与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行该任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
通过提供以下属性值之一来指定一个 Active Directory 细粒化的密码策略对象。括号中的标识符是该属性在轻量级目录访问协议（LDAP）中的显示名称。此参数的可接受值为：

- A distinguished name (distinguishedName)
- A GUID (objectGUID)
- A Name (name)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个非终止性的错误（即无法继续执行后续操作的错误）。

这个参数也可以通过管道运算符（pipeline operator）来获取相应的对象；或者，你可以将该参数设置为一个细粒度的密码策略对象实例。

```yaml
Type: ADFineGrainedPasswordPolicy
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此需提供以下值之一（对应于相应的域名或目录服务器）。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务、Active Directory 域服务或 Active Directory 快照实例。

以下是指定 Active Directory 域服务实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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

### -WhatIf
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy
一个细粒度的密码策略对象通过*Identity*参数被接收。

## 输出

### 无

## 备注
* This cmdlet does not work with Active Directory Lightweight Directory Services (AD LDS).
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.
* By default, this cmdlet has the *Confirm* parameter set, which prompts you to confirm before a removal of the specified object type can occur. To bypass prompting for confirmation before removal, you can specify `-Confirm:$False` when using this cmdlet.

## 相关链接

[Get-ADFineGrainedPasswordPolicy](./Get-ADFineGrainedPasswordPolicy.md)

[New-ADFineGrainedPasswordPolicy](./New-ADFineGrainedPasswordPolicy.md)

[Set-ADFineGrainedPasswordPolicy](./Set-ADFineGrainedPasswordPolicy.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

