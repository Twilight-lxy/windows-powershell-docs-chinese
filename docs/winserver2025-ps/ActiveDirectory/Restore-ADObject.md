---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/restore-adobject?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Restore-ADObject
---

# 恢复 AD 对象

## 摘要
恢复一个 Active Directory 对象。

## 语法

```
Restore-ADObject [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADObject> [-NewName <String>] [-Partition <String>] [-PassThru] [-Server <String>]
 [-TargetPath <String>] [<CommonParameters>]
```

## 描述
`Restore-ADObject` cmdlet 可以恢复已删除的 Active Directory 对象。

`NewName` 参数用于指定恢复对象的新名称。如果未指定 `NewName` 参数，则会使用具有轻型目录访问协议（LDAP）显示名 `msDS-lastKnownRDN` 的 Active Directory 属性的值。`TargetPath` 参数用于指定恢复对象的新位置；如果未指定 `TargetPath`，则会使用具有 LDAP 显示名 `lastKnownParent` 的 Active Directory 属性的值。

`Identity` 参数用于指定要恢复的 Active Directory 对象。您可以通过该对象的唯一名称（Distinguished Name）或 GUID 来标识它。您也可以将 `Identity` 参数设置为某个对象变量（例如 `$<localObject>`），或者通过管道将该对象传递给 `Identity` 参数。例如，您可以使用 **Get-ADObject** cmdlet 并指定 `IncludeDeletedObjects` 参数来获取被删除的对象，然后再将该对象通过管道传递给 `Restore-ADObject` cmdlet 进行恢复操作。

注意：您可以使用带有 *IncludeDeletedObjects* 参数的 **Get-ADObject** cmdlet 来获取已删除对象的名称。

## 示例

#### 示例 1：恢复一个被删除的对象，并为其设置属性
```
PS C:\> Restore-ADObject -Identity "613dc90a-2afd-49fb-8bd8-eac48c6ab59f" -NewName "Kim Abercrombie" -TargetPath "OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM"
```

此命令会恢复该**ADObject**，同时将已删除对象的**msDS-LastKnownRDN**属性设置为*NewName*参数，并将该对象的最后已知RDN地址设置为*TargetPath*参数。

### 示例 2：通过唯一名称恢复对象
```
PS C:\> Restore-ADObject -Identity "CN=Kim Abercrombie\0ADEL:613dc90a-2afd-49fb-8bd8-eac48c6ab59f,CN=Deleted Objects,DC=FABRIKAM,DC=COM" -NewName "Kim Abercrombie" -TargetPath "OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM"
```

该命令会恢复被删除的 **ADObject**，同时将已删除对象的 **msDS-LastKnownRDN** 属性设置为 *NewName* 参数，并将该对象的最后已知 RDN 值设置为 *TargetPath* 参数。

#### 示例 3：从过滤后的用户列表中恢复一个对象
```
PS C:\> Get-ADObject -Filter 'samaccountname -eq "pattifuller"' -IncludeDeletedObjects | Restore-ADObject
```

此命令会找到一个被删除的用户（其SAM账户名称为“pattifuller”），并恢复该用户的账户。

### 示例 4：通过对象的 GUID 恢复该对象
```
PS C:\> Restore-ADObject -Identity '6bb3bfe9-4355-48ee-b3b6-4fda6917d31d' -Server server1:50000
```

此命令使用 ObjectGUID 恢复一个 AD LDS 对象。

### 示例 5：通过对象的 `msds-LastKnownRDN` 属性来恢复该对象
```
PS C:\> Get-ADObject -Filter 'msds-lastknownrdn -eq "user1"' -Server server1:50000 -IncludeDeletedObjects -SearchBase "o=app1,c=us" | Restore-ADObject
```

此命令使用 **msds-LastKnownRDN** 属性来恢复一个 AD LDS 对象。

### 示例 6：在指定的日期/时间范围内恢复被删除的配置对象
```
PS C:\> $ChangeDate = New-Object DateTime(2008, 11, 18, 1, 40, 02)
PS C:\> Get-ADObject -Filter 'whenChanged -gt $ChangeDate -and isDeleted -eq $True -and -not (isRecycled -eq $True) -and lastKnownParent -eq "OU=Accounting,DC=Fabrikam,DC=com"' -IncludeDeletedObjects -SearchBase "CN=Deleted Objects,CN=Configuration,DC=contoso,DC=com" | Restore-ADObject
```

此命令可以恢复在特定日期/时间范围内被删除的配置对象。如果您知道这些对象是什么时候被删除的，那么这个命令会非常有用。

### 示例 7：恢复所有被删除的配置对象

```
Get-ADObject -filter 'isdeleted -eq $true -and name -ne "Deleted Objects"' -includeDeletedObjects -property * -SearchBase "CN=Deleted Objects,CN=Configuration,DC=contoso,DC=com" | Restore-ADObject
```

此命令会恢复所有被删除的配置对象。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值为：

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
在运行 cmdlet 之前会提示您确认是否要继续。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Active Directory PowerShell 提供程序驱动器运行的；如果是从这样的驱动器运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果执行该任务的账号没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
通过提供以下值之一来指定一个 Active Directory 组对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A Security Account Manager account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它将返回一个无法终止的错误信息。

这个参数也可以通过管道来获取该对象，或者你可以将该参数设置为某个对象的实例。

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
指定对象的新名称。此参数用于设置 Active Directory 对象的 **Name** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）即为新指定的名称。

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

### -Partition
指定一个 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上所支持的命名上下文之一。此 cmdlet 会在该分区中查找由 *Identity* 参数定义的对象。

在许多情况下，如果未指定值，则会使用默认值作为*Partition*参数的值。确定默认值的规则如下所示。请注意，首先列出的规则会被优先评估；一旦确定了默认值，后续的规则将不再被评估。

在 Active Directory 域服务（AD DS）环境中，以下情况下会为“分区”（Partition）设置默认值：

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter does not take a default value.

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
返回一个表示您当前正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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
指定要连接的 AD DS 实例，为此需要提供相应的域名或目录服务器的相关值。该服务可以是以下类型中的任意一种：AD LDS、AD DS 或 Active Directory 快照实例。

以下列方式之一指定 AD DS 实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们的列出顺序：

- By using the **Server** value from objects passed through the pipeline
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
指定对象的新位置。该位置必须是容器或组织单位的路径。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management.ADObject
*Identity* 参数接收到了一个 Active Directory 对象。

也接受派生类型，例如以下这些：

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADOrganizationalUnit**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**
- **Microsoft.ActiveDirectory.Management.ADDomain**

## 输出

### 无或 Microsoft.ActiveDirectory.Management.ADObject
当指定 *PassThru* 参数时，会返回恢复后的对象。默认情况下，此 cmdlet 不会生成任何输出。

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADObject](./Get-ADObject.md)

[Move-ADObject](./Move-ADObject.md)

[New-ADObject](./New-ADObject.md)

[Remove-ADObject](./Remove-ADObject.md)

[重命名 AD 对象](./Rename-ADObject.md)

[Set-ADObject](./Set-ADObject.md)

