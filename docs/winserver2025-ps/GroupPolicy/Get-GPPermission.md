---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/get-gppermission?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-GPPermission
---

# Get-GPPermission

## 摘要

获取指定GPO上一个或多个安全主体（security principal）的权限级别。

## 语法

### SourcebyGUID（默认值）

```
Get-GPPermission -Guid <Guid> [-TargetName <String>] [-TargetType <PermissionTrusteeType>]
 [-DomainName <String>] [-Server <String>] [-All] [<CommonParameters>]
```

### SourcebyName

```
Get-GPPermission [-Name] <String> [-TargetName <String>] [-TargetType <PermissionTrusteeType>]
 [-DomainName <String>] [-Server <String>] [-All] [<CommonParameters>]
```

## 描述

`Get-GPPermission` cmdlet 用于获取指定组策略对象（GPO）上一个或多个安全主体的权限级别。您可以使用 `TargetName` 和 `TargetType` 参数来指定要获取权限级别的用户、安全组或计算机；也可以使用 `All` 参数来获取所有安全主体（包括用户、安全组和计算机）的权限级别。此功能仅适用于那些对 GPO 拥有相应权限的用户、安全组或计算机。您可以按照 GPO 的显示名称或其 GUID 来指定目标对象。

## 示例

### 示例 1：获取指定 GPO 中组的权限级别

```powershell
Get-GPPermission -Name "TestGpo" -TargetName "Domain Users" -TargetType Group
```

```Output
Trustee         : Domain Users
TrusteeType     : Group
PermissionLevel : GpoRead
Inherited       : False
```

此命令用于获取名为TestGpo的GPO中“Domain Users”组的权限级别。

### 示例 2：获取指定 GPO 中组的权限级别（该 GPO 使用指定的 GUID）

```powershell
$params = @{
    Domain     = 'sales.contoso.com'
    Server     = 'DC1'
    GUID       = 'fa4a9473-6e2a-4b87-ab78-175e68d97bde'
    TargetName = 'Domain Admins'
    TargetType = 'Group'
}
Get-GPPermission @params
```

此命令用于获取 `Sales.Contoso.com` 域中具有 GUID `fa4a9473-6e2a-4b78-175e68d97bde` 的 GPO（组策略对象）上 “Domain Admins” 组的权限级别。操作完成后会与 `DC1.sales.contoso.com` 域控制器进行通信。

如果运行会话的用户所在域（或者对于启动和关闭脚本来说，是计算机所在的域）与 `sales.contoso.com` 域不同，那么这两个域之间必须存在信任关系，否则命令将失败。

### 示例 3：获取指定 GPO 中所有安全主体（security principals）的权限级别

```powershell
Get-GPPermission -Name "TestGPO" -All
```

```Output
Trustee     : Authenticated Users
TrusteeType : WellKnownGroup
Permission  : GpoApply
Inherited   : False

Trustee     : Domain Admins
TrusteeType : Group
Permission  : GpoEditDeleteModifySecurity
Inherited   : False

Trustee     : Enterprise Admins
TrusteeType : Group
Permission  : GpoEditDeleteModifySecurity
Inherited   : False

Trustee     : ENTERPRISE DOMAIN CONTROLLERS
TrusteeType : WellKnownGroup
Permission  : GpoRead
Inherited   : False

Trustee     : SYSTEM
TrusteeType : WellKnownGroup
Permission  : GpoEditDeleteModifySecurity
Inherited   : False
```

这个命令会获取每个对名为 `TestGPO` 的组策略对象 (Group Policy Object, GPO) 具有权限的安全主体的权限级别。

### 示例 4：获取每个 GPO 的显示名称以及其对应的特定权限设置

```powershell
Get-GPO -All | ForEach-Object {
    if ( $_ |
            $params = @{
                TargetName  = 'contoso\Domain Admins'
                TargetType  = 'Group'
                ErrorAction = 'SilentlyContinue'
            }
            Get-GPPermission @params) {
            $_.DisplayName
        }
    }
```

```Output
Default Domain Policy
TestGPO-1
TestGPO-2 Default Domain Controllers Policy
Internet Security
TestGPO
```

此命令会列出每个GPO（在域中）的显示名称，以及指定的安全主体在这些GPO上拥有的权限。

首先，使用 `Get-GPO` 命令来检索域中的所有组策略对象（`Get-GPO -All`）。然后，这些组策略对象的集合被传递给 `Foreach-Object` 命令。在处理每个组策略对象时，它会被进一步传递给 `Get-GPPermissions` 命令。如果 `Get-GPPermissions` 命令返回了某个权限级别信息，那么该组策略对象的 `DisplayName` 属性就会被显示出来。

**ErrorAction** 参数被设置为 `SilentlyContinue`。这是因为如果指定的安全主体没有对该 GPO 的权限，就会发生一个无法终止的错误。将 **ErrorAction** 设置为 `SilentlyContinue` 可以防止在那些安全主体没有权限的 GPO 上显示错误消息。有关 **ErrorAction** 参数的更多信息，请参阅 [关于 CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 参数

### -All

这表示该cmdlet会获取每个对GPO具有权限的用户、组或计算机的权限级别。

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

### -DomainName

指定此 cmdlet 所使用的域。必须提供该域的完全限定域名（FQDN）。所指定的 GPO 必须存在于该域中。

如果您没有指定 `Domain` 参数，系统将使用当前会话所运行用户的域信息。如果该 cmdlet 是从计算机启动或关闭脚本中运行的，那么将使用计算机的域信息。有关更多详细信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域名与当前会话正在运行的用户的域名不同（或者对于启动/关闭脚本来说，是与计算机所在的域不同），那么该域名与用户或计算机所在域之间必须存在信任关系。

您也可以使用该参数的内置别名“domain”来引用它。有关更多信息，请参阅[关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Domain

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Guid

通过其全局唯一标识符（GUID）指定用于检索权限级别的组策略对象（GPO）。该 `GUID` 可唯一地标识该 GPO。

您也可以使用 **Guid** 参数的内置别名 **Id** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: Guid
Parameter Sets: SourcebyGUID
Aliases: ID

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

指定通过其显示名称来检索权限级别的组策略对象（GPO）。

显示名称在域内不保证是唯一的。如果域中存在另一个具有相同显示名称的 GPO，将会发生错误。您可以使用 **Guid** 参数来唯一标识一个 GPO。

你也可以通过其内置的别名 **DisplayName** 来引用 **Name** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

### -Server

指定此 cmdlet 用于联系的域控制器的名称，以便完成操作。您可以指定完全合格的域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系 PDC （Primary Domain Controller，主域控制器）模拟器。

您也可以使用**Server**参数的内置别名**DC**来引用它。有关更多信息，请参阅[关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

指定要获取权限级别的安全主体的名称。您可以指定一个用户、一个安全组或一台计算机。您可以使用该安全主体的完全限定域名（例如 domain\account），也可以仅使用其名称。

例如，在 `contoso.com` 域名中，要指定如下内容：

- The username, use `contoso\someuser` or `someuser`.
- The Domain Admins security group, use `contoso\Domain Admins` or `Domain Admins`.
- The computer name, use `contoso\computer-01` or `computer-01`.

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

### -TargetType

需要获取权限级别的安全主体类型。该参数的可接受值包括：

- Computer
- User
- Group

```yaml
Type: PermissionTrusteeType
Parameter Sets: (All)
Aliases:
Accepted values: Computer, User, Group

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable,
-InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose,
-WarningAction, and -WarningVariable. For more information, see
[about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### Microsoft.GroupPolicy.Gpo

你可以将一个组策略对象（GPO）传递给这个 cmdlet 以获取其权限级别。不支持包含来自不同域的 GPO 的集合。

## 输出

### Microsoft.GroupPolicy.GPPermissionCollection

### Microsoft.GroupPolicy.GPPermission

此cmdlet返回一个对象，该对象表示指定安全主体（用户、组或计算机）在GPO上的权限。

## 备注

你可以使用 `DomainName` 参数来明确指定该 cmdlet 所使用的域名。如果你没有明确指定域名，cmdlet 会使用默认域名。默认域名是指当前会话运行的安全上下文用于访问网络资源的那个域名；这个域名通常就是启动该会话的用户所在的域（例如，通过打开 Windows PowerShell 启动会话的用户所属的域，或者在 `runas` 命令中指定的用户所属的域）。不过，计算机启动和关闭脚本是在 `LocalSystem` 账户的上下文中运行的。`LocalSystem` 是一个内置的本地账户，它以计算机账户的身份访问网络资源。因此，当从这个启动或关闭脚本中运行该 cmdlet 时，默认域名就是计算机所连接的那个域。

## 相关链接

[Set-GPPermission](./Set-GPPermission.md)
