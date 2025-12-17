---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/move-addirectoryserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Move-ADDirectoryServer
---

# 移动 AD 目录服务器

## 摘要
将 Active Directory 中的目录服务器移动到新的站点。

## 语法

```
Move-ADDirectoryServer [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADDirectoryServer> [-Server <String>] [-Site] <ADReplicationSite> [<CommonParameters>]
```

## 描述
`Move-ADDirectoryServer` cmdlet 可以将 Active Directory 中的目录服务器移动到同一域内的新站点。

`Identity` 参数用于指定要移动的目录服务器。您可以使用以下值之一来指定一个目录服务器对象：

- Name of the server object (name)
- A distinguished name  of the NTDS Settings object
- A distinguished name of the server object that represents the directory server
- GUID (objectGUID) of server object under the configuration partition
- GUID (objectGUID) of NTDS settings object under the configuration partition

You can also set the *Identity* parameter to a directory server object variable such as `$<localDirectoryServerObject>`, or you can pass an object through the pipeline to the *Identity* parameter.
For example, you can use the **Get-ADDomainController** cmdlet to get a directory server object and then pass that object through the pipeline to the **Move-ADDirectoryServer** cmdlet.

The *Site* parameter specifies the new site for the directory server.
You can identify a site by its distinguished name or GUID.

## 示例

### Example 1: Move a domain controller to an existing site
```
PS C:\> Move-ADDirectoryServer -Identity "USER01-DC2" -Site "Branch-Office-Site"
```

This command moves the domain controller USER01-DC2 to the site Branch-Office-Site.

### Example 2: Move read-only domain controllers to an existing site
```
PS C:\> Get-ADDomainController -Filter "IsReadOnly -eq `$True" | Move-ADDirectoryServer -Site "RODC-Site-Name"
```

This command moves all Read-Only domain controllers to the site RODC-Site-Name.

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

### -Identity
Specifies an Active Directory server object by providing one of the following values.
The identifier in parentheses is the Lightweight Directory Access Protocol (LDAP) display name for the attribute.

- Name of the server object (name)

For Active Directory Lightweight Directory Services (AD LDS) instances the syntax is of a name is `<computer-name>$<instance-name>`

Note: When you type this value in Windows PowerShell, you must use the backtick (\`) as an escape character for the dollar sign ($), for example, *asia-w7-vm4`$instance1*.

For other Active Directory instances, use the value of the name property.

- A distinguished Name of the NTDS Settings object
- A distinguished name of the server object that represents the directory server
- GUID (objectGUID) of server object under the configuration partition
- GUID (objectGUID) of NTDS settings object under the configuration partition

该cmdlet会在默认的命名上下文或分区中搜索目标对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误（即不会正常结束执行）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

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

### -Server
指定要连接的 Active Directory 域服务实例，为此请提供相应的域名或目录服务器的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，确定顺序按照列出的顺序进行：

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

### -Site
指定目录服务器的新站点。您可以通过以下属性值之一来识别该站点。注意：括号中的标识符是该属性的LDAP显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A name (name)

```yaml
Type: ADReplicationSite
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectory.Management.AddDirectoryServer
目录服务器对象是通过*Identity*参数接收到的。

## 输出

### 无

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.


## 相关链接

[Move-ADDirectoryServerOperationMasterRole](./Move-ADDirectoryServerOperationMasterRole.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

