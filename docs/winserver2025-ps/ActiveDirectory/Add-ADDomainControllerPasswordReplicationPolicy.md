---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/add-addomaincontrollerpasswordreplicationpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ADDomainControllerPasswordReplicationPolicy
---

# 添加 ADDomainControllerPasswordReplicationPolicy

## 摘要
将用户、计算机和组添加到只读域控制器密码复制策略的允许列表或拒绝列表中。

## 语法

### 允许使用的 PRP（Protocol Related Parameters）

```
Add-ADDomainControllerPasswordReplicationPolicy [-WhatIf] [-Confirm]
 -AllowedList <ADPrincipal[]> [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [[-Identity] <ADDomainController>] [-Server <String>] [<CommonParameters>]
```

### DeniedPRP

```
Add-ADDomainControllerPasswordReplicationPolicy [-WhatIf] [-Confirm]
 [-AuthType <ADAuthType>] [-Credential <PSCredential>] -DeniedList <ADPrincipal[]>
 [[-Identity] <ADDomainController>] [-Server <String>] [<CommonParameters>]
```

## 描述

`Add-ADDomainControllerPasswordReplicationPolicy` cmdlet 可将一个或多个用户、计算机和组添加到只读域控制器（RODC）的密码复制策略的允许列表或拒绝列表中。

**Identity** 参数用于指定仅读域控制器（RODC），该控制器使用允许列表和拒绝列表来应用密码复制策略。您可以通过域控制器的 GUID、IPV4Address、全球 IPV6Address 或 DNS 主机名来识别它；也可以通过表示该域控制器的服务器对象的名称、该服务器对象中的 NTDS 设置对象的 distinguished name、配置分区下该服务器对象的 NTDS 设置对象的 GUID，或者表示该域控制器的计算机对象的 distinguished name 来识别它。此外，您还可以将 **Identity** 参数设置为某个域控制器对象变量（例如 `$<localDomainControllerObject>`），或者通过管道将该域控制器对象传递给 **Identity** 参数。例如，您可以使用 `Get-ADDomainController` cmdlet 获取一个域控制器对象，然后通过管道将其传递给 `Add-ADDomainControllerPasswordReplicationPolicy` cmdlet。必须指定一个仅读域控制器；如果为此参数指定了可写域控制器，cmdlet 会返回一个未终止的错误。

**AllowedList** 参数用于指定要添加到允许列表中的用户、计算机和组；同样，**DeniedList** 参数用于指定要添加到拒绝列表中的用户、计算机和组。您必须至少指定其中一个参数（**AllowedList** 或 **DeniedList**），或者同时指定两个参数。可以通过唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier, SID）或安全帐户管理器（Security Accounts Manager, SAM）账户名来识别用户、计算机或组。您也可以指定用户、计算机或组的变量，例如 `$<localUserObject>`。如果指定了多个项目，请使用逗号分隔的列表格式。如果指定的用户、计算机或组不在允许列表或拒绝列表中，该 cmdlet 不会返回错误信息。

## 示例

### 示例 1

```powershell
$params = @{
    Identity = 'USER01-RODC1'
    AllowedList = 'PattiFuller', 'DavidChew'
}
Add-ADDomainControllerPasswordReplicationPolicy @params
```

该命令会将具有指定SamAccountNames的用户账户添加到由**Identity**参数指定的RODC（远程操作数据中心）的“允许访问”的列表中。

### 示例 2

```powershell
$params = @{
    Identity = 'USER02-RODC1'
    DeniedList = 'ElisaDaugherty', 'EvanNarvaez'
}
Add-ADDomainControllerPasswordReplicationPolicy @params
```

此命令会将具有指定SamAccountName的用户账户添加到由**Identity**参数指定的RODC（远程操作系统目录）的“Denied”列表中。

## 参数

### -AllowedList

指定要添加到允许将其密码复制到此RODC的账户列表中的用户、计算机、组或其他账户。您可以使用逗号分隔的列表来指定多个值。该参数的可接受值为：

- A distinguished name
- A GUID  (**objectGUID**)
- A security identifier (**objectSid**)
- A Security Accounts Manager (SAM) account name  (**sAMAccountName**)

```yaml
Type: Microsoft.ActiveDirectory.Management.ADPrincipal[]
Parameter Sets: AllowedPRP
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AuthType

Specifies the authentication method to use. The acceptable values for this parameter are:

- `Negotiate` or `0`
- `Basic` or `1`

The default authentication method is `Negotiate`.

A Secure Sockets Layer (SSL) connection is required for the `Basic` authentication method.

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

Prompts you for confirmation before running the cmdlet.

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

Specifies the user account credentials to use to perform this task. The default credentials are the
credentials of the currently logged on user unless the cmdlet is run from an Active Directory module
for Windows PowerShell provider drive. If the cmdlet is run from such a provider drive, the account
associated with the drive is the default.

To specify this parameter, you can type a user name, such as `User1` or `Domain01\User01` or you can
specify a **PSCredential** object. If you specify a user name for this parameter, the cmdlet prompts
for a password.

You can also create a **PSCredential** object by using a script or by using the `Get-Credential`
cmdlet. You can then set the **Credential** parameter to the **PSCredential** object.

If the acting credentials do not have directory-level permission to perform the task, Active
Directory module for Windows PowerShell returns a terminating error.

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

### -DeniedList

Specifies the users, computers, groups or other accounts to add to the list of accounts that are
denied the right to replicate their passwords to this RODC. You can specify more than one value by
using a comma-separated list. The acceptable values for this parameter are:

- A distinguished name
- A GUID  (**objectGUID**)
- A security identifier (**objectSid**)
- A Security Accounts Manager (SAM) account name  (**sAMAccountName**)

```yaml
Type: Microsoft.ActiveDirectory.Management.ADPrincipal[]
Parameter Sets: DeniedPRP
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity

Specifies an Active Directory domain controller object by providing one of the following values. The
identifier in parentheses is the Lightweight Directory Access Protocol (LDAP) display name for the
attribute. The acceptable values for this parameter are:

- A GUID (**objectGUID**)
- An IPV4Address
- A Global IPV6Address
- A   DNS Host Name (**dNSHostName**)
- A name of the server object
- A distinguished name of the NTDS Settings object
- A distinguished name of the server object that represents the domain controller
- A GUID of NTDS settings object under the configuration partition
- A GUID of server object under the configuration partition
- A distinguished name of the computer object that represents the domain controller

此cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误信息。

这个参数也可以通过管道来获取该对象，或者你可以将这个参数设置为某个对象的实例。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADDomainController
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下是指定 Active Directory 域服务实例的几种方法：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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

展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ActiveDirectory.Management ADDomainController

一个RODC对象是通过**Identity**参数接收到的。

## 输出

### 无

## 备注

- This cmdlet does not work with Active Directory Lightweight Directory Services.
- This cmdlet does not work with a read-only domain controller.
- This cmdlet does not work with an Active Directory snapshot.

## 相关链接

[Get-ADDomainController](./Get-ADDomainController.md)

[Get-ADDomainControllerPasswordReplicationPolicy](./Get-ADDomainControllerPasswordReplicationPolicy.md)
