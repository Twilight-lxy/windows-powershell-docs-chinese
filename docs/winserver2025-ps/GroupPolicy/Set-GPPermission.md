---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/set-gppermission?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-GPPermission
---

# Set-GPPermission

## 摘要

为某个安全主体授予针对一个GPO或域中所有GPO的一定权限级别。

## 语法

### PermissionOne（GUID）（默认值）

```
Set-GPPermission -Guid <Guid> -PermissionLevel <GPPermissionType> -TargetName <String>
 -TargetType <PermissionTrusteeType> [-DomainName <String>] [-Server <String>] [-Replace] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### PermissionOne（名称）

```
Set-GPPermission [-Name] <String> -PermissionLevel <GPPermissionType> -TargetName <String>
 -TargetType <PermissionTrusteeType> [-DomainName <String>] [-Server <String>] [-Replace] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 权限所有（Permission All）

```
Set-GPPermission -PermissionLevel <GPPermissionType> -TargetName <String>
 -TargetType <PermissionTrusteeType> [-DomainName <String>] [-Server <String>] [-All] [-Replace]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Set-GPPermission` cmdlet 为某个安全主体（用户、安全组或计算机）授予针对一个 Group Policy Object (GPO) 或域中所有 GPO 的权限级别。你可以使用 `TargetName` 和 `TargetType` 参数来指定要设置权限级别的用户、安全组或计算机。你可以使用 `Name` 或 `Guid` 参数为该安全主体在单个 GPO 上设置权限级别，也可以使用 `All` 参数为该安全主体在域中的所有 GPO 上设置权限级别。

默认情况下，如果安全主体的权限级别已经高于指定的权限级别，则更改不会被应用。您可以指定 `Replace` 参数，在设置新的权限级别之前先从组策略对象（GPO）中删除现有的权限级别。这样可以确保现有的权限级别被新权限级别所替换。

## 示例

#### 示例 1：为属于 GPO 的安全组设置权限级别

```powershell
Set-GPPermission -Name TestGpo -TargetName "Domain Users" -TargetType Group -PermissionLevel GpoRead
```

此命令将“Domain Users”安全组的权限级别设置为“GpoRead”，适用于名为“TestGpo”的组策略对象（GPO）。由于没有指定“Replace”参数，如果该组当前的权限级别已经高于“GpoRead”（例如为“GpoEdit”），则不会进行任何更改。

#### 示例 2：为属于所有组策略对象（GPO）的安全组设置权限级别

```powershell
$params = @{
    All             = $true
    TargetName      = "Marketing Admins"
    TargetType      = 'Group'
    PermissionLevel = 'GpoEdit'
    Replace         = $true
}
Set-GPPermission @params
```

此命令将“Marketing Admins”安全组的权限级别设置为“GpoEdit”，适用于域中的所有组策略对象（GPO）。这包括那些未与任何站点、域或组织单位（OU）关联的GPO。由于指定了“Replace”参数，因此新的权限级别会覆盖该组原有的权限设置。

### 示例 3：更改安全组的权限级别，该更改将应用于该组具有权限的所有组策略对象（GPO）

```powershell
Get-GPO -All |
    ForEach-Object {
        $getParams = @{
            TargetName  = "Marketing Admins"
            TargetType  = 'Group'
            ErrorAction = 'SilentlyContinue'
        }
        if ( $_ | Get-GPPermission @getParams) {
            $setParams = @{
                Replace         = $true
                PermissionLevel = 'GpoApply'
                TargetName      = "Marketing Admins"
                TargetType      = 'Group'
            }
            $_ | Set-GPPermission @setParams
        }
    }
```

```Output
DisplayName      : TestGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 24f217d4-1403-4d43-9247-d17eeedb22f0
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 3/1/2009 10:51:34 PM
ModificationTime : 3/2/2009 12:53:40 AM
UserVersion      : AD Version: 8, SysVol Version: 8
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :


DisplayName      : TestGPO-1
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : fe2f7402-101b-4b3c-87e4-85d3f47735cb
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 3/1/2009 7:22:03 PM
ModificationTime : 3/2/2009 12:53:54 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :
```

此命令会将“Marketing Admins”安全组的当前权限级别更改为适用于该组具有权限的所有GPO的权限设置（即使用GPOApply来应用新的权限规则）。命令会返回所有设置了新权限级别的GPO。

该 cmdlet 用于获取域中的所有 GPO（组策略对象）。随后，这些 GPO 被传递给 `ForEach-Object` 命令进行处理。对于每个被处理的 GPO，系统会进一步将其传递给 `Get-GPPermission` 命令以检查其权限设置。如果检测到“Marketing Admins”组的权限级别需要更新，那么该 GPO 会被传递给 `Set-GPPermission` 命令来修改其权限设置。同时指定了 `Replace` 参数，以确保原有的权限级别会被新设置的权限覆盖。

对于 `Get-GPPermissions` 命令，`ErrorAction` 参数被设置为 `SilentlyContinue`。这是因为如果指定的安全主体没有对该 GPO 的权限，将会出现一个无法终止的错误。将 `ErrorAction` 设置为 `SilentlyContinue` 可以避免在那些安全主体没有权限的 GPO 上显示错误消息。有关 `ErrorAction` 参数的更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 参数

### -All

该设置表示权限级别是为指定安全主体在域内的所有组策略对象（GPO）设置的。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: PermissionAll
Aliases:

Required: True
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

### -DomainName
指定此 cmdlet 所使用的域名。你必须提供该域名的完全限定域名（FQDN）。

对于 `Set-GPPermission` cmdlet 来说，需要获取权限级别的 GPO 必须存在于该域中。

如果您没有指定 **DomainName** 参数，那么将使用当前会话所在用户的域名。如果该 cmdlet 是通过计算机启动或关闭脚本来执行的，那么将使用计算机的域名。有关更多信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域名与当前会话所使用的用户的域名不同（或者对于启动/关闭脚本来说，是与计算机相关联的域名不同），那么该域名与用户或计算机的域名之间必须存在信任关系。

您也可以使用 **DomainName** 参数的内置别名 “domain” 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Domain

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Guid

通过全局唯一标识符（GUID）指定要设置权限级别的组策略对象（GPO）。该 GUID 可唯一地识别该 GPO。

您也可以通过其内置别名“Id”来引用**Guid**参数。

```yaml
Type: Guid
Parameter Sets: PermissionOne(GUID)
Aliases: ID

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

通过显示名称来指定要设置权限级别的GPO（组策略对象）。

显示名称在域内并不保证是唯一的。如果域中存在另一个具有相同显示名称的组策略对象（GPO），将会出现错误。您可以使用 **Guid** 参数来唯一标识一个 GPO。

您也可以通过其内置别名 **DisplayName** 来引用 Name 参数。

```yaml
Type: System.String
Parameter Sets: PermissionOne(Name)
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PermissionLevel

指定要为安全主体设置的身份级别（权限等级）。

此参数的可接受值为：

- GpoRead
- GpoApply
- GpoEdit
- GpoEditDeleteModifySecurity
- None

```yaml
Type: GPPermissionType
Parameter Sets: (All)
Aliases:
Accepted values: None, GpoApply, GpoRead, GpoEdit, GpoEditDeleteModifySecurity, GpoCustom, WmiFilterEdit, WmiFilterFullControl, WmiFilterCustom, StarterGpoRead, StarterGpoEdit, StarterGpoFullControl, StarterGpoCustom, SomCreateWmiFilter, SomWmiFilterFullControl, SomCreateGpo, SomCreateStarterGpo, SomLogging, SomPlanning, SomLink

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Replace

Specifies that the existing permission level for the group or user is removed before the new
permission level is set. If a security principal is already granted a permission level that is
higher than the specified permission level and you do not use the *Replace* parameter, no change is
made.

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

### -Server

指定此 cmdlet 用于联系以完成操作的域控制器的名称。您可以指定完全合格的域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系主域控制器（PDC）模拟器。

您也可以使用其内置别名“DC”来引用**Server**参数。

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

需要设置权限级别的安全主体的名称。您可以指定一个用户、一个安全组或一台计算机。您可以使用该安全主体的全限定域名（例如 domain\account），也可以仅使用其名称。

例如，在 `contoso.com` 域名中，要指定如下内容：

- The user SomeUser, use `contoso\SomeUser` or `SomeUser`.

- The Domain Admins security group, use `contoso\Domain Admins` or `Domain Admins`.

- The computer computer-01, use `contoso\computer-01` or `computer-01`.

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

### -TargetType

需要设置权限级别的安全主体的类型。您必须指定“用户”、“组”或“计算机”。

此参数的可接受值为：

- Computer
- User
- Group

```yaml
Type: PermissionTrusteeType
Parameter Sets: (All)
Aliases:
Accepted values: Computer, User, Group

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

Shows what would happen if the cmdlet runs. The cmdlet is not run.

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

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable,
-InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose,
-WarningAction, and -WarningVariable. For more information, see
[about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### Microsoft(GroupPolicy.Gpo)

You can pipe an object that represents a GPO to this cmdlet. Collections that contain GPOs from
different domains are not supported.

## 输出

### Microsoft(GroupPolicy.Gpo)

此cmdlet返回一个对象，该对象代表设置了权限级别的GPO（组策略对象）。

## 备注

* You can use the **DomainName** parameter to explicitly specify the domain for this cmdlet.

如果您没有明确指定域名，那么该 cmdlet 会使用默认域名。默认域名是指当前会话运行的安全上下文用于访问网络资源所使用的域名。这个域名通常就是运行该会话的用户的域名。例如，从“Program Files”菜单中打开 Windows PowerShell 启动会话的用户对应的域名，或者在 `runas` 命令中指定的用户对应的域名。然而，计算机启动和关闭脚本是在 `LocalSystem` 账户的上下文中运行的。`LocalSystem` 是一个内置的本地账户，它以计算机账户的身份访问网络资源。因此，当从这个启动或关闭脚本中运行该 cmdlet 时，默认域名就是计算机所属的域名称。

## 相关链接

[Get-GPPermission](./Get-GPPermission.md)

