---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adfinegrainedpasswordpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADFineGrainedPasswordPolicy
---

# 新版精细密码策略（New-ADFineGrainedPasswordPolicy）

## 摘要
创建一个新的Active Directory精细密码策略。

## 语法

```powershell
New-ADFineGrainedPasswordPolicy [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-ComplexityEnabled <Boolean>]
 [-Credential <PSCredential>] [-Description <String>] [-DisplayName <String>]
 [-Instance <ADFineGrainedPasswordPolicy>] [-LockoutDuration <TimeSpan>] [-LockoutObservationWindow <TimeSpan>]
 [-LockoutThreshold <Int32>] [-MaxPasswordAge <TimeSpan>] [-MinPasswordAge <TimeSpan>]
 [-MinPasswordLength <Int32>] [-Name] <String> [-OtherAttributes <Hashtable>] [-PassThru]
 [-PasswordHistoryCount <Int32>] [-Precedence] <Int32> [-ProtectedFromAccidentalDeletion <Boolean>]
 [-ReversibleEncryptionEnabled <Boolean>] [-Server <String>] [<CommonParameters>]
```

## 描述
`New-ADFineGrainedPasswordPolicy` cmdlet 可用于创建一个新的 Active Directory 细粒度密码策略。您可以通过使用 cmdlet 参数来设置常见的细粒度密码策略属性值；未与 cmdlet 参数关联的属性值则可以使用 `OtherAttributes` 参数进行配置。

你必须设置*名称*（Name）和*优先级*（Precedence）参数才能创建一个新的细粒度密码策略。

以下方法说明了使用此cmdlet创建对象的不同方式。

方法 1：使用 `New-ADFineGrainedPasswordPolicy` cmdlet，指定所需的参数，并通过该 cmdlet 的参数来设置任何额外的属性值。

方法 2：使用模板来创建新的对象。为此，可以新建一个细粒度密码策略对象，或者获取现有细粒度密码策略对象的副本，并将 *Instance* 参数设置为该对象。提供给 *Instance* 参数的对象将作为新对象的模板。您可以通过设置 cmdlet 参数来覆盖模板中的属性值。有关示例和更多信息，请参阅此 cmdlet 的 *Instance* 参数说明。

方法 3：使用 `Import-Csv` cmdlet 结合 `New-ADFineGrainedPasswordPolicy` cmdlet 来创建多个 Active Directory 细粒度密码策略对象。具体操作如下：首先使用 `Import-Csv` cmdlet 从包含对象属性列表的逗号分隔值（CSV）文件中导入这些自定义对象；然后通过管道运算符将这些对象传递给 `New-ADFineGrainedPasswordPolicy` cmdlet，从而生成细粒度密码策略对象。

## 示例

#### 示例 1：创建一个细粒度的密码策略
```powershell
PS C:\> New-ADFineGrainedPasswordPolicy -Name "DomainUsersPSO" -Precedence 500 -ComplexityEnabled $true -Description "The Domain Users Password Policy" -DisplayName "Domain Users PSO" -LockoutDuration "0.12:00:00" -LockoutObservationWindow "0.00:15:00" -LockoutThreshold 10
```

该命令创建了一个名为 DomainUsersPSO 的细粒度密码策略对象，并为该对象设置了以下属性：**Precedence**（优先级）、**ComplexityEnabled**（是否启用密码复杂性要求）、**Description**（描述信息）、**DisplayName**（显示名称）、**LockoutDuration**（锁定时长）、**LockoutObservationWindow**（锁定观察窗口）以及 **LockoutThreshold**（锁定阈值）。

### 示例 2：使用模板对象创建细粒度的密码策略
```powershell
PS C:\> $TemplatePSO = New-Object Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy
PS C:\> $TemplatePSO.ComplexityEnabled = $true
PS C:\> $TemplatePSO.LockoutDuration = [TimeSpan]::Parse("0.12:00:00")
PS C:\> $TemplatePSO.LockoutObservationWindow = [TimeSpan]::Parse("0.00:15:00")
PS C:\> $TemplatePSO.LockoutThreshold = 10
PS C:\> $TemplatePSO.MinPasswordAge = [TimeSpan]::Parse("0.00:10:00")
PS C:\> $TemplatePSO.PasswordHistoryCount = 24
PS C:\> $TemplatePSO.ReversibleEncryptionEnabled = $false
PS C:\> New-ADFineGrainedPasswordPolicy -Instance $TemplatePSO -Name "SvcAccPSO" -Precedence 100 -Description "The Service Accounts Password Policy" -DisplayName "Service Accounts PSO" -MaxPasswordAge "30.00:00:00" -MinPasswordLength 20
PS C:\> New-ADFineGrainedPasswordPolicy -Instance $TemplatePSO -Name "AdminsPSO" -Precedence 200 -Description "The Domain Administrators Password Policy" -DisplayName "Domain Administrators PSO" -MaxPasswordAge "15.00:00:00" -MinPasswordLength 10
```

这个示例使用一个模板对象创建了两个新的细粒度密码策略对象。

## 参数

### -AuthType
指定要使用的身份验证方法。此参数的可接受值为：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”。

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
指定密码策略是否启用了密码复杂度要求。如果启用了该要求，密码必须包含以下四种字符类型中的三种：

- Uppercase characters (A, B, C, D, E, ...)
- Lowercase characters (a, b, c, d, e, ...)
- Numerals (0, 1, 2, 3, ...)
- Special characters (#, $, *, %, ...)

此参数用于设置密码策略的 **ComplexityEnabled** 属性。该参数的可接受值为：

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
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您确认是否要继续执行该操作。

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

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果该执行任务的账户没有目录级别的权限，Windows PowerShell的Active Directory模块会返回一个终止错误。

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

### -Description
指定对象的描述信息。该参数用于设置对象의 **Description** 属性的值。轻量级目录访问协议（LDAP）中该属性的显示名称（**ldapDisplayName**）为 “description”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DisplayName
指定对象的显示名称。此参数用于设置对象的 **DisplayName** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）为 “displayName”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Instance
指定一个细粒度密码策略对象的实例，用作创建新的细粒度密码策略对象的模板。

你可以使用现有的细粒度密码策略对象的实例作为模板，或者通过使用 Windows PowerShell 命令行或脚本来创建一个新的细粒度密码策略对象。

方法 1：使用现有的细粒度密码策略对象作为新对象的模板。要获取现有细粒度密码策略对象的实例，可以使用诸如 **Get-ADFineGrainedPasswordPolicy** 这样的 cmdlet。然后将该对象传递给 **New-ADFineGrainedPasswordPolicy** cmdlet 的 *Instance* 参数，以创建一个新的细粒度密码策略对象。您可以通过设置相应的参数来覆盖新对象的属性值。

方法 2：创建一个新的 **ADFineGrainedPasswordPolicy** 对象，并使用 Windows PowerShell 命令行界面设置相应的属性值。接着将这个对象传递给 **New-ADFineGrainedPasswordPolicy** cmdlet 的 *Instance* 参数，从而创建新的 Active Directory 细粒度密码策略对象。

注意：指定的属性不会被进行验证；因此，如果尝试设置不存在或无法设置的属性，将会引发错误。

```yaml
Type: ADFineGrainedPasswordPolicy
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LockoutDuration
该参数用于指定当登录尝试失败次数超过锁定阈值后，账户被锁定的时间长度。在锁定期间内，用户无法登录到该账户；只有当锁定时长结束之后，用户才能再次尝试登录。如果将此参数值设置为0，则管理员需要手动解锁该账户。此参数用于设置密码策略对象中的**lockoutDuration**属性，其在LDAP中的显示名称（**ldapDisplayName**）为“msDS-LockoutDuration”。

对于密码策略而言，锁定时间的长度必须大于或等于锁定观察时间。可以使用 *LockOutObservationWindow* 参数来设置锁定观察时间。

请按照以下格式指定锁定持续时间间隔：

`D.H:M:S.F`

以下是翻译后的中文内容：

其中：  
- D = 天数（0 到 10675199）  
- H = 小时（0 到 23）  
- M = 分钟（0 到 59）  
- S = 秒数（0 到 59）  
- F = 秒的小数部分（0 到 9999999）

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LockoutObservationWindow
该参数用于指定两次失败的登录尝试之间的最大时间间隔，超过这个时间间隔后，失败登录尝试的次数将被重置为0。当失败登录尝试的次数超出密码策略规定的锁定阈值时，账户将会被锁定。此参数用于设置密码策略对象中的 **lockoutObservationWindow** 属性；该属性在 LDAP 显示名称（**ldapDisplayName**）中被称为 **msDS-lockoutObservationWindow**。

对于密码策略而言，锁定观察窗口的时长必须小于或等于锁定持续时间。请使用 *LockoutDuration* 参数来设置锁定持续时间的长度。

> [注意] > 将账户锁定观察窗口设置为0实际上意味着该窗口的时间太短，无法观察到多次密码输入尝试；因此，该账户永远不会被锁定。

请按照以下格式指定时间间隔：

`D:H:M:S.F`

以下是翻译后的中文内容：

其中：  
- D = 天数（0 到 10675199）  
- H = 小时（0 到 23）  
- M = 分钟（0 到 59）  
- S = 秒数（0 到 59）  
- F = 秒的小数部分（0 到 9999999）

注意：时间值必须位于以下范围内：0:0:0:0.0 到 10675199:02:48:05.4775807。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LockoutThreshold
该参数规定了在账户被锁定之前允许的失败登录尝试次数。当两次失败登录尝试之间的时间间隔小于密码策略中规定的“锁定观察时间窗口”时，允许的失败登录尝试次数会增加。此参数用于设置密码策略的 **LockoutThreshold** 属性。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MaxPasswordAge
指定可以使用相同密码的最大时间长度。超过这个时间期限后，密码将会失效，您必须创建一个新的密码。

这个参数用于设置密码策略中的 **maxPasswordAge** 属性。该属性在 LDAP 中的显示名称（**ldapDisplayName**）是 maxPwdAge。

请按照以下格式指定时间间隔：

`D.H:M:S.F`

以下是翻译后的中文内容：

其中：  
- D = 天数（0 到 10675199）  
- H = 小时（0 到 23）  
- M = 分钟（0 到 59）  
- S = 秒数（0 到 59）  
- F = 秒的小数部分（0 到 9999999）

注意：时间值必须介于以下范围内：0 到 10675199:02:48:05.4775807。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MinPasswordAge
指定在可以更改密码之前的最短时间间隔。

此参数用于设置密码策略中的 **minPasswordAge** 属性。该属性在 LDAP 中的显示名称（**ldapDisplayName**）为 `minPwdAge`。

请按照以下格式指定时间间隔：

`D.H:M:S.F`

以下是翻译后的中文内容：

其中：  
- D = 天数（0 到 10675199）  
- H = 小时（0 到 23）  
- M = 分钟（0 到 59）  
- S = 秒数（0 到 59）  
- F = 秒的小数部分（0 到 9999999）

注意：时间值必须在以下范围内：0 到 10675199:02:48:05。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定对象的名称。此参数用于设置 Active Directory 对象的 **Name** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）即为该对象的实际名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OtherAttributes
用于为那些未通过 cmdlet 参数表示的属性指定对象属性值。您可以使用此参数同时设置一个或多个属性值。如果某个属性支持多个值，您可以为其分配多个值。要标识某个属性，请使用在 Active Directory 架构中为其定义的 LDAPDisplayName（**ldapDisplayName**）。

语法：

要为某个属性指定一个单一的值：

`-其他属性 @{'AttributeLDAPDisplayName'=值}'`

要为某个属性指定多个值

`-其他属性 @{'AttributeLDAPDisplayName'=value1, value2, ...}'`

您可以使用分号（;）来分隔多个属性，从而为这些属性指定值。以下语法展示了如何为多个属性设置值：

`-其他属性 @{'Attribute1LDAPDisplayName'=值; 'Attribute2LDAPDisplayName'=值1,值2;...'}`

```yaml
Type: Hashtable
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不生成任何输出。

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
指定要保存的先前密码的数量。用户不能在已保存的密码列表中重复使用某个密码。此参数用于设置密码策略的 **PasswordHistoryCount** 属性。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Precedence
指定一个值，用于定义某个细粒度密码策略在所有细粒度密码策略中的优先级。该参数用于设置细粒度密码策略的 **优先级** 属性。此属性的 LDAP 显示名称（**ldapDisplayName**）为 `msDS-PasswordSettingsPrecedence`。

这个值用于确定当一个用户或组适用多个密码策略时应该使用哪个密码策略。当出现冲突时，优先级较低的密码策略会被选中。例如，如果 PasswordPolicy1 的 **Precedence** 属性值为 200，而 PasswordPolicy2 的 **Precedence** 属性值为 100，则会使用 PasswordPolicy2。

通常，密码策略的优先级值是以10或100的倍数来设置的，这样日后添加新策略时会更加方便。例如，如果你将所有策略的初始优先级值分别设置为100和200，那么之后就可以再添加一个优先级值为150的策略了。

如果指定的 `Precedence` 参数已经被分配给了另一个密码策略对象，那么该 cmdlet 会返回一个终止错误。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ProtectedFromAccidentalDeletion
指定是否阻止对象被删除。当此属性设置为 `true` 时，如果不更改该属性的值，则无法删除相应的对象。该参数的可接受值如下：

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReversibleEncryptionEnabled
Specifies whether the directory must store passwords using reversible encryption.
This parameter sets the **ReversibleEncryption** property for a password policy.
The acceptable values for this parameter are:

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services），或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的列出顺序：

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
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy
一个用于创建新的细粒度密码策略对象的模板形式的细粒度密码策略对象，通过*Instance*参数被接收。

## 输出

### 无值或 Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy
当指定 *PassThru* 参数时，此 cmdlet 会返回新的细粒度密码策略对象。默认情况下，该 cmdlet 不会生成任何输出。

## 备注
* This cmdlet does not work with Active Directory Lightweight Directory Services (AD LDS).
* This cmdlet does not work with a read-only domain controller.
* This cmdlet does not work with an Active Directory snapshot.

## 相关链接

[Get-ADFineGrainedPasswordPolicy](./Get-ADFineGrainedPasswordPolicy.md)

[Remove-ADFineGrainedPasswordPolicy](./Remove-ADFineGrainedPasswordPolicy.md)

[Set-ADFineGrainedPasswordPolicy](./Set-ADFineGrainedPasswordPolicy.md)

[Windows PowerShell中的AD DS管理cmdlet](./activedirectory.md)

