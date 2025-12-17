---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/rename-adobject?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Rename-ADObject
---

# 重命名 AD 对象

## 摘要
更改Active Directory对象的名称。

## 语法

```
Rename-ADObject [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADObject> [-NewName] <String> [-Partition <String>] [-PassThru] [-Server <String>]
 [<CommonParameters>]
```

## 描述
**Rename-ADObject** cmdlet 用于重命名 Active Directory 对象。该 cmdlet 会修改具有轻型目录访问协议（LDAP）显示名称（**ldapDisplayName**）的 Active Directory 对象的 **Name** 属性。若要修改用户的名字、姓氏或其他名称，请使用 Set-ADUser cmdlet；若要修改用户、计算机或组的安全账户管理器（SAM）账户名称，则可以使用 Set-ADUser、Set-ADComputer 或 Set-ADGroup cmdlet。

`Identity` 参数用于指定要重命名的对象。您可以通过对象的唯一名称（Distinguished Name）或 GUID 来识别该对象。您也可以将 `Identity` 参数设置为某个对象变量（例如 `$<localObject>`），或者通过管道将该对象传递给 `Identity` 参数。例如，您可以使用 **Get-ADObject** cmdlet 获取一个对象，然后通过管道将该对象传递给 `Rename-ADObject` cmdlet。此外，您还可以使用 **Get-ADGroup**, **Get-ADUser**, **Get-ADComputer**, **Get-ADServiceAccount**, **Get-ADOrganizationalUnit** 和 **Get-ADFineGrainedPasswordPolicy** cmdlets 来获取对象，并通过管道将这些对象传递给 `Rename-ADObject` cmdlet。

*NewName* 参数用于定义对象的新名称，必须指定该参数的值。

## 示例

### 示例 1：重命名一个网站
```
PS C:\> Rename-ADObject -Identity "CN=HQ,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM" -NewName "UnitedKingdomHQ"
```

此命令将现有站点HQ的名称更改为“UnitedKingdomHQ”。如果在*Identity*参数中提供了该站点的唯一标识名（distinguished name），则不需要使用*Partition*参数。

### 示例 2：重命名一个对象
```
PS C:\> Rename-ADObject -Identity "4777c8e8-cd29-4699-91e8-c507705a0966" -NewName "AmsterdamHQ" -Partition "CN=Configuration,DC=FABRIKAM,DC=COM"
```

此命令将GUID为4777c8e8-cd29-4699-91e8-c507705a0966的对象重命名为SiteNewName。*Partition*参数是必需的，因为从*Identity*参数指定的GUID中无法得知该站点对象的实际命名上下文信息。

#### 示例 3：通过唯一名称重命名一个对象
```
PS C:\> Rename-ADObject -Identity "OU=ManagedGroups,OU=Managed,DC=Fabrikam,DC=Com" -NewName "Groups"
```

此命令将名为“OU=ManagedGroups,OU=Managed,DC=Fabrikam,DC=Com”的对象重命名为“Groups”。

### 示例 4：通过 GUID 重命名对象
```
PS C:\> Rename-ADObject -Identity "4777c8e8-cd29-4699-91e8-c507705a0966" -NewName "DavidChew"
```

此命令将 GUID 为 4777c8e8-cd29-4699-91e8-c507705a0966 的对象重命名为 DavidChews。未指定 *Partition* 参数，因为该对象位于域的默认命名上下文中。

### 示例 5：在 LDS 实例中重命名容器
```
PS C:\> Rename-ADObject -Identity "CN=Apps,DC=AppNC" -NewName "InternalApps" -Server "FABRIKAM-SRV1:60000"
```

此命令将在一个LDS实例中将容器CN=Apps,DC=AppNC的重命名为InternalApps。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值为：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。

基本身份验证方法需要使用安全套接字层（SSL）连接。

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
在运行该cmdlet之前，会提示您进行确认。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Windows PowerShell提供程序的Active Directory模块驱动器中运行的。如果该cmdlet是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

您也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，可以将该对象的类型设置为 **PSCredential**。

如果执行该任务所需的目录级权限不在当前用户或角色的权限范围内，Windows PowerShell 的 Active Directory 模块会返回一个终止错误（即程序会立即结束）。

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
通过提供以下属性值之一来指定一个 Active Directory 对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个表示操作无法完成的错误信息（即非终止性错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

也接受派生类型，例如以下这些：

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**
- **Microsoft.ActiveDirectory.Management.ADDomain**

```yaml
Type: ADObject
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -NewName
Specifies the new name of the object.
This parameter sets the Name property of the Active Directory object.
The LDAP display name (**ldapDisplayName**) of this property is name.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Partition
Specifies the distinguished name of an Active Directory partition.
The distinguished name must be one of the naming contexts on the current directory server.
The cmdlet searches this partition to find the object defined by the *Identity* parameter.

In many cases, a default value is used for the *Partition* parameter if no value is specified.
The rules for determining the default value are given below.
Note that rules listed first are evaluated first and when a default value can be determined, no further rules are evaluated.

In Active Directory Domain Services (AD DS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter does not take any default value.

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
Specifies the AD DS instance to connect to, by providing one of the following values for a corresponding domain name or directory server.
The service may be any of the following: AD LDS, AD DS, or Active Directory snapshot instance.

Specify the AD DS instance in one of the following ways:

Domain name values:

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for this parameter is determined by one of the following methods in the order that they are listed:

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the AD DS Windows PowerShell provider drive, when the cmdlet runs in that drive
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

### 无 or Microsoft.ActiveDirectory.Management.ADObject
An Active Directory object is received by the *Identity* parameter.

也接受派生类型，例如以下这些：

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADOrganizationalUnit**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**

## 输出

### 无

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADObject](./Get-ADObject.md)

[Move-ADObject](./Move-ADObject.md)

[New-ADObject](./New-ADObject.md)

[Remove-ADObject](./Remove-ADObject.md)

[恢复 AD 对象](./Restore-ADObject.md)

[Set-ADObject](./Set-ADObject.md)

