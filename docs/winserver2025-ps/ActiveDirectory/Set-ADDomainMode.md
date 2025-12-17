---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 04/11/2024
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-addomainmode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADDomainMode
---

# Set-ADDomainMode

## 摘要
用于设置 Active Directory 域的域模式。

## 语法

```
Set-ADDomainMode [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-DomainMode] <ADDomainMode> [-Identity] <ADDomain> [-PassThru] [-Server <String>]
 [<CommonParameters>]
```

## 描述

`Set-ADDomainMode` cmdlet 用于设置域的域模式。您可以通过设置 **DomainMode** 参数来指定域模式。

**Identity** 参数用于指定要修改的 Active Directory 域。您可以通过该域的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier, SID）、DNS 域名或 NetBIOS 名称来识别该域。您还可以将 **Identity** 参数设置为某个域对象变量（例如 `$<localADDomainObject>`），或者通过管道将该域对象传递给 **Identity** 参数。例如，您可以使用 `Get-ADDomain` cmdlet 获取一个域对象，然后通过管道操作符将该对象传递给 `Set-ADDomainMode` cmdlet。

`Set-ADDomainMode` cmdlet 在执行时会始终提示用户是否需要授权（即是否允许操作），除非你明确指定了 `Confirm:$False`。

## 示例

### 示例 1：将指定用户的域模式设置为 Windows2003Domain

```powershell
Set-ADDomainMode -Identity user01.com -DomainMode Windows2003Domain
```

此命令将 `user01.com` 域的 **DomainMode** 属性设置为 `Windows2003Domain`。

### 示例 2：将当前用户所在域的域模式设置为 Windows2003Domain

```powershell
$PDC = Get-ADDomainController -Discover -Service PrimaryDC
Set-ADDomainMode -Identity $PDC.Domain -Server $PDC.HostName[0] -DomainMode Windows2003Domain
```

这个示例将当前登录用户的域的 **DomainMode** 设置为 Windows2003Domain。设置操作的目标是主域控制器（PrimaryDC FSMO），以便应用该更新。

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

### -Credential

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果是从这样的驱动器中运行 cmdlet，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01/User01`），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将这个 **Credential** 对象设置到相应的参数中。

如果执行该任务的代理组件没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

### -DomainMode

指定在创建新的森林时第一个域的域名功能级别。此参数支持的值可以是有效的整数，也可以是相应的枚举字符串值。例如，要将域模式级别设置为 Windows Server 2008 R2，您可以指定值 **4** 或 **Windows2008R2Domain**。

以下是当前支持的值：

- Windows Server 2000: **0** or **Windows2000Domain**
- Windows Server 2003 Interim Domain: **1** or **Windows2003InterimDomain**
- Windows Server 2003: **2** or **Windows2003Domain**
- Windows Server 2008: **3** or **Windows2008Domain**
- Windows Server 2008 R2: **4** or **Windows2008R2Domain**
- Windows Server 2012: **5** or **Windows2012Domain**
- Windows Server 2012 R2: **6** or **Windows2012R2Domain**
- Windows Server 2016: **7** or **WinThreshold**
- Windows Server 2025: **10** or **Windows2025Domain**

域的功能级别不能低于森林的功能级别，但可以高于森林的功能级别。功能级别是可以提升的，也可以降低的，前提是不要使用任何依赖于该功能级别的组件或功能（例如 Active Directory 回收站）。默认情况下，功能级别会由系统自动计算并设置。

```yaml
Type: ADDomainMode
Parameter Sets: (All)
Aliases:
Accepted values: Windows2000Domain, Windows2003InterimDomain, Windows2003Domain, Windows2008Domain, Windows2008R2Domain, Windows2012Domain, Windows2012R2Domain, Windows2016Domain, Windows2025Domain, UnknownDomain

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity

通过提供以下属性值之一来指定一个 Active Directory 域对象。括号中的标识符是该属性的轻型目录访问协议（LDAP）显示名称。所有值都适用于表示该域的 domainDNS 对象。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A DNS domain name
- A NetBIOS domain name

此cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误信息。

这个参数也可以通过管道获取该对象，或者你可以将该参数设置为某个域对象（domain object）的实例。

```yaml
Type: ADDomain
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
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

### -Server

指定要连接的 Active Directory 域服务实例，为此需要提供相应的域名或目录服务器的相关值。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services），或者 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下是指定 Active Directory 域服务实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

- By using the **Server** value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain Services Windows
  PowerShell provider drive, when the cmdlet runs in that drive
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

### -Confirm

在运行该cmdlet之前，会提示您确认是否要继续执行。

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

### -WhatIf

展示了如果该cmdlet被运行会发生什么情况。但实际上该cmdlet并没有被运行。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### Microsoft ActiveDirectory.Management.AddDomain

领域对象是通过 **Identity** 参数接收到的。

## 输出

没有相关设置，或者使用了 `Microsoft.ActiveDirectory.Management ADDomain` 类。

当指定 `PassThru` 参数时，此 cmdlet 会返回修改后的域对象。默认情况下，该 cmdlet 不生成任何输出。

## 备注

- This cmdlet does not work with Active Directory Lightweight Directory Services (AD LDS).
- This cmdlet does not work with an Active Directory snapshot.
- This cmdlet does not work with a read-only domain controller.
- This cmdlet does not work when connected to Global Catalog port.

## 相关链接

[Get-ADDomain](Get-ADDomain.md)
