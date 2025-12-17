---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adforest?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADForest
---

# Set-ADForest

## 摘要
修改Active Directory林（forest）。

## 语法

```
Set-ADForest [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADForest>
 [-PassThru] [-Server <String>] [-SPNSuffixes <Hashtable>] [-UPNSuffixes <Hashtable>] [<CommonParameters>]
```

## 描述
`Set-ADForest` cmdlet 用于修改 Active Directory 林的属性。您可以通过使用 cmdlet 参数来修改常用的属性值。那些未与 cmdlet 参数关联的属性值，则可以使用 `Add`、`Replace`、`Clear` 和 `Remove` 参数来进行修改。

`Identity` 参数用于指定要修改的 Active Directory 林（forest）。您可以通过其完全限定域名（FQDN）、GUID、DNS 主机名或 NetBIOS 名称来识别该林。您还可以将 `Identity` 参数设置为一个对象变量（例如 `$<localADForestObject>`），或者通过管道将该对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADForest` cmdlet 获取一个林对象，然后通过管道将该对象传递给 `Set-ADForest` cmdlet。

`Instance` 参数提供了一种通过应用对对象副本所做的更改来更新 Active Directory 林对象的方法。当您将 `Instance` 参数设置为已修改的 Active Directory 林对象的副本时，`Set-ADForest` cmdlet 会将对原始林对象进行相同的更改。要获取用于修改的对象副本，请使用 `Get-ADForest` 命令。在使用 `Instance` 参数时，不允许同时使用 `Identity` 参数。有关 `Instance` 参数的更多信息，请参阅其相关描述。

## 示例

### 示例 1：更新森林的某个属性
```
PS C:\> Set-ADForest -Identity fabrikam.com -UPNSuffixes @{replace="fabrikam.com","fabrikam","corp.fabrikam.com"}
```

此命令为 fabrikam.com 林设置了 **UPNSuffixes** 属性。

### 示例 2：为森林属性添加一个值
```
PS C:\> Set-ADForest -Identity fabrikam.com -SPNSuffixes @{add="corp.fabrikam.com"}
```

此命令将 `corp.fabrikam.com` 添加到森林 `fabrikam.com` 的 `SPNSuffixes` 属性中。

### 示例 3：更新森林的一个属性
```
PS C:\> Get-ADForest | Set-ADForest -SPNSuffixes @{Add="corp.fabrikam.com";Remove="fabrikam"}
```

该命令获取当前登录用户的 forests（森林对象），并更新 **SPNSuffixes** 属性。

### 示例 4：清除与森林相关的某个属性
```
PS C:\> Get-ADForest | Set-ADForest -UPNSuffixes $Null
```

这个命令会获取当前登录用户的“forest”（可能是某种数据结构或配置信息），并清除其中的**UPNSuffixes**属性。

### 示例 5：更新本地森林的一个属性
```
PS C:\> $Forest = Get-ADForest -Identity fabrikam.com
PS C:\> $Forest.UPNSuffixes = "fabrikam.com","fabrikam","corp.fabrikam.com"
PS C:\> Set-ADForest -Instance $Forest
```

这个示例修改了 fabrikam.com 林的 **UPNSuffixes** 属性。该示例首先修改 fabrikam.com 林的本地实例，然后将当前 cmdlet 的 *Instance* 参数设置为该本地实例。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值包括：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果该执行任务的用户账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
通过提供以下属性值之一来指定一个 Active Directory 林对象。括号中的标识符是该属性在轻量级目录访问协议（LDAP）中的显示名称。此参数的可接受值为：

- A fully qualified domain name
- A GUID (objectGUID)
- A DNS host name
- A NetBIOS name

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的操作错误（即操作会持续进行但不会成功完成）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个森林对象（forest object）的实例。

```yaml
Type: ADForest
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您当前操作对象的实例。默认情况下，此cmdlet不会生成任何输出。

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
指定要连接的 Active Directory 域服务（AD DS）实例，为此提供相应的域名或目录服务器之一的值。该服务可以是以下类型中的任意一种：Active Directory 轻量级目录服务（AD LDS）、AD DS 或 Active Directory 快照实例。

以下列方式之一指定 AD DS 实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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
### -SPNSuffixes
修改林中服务主体名称（Service Principal Name，简称 SPN）后缀的列表。该参数用于设置跨引用容器中的多值属性 **msDS-SPNSuffixes**。通过以下语法可以添加、删除、替换或清除 SPN 后缀的值：

要添加值：

`-SPNSuffixes @{Add=value1,value2,...}`

要删除某个值：

`-SPNSuffixes @{Remove=value3,value4,...}`

要替换值：

`-SPNSuffixes @{Replace=value1,value2,...}`

要清除所有值：

`-SPNSuffixes $Null`

你可以使用由分号分隔的列表来指定多个更改。例如，使用以下语法来添加或删除 SPN 后缀值：

`@{Add=value1,value2,...};@{Remove=value3,value4,...}`

操作符按照以下顺序应用：

- Remove
- Add
- Replace

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


### -UPNSuffixes
Modifies the list of user principal name (UPN) suffixes of the forest.
This parameter sets the multi-valued **msDS-UPNSuffixes** property of the cross-reference container.
This parameter uses the following syntax to add remove, replace, or clear UPN suffix values.

要添加值：

`-UPNSuffixes  @{Add=value1,value2,...}`

要删除某个值：

`-UPNSuffixes @{Remove=value3,value4,...}`

要替换值：

`-UPNSuffixes @{Replace=value1,value2,...}`

要清除所有值：

`-UPNSuffixes $Null`

You can specify more than one change by using a list separated by semicolons.
For example, use the following syntax to add and remove UPN suffix values:

`@{Add=value1,value2,...};@{Remove=value3,value4,...}`

操作符按照以下顺序应用：

- Remove
- Add
- Replace

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

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

没有相关对象，或者使用了 `MicrosoftActiveDirectory.Management.ADForest`。
一个森林对象通过*Identity*参数被接收。

通过使用 `Get-ADForest` cmdlet 获取到一个森林对象（forest object），对该对象进行修改后，修改后的结果会通过 `Instance` 参数传递进来。

## 输出

没有相关对象，或者使用了 `MicrosoftActiveDirectory.Management.ADForest`。
当指定“PassThru”参数时，该命令会返回修改后的森林对象（forest object）。默认情况下，此命令不会生成任何输出。

## 备注
* This cmdlet does not work with AD LDS.
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADForest](./Get-ADForest.md)

