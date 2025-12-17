---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ADGroupMember
---

# 添加 AD 组成员

## 摘要
将一个或多个成员添加到 Active Directory 组中。

## 语法

```
Add-ADGroupMember [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADGroup> [-Members] <ADPrincipal[]>
 [-MemberTimeToLive <TimeSpan>] [-Partition <String>] [-PassThru] [-Server <String>]
 [-DisablePermissiveModify] [<CommonParameters>]
```

## 描述

`Add-ADGroupMember` cmdlet 可以将一个或多个用户、组、服务帐户或计算机添加为 Active Directory 组的新成员。

`Identity` 参数指定了接收新成员的 Active Directory 组。您可以通过组的 distinguished name（唯一名称）、GUID、安全标识符或 Security Account Manager (SAM) 账户名来识别该组。您还可以指定一个组对象变量（例如 `$<localGroupObject>`），或者通过管道将某个组对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADGroup` cmdlet 获取一个组对象，然后将该对象通过管道传递给 `Add-ADGroupMember` cmdlet。

`Members` 参数用于指定要添加到组中的新成员。您可以通过新成员的独特名称、GUID、安全标识符或 SAM 账户名称来识别它。您还可以指定用户、计算机和组对象变量（例如 `$<localUserObject>`）。如果要指定多个新成员，请使用逗号分隔的列表。不能通过管道将用户、计算机或组对象传递给此 cmdlet。要通过管道将用户、计算机或组对象添加到组中，请使用 `Add-ADPrincipalGroupMembership` cmdlet。

对于 Active Directory 轻量级目录服务（AD LDS）环境，必须指定 **Partition** 参数，以下两种情况除外：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.
- To specify a default naming context for an AD LDS environment, set the
  **msDS-defaultNamingContext** property of the Active Directory directory service agent object
  (nTDSDSA) for the AD LDS instance.

## 示例

### 示例 1

```powershell
Add-ADGroupMember -Identity SvcAccPSOGroup -Members SQL01, SQL02
```

该命令将用户名为 `SQL01` 和 `SQL02` 的用户账户添加到 `SvcAccPSOGroup` 组中。

### 示例 2

```powershell
$params = @{
    Server = 'localhost:60000'
    SearchBase = 'OU=AccountDeptOU,DC=AppNC'
    Filter = "name -like 'AccountLeads'"
}
Get-ADGroup @params |
    Add-ADGroupMember -Members 'CN=PattiFuller,OU=AccountDeptOU,DC=AppNC'
```

这个命令从 AD LDS 实例 `localhost:60000` 中的组织单元 `OU=AccountDeptOU,DC=AppNC` 中获取一个名为 `AccountLeads` 的组，然后将该组传递给 `Add-ADGroupMember` 命令；`Add-ADGroupMember` 命令会将用户名为 `CN=PattiFuller,OU=AccountDeptOU,DC=AppNC` 的用户账户添加到该组中。

### 示例 3

```powershell
$userParams = @{
    Identity = 'CN=Chew David,OU=UserAccounts,DC=NORTHAMERICA,DC=FABRIKAM,DC=COM'
    Server = 'northamerica.fabrikam.com'
}
$User = Get-ADUser @userParams
$groupParams = @{
    Identity = 'CN=AccountLeads,OU=UserAccounts,DC=EUROPE,DC=FABRIKAM,DC=COM'
    Server = 'europe.fabrikam.com'
}
$Group = Get-ADGroup @groupParams
Add-ADGroupMember -Identity $Group -Members $User -Server "europe.fabrikam.com"
```

此命令将用户 `CN=Chew David,OU/UserAccounts` 从北美域添加到欧洲域中的组 `CN=AccountLeads,OU>UserAccounts`。

## 参数

### -AuthType

指定要使用的认证方法。该参数的可接受值包括：

- `Negotiate` or `0`
- `Basic` or `1`

默认的身份验证方法是`Negotiate`。

基本（Basic）身份验证方法需要使用安全套接字层（Secure Sockets Layer，简称SSL）连接。

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

在运行cmdlet之前会提示您进行确认。

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

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01<User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将这个 **Credential** 对象设置为相应的参数。

如果执行该任务的代理进程没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

### -DisablePermissiveModify

组成员信息的更新默认采用“允许修改”的设置。这种机制可以避免在尝试添加已经属于该组的成员时出现错误。当使用此参数时，系统会返回一条错误信息：“指定的账户名称已经是该组的成员”。

此参数在安装了2020年9月更新的Windows Server 2019系统中可用。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity

通过提供以下值之一来指定一个 Active Directory 组对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (**objectGUID**)
- A security identifier (**objectSid**)
- Security Accounts Manager account name (**sAMAccountName**)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个无法终止的错误（即程序会持续显示错误信息而无法继续执行）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为某个对象的实例。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADGroup
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -MemberTimeToLive

为新组成员指定生存时间（Time to Live，简称 TTL）。

```yaml
Type: System.TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Members

指定一个由用户对象、组对象和计算机对象组成的数组，这些对象以逗号分隔的列表形式存在，用于添加到某个组中。为了标识每个对象，请使用以下属性值之一。括号中的标识符是LDAP显示名称。该参数的可接受值为：

- Distinguished name
- GUID (**objectGUID**)
- Security identifier (**objectSid**)
- SAM account name (**sAMAccountName**)

您也可以直接将对象提供给这个参数。

以下示例展示了如何指定这个参数。

这个示例通过指定用户的唯一名称（Distinguished Name）和SAM账户名称属性来指定要添加的用户和组。

```  
-Members "CN=SaraDavis,CN=employees,CN=Users,DC=contoso,DC=com", "saradavisreports"  
```

这个示例指定了一个用户和一个组对象，这两个对象是在当前的 Windows PowerShell 会话中定义的，并作为参数的输入值。

`-成员：$userObject、$GroupObject`

此参数所指定的对象会被作为 **Microsoft.ActiveDirectory.Management_ADPrincipal** 对象进行处理。此外，该参数还会接收各种派生类型（如下所示）。

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADGroup**

You cannot pass objects through the pipeline to this parameter.

```yaml
Type: Microsoft.ActiveDirectory.Management.ADPrincipal[]
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

### Microsoft.ActiveDirectory.Management.ADGroup

A group object is received by the **Identity** parameter.

## 输出

### 无值或 Microsoft.ActiveDirectory.Management.ADGroup

当指定 **PassThru** 参数时，会返回修改后的组对象。默认情况下，此 cmdlet 不生成任何输出。

## 备注

- This cmdlet does not work with a read-only domain controller.
- This cmdlet does not work with an Active Directory snapshot.
- This cmdlet will allow you to add a group as a member of itself which could lead to unstable
  behavior.

## 相关链接

[Add-ADPrincipalGroupMembership](./Add-ADPrincipalGroupMembership.md)

[Get-ADGroup](./Get-ADGroup.md)

[Get-ADGroupMember](./Get-ADGroupMember.md)

[Get-ADPrincipalGroupMembership](./Get-ADPrincipalGroupMembership.md)

[Remove-ADGroupMember](./Remove-ADGroupMember.md)

[Remove-ADPrincipalGroupMembership](./Remove-ADPrincipalGroupMembership.md)
