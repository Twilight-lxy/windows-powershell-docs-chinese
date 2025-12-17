---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-addefaultdomainpasswordpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADDefaultDomainPasswordPolicy
---

# 设置 AD 默认域密码策略

## 摘要
修改 Active Directory 域的默认密码策略。

## 语法

```
Set-ADDefaultDomainPasswordPolicy [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-ComplexityEnabled <Boolean>]
 [-Credential <PSCredential>] [-Identity] <ADDefaultDomainPasswordPolicy> [-LockoutDuration <TimeSpan>]
 [-LockoutObservationWindow <TimeSpan>] [-LockoutThreshold <Int32>] [-MaxPasswordAge <TimeSpan>]
 [-MinPasswordAge <TimeSpan>] [-MinPasswordLength <Int32>] [-PassThru] [-PasswordHistoryCount <Int32>]
 [-ReversibleEncryptionEnabled <Boolean>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-ADDefaultDomainPasswordPolicy` cmdlet 用于修改域的默认密码策略的属性。您可以通过使用该 cmdlet 的参数来更改属性值。

`Identity` 参数用于指定您想要修改其默认密码策略的域。您可以按照该域的 distinguished name、GUID、Security Identifier (SID)、DNS 域名或 NETBIOS 名来识别该域。您也可以将此参数设置为一个 `ADDomain` 对象变量，或者通过管道将该 `ADDomain` 对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADDomain` cmdlet 来获取一个域对象，然后通过管道将该对象传递给 `Set-ADDefaultDomainPasswordPolicy` cmdlet。

## 示例

### 示例 1：为指定的域名设置默认密码策略
```powershell
PS C:\> Set-ADDefaultDomainPasswordPolicy -Identity fabrikam.com -LockoutDuration 00:40:00 -LockoutObservationWindow 00:20:00 -ComplexityEnabled $True -ReversibleEncryptionEnabled $False -MaxPasswordAge 10.00:00:00
```

此命令为通过使用 *Identity* 参数指定的域设置默认的域密码策略。注意：将 **MaxPwdAge** 设置为 0 表示该密码永远不会被更改；在目录中表示为 Int64.MinValue 或 -9223372036854775808。

### 示例 2：为当前登录用户的域设置默认域名策略
```powershell
PS C:\> Get-ADDefaultDomainPasswordPolicy -Current LoggedOnUser | Set-ADDefaultDomainPasswordPolicy -LockoutDuration 00:40:00 -LockoutObservationWindow 00:20:00 -ComplexityEnabled $true -ReversibleEncryptionEnabled $false -MinPasswordLength 12
```

此命令为当前登录用户的所在域设置默认的域密码策略。

## 参数

### -AuthType
指定要使用的认证方法。此参数的可接受值包括：

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

### -ComplexityEnabled
指定密码策略是否启用密码复杂度要求。如果启用了该要求，则密码必须包含以下四种字符类型中的三种：

- Uppercase characters (A, B, C, D, E, ...)
- Lowercase characters (a, b, c, d, e, ...)
- Numerals (0, 1, 2, 3, ...)
- Special characters (#, $, *, %, ...)

此参数用于设置密码策略的 **ComplexityEnabled** 属性。该参数的可接受值如下：

- $False or 0.
Disables password complexity.
- $True or 1.
Enables password complexity.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Windows PowerShell提供程序的Active Directory模块驱动器中运行的。如果该cmdlet是从此类驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

您也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行该任务的主体（即具有相应权限的对象）没有目录级别的权限，那么用于 Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
通过提供以下属性值之一来指定一个 Active Directory 域对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。所有值都适用于表示该域的 **domainDNS** 对象。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A DNS domain name
- A NetBIOS domain name

该cmdlet会在默认的命名上下文或分区中搜索对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误（即不会停止执行）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个域对象实例。

```yaml
Type: ADDefaultDomainPasswordPolicy
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -LockoutDuration
该参数用于指定当登录尝试失败次数超过锁定阈值后，账户被锁定的时间长度。在锁定期间结束之前，您无法登录该账户。此参数用于设置密码策略对象中的 **lockoutDuration** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）为 “lockoutDuration”。

对于密码策略而言，锁定时间的长度必须大于或等于锁定观察时间。请使用 *LockOutObservationWindow* 参数来设置锁定观察时间。

请按照以下格式指定封锁（锁定）持续时间间隔：

D.H:M:S.F

`where:`

D = 天数（范围从 0 到 10,675,199）

H = 小时（0到23）

M = 分钟（范围为 0 到 59）

S = 秒（范围从0到59）

F = 秒的分数（范围从 0 到 9999999）

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

### -LockoutObservationWindow
该参数用于指定两次登录尝试失败之间的最大时间间隔，超过此时间间隔后，登录失败的次数将重置为0。当登录失败的次数超过密码策略规定的锁定阈值时，账户将被锁定。该参数用于设置密码策略对象（password policy object）的 **lockoutObservationWindow** 属性；该属性在 LDAP 中的显示名称（**ldapDisplayName**）为 “lockoutObservationWindow”。

对于密码策略而言，锁定观察窗口的时长必须小于或等于锁定持续时间。请使用 *LockoutDuration* 参数来设置锁定持续的时间。

请按照以下格式指定时间间隔：

D:H:M:S.F

`where:`

D = 天数（范围从 0 到 10,675,199）

H = 小时（0到23）

M = 分钟（范围为 0 到 59）

S = 秒（范围从0到59）

F = 秒的分数（范围从 0 到 9999999）

注意：时间值必须在以下范围内：0:0:0:0.0 到 10675199:02:48:05.4775807。

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

### -LockoutThreshold
该参数用于指定在账户被锁定之前允许的不成功登录尝试次数。当两次不成功登录尝试之间的时间间隔小于锁定的观察时间窗口所规定的时间时，允许的失败登录尝试次数会增加。此参数用于设置密码策略中的 **LockoutThreshold** 属性。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxPasswordAge
指定了可以使用相同密码的最长时间期限。超过这个时间后，密码将会失效，您必须创建一个新的密码。

这个参数用于设置密码策略中的 `maxPasswordAge` 属性。该属性在 LDAP 中的显示名称（**ldapDisplayName**）是 `maxPwdAge`。

请按照以下格式指定时间间隔：

D.H:M:S.F

`where:`

D = 天数（范围从 0 到 10,675,199）

H = 小时（0到23）

M = 分钟（范围为 0 到 59）

S = 秒（范围从0到59）

F = 秒的分数（范围从 0 到 9999999）

注意：时间值必须在以下范围内：0 到 10675199:02:48:05.4775807。

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

### -MinPasswordAge
指定了在更改密码之前必须等待的最短时间长度。

此参数用于设置密码策略中的 `minPasswordAge` 属性。该属性在 LDAP 中的显示名称（`ldapDisplayName`）为 `minPwdAge`。

请按照以下格式指定时间间隔。

D.H:M:S.F

`where:`

D = 天数（范围从 0 到 10,675,199）

H = 小时（0到23）

M = 分钟（范围为 0 到 59）

S = 秒（范围从0到59）

F = 秒的分数（范围从 0 到 9999999）

注意：时间值必须在以下范围内：0 到 10675199:02:48:05.4775807。

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

### -MinPasswordLength
指定密码必须包含的最少字符数。此参数用于设置密码策略的 **MinPasswordLength** 属性。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -PasswordHistoryCount
指定要保存的先前密码的数量。用户不能在已保存的密码列表中使用重复的密码。此参数用于设置密码策略的 **PasswordHistoryCount** 属性。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReversibleEncryptionEnabled
指定该目录是否必须使用可逆加密方法来存储密码。此参数用于设置密码策略的 **ReversibleEncryption** 属性。该参数的可接受值为：

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此请提供相应的域名或目录服务器之一的值。该服务可以是以下类型之一：Active Directory 轻量级域服务、Active Directory 域服务或 Active Directory 快照实例。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

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
展示了如果运行该cmdlet会发生什么情况。不过实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectory.Management>AddDomain
一个领域对象是通过*Identity*参数接收到的。

## 输出

### 无

## 备注
* This cmdlet does not work with Active Directory Lightweight Directory Services.
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADDefaultDomainPasswordPolicy](./Get-ADDefaultDomainPasswordPolicy.md)

[Windows PowerShell 中的 AD DS 管理命令集](./activedirectory.md)

