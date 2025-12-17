---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-aduser?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADUser
---

# 删除 AD 用户

## 摘要
删除一个Active Directory用户。

## 语法

```
Remove-ADUser [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADUser>
 [-Partition <String>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Remove-ADUser` cmdlet 用于删除 Active Directory 用户。

`Identity` 参数用于指定要删除的 Active Directory 用户。您可以通过该用户的唯一名称（DN）、GUID、安全标识符（SID）或安全账户管理器（SAM）帐户名来识别用户。您还可以将 `Identity` 参数设置为一个用户对象变量（例如 `$<localUserObject>`），或者通过管道将该用户对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADUser` cmdlet 获取一个用户对象，然后通过管道将该对象传递给 `Remove-ADUser` cmdlet。

如果**ADUser**是通过其DN（Distinguished Name）来识别的，那么*Partition*参数将会自动被确定。

对于 AD LDS 环境而言，必须指定 *Partition* 参数，以下两种情况除外：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent (DSA) object (**nTDSDSA**) for the AD LDS instance.

## 示例

### 示例 1：删除指定的用户
```powershell
PS C:\> Remove-ADUser -Identity GlenJohn
```

此命令会删除用户名为GlenJohn的用户（该用户使用的是SAM账户）。

### 示例 2：移除过滤后的用户列表
```powershell
PS C:\> Search-ADAccount -AccountDisabled | where {$_.ObjectClass -eq 'user'} | Remove-ADUser
```

这条命令会搜索所有账号被禁用的用户，并将这些用户从系统中删除。

### 示例 3：通过用户名删除用户
```powershell
PS C:\> Remove-ADUser -Identity "CN=Glen John,OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM"
```

此命令将名为“CN=Glen John, OU=Finance, OU/UserAccounts, DC=FABRIKAM, DC=COM”的用户从系统中删除。

#### 示例 4：通过唯一名称获取用户信息并删除该用户
```powershell
PS C:\> Get-ADUser -Identity "cn=glenjohn,dc=appnc" -Server Lds.Fabrikam.com:50000 | Remove-ADUser
```

此命令从 AD LDS 实例中获取用户名为 cn=glenjohn,dc=appnc 的用户，并将其删除。

## 参数

### -AuthType
指定要使用的认证方法。此参数的可接受值为：

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
在运行cmdlet之前会提示您进行确认。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Active Directory PowerShell 提供程序驱动器中运行的；如果是从这样的驱动器中运行，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

您也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，可以将 `Credential` 参数设置为该 `PSCredential` 对象。

如果执行该任务的账号没有目录级别的权限，Active Directory PowerShell 会返回一个终止错误（即程序异常退出）。

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
通过提供以下属性值之一来指定一个 Active Directory 用户对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A Distinguished name
- A GUID (objectGUID)
- A Security Identifier (objectSid)
- A SAM account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个无法终止的错误（即程序会陷入无限循环）。

这个参数也可以通过管道来获取该对象，或者你可以将这个参数设置为一个对象实例。

```yaml
Type: ADUser
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Partition
指定一个 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上支持的命名上下文之一。此 cmdlet 会在此分区中查找由 *Identity* 参数所标识的对象。

在许多情况下，如果未指定 `Partition` 参数的值，系统会使用一个默认值。确定默认值的规则如下所示。请注意，列出的规则会按顺序依次被评估；一旦确定了默认值，后续的规则将不再被执行。

在 Active Directory Domain Services (AD DS) 环境中，以下情况下会为“Partition”（分区）设置默认值：

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* will be set to the default partition or naming context of the target domain.

In AD LDS environments, a default value for *Partition* will be set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* will be set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent (DSA) object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter will not take any default value.

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

### -Server
指定要连接的 AD DS 实例，为此请提供一个相应的域名或目录服务器的值。该服务可以是以下类型中的任意一种：AD LDS、AD DS 或 Active Directory 快照实例。

请通过以下方式之一指定 AD DS 实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无，或使用 Microsoft.ActiveDirectory.Management.ADUser
用户对象通过*Identity*参数被接收。

## 输出

### 无

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.
* By default, this cmdlet prompts for confirmation as it is defined with **High impact** and the default value of the **$ConfirmPreference** variable is **High**. To bypass prompting for confirmation before removal, you can specify `-Confirm:$False` when using this cmdlet.

## 相关链接

[Get-ADUser](./Get-ADUser.md)

[New-ADUser](./New-ADUser.md)

[Set-ADUser](./Set-ADUser.md)

