---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/add-adcomputerserviceaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ADComputerServiceAccount
---

# 添加 AD 计算机服务账户

## 摘要
将一个或多个服务账户添加到Active Directory计算机中。

## 语法

```
Add-ADComputerServiceAccount [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADComputer> [-Partition <String>] [-PassThru]
 [-Server <String>] [-ServiceAccount] <ADServiceAccount[]> [<CommonParameters>]
```

## 描述

`Add-ADComputerServiceAccount` cmdlet 可以将一个或多个计算机服务账户添加到 Active Directory 计算机上。

`Computer` 参数用于指定将托管新服务账户的 Active Directory 计算机。您可以通过计算机的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier，SID）或安全帐户管理器（Security Accounts Manager，SAM）账户名称来识别该计算机。您还可以将 `Computer` 参数设置为某个计算机对象变量（例如 `$<localComputerobject>`），或者通过管道将一个计算机对象传递给 `Computer` 参数。例如，您可以使用 `Get-ADComputer` cmdlet 获取一个计算机对象，然后将该对象通过管道传递给 `Add-ADComputerServiceAccount` cmdlet。

`ServiceAccount` 参数用于指定要添加的服务账户。您可以通过服务账户的独特名称、GUID、安全标识符（SID）或安全帐户管理器（SAM）账户名称来识别该服务账户。此外，您还可以指定服务账户对象变量，例如 `$<localServiceAccountObject>`。如果您需要指定多个账户，请使用逗号分隔的列表进行表示。

> [注意] > 添加服务账户与在本地安装服务账户是不同的操作。

## 示例

### 示例 1

```powershell
Add-ADComputerServiceAccount -Computer ComputerAcct1 -ServiceAccount SvcAcct1
```

此命令将服务账户 `SvcAcct1` 添加到计算机账户 `ComputerAcct1` 中。

### 示例 2

```powershell
Add-ADComputerServiceAccount -Computer ComputerAcct1 -ServiceAccount SvcAcct1, SvcAcct2
```

此命令将两个服务账户（`SvcAcct1` 和 `SvcAcct2`）添加到计算机账户 `ComputerAcct1` 中。

## 参数

### -AuthType

指定要使用的认证方法。该参数的可接受值包括：

- `Negotiate` or `0`
- `Basic` or `1`

默认的身份验证方法是`Negotiate`。

对于“基本”（Basic）认证方法而言，需要使用安全套接字层（Secure Sockets Layer，简称 SSL）进行连接。

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

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01\User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将该 **Credential** 对象设置为相应的参数。

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

通过提供以下属性值之一来指定一个 Active Directory 计算机对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (**objectGUID**)
- A security identifier (**objectSid**)
- Security Accounts Manager account name (**sAMAccountName**)

The cmdlet searches the default naming context or partition to find the object. If the identifier
given is a distinguished name, the partition to search is computed from that distinguished name. If
two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to a
computer object instance.

```yaml
Type: Microsoft.ActiveDirectory.Management.ADComputer
Parameter Sets: (All)
Aliases: Computer

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

Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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

### -ServiceAccount

Specifies one or more Active Directory service accounts.
The acceptable values for this parameter are:

- A distinguished name
- A GUID (**objectGUID**)
- A Security Identifier (**objectSid**)
- SAM account name (**sAMAccountName**)

```yaml
Type: Microsoft.ActiveDirectory.Management.ADServiceAccount[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft ActiveDirectory.Management.AdComputer

计算机对象是通过 `Computer` 参数接收到的。

## 输出

### 无值或 Microsoft ActiveDirectory.Management.AdComputer

当指定 **PassThru** 参数时，此 cmdlet 会返回修改后的计算机对象。默认情况下，此 cmdlet 不会产生任何输出。

## 备注

- This cmdlet does not work with AD LDS.
- This cmdlet does not work with a read-only domain controller.
- This cmdlet does not work when targeting a snapshot using the **Server** parameter.

## 相关链接

[Get-ADComputer](./Get-ADComputer.md)

[Get-ADComputerServiceAccount](./Get-ADComputerServiceAccount.md)

[ Remove-ADComputerServiceAccount](./Remove-ADComputerServiceAccount.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)
