---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-addomaincontroller?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADDomainController
---

# Get-ADDomainController

## 摘要
根据可发现的服务标准、搜索参数，或提供域名控制器标识符（如NetBIOS名称），获取一个或多个Active Directory域控制器。

## 语法

### 身份（默认值）
```
Get-ADDomainController [-AuthType <ADAuthType>] [-Credential <PSCredential>] [[-Identity] <ADDomainController>]
 [-Server <String>] [<CommonParameters>]
```

### DiscoverByService
```
Get-ADDomainController [-AuthType <ADAuthType>] [-AvoidSelf] [-Discover] [-DomainName <String>]
 [-ForceDiscover] [-MinimumDirectoryServiceVersion <ADMinimumDirectoryServiceVersion>] [-NextClosestSite]
 [-Service <ADDiscoverableService[]>] [-SiteName <String>] [-Writable] [<CommonParameters>]
```

### 过滤器
```
Get-ADDomainController [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String>
 [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADDomainController` cmdlet 可以获取由参数指定的域控制器。你可以通过设置 `Identity`、`Filter` 或 `Discover` 参数来获取所需的域控制器。

`Identity` 参数用于指定要获取的域控制器。您可以通过其 GUID、IPv4 地址、全局 IPv6 地址或 DNS 主机名称来识别域控制器；也可以通过表示该域控制器的服务器对象的名称、NTDS 设置对象的 distinguished name（唯一标识符）、配置分区下的 NTDS 设置对象/服务器对象的 GUID，或者表示该域控制器的计算机对象的 distinguished name 来识别它。此外，您还可以将 `Identity` 参数设置为某个域控制器对象变量（例如 `$<localDomainControllerObject>`），或将一个域控制器对象通过管道传递给 `Identity` 参数。

要搜索并检索多个域控制器，请使用 `Filter` 参数。`Filter` 参数利用 Windows PowerShell 表达式语言来编写 Active Directory 的查询字符串。Windows PowerShell 表达式语言语法为 `Filter` 参数接收的值类型提供了丰富的类型转换支持。有关 `Filter` 参数语法的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter`。您不能使用轻量级目录访问协议 (LDAP) 查询字符串与该 cmdlet 一起使用。

要使用 DCLocator 的发现机制来获取域控制器，请使用 *Discover* 参数。您可以通过设置诸如 *Service*、*SiteName*、*DomainName*、*NextClosestSite*、*AvoidSelf* 和 *ForceDiscover* 等参数来提供搜索条件。

## 示例

### 示例 1：在指定站点中获取一个域控制器
```
PS C:\> Get-ADDomainController -Discover -Site "Default-First-Site-Name"
```

该命令会获取由 *Site* 参数指定的站点中可用的一个域控制器。该命令使用了 Discovery（发现）机制来查找这些可用的域控制器。

### 示例 2：在指定站点中使用强制发现（force discovery）来获取可用的域控制器
```
PS C:\> Get-ADDomainController -Discover -Site "Default-First-Site-Name" -ForceDiscover
```

该命令会在该参数“*Site*”指定的站点中查找一个可用的域控制器。

### 示例 3：使用发现功能获取当前林中的全局目录
```
PS C:\> Get-ADDomainController -Discover -Service "GlobalCatalog"
```

此命令使用 Discovery 功能获取当前林中的全局目录信息。

### 示例 4：使用发现功能获取当前域中可用的域控制器
```
PS C:\> Get-ADDomainController -Discover
```

此命令使用“Discovery”功能来获取当前域中可用的一个域控制器。

### 示例 5：使用发现机制在指定域中获取可用的域控制器
```
PS C:\> Get-ADDomainController -Discover -Domain "user01.com"
```

此命令通过“发现”（Discovery）功能，在给定的域中获取一个可用的域控制器。

### 示例 6：使用发现功能获取作为时间服务器进行广播的主要域控制器
```
PS C:\> Get-ADDomainController -Discover -Domain "corp.contoso.com" -Service "PrimaryDC","TimeService"
```

该命令使用“发现”（Discovery）功能获取主域名控制器，并确保其能够作为时间服务器进行广播（即向其他设备提供时间信息）。

### 示例 7：使用域控制器的 NetBIOS 名称来获取该控制器
```
PS C:\> Get-ADDomainController -Identity "PDC-01"
```

这个命令使用域控制器的NetBIOS名称来获取该控制器。

### 示例 8：使用管理员凭据，在指定的站点中通过域名控制器的 DNS 主机名获取该域名控制器
```
PS C:\> Get-ADDomainController -Identity "TK5-CORP-DC-10.user01.com" -Server "user01.com" -Credential "corp\administrator"
```

该命令使用域控制器的DNS主机名，在由*Server*参数指定的域中获取该控制器，并需要提供管理员凭据。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值如下：

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

### -AvoidSelf
指定不要将当前计算机作为域控制器返回。如果当前计算机本身就不是域控制器，那么这个参数将被忽略。当你需要获取域中其他域控制器的名称时，可以设置这个参数。

```yaml
Type: SwitchParameter
Parameter Sets: DiscoverByService
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Windows PowerShell提供程序的Active Directory模块驱动器中运行的。如果该cmdlet是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果该执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

```yaml
Type: PSCredential
Parameter Sets: Identity, Filter
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Discover
指定返回一个符合命令参数所规定条件的可发现（即可被其他系统识别和使用的）域控制器。

要使用 DCLocator 的发现机制来获取域控制器，请使用 *Discover* 参数。除了这个参数外，您还可以通过设置诸如 *Service*、*SiteName*、*DomainName*、*NextClosestSite*、*AvoidSelf* 和 *ForceDiscover* 等参数来提供搜索条件。

```yaml
Type: SwitchParameter
Parameter Sets: DiscoverByService
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DomainName
指定要搜索的域。此cmdlet会在此域中查找可发现的域控制器。请使用该域的NetBIOS名称或完全限定域名（FQDN）来指定该域。

```yaml
Type: String
Parameter Sets: DiscoverByService
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Filter
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 Windows PowerShell 表达式语言的语法。Windows PowerShell 表达式语言为 *Filter* 参数接收的值类型提供了丰富的类型转换支持。这种语法采用“按顺序排列”的表示方式，即运算符被放置在操作数和值之间。有关 *Filter* 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter`。

语法：

以下语法使用了巴克斯-诺尔（Backus-Naur）形式来说明如何使用 Windows PowerShell 表达式语言来处理这个参数。

\<filter\>  ::= "{" \<FilterComponentList\> "}"

<FilterComponentList> ::= <FilterComponent> | <FilterComponent> <JoinOperator> <FilterComponent> | <NotOperator> <FilterComponent>

\<FilterComponent\> ::= \<attr\> \<FilterOperator\> \<value\> | ("\<FilterComponent\>:")

\<FilterOperator\> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

\<JoinOperator\> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

\<attr\> ::= \<propertyName\> | \<属性的 LDAP 显示名称\>

<value>::= <使用指定的<FilterOperator>将此值与<attr>进行比较>

要查看 `<value>` 支持的数据类型列表，请输入 `Get-Help about_ActiveDirectory_ObjectModel`。

注意：PowerShell中的通配符（除了*之外，例如?）不被*Filter*语法支持。

注意：要使用 LDAP 查询字符串进行查询，请使用 *LDAPFilter* 参数。

```yaml
Type: String
Parameter Sets: Filter
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ForceDiscover
表示该cmdlet会清除所有缓存的域控制器信息，并重新进行发现操作。如果未指定此参数，cmdlet可能会返回缓存的域控制器信息。

```yaml
Type: SwitchParameter
Parameter Sets: DiscoverByService
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity
通过提供以下值之一来指定一个 Active Directory 域控制器对象。括号中的标识符是该属性的 LDAP 显示名称。除非另有说明，这些值都是用于表示域控制器的服务器对象的。此参数的可接受值为：

- A GUID (objectGUID)
- An IPV4Address
- A Global IPV6Address
- A DNS Host Name (dNSHostName)
- The name of the server object
- The distinguished name of the NTDS Settings object
- The distinguished name of the server object that represents the domain controller
- The GUID of NTDS settings object under the configuration partition
- The GUID of server object under the configuration partition
- The distinguished name of the computer object that represents the domain controller

此cmdlet会在默认的命名上下文或分区中搜索该对象。如果找到两个或多个对象，cmdlet会返回一个无法终止的错误（即操作无法继续进行）。

这个参数也可以通过管道来获取该对象，或者你可以将该参数设置为一个对象实例。

```yaml
Type: ADDomainController
Parameter Sets: Identity
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -MinimumDirectoryServiceVersion
`Species` 是域名控制器可以使用的最早的操作系统版本，因此在使用 `*Discover` 参数获取域名控制器时，该信息会通过相应的 cmdlet 返回。此参数的可接受值包括：

- Windows2000 or 1
- Windows2008 or 2

```yaml
Type: ADMinimumDirectoryServiceVersion
Parameter Sets: DiscoverByService
Aliases:
Accepted values: Windows2000, Windows2008, Windows2012, Windows2012R2

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NextClosestSite
当在包含客户端的那個站点中找不到域控制器时，该选项指定返回下一个最近的站点中的域控制器。所谓“下一个最近的站点”，是指与当前站点相比具有最低站点链接成本的站点。站点之间的成本取决于多种因素，例如带宽以及物理距离等。

```yaml
Type: SwitchParameter
Parameter Sets: DiscoverByService
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

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
Parameter Sets: Identity, Filter
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Service
Species the types of domain controllers to get.
You can specify more than one type by using a comma-separated list.
The acceptable values for this parameter are:

- PrimaryDC or 1
- GlobalCatalog or 2
- KDC or 3
- TimeService or 4
- ReliableTimeService or 5
- ADWS or 6

```yaml
Type: ADDiscoverableService[]
Parameter Sets: DiscoverByService
Aliases:
Accepted values: PrimaryDC, GlobalCatalog, KDC, TimeService, ReliableTimeService, ADWS

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SiteName
Specifies the name of a site to search in to find the domain controller.
If this parameter is not set, the cmdlet searches for domain controllers in the same site as the client.
The name of the site is defined by the **Name** property of the site object.

```yaml
Type: String
Parameter Sets: DiscoverByService
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Writable
Specifies whether this is a writable domain controller.

```yaml
Type: SwitchParameter
Parameter Sets: DiscoverByService
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### Microsoft.ActiveDirectory.Management.ADDomainController
A domain controller object is received by the *Identity* parameter.

## 输出

### Microsoft.ActiveDirectory.Management.ADDomainController
This cmdlet returns one or more domain controller objects.

When you use the *Discover* parameter to get a domain controller, the cmdlet returns a default set of property values for each domain controller.

When you use the *Identity* or *Filter* parameters to get a domain controller, this cmdlet returns all of the properties of the domain controller.

To view all of the properties for an **ADDomainController** object, use the following command and replace \<domaincontroller\> with a domain controller identifier such as a DNS host name.

`Get-ADDomainController`\<domaincontroller\>`| Get-Member`

## 备注
* The **Name** and **HostName** properties of the **ADDomainController** objects returned by the cmdlet are set according to the following rules:

  - If the *Discover* parameter is used, HostName is the Fully Qualified Domain Name of the Domain Controller, and the Name is the NetBIOS name of the Domain Controller.
With the *Discover* parameter, the cmdlet will perform a second DCLocator call, to populate the **Name** property.
This property will not be set, to the NetBIOS name of the Domain Controller, if the WINS service is unavailable.

  - If the *Identity* or the *Filter* parameter is used, **HostName** is the **DNSHostName** attribute of the Domain Controller object, and the **Name** is the **Name** (RDN) attribute of the Domain Controller object.
With the *Identity* or the *Filter* parameter, the **HostName** property will not be set, if the **DNSHostName** attribute of the Domain Controller object is null.

* This cmdlet does not work with Active Directory Lightweight Directory Services (AD LDS).
* This cmdlet does not work when targeting a snapshot using the *Server* parameter.

## 相关链接

[Add-ADDomainControllerPasswordReplicationPolicy](./Add-ADDomainControllerPasswordReplicationPolicy.md)

[Get-ADDomainControllerPasswordReplicationPolicy](./Get-ADDomainControllerPasswordReplicationPolicy.md)

[Remove-ADDomainControllerPasswordReplicationPolicy](./Remove-ADDomainControllerPasswordReplicationPolicy.md)
