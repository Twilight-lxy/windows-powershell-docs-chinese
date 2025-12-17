---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/enable-adaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-ADAccount
---

# 启用 AD 账户

## 摘要
启用一个 Active Directory 账户。

## 语法

```
Enable-ADAccount [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADAccount> [-Partition <String>] [-PassThru]
 [-Server <String>] [<CommonParameters>]
```

## 描述

`Enable-ADAccount` cmdlet 可用于启用 Active Directory 中的用户账户、计算机账户或服务账户。

**Identity** 参数用于指定您想要启用的 Active Directory 用户、计算机或服务账户。您可以通过该账户的 distinguished name（唯一名称）、GUID（全局唯一标识符）、Security Identifier (SID) 或 Security Accounts Manager (SAM) 账户名称来识别该账户。您也可以将 **Identity** 参数设置为某个对象变量（例如 `$<localADAccountObject>`），或者通过管道将该账户对象传递给 **Identity** 参数。例如，您可以使用 `Get-ADUser` cmdlet 获取一个账户对象，然后通过管道将其传递给 `Enable-ADAccount` cmdlet；同样地，您也可以使用 `Get-ADComputer` 和 `Search-ADAccount` 来获取账户对象。

## 示例

### 示例 1：通过身份验证来启用一个账户

```powershell
Enable-ADAccount -Identity 'PattiFul'
```

此命令为身份为 SamAccountName `PattiFul` 的账户启用相关功能。

### 示例 2：通过“Distinguished Name”启用一个账户

```powershell
Enable-ADAccount -Identity 'CN=Patti Fuller,OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM'
```

此命令为名为`CN=Patti Fuller,OU=Finance,OU>UserAccounts,DC=FABRIKAM,DC=COM`的账户启用相应功能。

### 示例 3：使用过滤器启用组织单元中的所有账户

```powershell
$params = @{
    Filter = 'Name -like "*"'
    SearchBase = 'OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM'
}
Get-ADUser @params | Enable-ADAccount
```

此命令启用组织单元（`OU=Finance,OU>UserAccounts,DC=FABRIKAM,DC=COM`）中的所有账户。

## 参数

### -AuthType

指定要使用的认证方法。该参数的可接受值为：

- `Negotiate` or `0`
- `Basic` or `1`

默认的身份验证方法是`Negotiate`（协商）。

对于“基本”（Basic）认证方法来说，需要建立安全的套接字层（Secure Sockets Layer，简称 SSL）连接。

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

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认凭据将是与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01/User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将这个 **Credential** 对象设置为相应的参数值。

如果执行该任务的账户没有目录级权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

通过提供以下属性值之一来指定一个 Active Directory 账户对象。括号中的标识符是该属性在轻量级目录访问协议（LDAP）中的显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (**objectGUID**)
- A Security Identifier (**objectSid**)
- A SAM account name (**sAMAccountName**)

该cmdlet会在默认的命名上下文或分区中搜索对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误（即不会停止执行的错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为某个账户对象实例。

以下类似的派生类型也是被接受的：

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**

```yaml
Type: Microsoft.ActiveDirectory.Management.ADAccount
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
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

Returns an object representing the item with which you're working. By default, this cmdlet does not
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

### Microsoft.ActiveDirectory.Management.ADAccount

An account object is received by the **Identity** parameter.

Derived types, such as the following, are also accepted:

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**

## 输出

### 无

## 备注

- This cmdlet doesn't work with an Active Directory snapshot.
- This cmdlet doesn't work with a read-only domain controller.

## 相关链接

[Clear-ADAccountExpiration](./Clear-ADAccountExpiration.md)

[禁用 AD 账户](./Disable-ADAccount.md)

[Get-ADAccountAuthorizationGroup](./Get-ADAccountAuthorizationGroup.md)

[Search-ADAccount](./Search-ADAccount.md)

[Set-ADAccountControl](./Set-ADAccountControl.md)

[Set-ADAccountExpiration](./Set-ADAccountExpiration.md)

[Set-ADAccountPassword](./Set-ADAccountPassword.md)

[解锁 AD 账户](./Unlock-ADAccount.md)
