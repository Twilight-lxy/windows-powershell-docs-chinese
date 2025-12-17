---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-addomaincontrollerpasswordreplicationpolicyusage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADDomainControllerPasswordReplicationPolicyUsage
---

# 获取 AD 域控制器密码复制策略的使用情况

## 摘要
获取那些由只读域控制器进行身份验证的 Active Directory 账户，或者那些位于该域控制器公开列表中的账户。

## 语法

### RevealedAccounts（默认设置）
```
Get-ADDomainControllerPasswordReplicationPolicyUsage [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADDomainController> [-RevealedAccounts] [-Server <String>] [<CommonParameters>]
```

### 已认证账户
```
Get-ADDomainControllerPasswordReplicationPolicyUsage [-AuthenticatedAccounts] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADDomainController> [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADDomainControllerPasswordReplicationPolicyUsage` cmdlet 可以获取由只读域控制器（RODC）进行身份验证的用户或计算机账户，或者那些密码存储在 RODC 上的账户。存储在 RODC 上的账户列表被称为“公开列表”。

要获取由 RODC 进行身份验证的账户，请使用 **AuthenticatedAccounts** 参数。要获取密码存储在 RODC 上的账户，请使用 **RevealedAccounts** 参数。

`Identity` 参数用于指定 RODC（Windows 网域控制器对象）。您可以通过域控制器的 GUID、IPV4Address、全局 IPV6Address 或 DNS 主机名称来识别它。此外，您还可以通过表示该域控制器的服务器对象的名称、该服务器对象的 NTDS 设置对象的 distinguished name、配置分区下该服务器对象的 NTDS 设置对象的 GUID，或者表示该域控制器的计算机对象的 distinguished name 来识别它。您也可以将 `Identity` 参数设置为某个域控制器对象变量（例如 `$\<localDomainControllerObject\>`），或者通过管道将该域控制器对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADDomainController` cmdlet 获取一个域控制器对象，然后将其通过管道传递给 `Get-ADDomainControllerPasswordReplicationPolicyUsage` cmdlet。如果您为该 cmdlet 指定了一个可写入的域控制器，那么该 cmdlet 会返回一个非终止性错误。

## 示例

### 示例 1：获取特定 RODC 的已认证账户
```
PS C:\> Get-ADDomainControllerPasswordReplicationPolicyUsage -Identity "USER01-RODC1" -AuthenticatedAccounts | ft Name,ObjectClass -A
```

该命令会获取由 **Identity** 参数指定的 RODC（Remote Desktop Controller）中的已认证账户信息，并显示每个账户的名称和对象类别。

### 示例 2：获取指定 RODC 的已泄露账户信息
```
PS C:\> Get-ADDomainControllerPasswordReplicationPolicyUsage -Identity "USER01-RODC1" -RevealedAccounts | ft Name,ObjectClass -A
```

此命令用于获取由 **Identity** 参数指定的 RODC（Root Domain Controller）中所有被暴露的账户信息。该命令会显示每个返回的账户的名称和对象类别。

### 示例 3：获取缓存在所有 RODC 中的账户列表
```
PS C:\> Get-ADDomainController -Filter "IsReadOnly -eq `$true" | Get-ADDomainControllerPasswordReplicationPolicyUsage
DistinguishedName : CN=krbtgt_35512,CN=Users,DC=User01,DC=com
Enabled           : False
Name              : krbtgt_35512
ObjectClass       : user
ObjectGUID        : 8c7268f9-add3-409c-968b-de029e517211
SamAccountName    : krbtgt_35512
SID               : S-1-5-21-41432690-3719764436-1984117282-1106
UserPrincipalName :

DistinguishedName : CN=CSD2722780,OU=Domain Controllers,DC=User01,DC=com
Enabled           : True
Name              : CSD2722780
ObjectClass       : computer
ObjectGUID        : 63a5e005-e01f-4fc9-ae71-9d9367f808bc
SamAccountName    : CSD2722780$
SID               : S-1-5-21-41432690-3719764436-1984117282-1105
UserPrincipalName :
```

这个命令会获取存储在域中所有 RODC（Remote Domain Controllers）中的账户列表。

## 参数

### -AuthenticatedAccounts
指定搜索那些已经通过只读域控制器进行身份验证的账户。

```yaml
Type: SwitchParameter
Parameter Sets: AuthenticatedAccounts
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

指定用于执行任务的安全上下文的凭据。如果该安全上下文没有执行任务所需的目录级权限，那么目录会返回错误信息。如果在 Windows PowerShell 提供程序驱动器的 Active Directory 模块上下文中运行，则使用与该驱动器关联的凭据信息作为默认值；否则，将使用当前登录用户的 security context（安全上下文）。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果该执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
通过提供以下值之一来指定一个 Active Directory 域控制器对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A GUID (objectGUID).
- An IPV4Address.
- A Global IPV6Address.
- A DNS Host Name (dNSHostName).
- A name of the server object.
- A distinguished name of the NTDS Settings object.
- A distinguished name of the server object that represents the domain controller.
- A GUID of NTDS settings object under the configuration partition.
- A GUID of server object under the configuration partition.
- A distinguished name of the computer object that represents the domain controller.

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误（即程序会无限循环执行）。

这个参数也可以通过管道获取对象，或者你可以将这个参数设置为某个对象的实例。

```yaml
Type: ADDomainController
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -RevealedAccounts
指定搜索那些密码存储在只读域控制器上的账户。

```yaml
Type: SwitchParameter
Parameter Sets: RevealedAccounts
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
通过提供相应的域名或目录服务器的值之一，指定要连接的 Active Directory 域服务实例。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务、Active Directory 域服务或 Active Directory 快照实例。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name.
- NetBIOS name.

Directory server values:

- Fully qualified directory server name.
- NetBIOS name.
- Fully qualified directory server name and port.

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

- By using the **Server** value from objects passed through the pipeline.
- By using the server information associated with the Active Directory Domain Services Windows PowerShell provider drive when the cmdlet runs in that drive.
- By using the domain of the computer running Windows PowerShell.

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ActiveDirectory.Management.AddDomainController
域控制器对象是通过*Identity*参数接收到的。

## 输出

### Microsoft ActiveDirectory Management.ADAccount
此cmdlet返回一个或多个账户对象，这些对象代表那些由指定的RODC进行身份验证的用户、计算机和服务账户，或者是指那些密码存储在RODC上的账户。

## 备注
* This cmdlet does not work with Active Directory Lightweight Directory Services (AD LDS).
* This cmdlet does not work when targeting a snapshot using the *Server* parameter.

## 相关链接

[Get-ADDomainController](./Get-ADDomainController.md)

[Add-ADDomainControllerPasswordReplicationPolicy](./Add-ADDomainControllerPasswordReplicationPolicy.md)

[Get-ADDomainControllerPasswordReplicationPolicy](./Get-ADDomainControllerPasswordReplicationPolicy.md)

[Remove-ADDomainControllerPasswordReplicationPolicy](./Remove-ADDomainControllerPasswordReplicationPolicy.md)

[Windows PowerShell中的AD DS管理命令集](./activedirectory.md)

