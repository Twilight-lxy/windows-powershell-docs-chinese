---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/add-adfinegrainedpasswordpolicysubject?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ADFineGrainedPasswordPolicySubject
---

# 添加 AD FineGrainedPasswordPolicy 主题

## 摘要
将细粒度的密码策略应用到另外一些用户和组上。

## 语法

```
Add-ADFineGrainedPasswordPolicySubject [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADFineGrainedPasswordPolicy>
 [-Partition <String>] [-PassThru] [-Server <String>] [-Subjects] <ADPrincipal[]>
 [<CommonParameters>]
```

## 描述

`Add-ADFineGrainedPasswordPolicySubject` cmdlet 可将细粒度密码策略应用于一个或多个全局安全组及用户。

**Identity** 参数用于指定要应用的细粒度密码策略。您可以通过其唯一名称、GUID 或名称来识别某个细粒度密码策略。您还可以将 **Identity** 参数设置为某个细粒度密码策略对象变量（例如 `$<localPasswordPolicyObject>`），或者通过管道运算符将该细粒度密码策略对象传递给 **Identity** 参数。例如，您可以使用 `Get-ADFineGrainedPasswordPolicy` cmdlet 获取一个细粒度密码策略对象，然后通过管道运算符将该对象传递给 `Add-ADFineGrainedPasswordPolicySubject` cmdlet。

`Subjects` 参数用于指定用户和全局安全组。您可以通过用户的唯一名称（DN，即 Distinguished Name）、GUID、安全标识符（SID）或安全账户管理器（SAM）账户名称来识别相应的用户或全局安全组。此外，您还可以指定与用户和全局安全组相关的对象变量，例如 `$<localUserObject>`。如果需要指定多个用户或组，请使用逗号分隔的列表进行表示。要将用户和全局安全组对象通过管道传递给 `Subjects` 参数，可以使用 `Get-ADUser` 或 `Get-ADGroup` cmdlet 来检索这些对象，然后通过管道操作符将这些对象传递给 `Add-ADFineGrainedPasswordPolicySubject` cmdlet。

## 示例

### 示例 1

```powershell
Add-ADFineGrainedPasswordPolicySubject -Identity DomainUsersPSO -Subjects 'Domain Users'
```

此命令将名为 `DomainUsersPSO` 的细粒度密码策略应用于 `Domain Users` 全局安全组。

### 示例 2

```powershell
Add-ADFineGrainedPasswordPolicySubject -Identity DlgtdAdminsPSO -Subjects BobKe, KimAb
```

此命令将名为 `DlgtdAdminsPSO` 的细粒度密码策略应用于具有 SAM 账户名 `BobKe` 和 `KimAb` 的用户。

### 示例 3

```powershell
Add-ADFineGrainedPasswordPolicySubject -Identity DlgtdAdminsPSO -Subjects DlgtdAdminGroup
```

此命令将名为 `DlgtdAdminsPSO` 的细粒度密码策略应用到 `DlgtdAdminGroup` 组中。

### 示例 4

```powershell
Get-ADUser -Filter "lastname -eq 'Fuller'" |
    Add-ADFineGrainedPasswordPolicySubject -Identity DlgtdAdminsPSO
```

该命令将名为 `DlgtdAdminsPSO` 的细粒度密码策略应用于所有姓氏为 `Fuller` 的用户。

## 参数

### -AuthType

指定要使用的身份验证方法。该参数的可接受值包括：

- `Negotiate` or `0`
- `Basic` or `1`

默认的认证方法是`Negotiate`。

对于“基本”（Basic）认证方法来说，需要建立安全套接字层（SSL）连接。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADAuthType
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
Type: System.Management.Automation.SwitchParameter
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

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01/User01`），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 **Credential** 参数设置为这个 **PSCredential** 对象。

如果执行该任务的代理凭据没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

```yaml
Type: System.Management.Automation.PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity

通过提供以下属性值之一来指定一个 Active Directory 的细粒度密码策略对象。括号中的标识符是该属性在轻量级目录访问协议（LDAP）中的显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (**objectGUID**)
- A name (name)

该cmdlet会在默认的命名上下文或分区中搜索所需的对象。如果找到两个或多个对象，它将返回一个无法终止的错误（即程序会一直执行而不会停止）。

该参数也可以通过管道获取这个对象，或者你可以将此参数设置为一个细粒度的密码策略对象实例。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Partition

指定 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上支持的命名上下文之一。此 cmdlet 会在此分区中查找由 **Identity** 参数所定义的对象。

在很多情况下，如果未指定 `Partition` 参数的值，系统会使用一个默认值。确定默认值的规则如下所示。请注意，列出的规则会按照顺序依次被执行；一旦确定了默认值，后续的规则将不再被评估。

在 Active Directory 域服务环境中，以下情况下会为 **Partition（分区）** 设置默认值：

- If the **Identity** parameter is set to a distinguished name, the default value of **Partition**
  is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of **Partition** is
  automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of **Partition** is set to the default
  partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for
**Partition** is set in the following cases:

- If the **Identity** parameter is set to a distinguished name, the default value of **Partition**
  is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of **Partition** is
  automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of **Partition** is
  set to the default naming context. To specify a default naming context for an AD LDS environment,
  set the **msDS-defaultNamingContext** property of the Active Directory directory service agent
  (DSA) object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the **Partition** parameter will not take any default value.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru

返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不生成任何输出。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下是几种指定 Active Directory 域服务实例的方法：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

- By using the **Server** value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain Services Windows
  PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Subjects

指定一个或多个用户或组。如果要指定多个用户或组，请使用逗号分隔的列表。您可以通过以下属性值之一来识别用户或组：

- Distinguished name (DN)
- GUID (**objectGUID**)
- Security Identifier (**objectSid**)
- SAM account name (**sAMAccountName**)

注意：括号中的标识符是该属性在LDAP（轻量级目录访问协议）中的显示名称。

您也可以直接将对象传递给这个参数。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADPrincipal[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft ActiveDirectory.Management.ADFineGrainedPasswordPolicy

一个详细的密码策略对象通过 **Identity** 参数被接收。

### Microsoft ActiveDirectory.Management.AdPrincipal

一个或多个代表用户和安全组对象的主要实体会被传递给 `Subjects` 参数。`Subjects` 参数也接受派生出的主体类型（例如以下这些类型）。

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**

## 输出

### 无

### Microsoft ActiveDirectory.Management.ADFineGrainedPasswordPolicy

当指定 `PassThru` 参数时，该命令会返回修改后的细粒度密码策略对象。默认情况下，此命令不会生成任何输出。

## 备注

- This cmdlet does not work with AD LDS.
- This cmdlet does not work with a read-only domain controller.
- This cmdlet does not work with an Active Directory snapshot.

## 相关链接

[Get-ADFineGrainedPasswordPolicySubject](./Get-ADFineGrainedPasswordPolicySubject.md)

[Remove-ADFineGrainedPasswordPolicySubject](./Remove-ADFineGrainedPasswordPolicySubject.md)
