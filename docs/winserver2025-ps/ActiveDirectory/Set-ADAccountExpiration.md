---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adaccountexpiration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADAccountExpiration
---

# 设置 AD 账户过期时间

## 摘要
用于设置 Active Directory 账户的过期日期。

## 语法

```
Set-ADAccountExpiration [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [[-DateTime] <DateTime>] [-Identity] <ADAccount> [-Partition <String>] [-PassThru] [-Server <String>]
 [-TimeSpan <TimeSpan>] [<CommonParameters>]
```

## 描述
`Set-ADAccountExpiration` cmdlet 用于设置用户、计算机或服务账户的过期时间。要指定一个确切的时间，可以使用 `DateTime` 参数；要指定从当前时间开始的一个时间段，则使用 `TimeSpan` 参数。

`Identity` 参数指定了要修改的 Active Directory 账户。

您可以通过账户的独特名称、GUID、安全标识符（SID）或安全帐户管理器（SAM）账户名称来识别该账户。您还可以将 *Identity* 参数设置为一个对象变量（例如 `$<localADAccountObject>`），或者通过管道将该账户对象传递给 *Identity* 参数。例如，您可以使用 **Search-ADAccount** cmdlet 来检索一个账户对象，然后通过管道将该对象传递给 Set-ADAccountExpiration cmdlet。同样地，您也可以使用 **Get-ADUser**、**Get-ADComputer** 或 **Get-ADServiceAccount** cmdlets 来检索账户对象，并将这些对象通过管道传递给相应的 cmdlet。

对于使用 Active Directory 轻量级目录服务（AD LDS）的环境来说，必须指定 *Partition* 参数，以下两种情况除外：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.

要为 AD LDS 环境指定一个默认的命名上下文，请设置 AD LDS 实例的 Active Directory 目录服务代理（DSA）对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性。

## 示例

### 示例 1：为指定的用户设置账户到期日期
```
PS C:\> Set-ADAccountExpiration -Identity PattiFu -DateTime "10/18/2008"
```

该命令将名为PattiFu的账户设置为在2008年10月18日过期。

### 示例 2：为指定组中的所有用户账户设置账户到期日期
```
PS C:\> Get-ADGroupMember -Identity BO1Accounts | where {$_.objectClass -eq "user"} | Set-ADAccountExpiration -TimeSpan 60.0:0
```

该命令将属于BO1Accounts组的所有用户账户的过期日期设置为从现在起60天后。

## 参数

### -AuthType
指定要使用的身份验证方法。此参数的可接受值包括：

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
在运行cmdlet之前会提示您确认是否要继续。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Windows PowerShell的Active Directory模块提供程序驱动器中运行的。如果该cmdlet是从此类提供程序驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将该 `PSCredential` 对象设置为 `Credential` 参数的值。

如果执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

### -DateTime
使用一个 **DateTime** 值来指定账户的过期时间。除非另有说明，否则时间默认为本地时间。当没有指定时间值时，时间被假设为当天的凌晨 12:00:00（本地时间）；当没有指定日期时，日期被假设为当前日期。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity
通过提供以下属性值之一来指定一个 Active Directory 账户对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个非终止性的错误（即无法继续执行的错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为某个账户对象实例的值。

也接受以下这样的派生类型：

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**

```yaml
Type: ADAccount
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
Note that rules listed first are evaluated first and once a default value can be determined, no further rules are evaluated.

In Active Directory Domain Services (AD DS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In AD LDS environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
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
The service may be any of the following:  Active Directory Lightweight Domain Services, Active Directory Domain Services or Active Directory snapshot instance.

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

### -TimeSpan
Specifies a time interval that begins at the current time.
The account expires at the end of the time interval.

Specify the time interval in the following format:

\[-\]D.H:M:S.F

where:

- D = Days (0 to 10675199)
- H = Hours (0 to 23)
- M = Minutes (0 to 59)
- S = Seconds (0 to 59)
- F = Fractions of a second (0 to 9999999)

Note: Time values must be between the following values:

-10675199:02:48:05.4775808 and 10675199:02:48:05.4775807.

```yaml
Type: TimeSpan
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

### 无 or Microsoft.ActiveDirectory.Management.ADAccount
An account object is received by the *Identity* parameter.

Derived types, such as the following are also accepted:

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**

## 输出

### 无

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Clear-ADAccountExpiration](./Clear-ADAccountExpiration.md)

[Get-ADComputer](./Get-ADComputer.md)

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[Get-ADUser](./Get-ADUser.md)

[Search-ADAccount](./Search-ADAccount.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

