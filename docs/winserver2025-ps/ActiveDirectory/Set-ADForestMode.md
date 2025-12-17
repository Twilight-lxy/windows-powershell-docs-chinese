---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 04/11/2024
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adforestmode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADForestMode
---

# 设置 AD 森林模式（Set-ADForestMode）

## 摘要
设置 Active Directory 林的森林模式（forest mode）。

## 语法

```
Set-ADForestMode [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-ForestMode] <ADForestMode> [-Identity] <ADForest> [-PassThru] [-Server <String>]
 [<CommonParameters>]
```

## 描述

`Set-ADForestMode` cmdlet 用于设置 Active Directory 林的森林模式。您可以通过设置 **ForestMode** 参数来指定森林模式。

`Identity` 参数用于指定要修改的 Active Directory 林。您可以通过其完全限定域名（FQDN）、GUID、DNS 主机名或 NetBIOS 名来识别一个林。也可以通过将林对象传递到管道中来指定该林。例如，您可以使用 `Get-ADForest` cmdlet 获取一个林对象，然后将该对象通过管道传递给 `Set-ADForestMode` cmdlet。

`Set-ADForestMode` 默认会提示用户进行确认。

## 示例

#### 示例 1：为某片森林设置“森林模式”

```powershell
Set-ADForestMode -Identity fabrikam.com -ForestMode Windows2003Forest
```

此命令将森林 `fabrikam.com` 中的 **ForestMode** 设置为 `Windows2003Forest`。

### 示例 2：为当前用户设置森林模式

```powershell
$params = @{
    Identity = (Get-ADForest)
    Server = $params.Identity.SchemaMaster
    ForestMode = 'Windows2008R2Forest'
}
Set-ADForestMode @params
```

这个示例用于设置当前用户的森林（forest）模式。设置操作针对的是“架构主节点灵活单主操作”（Flexible Single Master Operation, FSMO）角色，以便应用相应的更新。

## 参数

### -AuthType

指定要使用的认证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”。

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

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果是从这样的驱动器中运行 cmdlet，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01/User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

您也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，可以将这个 **Credential** 对象设置为相应的参数。

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

### -ForestMode

用于指定 Active Directory 林的林模式（forest mode）。该参数的可接受值为：

- Windows2000Forest or 0
- Windows2003InterimForest or 1
- Windows2003Forest or 2
- Windows2008Forest or 3
- Windows2008R2Forest or 4
- Windows2012Forest or 5
- Windows2012R2Forest or 6
- Windows2016Forest or 7
- Windows2025Forest or 10

这些数值是按照功能从弱到强的顺序排列的。

```yaml
Type: ADForestMode
Parameter Sets: (All)
Aliases:
Accepted values: Windows2000Forest, Windows2003InterimForest, Windows2003Forest, Windows2008Forest, Windows2008R2Forest, Windows2012Forest, Windows2012R2Forest, Windows2016Forest, Windows2025Forest, UnknownForest

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity

通过提供以下属性值之一来指定一个 Active Directory 林对象。括号中的标识符是该属性的轻型目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A fully qualified domain name
- A GUID (objectGUID)
- A DNS host name
- A NetBIOS name

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止（即持续出现的）错误信息。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为某个 Forest 对象的实例。

```yaml
Type: ADForest
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru

返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

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

指定要连接的 Active Directory 域服务（AD DS）实例，为此需要提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型中的任意一种：

- Active Directory Lightweight Directory Services (AD LDS)
- AD DS
- Active Directory snapshot instance.

Specify the AD DS instance in one of the following ways:

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

- By using the **Server** value from objects passed through the pipeline
- By using the server information associated with the AD DS Windows PowerShell provider drive, when
  the cmdlet runs in that drive
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

在运行该 cmdlet 之前会提示您确认是否要执行该操作。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无或使用 MicrosoftActiveDirectory.Management.ADForest

你可以将一个森林对象（forest object）传递给 **Identity** 参数。

## 输出

### 无或使用 MicrosoftActiveDirectory.Management.ADForest

当指定 **PassThru** 参数时，此 cmdlet 会返回修改后的森林对象（forest object）。默认情况下，该 cmdlet 不会生成任何输出。

## 备注

- This cmdlet does not work with AD LDS.
- This cmdlet does not work with an Active Directory snapshot.
- This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADForest](Get-ADForest.md)
