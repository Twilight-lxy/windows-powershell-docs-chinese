---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adcomputer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADComputer
---

# 删除广告相关计算机

## 摘要
删除一台Active Directory计算机。

## 语法

```
Remove-ADComputer [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADComputer> [-Partition <String>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Remove-ADComputer` cmdlet 用于删除 Active Directory 中的一台计算机。

`Identity` 参数用于指定要删除的 Active Directory 计算机。您可以通过计算机的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier，SID）或安全账户管理器（Security Accounts Manager，SAM）帐户名来识别该计算机。此外，您还可以将 `Identity` 参数设置为一个计算机对象变量（例如 `$<localComputerObject>`），或者通过管道将该计算机对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADComputer` cmdlet 获取一个计算机对象，然后将其通过管道传递给 `Remove-ADComputer` cmdlet。

## 示例

### 示例 1：从 Active Directory 中删除指定的计算机
```
PS C:\> Remove-ADComputer -Identity "USER04-SRV4"
```

此命令会将指定的计算机从 Active Directory 中删除。

### 示例 2：使用过滤器从指定位置删除所有计算机
```
PS C:\> Get-ADComputer -Filter 'Location -eq "NA/HQ/Building A"' | Remove-ADComputer


Confirm
Are you sure you want to perform this action? Performing operation "Remove" on Target "CN=LabServer-01,CN=Computers,DC=Fabrikam,DC=com".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): a
```

此命令使用*Filter*参数删除指定位置中的所有计算机。

### 示例 3：使用过滤器从指定位置移除所有计算机
```
PS C:\> Get-ADComputer -Filter 'Location -eq "NA/HQ/Building A"' | Remove-ADComputer -Confirm:$False
```

此命令会使用“*Filter*”参数从指定位置删除所有计算机。该命令不会提示您进行确认。

### 示例 4：删除指定目录下的某台计算机以及该目录下所有的子对象（即叶子节点）
```
PS C:\> Get-ADComputer -Identity "USER01-SRV4" | Remove-ADObject -Recursive
```

此命令会删除目录中的一台计算机及其所有子对象。需要注意的是，只有少数计算机对象才会创建子对象（例如运行集群服务的服务器）。这个示例对于删除这些计算机及其相关的所有子对象非常有用。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值包括：

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
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: True
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认凭据将是与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行该任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
- A Security Accounts Manager account name (sAMAccountName)

此 cmdlet 会在默认的命名上下文或分区中搜索相应的对象。如果提供的标识符是一个“区分名称”（distinguished name），则会根据该名称来确定需要搜索的分区。如果找到两个或多个对象，cmdlet 会返回一个表示无法继续执行的错误信息。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为某个计算机对象的实例。

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
指定一个 Active Directory 分区的独特名称（distinguished name）。该唯一名称必须是当前目录服务器上支持的命名上下文之一。此 cmdlet 会在该分区中查找由 *Identity* 参数所定义的对象。

在许多情况下，如果未指定 `Partition` 参数的值，系统会使用一个默认值。确定默认值的规则如下所示。请注意，列出的规则会按顺序依次进行评估；一旦确定了默认值，后续的规则将不再被执行。

在 Active Directory 域服务环境中，以下情况下会为“分区（Partition）”设置默认值：

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
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下是指定 Active Directory 域服务实例的几种方式之一：

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management_ADComputer
一个计算机对象通过*Identity*参数被接收。

## 输出

### 无

## 备注
* This cmdlet does not work with AD LDS.
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.
* By default, this cmdlet has the *Confirm* parameter set, which prompts you to confirm before a removal of the specified object type can occur. To bypass prompting for confirmation before removal, you can specify `-Confirm:$False` when using this cmdlet.

## 相关链接

[Add-ADComputerServiceAccount](./Add-ADComputerServiceAccount.md)

[Get-ADComputer](./Get-ADComputer.md)

[Get-ADComputerServiceAccount](./Get-ADComputerServiceAccount.md)

[New-ADComputer](./New-ADComputer.md)

[Remove-ADComputerServiceAccount](./Remove-ADComputerServiceAccount.md)

[Set-ADComputer](./Set-ADComputer.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

