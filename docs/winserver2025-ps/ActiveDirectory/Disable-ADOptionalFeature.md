---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/disable-adoptionalfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-ADOptionalFeature
---

# 禁用可选的广告功能（Disable-ADOptionalFeature）

## 摘要
禁用 Active Directory 的一个可选功能。

## 语法

```
Disable-ADOptionalFeature [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADOptionalFeature> [-PassThru]
 [-Scope] <ADOptionalFeatureScope> [-Server <String>] [-Target] <ADEntity>
 [<CommonParameters>]
```

## 描述

` Disable-ADOptionalFeature` 命令用于禁用与特定域模式或林模式相关联的 Active Directory 可选功能。

**Identity** 参数用于指定您想要禁用的 Active Directory 可选功能。您可以通过该功能的唯一名称（distinguished name）、功能 GUID 或对象 GUID 来识别它。此外，您还可以将此参数设置为某个可选功能对象变量（例如 `$<localOptionalFeatureObject>`），或者通过管道将该可选功能对象传递给 **Identity** 参数。例如，您可以使用 `Get-ADOptionalFeature` cmdlet 获取一个可选功能对象，然后通过管道将其传递给 `Disable-ADOptionalFeature` cmdlet。

`Scope` 参数指定了该可选功能被禁用的范围。

`Target` 参数用于指定要禁用该可选功能的域或林。您可以通过其完全限定域名（FQDN）、NetBIOS 名称或域命名上下文的区分名称来识别该域或林。

## 示例

#### 示例 1：禁用 NetBIOS 目标的某个功能

```powershell
$params = @{
    Identity = 'Feature 1'
    Scope = 'ForestOrConfigurationSet'
    Target = 'fabrikam'
    Server = 'DC1'
}
Disable-ADOptionalFeature @params
```

此命令将禁用名为“Feature 1”的可选功能，该功能适用于NetBIOS名称为“fabrikam”的森林（即网络环境）。此操作应在拥有域命名主控器（Flexible Single Master Operations, FSMO）角色的域控制器上执行。

#### 示例 2：通过唯一名称禁用某个功能

```powershell
$params = @{
    Identity = 'CN=Feature 1,CN=Optional Features,CN=Directory Service,CN=Windows NT,CN=Services,CN=Configuration,DC=fabrikam,DC=com'
    Scope = ForestOrConfigurationSet
    Target = 'fabrikam.com'
    Server = 'DC1'
}
Disable-ADOptionalFeature @params
```

此命令将禁用名为 `CN=Feature 1,CN=Optional Features,CN=Directory Service,CN=Windows NT,CN=Services,CN=Configuration,DC=fabrikam,DC=com` 的可选功能，该功能适用于名为 `fabrikam.com` 的森林。此操作应在拥有域命名主 FSMO 角色的域控制器上执行。

### 示例 3：通过 GUID 禁用某个功能

```powershell
$params = @{
    Identity = '54ec6e43-75a8-445b-aa7b-346a1e096659'
    Scope = 'Domain'
    Target = 'DC=fabrikam,DC=com'
    Server = 'DC1'
}
Disable-ADOptionalFeature @params
```

此命令将禁用一个可选功能。该功能的 GUID 为 `54ec6e43-75a8-445b-aa7b-346a1e096659`，且适用于域名 `DC=ntdev,DC=fabrikam,DC=com`。此操作需要在持有域命名主 FSMO 角色的域控制器上执行。

### 示例 4：禁用 AD LDS 实例的某个功能

```powershell
$params = @{
    Identity = 'Feature 1'
    Scope = 'ForestOrConfigurationSet'
    Target = 'CN=Configuration,CN={0241853A-6BBF-48AA-8AE0-9C35D0C91B7B}'
    Server = 'server1:50000'
}
Disable-ADOptionalFeature @params
```

此命令将禁用具有 distinguished name `CN=Configuration,CN={0241853A-6BBF-48AA-8AE0-9C35D0C91B7B}` 的 Active Directory Lightweight Directory Services (AD LDS) 实例中的可选功能“Feature 1”。该操作应针对持有域命名主 FSMO 角色的 AD LDS 实例进行。

## 参数

### -AuthType

指定要使用的认证方法。该参数的可接受值包括：

- `Negotiate` or `0`
- `Basic` or `1`

默认的身份验证方法是“Negotiate”。

基本（Basic）认证方法需要使用安全套接字层（SSL）连接。

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

在运行cmdlet之前会提示您进行确认。

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

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01\User01`），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，可以将该 **Credential** 对象设置为相应的参数值。

如果该执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

- FQDN
- Feature GUID (**featureGUID**)
- Object GUID (**objectGUID**)

The cmdlet searches the default naming context or partition to find the object. If two or more
objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to an
optional feature object instance.

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

Returns an object representing the item with which you're working. By default, this cmdlet does not
generate any output.

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

Specifies the scope at which the feature is enabled or disabled. The acceptable values for this
parameter are:

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

Specifies the Active Directory Domain Services instance to connect to, by providing one of the
following values for a corresponding domain name or directory server. The service may be any of the
following: Active Directory Lightweight Domain Services, Active Directory Domain Services or Active
Directory snapshot instance.

Specify the Active Directory Domain Services instance in one of the following ways:

Domain name values:

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
- Distinguished name of the domain naming context

The following example shows how to set this parameter to a domain naming context.

`-Target "DC=corp,DC=Fabrikam,DC=com"`

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

展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft ActiveDirectory.Management.AdOptionalFeature

**Identity** 参数接收一个可选的功能对象。

## 输出

### 无

## 备注

- This cmdlet doesn't work with an Active Directory snapshot.
- This cmdlet doesn't work with a read-only domain controller.

## 相关链接

[Enable-ADOptionalFeature](./Enable-ADOptionalFeature.md)

[Get-ADOptionalFeature](./Get-ADOptionalFeature.md)
