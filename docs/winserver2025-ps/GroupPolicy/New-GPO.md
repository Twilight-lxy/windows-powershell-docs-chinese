---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/new-gpo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-GPO
---

# 新GPO（Group Policy Object）

## 摘要

创建一个组策略对象（GPO）。

## 语法

### 新设置（默认值）

```
New-GPO [-Name] <String> [-Comment <String>] [-Domain <String>] [-Server <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### NewStarterGUID

```
New-GPO [-Name] <String> -StarterGpoGuid <Guid> [-Comment <String>] [-Domain <String>]
 [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### NewStarterName

```
New-GPO [-Name] <String> -StarterGpoName <String> [-Comment <String>] [-Domain <String>]
 [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`New-GPO` cmdlet 可用于创建具有指定名称的 GPO（组策略对象）。默认情况下，新创建的 GPO 不会关联到任何站点、域或组织单元（OU）。

你可以使用这个cmdlet来创建一个基于“起始GPO”（Starter GPO）的新GPO。具体方法有两种：一种是指定该起始GPO的GUID或显示名称；另一种是将一个**StarterGpo**对象通过管道传递给该cmdlet。

该cmdlet返回一个**GPO**对象（组策略对象），代表创建的GPO，你可以将其传递给其他组策略cmdlet。

## 示例

### 示例 1：在用户的域中创建一个组策略对象（GPO）

```powershell
New-GPO -Name TestGPO -Comment "This is a test GPO."
```

```Output
DisplayName      : TestGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : b8c1f2c2-fbd3-4a1f-94e1-3e156a65a29a
GpoStatus        : AllSettingsEnabled
Description      : This is a test GPO.
CreationTime     : 3/2/2009 3:37:23 AM
ModificationTime : 3/2/2009 3:37:22 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :
```

这个命令在用户的域中创建一个GPO（组策略对象）。该GPO会带有指定的注释信息进行创建。

### 示例 2：在用户的域中创建一个 GPO，并预先为其设置“Starter GPO”中的配置

```powershell
New-GPO -Name "FromStarterGPO" -StarterGPOName "Windows Vista EC Computer Starter GPO"
```

此命令在用户的域中创建一个名为“FromStarterGPO”的组策略对象（GPO）。该GPO预先设置了与“Starter GPO”相同的配置参数。

#### 示例 3：在用户的域中创建一个 GPO，并将其链接到一个组织单元（OU）

```powershell
New-GPO -Name TestGPO | New-GPLink -Target "ou=Marketing,dc=contoso,dc=com" |
    Set-GPPermissions -PermissionLevel gpoedit -TargetName "Marketing Admins" -TargetType Group
```

```Output
DisplayName      : TestGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : b8c1f2c2-fbd3-4a1f-94e1-3e156a65a29a
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 3/2/2009 3:37:23 AM
ModificationTime : 3/2/2009 3:37:22 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :
```

此命令创建一个名为 `TestGPO` 的组策略对象（Group Policy Object，简称 GPO），将其链接到 `contoso.com` 域中的 `Marketing` 组织单位（Organizational Unit，简称 OU），并授予 `Marketing Admins` 安全组编辑该 GPO 的权限。

该命令会返回一个 GPO（组策略对象），因此您可以通过将输出结果传递给其他 cmdlet 来继续配置这个新的 GPO。例如，您可以将输出结果传递给 `Set-GPPrefRegistryValue` 或 `Set-GPRegistryValue`，从而设置注册表偏好项或基于注册表的策略设置。

## 参数

### -Comment

包含一条关于新 GPO 的注释。该注释字符串必须用双引号或单引号括起来，且长度不得超过 2,047 个字符。

请使用注释来记录该组策略对象（GPO）及其在您环境中的实施情况。另外，如果您在注释中插入关键词，就可以利用关键词过滤器来查找包含这些关键词的GPO。

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

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

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

### -Domain

指定此cmdlet所使用的域名。你必须提供该域名的完全合格域名（FQDN）。

对于 `New-GPO` cmdlet：

- The new GPO is created in this domain.

- If a Starter GPO is specified, it must exist in this domain.

如果您没有指定 **Domain** 参数，那么将使用当前会话所运行用户的域信息。如果该 cmdlet 是从计算机启动或关闭脚本中运行的，则会使用计算机的域信息。有关更多详细信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域与当前会话的用户所在的域不同（或者对于启动或关闭脚本来说，与运行该脚本的计算机所在的域不同），那么该域与用户所在域或计算机所在域之间必须存在信任关系。

您也可以使用该 **域名** 的内置别名 **DomainName** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DomainName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

为新GPO指定一个显示名称。

如果域中存在另一个具有相同显示名称的 GPO，则会发生错误。

您也可以通过其内置别名 **DisplayName** 来引用 **Name** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

指定此cmdlet用于联系的域控制器的名称，以便完成操作。您可以指定完全 Qualified Domain Name（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将联系主域控制器（PDC）模拟器。

您也可以使用该参数的内置别名“DC”来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

### -StarterGpoGuid

通过其全局唯一标识符（GUID）来指定一个“启动GPO”（Starter GPO）。该GUID能够唯一地识别这个“启动GPO”。如果指定了某个“启动GPO”，那么系统就会根据该GPO的设置创建相应的组策略对象（GPO）。

您也可以通过其内置别名 **Id** 来引用 **StarterGpoGuid** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: Guid
Parameter Sets: NewStarterGUID
Aliases: Id

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StarterGpoName

通过显示名称来指定一个起始组策略对象（Starter GPO）。该名称最多可以包含255个字符。如果名称中包含空格，请使用双引号或单引号将其括起来。如果指定了一个起始组策略对象，系统将创建该对象并应用其设置。

显示名称在域内并不保证是唯一的。如果该域中存在另一个具有相同显示名称的“启动GPO”（Starter GPO），将会出现错误。您可以使用 **StarterGpoGuid** 参数来唯一标识一个“启动GPO”。

您也可以通过其内置别名 **DisplayName** 来引用 **Name** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: NewStarterName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft(GroupPolicy.StarterGpo)

你可以将一个具有预定义设置的起始GPO（Starter GPO）通过管道传递给这个cmdlet。

## 输出

### Microsoft.GroupPolicy.Gpo

此cmdlet会返回创建的GPO（组策略对象）。

## 备注

* Only domain administrators, enterprise administrators, and members of the Group Policy creator
  owners group can create GPOs. These users must run Windows PowerShell in an elevated state.

你可以使用 `Domain` 参数来明确指定此 cmdlet 的域名称。

如果您没有明确指定域名，那么该 cmdlet 会使用默认域名。默认域名是指当前会话运行所使用的安全上下文用于访问网络资源的那个域名。这个域名通常就是启动该会话的用户所属的域名（例如，通过“程序文件”菜单打开 Windows PowerShell 启动会话的用户所在的域，或者在 “RunAs” 命令中指定的用户所在的域）。不过，计算机启动和关闭脚本是在 LocalSystem 计户名的上下文中运行的。LocalSystem 是一个内置的本地账户，它以计算机账户的权限来访问网络资源。因此，当从这个启动或关闭脚本中运行该 cmdlet 时，默认域名就是计算机所连接的那个域名。

## 相关链接

[备份GPO](./Backup-GPO.md)

[复制GPO](./Copy-GPO.md)

[Get-GPO](./Get-GPO.md)

[Import-GPO](./Import-GPO.md)

[Remove-GPO](./Remove-GPO.md)

[重命名GPO](./Rename-GPO.md)

[ Restore-GPO](./Restore-GPO.md)

