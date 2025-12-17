---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/move-addirectoryserveroperationmasterrole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Move-ADDirectoryServerOperationMasterRole
---

# 移动 AD 目录服务器操作主角色

## 摘要
将操作主控角色的功能转移到 Active Directory 目录服务器上。

## 语法

```
Move-ADDirectoryServerOperationMasterRole [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Force] [-Identity] <ADDirectoryServer>
 [-OperationMasterRole] <ADOperationMasterRole[]> [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述
`Move-ADDirectoryServerOperationMasterRole` cmdlet 可以将一个或多个操作主角色（operation master roles）移动到目录服务器上。如果两个域中的凭据相同，你也可以将这些操作主角色移动到属于不同域的目录服务器上。

`Identity` 参数用于指定接收角色的目录服务器。您可以通过以下值之一来指定目录服务器对象：

- Name of the server object (name)
- The distinguished name of the NTDS Settings object
- The distinguished name of the server object that represents the directory server
- GUID (objectGUID) of server object under the configuration partition
- GUID (objectGUID) of NTDS settings object under the configuration partition

For Active Directory Lightweight Directory Services (AD LDS) instances the syntax for the server object name is `<computer-name>$<instance-name>`.
The following is an example of this syntax:

`asia-w7-vm4$instance1`

When you type this value in Windows PowerShell, you must use the backtick (\`) as an escape character for the dollar sign ($).
Therefore, for this example, you would type the following:

*asia-w7-vm4\`$instance1*

You can also set the parameter to a directory server object variable, such as `$<localDirectoryServerObject>`.

The **Move-ADDirectoryServerOperationMasterRole** cmdlet provides two options for moving operation master roles:

**Role transfer**, which involves transferring roles to be moved by running the cmdlet using the *Identity* parameter to specify the current role holder and the *OperationMasterRole* parameter to specify the roles for transfer.
This is the recommended option.

Operation roles include PDCEmulator, RIDMaster, InfrastructureMaster, SchemaMaster, or DomainNamingMaster.
To specify more than one role, use a comma-separated list.

**Role seizure**, which involves seizing roles you previously attempted to transfer by running the cmdlet a second time using the same parameters as the transfer operation, and adding the *Force* parameter.
The *Force* parameter must be used as a switch to indicate that seizure, instead of transfer, of operation master roles is being performed.
This operation still attempts graceful transfer first, then seizes if transfer is not possible.

Unlike using Ntdsutil.exe to move operation master roles, the **Move-ADDirectoryServerOperationMasterRole** cmdlet can be remotely executed from any domain joined computer where the Active Directory module for Windows PowerShell administration module is installed and available for use.
This can make the process of moving roles simpler and easier to centrally administer as each of the two command operations required can be run remotely and do not have to be locally executed at each of the corresponding role holders involved in the movement of the roles, for instance, role transfer only allowed at the old role holder, role seizure only allowed at the new role holder.

## 示例

### Example 1: Move a PDC emulator to a domain controller
```
PS C:\> Move-ADDirectoryServerOperationMasterRole -Identity "USER01-DC1" -OperationMasterRole PDCEmulator
```

This command moves the primary domain controller (PDC) Emulator role to the domain controller USER01-DC1.

### Example 2: Move the PDC emulator and schema master roles to a domain controller
```
PS C:\> Move-ADDirectoryServerOperationMasterRole -Identity "USER02-DC2" -OperationMasterRole PDCEmulator,SchemaMaster
```

This command moves the PDC Emulator and schema master roles to the domain controller USER02-DC2.

### Example 3: Move the schema master FSMO owner to the AD LDS instance on a server
```
PS C:\> Move-ADDirectoryServerOperationMasterRole -Identity User03-DC`$instance1 -OperationMasterRole schemaMaster -Server User03-DC:50000
```

This command moves the schema master flexible single master operations (FSMO) owner to the AD LDS instance instance1 on the server User03-DC.

### Example 4: Seize specific roles for a specified user
```
PS C:\> Move-ADDirectoryServerOperationMasterRole -Identity USER04-DC1 -OperationMasterRole RIDMaster,InfrastructureMaster,DomainNamingMaster -Force
```

This command seizes the roles RID master, infrastructure master, and domain naming master.

### Example 5: Transfer roles to a specific domain controller
```
PS C:\> $Server = Get-ADDomainController -Identity "TK5-CORP-DC-10.fabrikam.com"
PS C:\> Move-ADDirectoryServerOperationMasterRole -Identity $Server -OperationMasterRole SchemaMaster,DomainNamingMaster,PDCEmulator,RIDMaster,InfrastructureMaster
```

This command transfers the FSMO role to the specified domain controller.
When using the fully qualified domain name (FQDN) to identify the domain controller, the **Get-ADDomainController** cmdlet must be used first as a preliminary step.
There is a known issue where the **Move-ADDirectoryServerOperationMasterRole** cmdlet fails when an FQDN is specified directly as the value of the *Identity* parameter.

## 参数

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

### -Force
Indicates that the cmdlet is used for seize operations on domain controllers with the flexible single master operations (FSMO) role.

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

### -Identity
Specifies an Active Directory server object by providing one of the following values.
The identifier in parentheses is the Lightweight Directory Access Protocol (LDAP) display name for the attribute.

- Name of the server object (name)

For Active Directory Lightweight Directory Services (AD LDS) instances the syntax is of a name is `<computer-name>$<instance-name>`.

Note: When you type this value in Windows PowerShell, you must use the backtick (\`) as an escape character for the dollar sign ($).
For instance, *asia-w7-vm4\`$instance1*.

For other Active Directory instances, use the value of the name property.

- The distinguished name of the NTDS Settings object
- The distinguished name of the server object that represents the directory server
- GUID (objectGUID) of server object under the configuration partition
- GUID (objectGUID) of NTDS settings object under the configuration partition

The cmdlet searches the default naming context or partition to find the object.
If two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

```yaml
Type: ADDirectoryServer
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -OperationMasterRole
Specifies one or more operation master roles to move to the specified directory server in Active Directory Domain Services.
The acceptable values for this parameter are:

- PDCEmulator or 0
- RIDMaster or 1
- InfrastructureMaster or 2
- SchemaMaster or 3
- DomainNamingMaster or 4

To specify multiple operation master roles, use a comma-separated list.

```yaml
Type: ADOperationMasterRole[]
Parameter Sets: (All)
Aliases:
Accepted values: PDCEmulator, RIDMaster, InfrastructureMaster, SchemaMaster, DomainNamingMaster

Required: True
Position: 1
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
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ActiveDirectory.Management.AddDirectoryServer
目录服务器对象是通过*Identity*参数接收到的。

## 输出

### 无值或 Microsoft.ActiveDirectory.Management ADDirectoryServer
当指定*PassThru*参数时，此命令会返回修改后的目录服务器对象。默认情况下，该命令不会生成任何输出。

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Move-ADDirectoryServer](./Move-ADDirectoryServer.md)

[Windows PowerShell中的AD DS管理命令集](./activedirectory.md)

