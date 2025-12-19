---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/rename-gpo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Rename-GPO
---

# 重命名GPO

## 摘要

为组策略对象（GPO）分配一个新的显示名称。

## 语法

### RenameByGUID（默认值）

```
Rename-GPO -Guid <Guid> -TargetName <String> [-Domain <String>] [-Server <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### RenameByName

```
Rename-GPO [-Name] <String> -TargetName <String> [-Domain <String>] [-Server <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Rename-GPO` cmdlet 为组策略对象（GPO）分配一个不同的、非空的显示名称。此 cmdlet 对 GPO 的 GUID 没有任何影响。

## 示例

### 示例 1：重命名一个组策略对象（GPO）

```powershell
Rename-GPO -Name "SampleGPO" -TargetName "SecurityGPO"
```

```Output
DisplayName      : securityGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 2c08f9b5-32c3-43fa-af8f-f1939b1ac8a0
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 3/6/2009 4:20:25 PM
ModificationTime : 3/6/2009 4:20:24 PM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :
```

这个命令将名为“SampleGPO”的GPO重命名为“SecurityGPO”。

## 参数

### -Confirm

在运行 cmdlet 之前会提示您进行确认。

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

指定此 cmdlet 所使用的域名。必须提供该域名的完全限定域名（FQDN）。

对于 `Rename-GPO` cmdlet 来说，这里指的是您想要重命名的 GPO 所所属的域。

如果您没有指定 **Domain** 参数，将使用当前会话所运行的用户的域信息。如果该 cmdlet 是从计算机启动或关闭脚本中执行的，则会使用计算机的域信息。有关更多详细信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域与当前会话所使用的用户的域不同（或者对于启动/关闭脚本来说，是与计算机相关的域不同），那么该域与用户或计算机的域之间必须存在信任关系。

您也可以使用其内置别名 **DomainName** 来引用 **Domain** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

### -Guid

通过全局唯一标识符（GUID）指定要重命名的组策略对象（GPO）。该 GUID 可唯一地识别该 GPO。

您也可以通过其内置别名**Id**来引用**Guid**参数。

```yaml
Type: Guid
Parameter Sets: RenameByGUID
Aliases: Id

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

指定要重命名的GPO，使用其当前的显示名称进行操作。

显示名称在该域内并不保证是唯一的。如果该域中存在另一个具有相同显示名称的组策略对象（GPO），将会发生错误。您可以使用 **Guid** 参数来唯一地标识一个 GPO。

您也可以通过其内置别名 **DisplayName** 来引用 Name 参数。

```yaml
Type: System.String
Parameter Sets: RenameByName
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Server

指定此 cmdlet 用于联系以完成操作的域控制器的名称。您可以指定完全合格的域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系主域控制器（Primary Domain Controller，简称 PDC）的模拟器。

您也可以通过其内置别名“DC”来引用**Server**参数。

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

### -TargetName

指定新的组策略对象（GPO）的显示名称。由于显示名称可能不具有唯一性，如果域中存在另一个具有相同显示名称的GPO，则会返回错误信息。

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

展示了如果运行该cmdlet会发生什么情况。不过实际上并没有运行这个cmdlet。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft(GroupPolicy.Gpo)

你可以将一个 **GPO（组策略对象）** 传递给另一个 GPO 以进行重命名。但是，包含来自不同域的 GPO 的集合是不被支持的。

## 输出

### Microsoft(GroupPolicy.Gpo)

此cmdlet会返回具有新显示名称的GPO（组策略对象）。

## 备注

* You can use the **Domain** parameter to explicitly specify the domain for this cmdlet.

如果您没有明确指定域名，该 cmdlet 会使用默认域名。默认域名是指当前会话运行的安全上下文用于访问网络资源时所使用的域名。这个域名通常是与运行该会话的用户相关的域名；例如，通过“程序文件”菜单启动 Windows PowerShell 的用户的域名，或者在 `runas` 命令中指定的用户的域名。然而，计算机启动和关闭脚本是在 `LocalSystem` 账户的上下文中运行的。`LocalSystem` 账户是一个内置的本地账户，它以计算机账户的身份访问网络资源。因此，当从这个启动或关闭脚本中运行该 cmdlet 时，默认域名就是计算机所隶属于的域名。

## 相关链接

[备份GPO](./Backup-GPO.md)

[复制GPO](./Copy-GPO.md)

[Get-GPO](./Get-GPO.md)

[导入GPO](./Import-GPO.md)

[New-GPO](./New-GPO.md)

[Remove-GPO](./Remove-GPO.md)

[恢复GPO](./Restore-GPO.md)

