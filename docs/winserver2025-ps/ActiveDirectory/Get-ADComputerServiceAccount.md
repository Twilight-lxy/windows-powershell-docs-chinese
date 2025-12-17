---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adcomputerserviceaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADComputerServiceAccount
---

# Get-ADComputerServiceAccount

## 摘要
获取由某台计算机托管的服务账户信息。

## 语法

```
Get-ADComputerServiceAccount [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADComputer>
 [-Partition <String>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADComputerServiceAccount` cmdlet 可以获取由指定计算机托管的所有服务账户信息。

`Computer` 参数用于指定托管服务账户的 Active Directory 服务器。您可以通过计算机的 distinguished name（唯一名称）、GUID、安全标识符 (SID) 或 Security Accounts Manager (SAM) 账户名称来识别该计算机。您还可以将 `Computer` 参数设置为某个计算机对象变量（例如 `$<localComputerobject>`），或者通过管道将该计算机对象传递给 `Computer` 参数。例如，您可以使用 `Get-ADComputer` cmdlet 获取一个计算机对象，然后通过管道将该对象传递给 `Get-ADComputerServiceAccount` cmdlet。

## 示例

### 示例 1：获取所有托管在指定计算机账户上的服务账户
```
PS C:\> Get-ADComputerServiceAccount -Identity ComputerAcct1
Enabled           : True
Name              : SvcAcct1
UserPrincipalName :
SamAccountName    : SvcAcct1$
ObjectClass       : msDS-ManagedServiceAccount
SID               : S-1-5-21-159507390-2980359153-3438059098-1104
ObjectGUID        : 8d759d66-ef68-4360-aff6-ec3bb3425ac1
HostComputers     : {CN=ComputerAcct1,CN=Computers,DC=contoso,DC=com}
DistinguishedName : CN=SvcAcct1,CN=Managed Service Accounts,DC=contoso,DC=com
```

这个命令用于获取托管在计算机账户“ComputerAcct1”上的服务账户信息。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值为：

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

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

您也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

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
通过提供以下属性值之一来指定一个 Active Directory 计算机对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- Security Accounts Manager account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果提供的标识符是一个“distinguished name”（特殊名称），那么用于搜索的分区将根据这个名称来确定。如果找到两个或多个对象，cmdlet会返回一个表示搜索未完成的错误信息。

这个参数也可以通过数据流（pipeline）来获取相应的对象，或者你可以将这个参数设置为一个计算机对象的实例。

```yaml
Type: ADComputer
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Partition
指定 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上支持的命名上下文之一。此 cmdlet 会在该分区中查找由 *Identity* 参数定义的对象。

在许多情况下，如果未指定 `Partition` 参数的值，则会使用默认值。确定默认值的规则如下所示。请注意，列出的规则会按顺序依次进行评估；一旦确定了默认值，后续的规则将不再被执行。

在 Active Directory 域服务环境中，在以下情况下会为“分区（Partition）”设置一个默认值：

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

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

### -Server
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的相关值。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，确定顺序按照列出的顺序进行：

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft ActiveDirectory.Management_ADComputer
计算机对象通过“Computer”参数被接收。

## 输出

### Microsoft.ActiveDirectory.Management.ADServiceAccount
返回一个或多个对象，这些对象代表由指定计算机托管的服务账户。

## 备注
* This cmdlet does not work with AD LDS.

## 相关链接

[Add-ADComputerServiceAccount](./Add-ADComputerServiceAccount.md)

[Get-ADComputer](./Get-ADComputer.md)

[Remove-ADComputerServiceAccount](./Remove-ADComputerServiceAccount.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

