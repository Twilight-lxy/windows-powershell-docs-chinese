---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adforest?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADForest
---

# Get-ADForest

## 摘要
获取一个 Active Directory 林（即多个域组成的集合）。

## 语法

### 当前设置（默认值）
```
Get-ADForest [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Current <ADCurrentForestType>]
 [-Server <String>] [<CommonParameters>]
```

### 身份
```
Get-ADForest [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADForest> [-Server <String>]
 [<CommonParameters>]
```

## 描述
`Get-ADForest` cmdlet 可以获取指定的 Active Directory 林（forest）。你可以通过设置 `Identity` 或 `Current` 参数来指定所需的 Active Directory 林。

`Identity` 参数用于指定要获取的 Active Directory 林（forest）。您可以通过其完全限定域名（FQDN）、DNS 主机名或 NetBIOS 名来识别该林。您还可以将此参数设置为一个林对象变量（例如 `$<localForestObject>`），或者通过管道将一个林对象传递给 `Identity` 参数。

要获取本地计算机或当前登录用户的详细信息，请将 *Current* 参数设置为 LocalComputer 或 LoggedOnUser。当您设置了 *Current* 参数后，就无需再设置 *Identity* 参数了。

当 *Current* 参数被设置为 LocalComputer 或 LoggedOnUser 时，该 cmdlet 会使用 *Server* 和 *Credential* 参数的值来确定域名以及用于识别该域的凭据。具体规则如下：

- If both the *Server* and *Credential* parameters are not specified:

该域名被设置为 LocalComputer 或 LoggedOnUser 的所属域，并且有一台服务器位于这个域中。当前登录用户的凭据被用来获取该域名。

- If the *Server* parameter is specified and the *Credential* parameter is not specified:

该域名被设置为指定服务器所属的域名，然后该cmdlet会检查该服务器是否属于LocalComputer或LoggedOnUser所在的域。接着，使用当前登录用户的凭据来获取相应的域名信息。如果该服务器不属于LocalComputer或LoggedOnUser所在的域，则会返回错误信息。

- If the *Server* parameter is not specified and the *Credential* parameter is specified:

该域名被设置为 LocalComputer 或LoggedOnUser 的所属域，并且有一个服务器位于这个域中。然后，使用 *Credential* 参数指定的凭据来获取该域名。

- If the *Server* and *Credential* parameters are specified:

该域名被设置为指定服务器所属的域名称，然后cmdlet会检查该服务器是否属于LocalComputer或LoggedOnUser所在的域。接着，使用由*Credential*参数指定的凭据来获取该域名。如果该服务器不属于LocalComputer或LoggedOnUser所在的域，则会返回错误信息。

## 示例

### 示例 1：获取域森林的相关信息
```
PS C:\> Get-ADForest -Identity Fabrikam.com
```

这个命令用于获取Fabrikam.com森林（即该网络环境）的相关信息。

### 示例 2：获取本地计算机群组的信息
```
PS C:\> Get-ADForest -Current LocalComputer
```

这个命令可以获取当前本地计算机所属的森林（forest）的相关信息。

### 示例 3：获取当前用户所管理的森林的相关信息
```
PS C:\> Get-ADForest -Current LoggedOnUser
```

这个命令可以获取当前登录用户的森林（forest）相关信息。

### 示例 4：获取当前用户所在森林的信息
```
PS C:\> Get-ADForest
ApplicationPartitions  : {DC=ForestDnsZones,DC=Fabrikam,DC=com, DC=DomainDnsZones,DC=Fabrikam,DC=com}
CrossForestReferences  : {CN=northwind,CN=Partitions,CN=Configuration,DC=Fabrikam,DC=com}
DomainNamingMaster     : Fabrikam-DC1.Fabrikam.com
Domains                : {Fabrikam.com}
ForestMode             : Windows2003Forest
GlobalCatalogs         : {Fabrikam-DC1.Fabrikam.com, CSD2722780.Fabrikam.com}
Name                   : Fabrikam.com
PartitionsContainer    : CN=Partitions,CN=Configuration,DC=Fabrikam,DC=com
RootDomain             : Fabrikam.com
SchemaMaster           : Fabrikam-DC1.Fabrikam.com
Sites                  : {Default-First-Site-Name, UnitedKingdomHQ, BO3, RODC-Site-Name}
SPNSuffixes            : {}
UPNSuffixes            : {}
```

这个命令可以获取当前登录用户的森林（forest）相关信息。

### 示例 5：获取林中所有域的所有域控制器
```
PS C:\> $AllDCs = (Get-ADForest).Domains | %{ Get-ADDomainController -Filter * -Server $_ }
```

这个命令可以获取整个林中所有域的所有域控制器信息。

## 参数

### -AuthType
指定要使用的身份验证方法。此参数的可接受值包括：

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

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Windows PowerShell提供程序的Active Directory模块驱动器中运行的。如果该cmdlet是从此类驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行该任务的代理程序没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

### -Current
指定是返回本地计算机的域名还是当前登录用户的身份信息。该参数的可接受值包括：

- LocalComputer or 0
- LoggedOnUser  or 1

```yaml
Type: ADCurrentForestType
Parameter Sets: Current
Aliases:
Accepted values: LocalComputer, LoggedOnUser

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity
通过提供以下属性值之一来指定一个 Active Directory 林对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A fully qualified domain name
- A GUID (objectGUID)
- A DNS host name
- A NetBIOS name

该cmdlet会在默认的命名上下文或分区中搜索目标对象。如果找到两个或多个对象，它将返回一个无法终止的错误信息。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个森林对象（forest object）的实例。

```yaml
Type: ADForest
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务（AD DS）实例，为此提供相应的域名或目录服务器之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级目录服务（AD LDS）、AD DS 或 Active Directory 快照实例。

以下是几种指定 AD DS 实例的方法：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无，或使用 `Microsoft ActiveDirectory.Management.ADForest`
一个森林对象通过*Identity*参数被接收。

## 输出

### Microsoft ActiveDirectory.Management.ADForest
返回一个或多个森林对象（forest objects）。

此cmdlet会返回森林（forest）的所有属性。要查看某个**ADForest**对象的所有属性，请使用以下命令，并将\<forest\>替换为相应的森林标识符（例如DNS主机名）。

`Get-ADForest `<forest>` | Get-Member`

## 备注
* This cmdlet does not work with AD LDS.
* This cmdlet does not work when targeting a snapshot using the *Server* parameter.

## 相关链接

[Set-ADForest](./Set-ADForest.md)

