---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-addefaultdomainpasswordpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADDefaultDomainPasswordPolicy
---

# 获取 AD 默认域密码策略

## 摘要
获取Active Directory域的默认密码策略。

## 语法

### 当前（默认）设置
```
Get-ADDefaultDomainPasswordPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [[-Current] <ADCurrentDomainType>] [-Server <String>] [<CommonParameters>]
```

### 身份
```
Get-ADDefaultDomainPasswordPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADDefaultDomainPasswordPolicy> [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADDefaultDomainPasswordPolicy` cmdlet 可以获取某个域的默认密码策略。

`Identity` 参数用于指定 Active Directory 域。您可以通过域的 distinguished name、GUID、Security Identifier (SID)、DNS 域名或 NETBIOS 名来识别一个域。此外，您还可以将该参数设置为某个域对象变量（例如 `$<localDomainObject>`），或者通过管道将一个域对象传递给 `Identity` 参数。

## 示例

### 示例 1：从已登录用户的域中获取默认的域名密码策略
```
PS C:\> Get-ADDefaultDomainPasswordPolicy -Current LoggedOnUser
```

该命令从当前登录用户的域中获取默认的域名密码策略。

### 示例 2：从当前本地计算机获取默认的域密码策略
```
PS C:\> Get-ADDefaultDomainPasswordPolicy -Current LocalComputer
```

此命令从当前的本地计算机获取默认的域名密码策略。

### 示例 3：从指定的域中获取默认的域名密码策略
```
PS C:\> Get-ADDefaultDomainPasswordPolicy -Identity fabrikam.com
```

该命令从由 **Site** 参数指定的域中获取默认的域名密码策略。

### 示例 4：从森林中的所有域中获取默认的域名密码策略对象
```
PS C:\> (Get-ADForest -Current LoggedOnUser).Domains | %{ Get-ADDefaultDomainPasswordPolicy -Identity $_ }
```

此命令从林中的所有域中获取默认的域名密码策略对象。

### 示例 5：从已登录用户的域中获取默认的域名密码策略。
```
PS C:\> Get-ADDefaultDomainPasswordPolicy
```

该命令从当前登录用户的域中获取默认的域名密码策略。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值包括：

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

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将该 `Credential` 对象设置为相应的参数。

如果执行该任务的代理凭据没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
- LoggedOnUser or 1

```yaml
Type: ADCurrentDomainType
Parameter Sets: Current
Aliases:
Accepted values: LocalComputer, LoggedOnUser

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity
通过提供以下属性值之一来指定一个 Active Directory 域对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。所有值都适用于表示该域的 domainDNS 对象。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A DNS domain name
- A NetBIOS domain name

该 cmdlet 会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，cmdlet 会返回一个非终止性的错误（即搜索过程无法正常结束）。

这个参数也可以通过管道来获取该对象，或者你可以将这个参数设置为一个域对象的实例。

```yaml
Type: ADDefaultDomainPasswordPolicy
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Server
用于指定要连接的 Active Directory 域服务实例，可以通过提供相应的域名或目录服务器的其中一个值来实现。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft ActiveDirectory.Management.AddDomain
一个域对象通过*Identity*参数被接收。

## 输出

### Microsoft Active Directory Management.AdDefaultDomainPasswordPolicy
返回指定域的默认域密码策略对象。

## 备注
* This cmdlet does not work with AD LDS.
* This cmdlet does not work when targeting a snapshot using the *Server* parameter.

## 相关链接

[Set-ADDefaultDomainPasswordPolicy](./Set-ADDefaultDomainPasswordPolicy.md)

[Get-ADDomain](./Get-ADDomain.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

