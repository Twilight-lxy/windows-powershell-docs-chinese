---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/copy-gpo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Copy-GPO
---

# 复制组策略对象（Copy-GPO）

## 摘要

复制一个组策略对象（GPO）。

## 语法

### SourcebyGUID（默认值）

```
Copy-GPO -SourceGuid <Guid> -TargetName <String> [-SourceDomain <String>] [-TargetDomain <String>]
 [-SourceDomainController <String>] [-TargetDomainController <String>] [-MigrationTable <String>]
 [-CopyAcl] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SourcebyName

```
Copy-GPO [-SourceName] <String> -TargetName <String> [-SourceDomain <String>]
 [-TargetDomain <String>] [-SourceDomainController <String>] [-TargetDomainController <String>]
 [-MigrationTable <String>] [-CopyAcl] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Copy-GPO` cmdlet 可以创建一个目标组策略对象（GPO），并将源 GPO 的设置复制到新的 GPO 中。该 cmdlet 可用于在同一森林内的不同域之间复制 GPO。在跨域复制时，您可以指定一个迁移表来映射安全主体和路径；同时还可以选择是否将源 GPO 的访问控制列表（ACL）也复制到目标 GPO 中。

如果目标域中已经存在具有指定显示名称的 GPO，则此 cmdlet 不会复制源 GPO。在这种情况下，将会出现错误，GPO 也不会被复制。

## 示例

### 示例 1：复制一个 GPO（组策略对象）

```powershell
Copy-GPO -SourceName "TestGpo1" -TargetName "TestGpo2"
```

```Output
DisplayName      : TestGpo2
DomainName       : contoso.com
Owner            : CONTOSO\Domain
Admins Id        : 37eeb072-cc31-42bb-8c3a-446c2b6ddd3f
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/25/2009 9:12:05 PM
ModificationTime : 2/25/2009 9:12:05 PM
UserVersion      : AD Version: 1, SysVol Version: 1
ComputerVersion  : AD Version: 1, SysVol Version: 1
WmiFilter        :
```

这个命令将名为 `TestGpo1` 的组策略对象（GPO）复制到一个名为 `TestGpo2` 的 GPO 中。这两个 GPO 都存在于运行该会话的用户所在的域中。

### 示例 2：将一个 GPO 从一个域复制到另一个域

```powershell
$params = @{
    SourceName   = 'TestGpo1"'
    SourceDomain = 'test.contoso.com'
    TargetName   = 'TestGpo1'
    TargetDomain = 'sales.contoso.com'
}
Copy-GPO @params
```

此命令将 `TestGpo1` 这个组策略对象（GPO）从 `test.contoso.com` 域复制到 `sales.contoso.com` 域中一个名为 `TestGpo1` 的 GPO 中。

源域名和目标域名之间必须存在信任关系。此外，如果源域名或目标域名（或两者皆是）与运行会话的用户所在的域名不同，则该域名与用户所在域名之间也必须存在信任关系。

### 示例 3：将一个域中的所有 GPO 复制到另一个域

```powershell
Get-GPO -All -Domain "sales1.contoso.com" | ForEach-Object {
    $params = @{
        'TargetName'     = $_.DisplayName
        'TargetDomain'   = "sales2.contoso.com"
        'CopyACL'        = $true
        'MigrationTable' = 'c:\tables\MigrationTable.migtable'
    }
    $_ | Copy-GPO @params  }
```

此命令将 `sales1.contoso.com` 域中的所有 GPO（组策略对象）复制到 `sales2.contoso.com` 域中。

源域中的所有组策略对象（GPO）都是通过使用 `Get-GPO` cmdlet 并设置 `All` 参数来获取的。`Get-GPO` 的输出结果会被传递给 `ForEach-Object` 命令。在处理每个 GPO 时，其信息会被进一步传递给 `Copy-GPO` 命令，并将相应的显示名称作为 `-TargetName` 参数的值（即 `$_.DisplayName`）。同时设置了 `CopyACL` 参数，用于将每个 GPO 的访问控制列表（ACL）复制到目标域。`MigrationTable` 参数用于指定迁移表，以便将安全主体和 UNC 路径迁移到目标域。`CopyACL` 和 `MigrationTable` 两个参数都是可选的。

如果在目标域中已经存在一个与源GPO具有相同显示名称的GPO，那么当尝试使用此命令复制源GPO时将会出现错误。由于该命令会复制源域中的所有GPO，因此默认GPO（例如“Default Domain Policy” GPO和“Default Domain Controllers Policy” GPO）也会受到影响，导致这些GPO无法被复制。你可以通过在`Copy-GPO`命令中为`ErrorAction`参数指定值`SilentlyContinue`来抑制这些错误消息。有关`ErrorAction`参数的更多信息，请参阅[关于CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

此命令会返回成功复制的目标组策略对象（GPO）。默认情况下，这些目标GPO会被显示在屏幕上；不过你也可以在命令流程的末尾添加其他命令来进一步配置它们。例如，你可以添加 `Set-GPLink` cmdlet，将所有目标GPO链接到某个站点、域或组织单元。

源域名和目标域名之间必须存在信任关系。此外，如果源域名或目标域名（或两者都是）与运行会话的用户所在的域名不同，那么该域名与用户所在域或计算机所在域之间也必须存在信任关系。

## 参数

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

### -CopyAcl

表示该cmdlet会将源GPO的ACL复制到目标GPO中。

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

### -MigrationTable

指定用于该命令的迁移表的位置。必须提供文件的完整路径；例如：`\\Server1\MigrationTables\TestToSalesTable.migtable`。如果提供了迁移表，在跨域复制组策略对象（GPO）时，安全主体和通用命名 convention (UNC) 路径会被映射到目标 GPO 中。如果没有提供迁移表，则目标 GPO 中的安全主体和 UNC 路径不会被修改。

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

### -SourceDomain

指定源GPO所在的域。你必须提供该域的完全限定域名（FQDN）。

如果您不指定 **SourceDomain** 参数，将使用当前会话所在用户的域名。如果该 cmdlet 是从计算机启动或关闭脚本中运行的，则将使用计算机的域名。有关更多信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域与当前会话的用户所使用的域不同（或者对于启动/关闭脚本来说，是与计算机所使用的域不同），那么该域与用户或计算机的域之间必须存在信任关系。

您也可以使用 **SourceDomain** 参数的内置别名 **DomainName** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

### -SourceDomainController

指定此 cmdlet 用于联系源域的域控制器的名称。您可以指定完全 Qualified Domain Name（FQDN）或主机名。

如果您不使用 **SourceDomainController** 参数来指定名称，系统将会联系主域控制器（PDC）模拟器。

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

### -SourceGuid

通过其全局唯一标识符（GUID）来指定源GPO。该GUID可以唯一地标识该GPO。

您也可以通过其内置别名 **Id** 来引用 **SourceGuid** 参数。

```yaml
Type: System.Management.Automation.Guid
Parameter Sets: SourcebyGUID
Aliases: Id

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SourceName

通过显示名称来指定源GPO。

显示名称在该域内不保证是唯一的。如果该域中存在另一个具有相同显示名称的 GPO，将会发生错误。你可以使用 **SourceGuid** 参数来唯一标识一个 GPO。

您也可以使用其内置别名 **DomainName** 来引用 **SourceDomain** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: SourcebyName
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetDomain

指定您希望将GPO复制到的域。必须提供该域的完全限定域名（FQDN）。

如果您没有指定 **TargetDomain** 参数，那么将使用当前会话所运行的用户的域名。如果该 cmdlet 是从计算机启动或关闭脚本中执行的，那么将使用计算机的域名。有关更多信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域名与当前会话所使用的用户的域名不同，则该域名与用户或计算机的域名之间必须存在信任关系。

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

### -TargetDomainController

指定此cmdlet用于联系目标域的域名控制器的名称。您可以指定FQDN或主机名。

如果您不使用 **TargetDomainController** 参数来指定名称，系统将联系主域控制器（Primary Domain Controller，简称 PDC）的仿真器。

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

### -TargetName

指定目标 GPO 的显示名称。如果目标域中存在另一个具有相同显示名称的 GPO，则会发生错误。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.GroupPolicy.Gpo

该cmdlet接受一个GPO（组策略对象）作为输入。通过管道传递给该cmdlet的GPO对象将用作源GPO。不支持包含来自不同域的GPO的集合。

## 输出

### Microsoft.GroupPolicy.Gpo

此cmdlet会输出指定GPO的副本。

## 备注

* You can use the `Copy-GPO` cmdlet to copy a GPO within a domain or from one domain to another
  within the same forest.

你可以使用 `SourceDomain` 和 `TargetDomain` 参数来明确指定此 cmdlet 的源域名或目标域名。

如果您没有明确指定域名，该cmdlet会使用默认域名。默认域名是指当前会话所运行的安全上下文用于访问网络资源的那个域名。这个域名通常就是启动该会话的用户所属的域名；例如，通过“Program Files”菜单打开Windows PowerShell来启动会话的用户对应的域名，或者在“runas”命令中指定的用户的域名。然而，计算机启动和关闭脚本是在LocalSystem账户的上下文中运行的。LocalSystem账户是一个内置的本地账户，它以计算机账户的身份访问网络资源。因此，当从这个启动或关闭脚本中运行该cmdlet时，默认域名就是计算机所属的域名。

## 相关链接

[Get-GPO](./Get-GPO.md)

[Import-GPO](./Import-GPO.md)

[New-GPO](./New-GPO.md)

[恢复GPO](./Restore-GPO.md)

[Set-GPLink](./Set-GPLink.md)

