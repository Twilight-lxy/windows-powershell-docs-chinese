---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/enable-adoptionalfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-ADOptionalFeature
---

# 启用 AD 可选功能

## 摘要
启用 Active Directory 的一个可选功能。

## 语法

```
Enable-ADOptionalFeature [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADOptionalFeature> [-PassThru]
 [-Scope] <ADOptionalFeatureScope> [-Server <String>] [-Target] <ADEntity>
 [<CommonParameters>]
```

## 描述

`Enable-ADOptionalFeature` cmdlet 可以启用与特定域模式或林模式关联的 Active Directory 可选功能。那些依赖于特定域模式或林模式的 Active Directory 可选功能，必须在该域模式或林模式设置完成后才可显式启用。

**Identity** 参数用于指定您想要启用的 Active Directory 可选功能。您可以通过该功能的唯一名称（distinguished name）、功能 GUID 或对象 GUID 来识别它。此外，您还可以将该参数设置为某个可选功能对象变量（例如 `$<localOptionalFeatureObject>`），或者通过管道将某个可选功能对象传递给 **Identity** 参数。例如，您可以使用 `Get-ADOptionalFeature` cmdlet 获取一个可选功能对象，然后通过管道将该对象传递给 `Enable-ADOptionalFeature` cmdlet。

`Scope` 参数指定了可选功能启用的范围。

`Target` 参数指定了可选功能启用的域或林（forest）。您可以通过该域或林的完全限定域名（FQDN）、NetBIOS 名称，或者域命名上下文的区分名称来识别它。

## 示例

### 示例 1：为一片森林启用“回收站”功能

```powershell
$params = @{
    Identity = 'Recycle Bin Feature'
    Scope = 'ForestOrConfigurationSet'
    Target = 'fabrikam.com'
    Server = 'dc1'
}
Enable-ADOptionalFeature @params
```

此命令为 `fabrikam.com` 林启用可选的“回收站功能”。该操作必须在与拥有域命名主控（Flexible Single Master Operations, FSMO）角色的域控制器上执行。

### 示例 2：为 AD LDS 实例启用回收站功能

```powershell
$params = @{
    Identity = 'Feature 1'
    Scope = 'ForestOrConfigurationSet'
    Target = 'CN=Configuration,CN={0241853A-6BBF-48AA-8AE0-9C35D0C91B7B}'
    Server = 'lds.fabrikam.com:50000'
}
Enable-ADOptionalFeature @params
```

此命令为 AD LDS 实例 `lds.fabrikam.com` 启用了可选功能“Feature 1”。该操作必须在对拥有域命名主 FSMO 角色的 AD LDS 实例上进行。

## 参数

### -AuthType

指定要使用的认证方法。该参数的可接受值为：

- `Negotiate` or `0`
- `Basic` or `1`

默认的认证方法是`Negotiate`。

对于“基本”（Basic）认证方法来说，需要建立安全套接字层（SSL）连接。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADAuthType
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

在运行cmdlet之前，会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从此类驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01/User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 **Credential** 参数设置为该 **PSCredential** 对象。

如果执行该任务的代理程序没有目录级权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

```yaml
Type: System.Management.Automation.PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity

通过提供以下值之一来指定一个 Active Directory 可选功能对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A FQDN
- A feature GUID (**featureGUID**)
- An object GUID (**objectGUID**)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个无法终止的错误信息。

这个参数也可以通过数据流（pipeline）获取相应的对象；或者你可以将这个参数设置为一个可选的功能对象实例（optional feature object instance）。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADOptionalFeature
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru

返回一个对象，该对象表示您正在操作的项目。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Scope

指定该功能启用或禁用的范围。此参数的可接受值包括：

- `Domain` or `0`
- `Forest` or `1`

```yaml
Type: Microsoft.ActiveDirectory.Management.ADOptionalFeatureScope
Parameter Sets: (All)
Aliases:
Accepted values: Unknown, ForestOrConfigurationSet, Domain

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

指定要连接的 Active Directory 域服务实例，为此提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务、Active Directory 域服务或 Active Directory 快照实例。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for this parameter is determined by one of the following methods in the order that
they are listed:

- By using the **Server** value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain Services Windows
  PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Target

Specifies the domain or forest in which to modify the optional feature. You can identify the target
domain or forest by providing one of the following values:

- FQDN of the forest or domain
- NetBIOS name of the forest or domain

当 **Scope** 被设置为 `Domain` 时，你可以使用以下值：

- Distinguished name of the domain naming context

```yaml
Type: Microsoft.ActiveDirectory.Management.ADEntity
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ActiveDirectory.Management.ADOptionalFeature

**Identity** 参数接收一个可选的功能对象（feature object）。

## 输出

### 无

## 备注

- This cmdlet doesn't work with an Active Directory snapshot.
- This cmdlet doesn't work with a read-only domain controller.
- Recycle Bin Feature: Once the Active Directory Recycle Bin is enabled, all objects deleted before
  the Active Directory Recycle Bin was enabled (tombstone objects) become recycled objects. They are
  no longer visible in the Deleted Objects container and they cannot be recovered using Active
  Directory Recycle Bin. The only way to restore these objects is through an authoritative restore
  from an AD DS backup taken before the Active Directory Recycle Bin was enabled.

## 相关链接

[ Disable-ADOptionalFeature](./Disable-ADOptionalFeature.md)

[Get-ADOptionalFeature](./Get-ADOptionalFeature.md)
