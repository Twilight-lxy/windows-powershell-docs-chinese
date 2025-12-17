---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adfinegrainedpasswordpolicysubject?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADFineGrainedPasswordPolicySubject
---

# 移除 ADFineGrainedPasswordPolicySubject

## 摘要
将一个或多个用户从细粒度的密码策略中移除。

## 语法

```
Remove-ADFineGrainedPasswordPolicySubject [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADFineGrainedPasswordPolicy> [-Partition <String>] [-PassThru]
 [-Server <String>] [-Subjects] <ADPrincipal[]> [<CommonParameters>]
```

## 描述
`Remove-ADFineGrainedPasswordPolicySubject` cmdlet 用于将一个或多个全局安全组及用户从细粒度密码策略中移除。

`Identity` 参数用于指定细粒度的密码策略。您可以通过其唯一名称或 GUID 来识别某个细粒度的密码策略。此外，您还可以将 `Identity` 参数设置为一个细粒度密码策略对象变量（例如 `$<localFineGrainedPasswordPolicyObject>`），或者通过管道将该细粒度密码策略对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADFineGrainedPasswordPolicy` cmdlet 获取一个细粒度密码策略对象，然后通过管道将该对象传递给 `Remove-ADFineGrainedPasswordPolicySubject` cmdlet。

`Subjects` 参数用于指定要从密码策略中移除的用户和组。您可以通过用户的唯一名称（DN，Distinguished Name）、GUID（Globally Unique Identifier）、安全标识符（SID，Security Identifier）、安全账户管理器（SAM，Security Account Manager）帐户名或规范名称来识别用户或组。此外，您还可以指定用户或组对象变量，例如 `$<localUserObject>`。如果要指定多个用户或组，请使用逗号分隔的列表。

## 示例

#### 示例 1：从多个用户中移除特定的细粒度密码策略设置
```
PS C:\> Remove-ADFineGrainedPasswordPolicySubject -Identity DlgtdAdminsPSO -Subjects BobKe,KimAb
```

此命令会从使用SAM账户名称BobKe和KimAb的用户中删除名为DlgtdAdminsPSO的细粒度密码策略主体。

### 示例 2：按名称删除细粒度的密码策略主题
```
PS C:\> Get-ADFineGrainedPasswordPolicySubject -Identity DlgtdAdminsPSO | where {$_.Name -like "*Price"} | Remove-ADFineGrainedPasswordPolicySubject -Identity DlgtdAdminsPSO
```

此命令会从名称列表中删除所有名称以“Price”结尾的科目。该名称列表适用于名为 DlgtdAdminsPSO 的细粒度密码策略。

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
在运行cmdlet之前会提示您确认是否要继续执行该操作。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

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
通过提供以下属性值之一来指定一个 Active Directory 细粒度密码策略对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A name (name)

此cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个非终止性的错误（即无法继续执行的错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个细粒度的密码策略对象实例。

```yaml
Type: ADFineGrainedPasswordPolicy
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Partition
用于指定 Active Directory 分区的唯一名称（Distinguished Name）。该唯一名称必须是当前目录服务器上支持的命名上下文之一。此 cmdlet 会在此分区中搜索由 *Identity* 参数定义的对象。

在很多情况下，如果未指定值，则会为*Partition*参数使用一个默认值。确定默认值的规则如下所示。请注意，列出的规则会按顺序依次进行评估；一旦确定了默认值，后续的规则将不再被执行。

在 Active Directory 域服务（AD DS）环境中，以下情况下会为“分区”（Partition）设置默认值：

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (nTDSDSA) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter does not take any default value.

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

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -Server
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot instance）。

以下列方式之一指定 Active Directory 域服务实例：

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

### -Subjects
指定一个或多个用户或组。要指定多个用户或组，请使用逗号分隔的列表。您可以通过以下属性值之一来识别用户或组：

- Distinguished Name (DN)
- GUID (objectGUID)
- Security Identifier (objectSid)
- SAM Account Name (sAMAccountName)

注意：括号中的标识符是该属性在 LDAP 中的显示名称。

您也可以直接将对象作为参数传递给这个参数。

```yaml
Type: ADPrincipal[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或使用 `Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy`
一个细粒度的密码策略对象通过“Identity”参数被接收。

## 输出

### 无或使用 `Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy`
当指定*PassThru*参数时，该命令会返回一个对象，该对象表示修改后的细粒度密码策略对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* This cmdlet does not work with AD LDS.
* This cmdlet does not work with an Active Directory Snapshot.
* This cmdlet does not work with a read-only domain controller.
* By default, this cmdlet has the *Confirm* parameter set, which prompts you to confirm before a removal of the specified object type can occur. To bypass prompting for confirmation before removal, you can specify `Confirm:$False` when using this cmdlet.

## 相关链接

[Add-ADFineGrainedPasswordPolicySubject](./Add-ADFineGrainedPasswordPolicySubject.md)

[Get-ADFineGrainedPasswordPolicySubject](./Get-ADFineGrainedPasswordPolicySubject.md)

