---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-aduserresultantpasswordpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADUserResultantPasswordPolicy
---

# Get-ADUserResultantPasswordPolicy

## 摘要
获取用户的最终密码策略。

## 语法

```
Get-ADUserResultantPasswordPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADUser>
 [-Partition <String>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADUserResultantPasswordPolicy` cmdlet 可以获取用户的最终密码策略对象（RSoP，即 Resultant Password Policy）。该密码策略由 Active Directory 中名为 `msDS-ResultantPSO` 的属性定义。

一个用户可以关联多个密码策略对象（Password Policy Objects，简称PSO），但其中只有一个PSO是“推荐的密码策略”（Recommended Security Practice，简称RSoP）。当某个PSO直接适用于该用户，或者该PSO适用于包含该用户的Active Directory组时，该PSO就会与该用户关联起来。如果一个用户或组关联了多个PSO策略，则RSoP的值将决定应应用哪个PSO。

用户的最终密码策略（Password Policy）或角色安全要求（Role Security Requirements, RSoP）是通过以下流程确定的：

- If only one PSO is associated with a user, this PSO is the RSoP.
- If more than one PSO is associated with a user, the PSO that applies directly to the user is the RSoP.
- If more than one PSO applies directly to the user, the PSO with the lowest **msDS-PasswordSettingsPrecedence** attribute value is the RSoP and this event is logged as a warning in the Active Directory event log.
The lowest attribute value represents the highest PSO precedence.
For example, if the **msDS-PasswordSettingsPrecedence** values of two PSOs are 100 and 200, the PSO with the attribute value of 100 is the RSoP.
- If there are no PSOs that apply directly to the user, the PSOs of the global security groups that have the user as a member are compared.
The PSO with the lowest **msDS-PasswordSettingsPrecedence** value is the RSoP.

`Identity` 参数用于指定 Active Directory 用户。您可以通过用户的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier, SID）或安全账户管理器（Security Account Manager, SAM）账户名来识别用户。您还可以将该参数设置为某个用户对象变量（例如 `$<localUserObject>`），或者通过管道将用户对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADUser` cmdlet 获取一个用户对象，然后通过管道将该对象传递给 `Get-ADUserResultantPasswordPolicy` cmdlet。

## 示例

### 示例 1：获取用户的最终密码策略
```
PS C:\> Get-ADUserResultantPasswordPolicy -Identity BobKe
Name                        : DomainUsersPSO
ComplexityEnabled           : True
LockoutThreshold            : 10
ReversibleEncryptionEnabled : False
LockoutDuration             : 12:00:00
LockoutObservationWindow    : 00:15:00
MinPasswordLength           : 8
Precedence                  : 500
ObjectGUID                  : f8d2653c-9b3b-499e-b272-4c7f4268df4c
ObjectClass                 : msDS-PasswordSettings
PasswordHistoryCount        : 24
MinPasswordAge              : 1.00:00:00
MaxPasswordAge              : 60.00:00:00
AppliesTo                   : {CN=Domain Users,CN=Users,DC=FABRIKAM,DC=COM}
DistinguishedName           : CN=DomainUsersPSO,CN=Password Settings Container,CN=System,DC=FABRIKAM,DC=COM
```

这个命令会获取用户BobKe（其SAM账户名为BobKe）所适用的新密码策略。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”。

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

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Active Directory PowerShell 提供程序驱动器中运行的。如果该 cmdlet 是从此类提供程序驱动器中运行的，则默认凭据将是与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果执行该任务的代理组件没有目录级别的权限，Active Directory PowerShell 会返回一个终止错误（即程序立即退出）。

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
通过提供以下属性值之一来指定一个 Active Directory 用户对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- Security identifier (objectSid)
- SAM account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误（即不会停止执行的错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

```yaml
Type: ADUser
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Partition
指定一个 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上所支持的命名上下文之一。此 cmdlet 会在该分区中搜索由 *Identity* 参数定义的对象。

在许多情况下，如果未指定“Partition”参数的值，系统会使用默认值。确定默认值的规则如下所示。请注意，列出的规则会按顺序依次被评估；一旦确定了默认值，后续的规则将不再被执行。

在 Active Directory Domain Services (AD DS) 环境中，以下情况下会为“Partition”（分区）设置默认值：

- If the *Identity* parameter is set to a distinguished name, the default value of Partition is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* will be set to the default partition or naming context of the target domain.

In AD LDS environments, a default value for Partition will be set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* will be set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent (DSA) object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter will not take any default value.

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

### -Server
指定要连接的 AD DS 实例，为此需提供相应的域名或目录服务器之一。该服务可以是以下类型中的任意一种：AD LDS、AD DS 或 Active Directory 快照实例。

以下列方式之一指定 AD DS 实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法中的一种确定的，具体采用哪种方法取决于它们的排列顺序：

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the AD DS Windows PowerShell provider drive, when the cmdlet runs in that drive
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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ActiveDirectory.Management.ADUser
用户对象通过 *Identity* 参数被接收。

## 输出

### Microsoft ActiveDirectory.Management.ADFineGrainedPasswordPolicy
返回一个细粒度的密码策略对象，该对象代表了用户的最终密码策略。

## 备注
* This cmdlet does not work with AD LDS.
* This cmdlet does not work with an Active Directory snapshot.

## 相关链接

[Get-ADUser](./Get-ADUser.md)

