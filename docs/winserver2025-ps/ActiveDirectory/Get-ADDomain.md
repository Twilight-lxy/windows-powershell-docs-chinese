---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-addomain?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADDomain
---

# Get-ADDomain

## 摘要
获取一个 Active Directory 域名。

## 语法

### 当前设置（默认值）
```
Get-ADDomain [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Current <ADCurrentDomainType>]
 [-Server <String>] [<CommonParameters>]
```

### 身份证明
```
Get-ADDomain [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADDomain> [-Server <String>]
 [<CommonParameters>]
```

## 描述
`Get-ADDomain` cmdlet 可以获取由参数指定的 Active Directory 域名。您可以通过设置 `Identity` 或 `Current` 参数来指定该域名。

`Identity` 参数用于指定要获取的 Active Directory 域。您可以通过该域对象的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier，SID）、DNS 域名或 NetBIOS 名称来识别该域对象。此外，您还可以将该参数设置为某个域对象变量（例如 `$<localDomainObject>`），或者通过管道将一个域对象传递给 `Identity` 参数。

要获取本地计算机的域名或当前登录用户的身份信息，请将 *Current* 参数设置为 LocalComputer 或 LoggedOnUser。当您设置了 *Current* 参数后，就不需要再设置 *Identity* 参数了。

当 *Current* 参数设置为 LocalComputer 或 LoggedOnUser 时，cmdlet 会根据以下规则使用 *Server* 和 *Credential* 参数。

- If both the *Server* and *Credential* parameters are not specified:
- The domain is set to the domain of the LocalComputer or LoggedOnUser and a server is located in this domain. The credentials of the current logged on user are used to get the domain.
- If the *Server* parameter is specified and the *Credential* parameter is not specified:
- The domain is set to the domain of the specified server and the cmdlet checks to make sure that the server is in the domain of the LocalComputer or LoggedOnUser. Then the credentials of the current logged on user are used to get the domain. An error is returned when the server is not in the domain of the LocalComputer or LoggedOnUser.
- If the *Server* parameter is not specified and the *Credential* parameter is specified:
- The domain is set to the domain of the LocalComputer or LoggedOnUser and a server is located in this domain. Then the credentials specified by the *Credential* parameter are used to get the domain.
- If the *Server* and *Credential* parameters are specified:
- The domain is set to the domain of the specified server and the cmdlet checks to make sure that the server is in the domain of the LocalComputer or LoggedOnUser. Then the credentials specified by the *Credential* parameter are used to get the domain. An error is returned when the server is not in the domain of the LocalComputer or LoggedOnUser.

## 示例

### 示例 1：从 Active Directory 中获取域名信息
```
PS C:\> Get-ADDomain -Identity user.com
```

这个命令用于获取域 user.com 的相关域名信息。

### 示例 2：获取当前本地计算机所在域的域名信息
```
PS C:\> Get-ADDomain -Current LocalComputer
```

这个命令用于获取当前本地计算机所在域的域名信息。

### 示例 3：获取当前登录用户的域名对应的域信息
```
PS C:\> Get-ADDomain -Current LoggedOnUser
```

这个命令可以获取当前登录用户的所属域的域名信息。

### 示例 4：获取当前登录用户的域名所属域的信息
```
PS C:\> Get-ADDomain
AllowedDNSSuffixes                 : {}
ChildDomains                       : {}
ComputersContainer                 : CN=Computers,DC=User04,DC=com
DeletedObjectsContainer            : CN=Deleted Objects,DC=User04,DC=com
DistinguishedName                  : DC=User04,DC=com
DNSRoot                            : User04.com
DomainControllersContainer         : OU=Domain Controllers,DC=User04,DC=com
DomainMode                         : Windows2003Domain
DomainSID                          : S-1-5-21-41432690-3719764436-1984117282
ForeignSecurityPrincipalsContainer : CN=ForeignSecurityPrincipals,DC=User04,DC=com
Forest                             : User04.com
InfrastructureMaster               : User04-DC1.User04.com
LastLogonReplicationInterval       :
LinkedGroupPolicyObjects           : {CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=User04,DC=com}
LostAndFoundContainer              : CN=LostAndFound,DC=User04,DC=com
ManagedBy                          :
Name                               : User04
NetBIOSName                        : USER04
ObjectClass                        : domainDNS
ObjectGUID                         : b63b4f44-58b9-49cf-8911-b36e8575d5eb
ParentDomain                       :
PDCEmulator                        : User04-DC1.User04.com
QuotasContainer                    : CN=NTDS Quotas,DC=User04,DC=com
ReadOnlyReplicaDirectoryServers    : {CSD2722780.User04.com}
ReplicaDirectoryServers            : {User04-DC1.User04.com}
RIDMaster                          : User04-DC1.User04.com
SubordinateReferences              : {DC=ForestDnsZones,DC=User04,DC=com, DC=DomainDnsZones,DC=User04,DC=com, CN=Co
nfiguration,DC=User04,DC=com}
SystemsContainer                   : CN=System,DC=User04,DC=com
UsersContainer                     : CN=Users,DC=User04,DC=com
```

这个命令可以获取当前登录用户的所属域的域名信息。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的提供程序驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定这个参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

您也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行任务的代理（acting agent）没有相应的目录级别权限，Windows PowerShell 的 Active Directory 模块将会返回一个终止错误（terminating error）。

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
Type: ADCurrentDomainType
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
通过提供以下属性值之一来指定一个 Active Directory 域对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。所有值都适用于表示该域的 **domainDNS** 对象。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A DNS domain name
- A NetBIOS domain name

该cmdlet会在默认的命名上下文或分区中搜索以找到相应的对象。如果找到了两个或多个对象，该cmdlet会返回一个无法终止（即持续出现的）错误信息。

这个参数也可以通过管道获取该对象，或者你可以将此参数设置为一个域对象的实例。

```yaml
Type: ADDomain
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列任意一种方式指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法中的一种确定的，确定顺序按照列出的顺序进行：

- By using the **Server** value from objects passed through the pipeline
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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft ActiveDirectory.Management.AddDomain
域对象是通过*Identity*参数接收到的。

## 输出

### Microsoft ActiveDirectory.Management.AddDomain
此cmdlet返回一个或多个域对象。

该cmdlet会返回该域的所有属性。要查看某个**ADDomain**对象的所有属性，请使用以下命令，并将\<domain\>替换为域名控制器标识符（例如DNS主机名）。

`Get-ADDomain <domain>` | `Get-Member`

## 备注
* This cmdlet does not work with Active Directory Lightweight Directory Services (AD LDS).
* This cmdlet does not work when targeting a snapshot using the *Server* parameter.

## 相关链接

[Set-ADDomain](./Set-ADDomain.md)

[Set-ADDomainMode](./Set-ADDomainMode.md)

