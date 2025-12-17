---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-addomaincontrollerpasswordreplicationpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADDomainControllerPasswordReplicationPolicy
---

# 移除 ADDomainControllerPasswordReplicationPolicy

## 摘要
从只读域控制器的密码复制策略的允许列表或拒绝列表中移除用户、计算机和组。

## 语法

### 允许的 PRP（Public Review Process）
```
Remove-ADDomainControllerPasswordReplicationPolicy [-WhatIf] [-Confirm] -AllowedList <ADPrincipal[]>
 [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADDomainController> [-PassThru]
 [-Server <String>] [<CommonParameters>]
```

### DeniedPRP
```
Remove-ADDomainControllerPasswordReplicationPolicy [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] -DeniedList <ADPrincipal[]> [-Identity] <ADDomainController> [-PassThru]
 [-Server <String>] [<CommonParameters>]
```

## 描述
`Remove-ADDomainControllerPasswordReplicationPolicy` cmdlet 用于将一个或多个用户、计算机或组从只读域控制器（RODC）的密码复制策略的允许列表或拒绝列表中移除。

`Identity` 参数指定了用于应用密码复制策略的 RODC（Remote Domain Controller，远程域控制器）。您可以通过域控制器的 GUID、IPv4 地址、全局 IPv6 地址或 DNS 主机名来识别它；也可以通过表示该域控制器的服务器对象的名称、NTDS 设置对象的 distinguished name（唯一名称）、配置分区下的 NTDS 设置对象或服务器对象的 GUID，或者表示该域控制器的计算机对象的 distinguished name 来识别它。此外，您还可以将 `Identity` 参数设置为某个域控制器对象变量（例如 `$<localDomainControllerObject>`），或者通过管道运算符将该域控制器对象传递给 `Identity` 参数。例如，可以使用 **Get-ADDomainController** cmdlet 获取一个域控制器对象，然后通过管道运算符将其传递给 **Remove-ADDomainControllerPasswordReplicationPolicy** cmdlet。请确保使用的是只读权限的域控制器。

`AllowedList` 参数用于指定要从允许列表中移除的用户、计算机和组；同样，`DeniedList` 参数用于指定要从拒绝列表中移除的用户、计算机和组。您必须指定 ` AllowedList` 和/或 `DeniedList` 中的一个或多个参数。您可以通过唯一名称（DN）、GUID、安全标识符（SID）或安全账户管理器（SAM）账户名来识别用户、计算机或组。您还可以指定用户、计算机或组的变量，例如 `$<localUserObject>`。如果您要指定多个项目，请使用逗号分隔的列表。

## 示例

### 示例 1：从 RODC 的“允许访问的用户列表”中移除特定用户
```
PS C:\> Remove-ADDomainControllerPasswordReplicationPolicy -Identity "USER01-RODC1" -AllowedList "PattiFuller", "DavidChew"
```

此命令会将用户名为PattiFuller和DavidChew的用户从RODC USER01-RODC1上的“允许访问”的用户列表中删除。

### 示例 2：从 RODC（远程目录服务器）上的“拒绝访问”列表中移除特定用户
```
PS C:\> Remove-ADDomainControllerPasswordReplicationPolicy -Identity "USER01-RODC1" -DeniedList "ElisaDaugherty", "EvanNarvaez"
```

此命令将从 RODC FABRIKAM-RODC1 的“Denied”列表中删除用户名为 Elisa Daugherty 和 Evan Narvaez 的用户。

## 参数

### -AllowedList
指定要添加到允许将其密码复制到此 RODC 的账户列表中的用户、计算机、组或其他账户。可以通过使用逗号分隔的列表来指定多个值。该参数的可接受值为：

- A distinguished name
- A GUID  (objectGUID)
- A security identifier (objectSid)
- A Security Accounts Manager (SAM) account name  (sAMAccountName)

```yaml
Type: ADPrincipal[]
Parameter Sets: AllowedPRP
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AuthType
Specifies the authentication method to use.
The acceptable values for this parameter are:

- Negotiate or 0
- Basic or 1

The default authentication method is Negotiate.

A Secure Sockets Layer (SSL) connection is required for the Basic authentication method.

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
Prompts you for confirmation before running the cmdlet.

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
Specifies the user account credentials to use to perform this task.
The default credentials are the credentials of the currently logged on user unless the cmdlet is run from an Active Directory module for Windows PowerShell provider drive.
If the cmdlet is run from such a provider drive, the account associated with the drive is the default.

To specify this parameter, you can type a user name, such as User1 or Domain01\User01 or you can specify a **PSCredential** object.
If you specify a user name for this parameter, the cmdlet prompts for a password.

You can also create a **PSCredential** object by using a script or by using the **Get-Credential** cmdlet.
You can then set the *Credential* parameter to the **PSCredential** object.

If the acting credentials do not have directory-level permission to perform the task, Active Directory module for Windows PowerShell returns a terminating error.

Specifies the credentials for the security context under which the task is performed.
If this security context doesn't have directory level permissions to perform the task, then an error is returned by the directory.
If running under the context of an Active Directory module for Windows PowerShell provider drive, the credentials information associated with the drive is used as the default value; otherwise, the currently logged on user security context is used.

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

### -DeniedList
Specifies the users, computers, groups or other accounts to add to the list of accounts that are denied the right to replicate their passwords to this RODC.
You can specify more than one value by using a comma-separated list.
The acceptable values for this parameter are:

- A distinguished name
- A GUID  (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

```yaml
Type: ADPrincipal[]
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
- A  name of the server object
- A distinguished name of the NTDS Settings object
- A distinguished name of the server object that represents the domain controller
- A GUID of NTDS settings object under the configuration partition
- A GUID of server object under the configuration partition
- A distinguished name of the computer object that represents the domain controller

The cmdlet searches the default naming context or partition to find the object.
If two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

```yaml
Type: ADDomainController
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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
Specifies the Active Directory Domain Services instance to connect to, by providing one of the following values for a corresponding domain name or directory server.
The service may be any of the following: Active Directory Lightweight Domain Services, Active Directory Domain Services or Active Directory snapshot instance.

Specify the Active Directory Domain Services instance in one of the following ways:

Domain name values:

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for this parameter is determined by one of the following methods in the order that they are listed:

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
Shows what would happen if the cmdlet runs.
The cmdlet is not run.

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
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### None or Microsoft.ActiveDirectory.Management.ADDomainController
A read-only domain controller object is received by the *Identity* parameter.

## 输出

### None or Microsoft.ActiveDirectory.Management.ADDomainController
This cmdlet returns the modified read-only domain controller object when the *PassThru* parameter is specified.
By default, this cmdlet does not generate any output.

## 备注
* 该cmdlet不支持Active Directory轻型目录服务（AD LDS）。  
* 该cmdlet无法用于Active Directory快照。  
* 该cmdlet也无法在只读域控制器上使用。  
* 默认情况下，此cmdlet会设置**Confirm**参数，在删除指定类型的对象之前会提示用户进行确认。如果你想跳过删除前的确认提示，可以在使用该cmdlet时指定`-Confirm:$False`。

## 相关链接

[添加 AD 域控制器密码复制策略](./Add-ADDomainControllerPasswordReplicationPolicy.md)

[Get-ADDomainController](./Get-ADDomainController.md)

[Get-ADDomainControllerPasswordReplicationPolicy](./Get-ADDomainControllerPasswordReplicationPolicy.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

