---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/add-adprincipalgroupmembership?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ADPrincipalGroupMembership
---

# 添加 ADPrincipalGroup 成员资格

## 摘要
将一个成员添加到一个或多个Active Directory组中。

## 语法

```
Add-ADPrincipalGroupMembership [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADPrincipal> [-MemberOf] <ADGroup[]>
 [-Partition <String>] [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述

`Add-ADPrincipalGroup Membership` cmdlet 可以将用户、组、服务账户或计算机添加为一个或多个 Active Directory 组的新成员。

**Identity** 参数用于指定要添加的新用户、计算机或组。您可以通过该对象的可识别名称（distinguished name）、GUID、安全标识符（Security Identifier, SID）或安全账户管理器（Security Account Manager, SAM）帐户名称来识别该用户、组或计算机。您还可以指定一个用户/组/计算机对象变量（例如 `$<localGroupObject>`），或者通过管道将某个对象传递给 **Identity** 参数。例如，您可以使用 `Get-ADGroup` cmdlet 获取一个组对象，然后将该对象通过管道传递给 `Add-ADPrincipalGroupMembership` cmdlet；同样地，您也可以使用 `Get-ADUser` 或 `Get-ADComputer` 来获取用户或计算机对象，并将其通过管道进行传递。

这个cmdlet会从管道中收集所有的用户、计算机和组对象，然后通过一次Active Directory操作将这些对象添加到指定的组中。

`MemberOf` 参数用于指定接收新成员的组。您可以通过组的唯一名称、GUID、SID 或 SAM 账户名来识别该组，也可以使用组对象变量（例如 `$<localGroupObject>`）。如果要指定多个组，请使用逗号分隔的列表。需要注意的是，不能将组对象直接通过管道传递给 `MemberOf` 参数；如果需要通过管道将某个组添加到其他组中，应使用 `Add-ADGroupMember` cmdlet 来完成这一操作。

对于 Active Directory 轻量级目录服务（AD LDS）环境，除非满足以下两种情况，否则必须指定 **Partition** 参数：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.

要为 AD LDS 环境指定一个默认的命名上下文，请设置该 AD LDS 实例的 Active Directory 目录服务代理对象（nTDSDSA）的 **msDS-defaultNamingContext** 属性。

## 示例

#### 示例 1：向组中添加成员

```powershell
Add-ADPrincipalGroupMembership -Identity SQLAdmin1 -MemberOf DlgtdAdminsPSOGroup
```

该命令将用户名为 `SQLAdmin1` 的用户添加到名为 `DlgtdAdminsPSOGroup` 的组中。

### 示例 2：将过滤后的用户添加到某个组中

```powershell
Get-ADUser -Filter 'Name -like "*SvcAccount*"' |
    Add-ADPrincipalGroupMembership -MemberOf SvcAccPSOGroup
```

这个命令会找到所有名字中包含“SvcAccount”的用户，并将他们添加到名为“SvcAccPSOGroup”的组中。

### 示例 3：将筛选后的用户添加到某个特殊名称组（distinguished name group）中

```powershell
$params = @{
    Server = 'localhost:60000'
    SearchBase = 'DC=AppNC'
    Filter = "Title -eq 'Account Lead' -and Office -eq 'Branch1'"
}
Get-ADUser @params |
    Add-ADPrincipalGroupMembership -MemberOf "CN=AccountLeads,OU=AccountDeptOU,DC=AppNC"
```

此命令将所有位于 `Branch1` 中、在 AD LDS 实例 `localhost:60000` 上工作且职位为 “Account Lead” 的员工添加到名为 `CN=AccountLeads,OU=AccountDeptOU,DC=AppNC` 的组中。

## 参数

### -AuthType

指定要使用的身份验证方法。此参数的可接受值包括：

- `Negotiate` or `0`
- `Basic` or `1`

默认的认证方法是 `Negotiate`（协商）。

对于“基本”（Basic）认证方法来说，需要使用安全套接字层（Secure Sockets Layer，简称SSL）进行连接。

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

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果是从此类驱动器中运行 cmdlet，则默认使用与该驱动器关联的帐户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01/User01`），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，可以将这个 **Credential** 对象设置为相应的参数。

如果执行该任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

通过提供以下属性值之一来指定一个 Active Directory 主体对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- Distinguished name
- GUID (**objectGUID**)
- Security identifier (**objectSid**)
- A SAM account name (**sAMAccountName**)

The cmdlet searches the default naming context or partition to find the object. If two or more
objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to an
object instance.

Derived types, such as the following are also accepted:

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**

This example shows how to set the parameter to a distinguished name.

`-Identity  "CN=saradavis,CN=Users,DC=corp,DC=contoso,DC=com"`

This example shows how to set this parameter to a principal object instance named principalInstance.

`-Identity $principalInstance`

```yaml
Type: Microsoft.ActiveDirectory.Management.ADPrincipal
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -MemberOf

Specifies the Active Directory groups to add a user, computer, or group to as a member. You can
identify a group by providing one of the following values. Note: The identifier in parentheses is
the LDAP display name for the attribute. The acceptable values for this parameter are:

- Distinguished name
- GUID (**objectGUID**)
- Security identifier (**objectSid**)
- Security Account Manager (SAM) account name (**sAMAccountName**)

If you are specifying more than one group, use commas to separate the groups in the list.

The following example shows how to specify this parameter by using SAM account name values.

`-MemberOf "SaraDavisGroup", "JohnSmithGroup"`

```yaml
Type: Microsoft.ActiveDirectory.Management.ADGroup[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Partition

Specifies the distinguished name of an Active Directory partition. The distinguished name must be
one of the naming contexts on the current directory server. The cmdlet searches this partition to
find the object defined by the **Identity** parameter.

In many cases, a default value is used for the **Partition** parameter if no value is specified. The
rules for determining the default value are given below. Note that rules listed first are evaluated
first and once a default value can be determined, no further rules are evaluated.

In Active Directory Domain Services environments, a default value for **Partition** is set in the
following cases:

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

Returns an object representing the item with which you're working. By default, this cmdlet doesn't
generate any output.

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

Specifies the Active Directory Domain Services instance to connect to, by providing one of the
following values for a corresponding domain name or directory server. The service may be any of the
following: Active Directory Lightweight Domain Services, Active Directory Domain Services or Active
Directory snapshot instance.

Specify the Active Directory Domain Services instance in one of the following ways:

Domain name values:

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for this parameter is determined by one of the following methods in the order that
they are listed:

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

### -WhatIf

Shows what would happen if the cmdlet runs. The cmdlet isn't run.

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

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable,
-InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose,
-WarningAction, and -WarningVariable. For more information, see
[about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### Microsoft.ActiveDirectory.Management.ADPrincipal

A principal object (**Microsoft.ActiveDirectory.Management.ADPrincipal**) that represents a user,
computer or group is received by the Identity parameter. Derived types, such as the following are
also received by this parameter.

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADGroup**

## 输出

### 无值或 `Microsoft.ActiveDirectory.Management.ADPrincipal`

当指定 **PassThru** 参数时，该命令会返回一个表示已修改的用户、计算机或组对象的主体对象。默认情况下，此cmdlet不会生成任何输出。

## 备注

- This cmdlet does not work with a read-only domain controller.
- This cmdlet does not work with an Active Directory snapshot.

## 相关链接

[Add-ADGroupMember](./Add-ADGroupMember.md)

[Get-ADComputer](./Get-ADComputer.md)

[Get-ADGroup](./Get-ADGroup.md)

[Get-ADGroupMember](./Get-ADGroupMember.md)

[Get-ADPrincipalGroupMembership](./Get-ADPrincipalGroupMembership.md)

[Get-ADUser](./Get-ADUser.md)

[Remove-ADGroupMember](./Remove-ADGroupMember.md)

[Remove-ADPrincipalGroupMembership](./Remove-ADPrincipalGroupMembership.md)
