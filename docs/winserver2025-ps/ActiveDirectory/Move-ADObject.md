---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/move-adobject?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Move-ADObject
---

# 移动 AD 对象

## 摘要
将一个 Active Directory 对象或其对象容器移动到另一个容器或域中。

## 语法

```
Move-ADObject [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADObject>
 [-Partition <String>] [-PassThru] [-Server <String>] [-TargetPath] <String> [-TargetServer <String>]
 [<CommonParameters>]
```

## 描述
`Move-ADObject` cmdlet 可以将一个对象或包含多个对象的容器从一个容器移动到另一个容器，或者在同一林（forest）内的不同域之间进行移动。

当一个对象在不同的域之间移动时，源DC和目标DC都需要成为各自所在域的RID Master。如果使用了其他DC，将会出现以下错误：

`move-adobject`：无法执行所请求的操作，因为目录服务不是该类型操作的主管（即不具备执行该操作所需的权限或状态）。

`Identity` 参数用于指定要移动的 Active Directory 对象或容器。您可以通过该对象或容器的唯一名称（distinguished name）或 GUID 来识别它。此外，您还可以将 `Identity` 参数设置为一个对象变量（例如 `$<localObject>`），或者通过管道将某个对象传递给 `Identity` 参数。例如，您可以使用 **Get-ADObject** cmdlet 获取一个对象，然后将该对象通过管道传递给 `Move-ADObject` cmdlet。同时，您也可以使用 **Get-ADGroup**、**Get-ADUser**、**Get-ADComputer**、**Get-ADServiceAccount**、**Get-ADOrganizationalUnit** 和 **Get-ADFineGrainedPasswordPolicy** cmdlets 来获取对象，并将这些对象通过管道传递给 `Move-ADObject` cmdlet。

必须指定 *TargetPath* 参数。该参数用于确定对象或容器的新位置。

当用户或计算机对象在森林内的不同域之间移动时，该cmdlet也会同时更新相应的密码。


## 示例

### 示例 1：将一个组织单元（OU）移动到新的位置
```
PS C:\> Move-ADObject -Identity "OU=ManagedGroups,DC=Fabrikam,DC=Com" -TargetPath "OU=Managed,DC=Fabrikam,DC=Com"
```

该命令将名为“ManagedGroups”的组织单元（Organizational Unit, OU）移动到新的位置。为了成功完成迁移，必须确保这个名为“ManagedGroups”的组织单元不会被设置为防止意外删除的状态。

### 示例 2：将一个对象移动到新的位置
```
PS C:\> Move-ADObject -Identity "8d0bcc44-c826-4dd8-af5c-2c69960fbd47" -TargetPath "OU=Managed,DC=Fabrikam,DC=Com"
```

此命令将由指定 GUID 标识的对象移动到新位置。

### 示例 3：将对象移动到由 GUID 指定的位置
```
PS C:\> Move-ADObject -Identity "8d0bcc44-c826-4dd8-af5c-2c69960fbd47" -TargetPath "1c2ea8a8-c2b7-4a87-8190-0e8a166aee16"
```

此命令将一个对象移动到新的位置。对象和目标路径都是使用 GUID（全局唯一标识符）来指定的。

### 示例 4：移动通过唯一名称指定的对象
```
PS C:\> Move-ADObject -Identity "CN=Peter Bankov,OU=Accounting,DC=Fabrikam,DC=com" -TargetPath "OU=Accounting,DC=Europe,DC=Fabrikam,DC=com" -TargetServer "server01.europe.fabrikam.com"
```

这个命令会将一个对象移动到另一个域中。该对象的唯一名称为：CN=Peter Bankov, OU=Accounting, DC=Fabrikam, DC=com。

### 示例 5：在 AD LDS 实例中移动对象
```
PS C:\> Move-ADObject -Identity "CN=AccountLeads,DC=AppNC" -TargetPath "OU=AccountDeptOU,DC=AppNC" -Server "FABRIKAM-SRV1:60000"
```

此命令将一个对象移动到 AD LDS 实例中的新位置。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值为：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果是从这样的驱动器中运行该 cmdlet，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果该执行任务的账号没有目录级别的权限，那么用于 Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
通过提供以下属性值之一来指定一个 Active Directory 对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个非终止性的错误（即无法继续执行的错误）。

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
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent (DSA) object (**nTDSDSA**) for the AD LDS instance.
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

### -TargetPath
Specifies the new location for the object.
This location must be the path to a container or organizational unit.

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

### -TargetServer
Specifies the Active Directory instance to use by providing the following value for a corresponding domain name or directory server.

Note: A cross-domain move requires a fully qualified server name and the use of the RID Master in both domains.

Domain name values:

- Fully qualified domain name (FQDN)

Directory server values:

- Fully qualified directory server name
- Fully qualified directory server name and port

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

### Microsoft.ActiveDirectory.Management.AObject
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

[New-ADObject](./New-ADObject.md)

[Remove-ADObject](./Remove-ADObject.md)

[重命名 AD 对象](./Rename-ADObject.md)

[恢复AD对象](./Restore-ADObject.md)

[Set-ADObject](./Set-ADObject.md)

[Sync-ADObject](./Sync-ADObject.md)

