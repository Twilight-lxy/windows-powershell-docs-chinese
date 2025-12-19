---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/get-gpstartergpo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-GPStarterGPO
---

# Get-GPStarterGPO

## 摘要

获取一个启动组策略对象（Starter GPO），或者获取域中的所有启动组策略对象。

## 语法

### 使用 ByGUID（默认值）

```
Get-GPStarterGPO -Guid <Guid> [-Domain <String>] [-Server <String>] [-All] [<CommonParameters>]
```

### 按名称查找

```
Get-GPStarterGPO [-Name] <String> [-Domain <String>] [-Server <String>] [-All] [<CommonParameters>]
```

### GetAll

```
Get-GPStarterGPO [-Domain <String>] [-Server <String>] [-All] [<CommonParameters>]
```

## 描述

`Get-GPStarterGPO` cmdlet 可以获取一个启动组策略对象（Starter Group Policy Object，简称 GPO），或者获取域中的所有启动 GPO。你可以通过显示名称或 GUID 来指定要获取的特定启动 GPO；也可以使用 `All` 参数来获取域中的所有启动 GPO。

你可以使用这个cmdlet来获取关于StarterGPO的信息，或者可以通过将这个cmdlet的输出通过管道（pipe）传递给`New-GPO` cmdlet来根据指定的Starter GPO创建一个新的GPO。

## 示例

### 示例 1：按名称获取一个起始 GPO（组策略对象）

```powershell
Get-GPStarterGPO -Name "Windows Vista EC User"
```

```Output
DisplayName       : Windows Vista EC User
Id                : 8780588e-ef91-442b-bd5f-2d50de7abf76
Owner             : BUILTIN\Administrators
Created           : 9/10/2008 12:18:46 PM
Modified          : 4/26/2008 3:25:52 PM
UserVersion       :
ComputerVersion   :
StarterGpoVersion : 0
StarterGpoType    : System
Author            : Microsoft


Description : This Starter GPO contains the user Group Policy settings recommended for the
              Enterprise Client (EC) environment described in the Windows Vista security guide.

              For more information about each of these settings, see the
              [Windows Vista Security Guide](http://go.microsoft.com/fwlink/?LinkID=121852).
```

这个命令用于获取名为“Windows Vista EC User”的起始组策略对象（Starter GPO）。

### 示例 2：使用管道运算符按名称获取一个初始 GPO（组策略对象）

```powershell
Get-GPStarterGPO -Name "Windows Vista EC User" |
    New-GPO -Name "TestGPO" -Comment "Create a GPO by using a Starter GPO"
```

```Output
DisplayName       : TestGPO
DomainName        : contoso.com
Owner             : CONTOSO\Domain Admins
GpoId             : f2828b5c-363a-41f6-afb1-5fa111df715f
GpoStatus         : AllSettingsEnabled
Description       : Create a GPO by using a Starter GPO
CreatedTime       : 2/5/2009 6:46:04 PM
LastModified      : 2/5/2009 6:46:04 PM
UserVersion       : AD Version: 1, SysVol Version: 1
ComputerVersion   : AD Version: 1, SysVol Version: 1
WmiFilter         :
```

这个命令会从名为“Windows Vista EC User Starter”的GPO中创建一个新的GPO，名为“TestGPO”。该命令首先使用`Get-SPStarterGPO` cmdlet来获取这个起始GPO，然后将其结果传递给`New-GPO` cmdlet以生成新的GPO。

## 参数

### -All

返回域中的所有Starter GPO（初始组策略对象）。

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

指定此 cmdlet 的域名。您必须提供该域的完全限定域名（FQDN）。

对于 `Get-GPStarterGPO` cmdlet 来说，该起始组策略对象（Starter GPO）必须存在于这个域中。

如果您不指定**Domain**参数，将使用当前会话所运行用户的域信息。如果该cmdlet是从计算机启动或关闭脚本中运行的，则会使用计算机的域信息。有关更多详细信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域名与当前会话的用户所在域名的不同（或者对于启动/关闭脚本来说，是与计算机所在的域名的不同），那么该域名与用户所在域名或计算机所在域名之间必须存在信任关系。

您也可以使用该参数的内置别名 **DomainName** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DomainName

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Guid

指定此 cmdlet 通过其全局唯一标识符（GUID）获取的启动组策略（Starter GPO）。该 GUID 能唯一地标识这个启动组策略。

您也可以使用该参数的内置别名 **Id** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: Guid
Parameter Sets: ByGUID
Aliases: Id

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

指定此cmdlet所使用的Starter GPO（起始组策略对象）的显示名称。

显示名称在域内并不保证是唯一的。如果域中存在另一个具有相同显示名称的起始组策略对象（Starter GPO），则会发生错误。您可以使用 **Guid** 参数来唯一标识一个起始组策略对象。

你也可以使用其内置别名 **DisplayName** 来引用 **Name** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

指定此cmdlet用于联系的域控制器的名称，以便完成操作。您可以指定完全合格的域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系主域控制器（Primary Domain Controller，简称 PDC）的模拟器。

您也可以通过其内置别名“DC”来引用**Server**参数。有关更多信息，请参阅[关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DC

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft GROUP Policy StarterGPO

你可以将一个起始组策略对象（Starter GPO）通过管道传递给这个命令行工具（cmdlet）。

## 输出

### Microsoft GROUP Policy StarterGPO 对象

这个cmdlet返回一个“Starter GPO”对象。

## 备注

* You can use the **Domain** parameter to explicitly specify the domain for this cmdlet.

如果你没有明确指定域名，该 cmdlet 会使用默认域名。默认域名是指当前会话所运行的安全上下文用于访问网络资源的那个域名。这个域名通常是与运行该会话的用户相关的域名——例如，通过打开 Windows PowerShell 启动会话的用户所属的域名，或者在 runas 命令中指定的用户的域名。然而，计算机启动和关闭脚本是在 LocalSystem 账户的上下文中运行的。LocalSystem 是一个内置的本地账户，它以计算机的身份访问网络资源。因此，当从这个启动或关闭脚本中运行该 cmdlet 时，默认域名就是计算机所加入的那个域名。

## 相关链接

[New-GPO](./New-GPO.md)

[New-GPStarterGPO](./New-GPStarterGPO.md)

