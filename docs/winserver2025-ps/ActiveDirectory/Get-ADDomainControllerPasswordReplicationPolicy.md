---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-addomaincontrollerpasswordreplicationpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADDomainControllerPasswordReplicationPolicy
---

# 获取 AD 域控制器密码复制策略

## 摘要
获取只读域控制器的密码复制策略中允许列表（allowed list）或拒绝列表（denied list）的成员信息。

## 语法

### 允许的 PRP 值（默认值）
```
Get-ADDomainControllerPasswordReplicationPolicy [-Allowed] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADDomainController> [-Server <String>] [<CommonParameters>]
```

### DeniedPRP
```
Get-ADDomainControllerPasswordReplicationPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Denied]
 [-Identity] <ADDomainController> [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADDomainControllerPasswordReplicationPolicy` cmdlet 可用于获取属于某个只读域控制器（RODC）密码复制策略的“应用列表”或“拒绝列表”中的用户、计算机、服务账户及组。若要获取“应用列表”中的成员，请指定 *AppliedList* 参数；若要获取“拒绝列表”中的成员，请指定 *DeniedList* 参数。

`Identity` 参数指定了用于应用密码复制策略的 RODC（域控制器对象）。您可以通过域控制器的 GUID、IPV4Address、IPV6Address 或 DNS 主机名来识别它。此外，您还可以通过以下方式来识别域控制器：代表该域控制器的服务器对象的名称、NTDS 设置对象的区分名称或服务器对象的名称、配置分区下 NTDS 设置对象或服务器对象的 GUID，以及代表该域控制器的计算机对象的区分名称。

您还可以将*Identity*参数设置为某个域控制器对象变量（例如`$<localDomainControllerObject>`），或者通过管道运算符将该域控制器对象传递给*Identity*参数。例如，您可以使用**Get-ADDomainController** cmdlet来检索一个域控制器对象，然后通过管道运算符将该对象传递给**Get-ADDomainControllerPasswordReplicationPolicy** cmdlet。

如果你为这个cmdlet指定了一个可写入的域控制器，那么该cmdlet会返回一个无法终止的错误。

## 示例

### 示例 1：从 RODC 域控制器密码复制策略中获取允许的账户信息，并显示每个账户的名称和对象类
```
PS C:\> Get-ADDomainControllerPasswordReplicationPolicy -Identity "USER01-RODC1" -Allowed | ft Name,ObjectClass
```

此命令从 RODC（Remote Desktop Domain Controller）域控制器的密码复制策略中获取允许使用的账户信息，同时显示每个账户的名称和对象类别。

### 示例 2：从域中的所有 RODC（远程操作系统目录）获取允许的密码复制策略列表
```
C:\PS>Get-ADDomainController -Filter "IsReadOnly -eq `$true" | Get-ADDomainControllerPasswordReplicationPolicy -Allowed

DistinguishedName : CN=Allowed RODC Password Replication Group,CN=Users,DC=Fabrikam,DC=com
Name              : Allowed RODC Password Replication Group
ObjectClass       : group
ObjectGUID        : 239b0470-7f49-472d-8fcb-4911e90b2c5e
SamAccountName    : Allowed RODC Password Replication Group
SID               : S-1-5-21-41432690-3719764436-1984117282-571
```

此命令从域中的所有 RODC（远程操作系统目录）中获取允许的密码复制策略列表。

## 参数

### -Allowed
指定搜索那些已通过只读域控制器进行身份验证的账户。

```yaml
Type: SwitchParameter
Parameter Sets: AllowedPRP
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AuthType
指定要使用的身份验证方法。此参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。

基本认证方法需要使用安全套接字层（SSL）连接。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认凭据将是与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

您也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，可以将 `Credential` 参数设置为该 `PSCredential` 对象。

如果该执行脚本的用户没有目录级别的权限来完成任务，Windows PowerShell 的 Active Directory 模块会返回一个终止错误（即程序会立即退出）。

指定用于执行任务的安全上下文的凭据。如果该安全上下文没有执行任务所需的目录级权限，目录会返回错误信息。如果在 Windows PowerShell 提供程序的 Active Directory 模块驱动器上下文中运行，则使用与该驱动器关联的凭据信息作为默认值；否则，将使用当前登录用户的身份安全上下文。

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

### -Denied
指定要添加到被禁止将密码复制到此只读域控制器（RODC）的账户列表中的用户、计算机、组或其他账户。可以通过使用逗号分隔的列表来指定多个值。该参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

```yaml
Type: SwitchParameter
Parameter Sets: DeniedPRP
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity
Specifies an Active Directory domain controller object by providing one of the following values.
The identifier in parentheses is the Lightweight Directory Access Protocol (LDAP) display name for the attribute.
The acceptable values for this parameter are:

- A GUID (objectGUID)
- An IPV4Address
- A Global IPV6Address
- A DNS Host Name (dNSHostName)
- A name of the server object
- A Distinguished Name of the NTDS Settings object
- A distinguished name of the server object that represents the domain controller
- A GUID of NTDS settings object under the configuration partition
- A GUID of server object under the configuration partition
- A distinguished name of the computer object that represents the domain controller.

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个无法终止的错误信息。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为某个对象的实例。

```yaml
Type: ADDomainController
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此需要提供相应的域名或目录服务器之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

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

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ActiveDirectory.Management.AddDomainController
域名控制器对象是通过*Identity*参数接收到的。

## 输出

### Microsoft ActiveDirectory.Management_ADPrincipal
返回一个或多个对象，这些对象表示属于域控制器密码复制策略的应用列表或拒绝列表的用户、计算机、服务账户和组。返回的列表取决于所指定的参数。

## 备注
* This cmdlet does not work with Active Directory Lightweight Directory Services.
* This cmdlet does not work when targeting a snapshot using the Server parameter.

## 相关链接

[Add-ADDomainControllerPasswordReplicationPolicy](./Add-ADDomainControllerPasswordReplicationPolicy.md)

[Remove-ADDomainControllerPasswordReplicationPolicy](./Remove-ADDomainControllerPasswordReplicationPolicy.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

