---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/get-gpo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-GPO
---

# Get-GPO

## 摘要

可以获取一个GPO或域中的所有GPO。

## 语法

### ByGUID（默认值）

```
Get-GPO [-Guid] <Guid> [[-Domain] <String>] [[-Server] <String>] [-All] [<CommonParameters>]
```

### 按名称查找

```
Get-GPO [-Name] <String> [[-Domain] <String>] [[-Server] <String>] [-All] [<CommonParameters>]
```

### getAll

```
Get-GPO [[-Domain] <String>] [[-Server] <String>] [-All] [<CommonParameters>]
```

## 描述

`Get-GPO` cmdlet 可以获取一个组策略对象（GPO）或域中的所有 GPO。你可以通过 GPO 的显示名称或其全局唯一标识符（GUID）来指定某个特定的 GPO；或者，你也可以使用 `All` 参数来获取域中的所有 GPO。

此 cmdlet 返回一个或多个表示所请求的组策略对象（GPO）的实例。默认情况下，这些 GPO 的属性会显示在屏幕上；不过，您也可以将 `Get-GPO` cmdlet 的输出结果传递给其他组策略相关的 cmdlet。

## 示例

### 示例 1：从域中获取一个 GPO（组策略对象）

```powershell
Get-GPO -Name "Group Policy Test"
```

```Output
DisplayName      : Group Policy Test
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 31a09564-cd4a-4520-98fa-446a2af23b4b
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/26/2009 12:15:42 AM
ModificationTime : 2/26/2009 12:15:42 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :
```

### 示例 2：通过 GUID 获取单个 GPO

这个命令用于获取名为“Group Policy Test”的GPO（组策略对象）。该GPO必须存在于运行此会话的用户所在的域中（对于启动和关闭脚本而言，则是计算机所在的域中）。该命令通过联系主域控制器（Primary Domain Controller，简称PDC）来获取GPO的相关信息。

```powershell
Get-GPO -Guid 31a09564-cd4a-4520-98fa-446a2af23b4b -Domain "sales.contoso.com"
```

```Output
DisplayName      : Group Policy Test
DomainName       : sales.contoso.com
Owner            : SALES\Domain Admins
Id               : 31a09564-cd4a-4520-98fa-446a2af23b4b
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/26/2009 12:15:42 AM
ModificationTime : 2/26/2009 12:15:42 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :
```

此命令用于获取位于 `sales.contoso.com` 域中、ID（GUID）为 `331a09564-cd4a-4520-98fa-446a2af23b4b` 的 GPO。如果运行该命令的用户所在的域（或者对于启动和关闭脚本来说，是计算机所在的域）与 `sales.contoso.com` 不同，则这两个域之间必须存在信任关系。该命令通过联系 `sales.contoso.com` 域中的 PDC 来检索 GPO 的相关信息。

### 示例 3：从某个域中获取所有组策略对象（GPO）

```powershell
Get-GPO -All -Domain "sales.contoso.com"
```

这个命令可以获取 `sales.contoso.com` 域中的所有组策略对象（GPO）。

## 参数

### -All

表示该cmdlet会获取域中的所有GPO（组策略对象）。

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

### -Domain

指定此 cmdlet 的相关域名。您必须提供该域名的完整限定域名（FQDN）。

对于 `Get-GPO` cmdlet 来说，该 cmdlet 所获取的一个或多个 GPO 必须存在于当前域中。

如果您没有指定 **Domain** 参数，那么将使用运行当前会话的用户的域信息。如果该cmdlet是从计算机启动或关闭脚本中运行的，那么将使用计算机的域信息。有关更多详细信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域与当前会话的用户所使用的域不同（或者对于启动/关闭脚本来说，是与计算机相关的域不同），那么该域与用户或计算机的所在域之间必须存在信任关系。

您也可以使用**Domain**参数的内置别名**DomainName**来引用它。有关更多信息，请参阅[关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DomainName

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Guid

通过其全局唯一标识符（GUID）指定要检索的组策略对象（GPO）。该 GUID 可唯一地标识该 GPO。

您也可以通过其内置别名 **Id** 来引用 **Guid** 参数。

```yaml
Type: Guid
Parameter Sets: ByGUID
Aliases: Id

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

指定要根据其显示名称检索的组策略对象（GPO）。

显示名称在域中并不保证是唯一的。如果该域中存在另一个具有相同显示名称的组策略对象（GPO），则会出现错误。您可以使用 **Guid** 参数来唯一标识一个 GPO。

您也可以通过其内置别名 **DisplayName** 来引用 **Name** 参数。

```yaml
Type: System.String
Parameter Sets: ByName
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Server

指定此cmdlet用于联系以完成操作的域控制器的名称。您可以指定完全限定的域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系主域控制器（Primary Domain Controller，简称 PDC）的模拟器。

您也可以使用其内置别名“DC”来引用**Server**参数。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DC

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。


## 输入

### Microsoft.GroupPolicy.Gpo

你可以将一个GPO（组策略对象）通过管道传递给这个cmdlet，以便获取相关信息。你也可以将多个GPO对象通过管道传递给这个cmdlet来显示这些GPO的详细信息。不过，包含来自不同域的GPO的集合是不被支持的。

## 输出

### Microsoft.GroupPolicy.Gpo

此cmdlet返回一个对象，该对象表示所请求的GPO（组策略对象）。

## 备注

- You can use the **Domain** parameter to explicitly specify the domain for this cmdlet.

如果您没有明确指定域名，该cmdlet会使用默认域名。默认域名是指当前会话运行的安全上下文用于访问网络资源所使用的域名。这个域名通常是运行该会话的用户的域名。例如，通过“程序文件”菜单打开Windows PowerShell来启动会话的用户对应的域名，或者在runas命令中指定的用户对应的域名。然而，计算机启动和关闭脚本是在LocalSystem账户的上下文中运行的。LocalSystem账户是一个内置的本地账户，它以计算机账户的身份访问网络资源。因此，当从这个启动或关闭脚本中运行该cmdlet时，默认域名就是计算机所属的域名。

此 cmdlet 的实例只能使用一个域。如果您将一组 GPO（**Microsoft.GroupPolicy.Gpo**）对象通过管道传递给此 cmdlet，那么集合中第一个 GPO 对象的 **DomainName** 属性将指定该 cmdlet 使用的域。这是因为 **DomainName** 是 **Domain** 参数的内置别名，而 **Domain** 参数可以从管道中通过属性名称获取其值。如果集合中的任何 GPO 不属于该域，则会引发错误（且此错误无法被终止）。如果该域与用户账户所属的域不同（例如在启动或关闭脚本中使用的计算机账户），则这两个域之间必须存在信任关系。

## 相关链接

[备份GPO](./Backup-GPO.md)

[复制GPO](./Copy-GPO.md)

[Import-GPO](./Import-GPO.md)

[New-GPO](./New-GPO.md)

[Remove-GPO](./Remove-GPO.md)

[重命名GPO](./Rename-GPO.md)

[恢复GPO](./Restore-GPO.md)
