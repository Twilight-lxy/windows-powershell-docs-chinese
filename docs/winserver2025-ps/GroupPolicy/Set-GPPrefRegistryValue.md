---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/set-gpprefregistryvalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-GPPrefRegistryValue
---

# Set-GPPrefRegistryValue

## 摘要

在组策略对象（GPO）中，将某个注册表设置项配置到“计算机配置”或“用户配置”类别下。

## 语法

### 使用 ByGUID（默认值）

```
Set-GPPrefRegistryValue -Guid <Guid> -Context <GpoConfiguration> -Key <String>
 [-ValueName <String>] [-Value <PSObject>] [-Type <RegistryValueKind>] -Action <PreferenceAction>
 [-Order <Int32>] [-Domain <String>] [-Server <String>] [-Disable] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 按名称查找

```
Set-GPPrefRegistryValue [-Name] <String> -Context <GpoConfiguration> -Key <String>
 [-ValueName <String>] [-Value <PSObject>] [-Type <RegistryValueKind>] -Action <PreferenceAction>
 [-Order <Int32>] [-Domain <String>] [-Server <String>] [-Disable] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

在组策略对象（GPO）中，将某个注册表设置项配置到“计算机配置”或“用户配置”之下。

您可以配置注册表首选项项，该首选项项适用于注册表键或注册表值中的任意一种：

- For a registry key, specify the **Key** parameter, but do not specify the **ValueName**, **Type**,
  or **Value** parameters.

- For a registry value, specify the **Key** parameter together with the **ValueName**, **Type**, and
  **Value** parameters.

您必须指定 **Context** 参数（用户或计算机），以指示是在“计算机配置”还是“用户配置”中设置注册表偏好项。同时，您还需要指定 **Action** 参数来设定应应用于客户端的具体操作。您可以按照组策略对象的显示名称或 GUID 来进行选择。此外，您还可以通过设置 **Disable** 参数来创建一个被禁用的注册表偏好项。

此cmdlet用于配置新的注册表偏好设置项，不会修改现有的注册表偏好设置项。

此cmdlet可以从管道中接收输入数据：

- You can pipe GPO objects to this cmdlet to set a specified Registry preference item on one or more
  GPOs.

- You can pipe **PreferenceRegistrySetting** objects to this cmdlet to set one or more Registry
  preference items on a specified GPO.

## 示例

#### 示例 1：为组策略对象（GPO）中的某个注册表值配置一个注册表偏好设置项

```powershell
$params = @{
    Name      = 'TestGPO'
    Context   = 'User'
    Key       = 'HKCU\Software\Policies\Microsoft\Windows\Control Panel'
    ValueName = 'ScreenSaveIsSecure'
    Value     = '1'
    Type      = 'String'
    Action    = 'Update'
}
Set-GPPrefRegistryValue @params
```

```Output
DisplayName      : TestGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 35c12ab3-956c-45d5-973b-46b17d225f47
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/24/2009 4:41:03 PM
ModificationTime : 2/25/2009 12:16:28 PM
UserVersion      : AD Version: 1, SysVol Version: 1
ComputerVersion  : AD Version: 34, SysVol Version: 34
WmiFilter        :
```

此命令为名为“TestGPO”的组策略对象（GPO）中的“用户”配置设置了一个注册表偏好项。该偏好项针对的注册表值为 `HKCU\Software\Policies\Microsoft\Windows\Control Panel\ScreenSaveIsSecure`。当该 GPO 应用于客户端时，该注册表值会被更新为字符串类型（REG_SZ），其值为 `1`。

### 示例 2：为组策略对象（GPO）中的注册表值配置一个注册表偏好设置项

```powershell
$params = @{
    Name      = 'TestGPO'
    Context   = 'User'
    Action    = 'Create'
    Key       = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey'
    ValueName = 'ValueOne'
    Value     = 'NewData'
    Type      = 'String'
}
Set-GPPrefRegistryValue @params
```

此命令为名为 `TestGPO` 的组策略对象（GPO）的“用户配置”部分中的注册表值 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey ValueOne` 配置了一个注册表偏好设置项。当该 GPO 应用于客户端时，会创建一个数据类型为 `String`（REG_SZ）、值为 `NewData` 的注册表条目。

### 示例 3：为通过 GUID 指定的 GPO 配置注册表值的相关注册表偏好设置项

```powershell
$params = @{
    Guid    = '35c12ab3-956c-45d5-973b-46b17d225f47'
    Context = 'Computer'
    Action  = 'Create'
    Key     = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey\ExampleKey2'
}
Set-GPPrefRegistryValue @params
```

此命令为具有ID `35c12ab3-956c-45d5-973b-46b17d225f47`的GPO（组策略对象）中的“计算机”配置设置一个注册表偏好项，该偏好项应用于注册表键 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey\ExampleKey2`。当GPO应用到客户端时，相应的注册表键将被创建。

### 示例 4：为组策略对象（GPO）中的某个注册表值创建一个被禁用的注册表偏好设置项

```powershell
$removeGPPrefParams = @{
    Name      = 'TestGPO'
    Context   = 'User'
    Key       = 'HKLM\SOFTWARE\Microsoft\ExampleKey'
    ValueName = 'ValueOne'
}
$setGPPrefParams = @{
    Context   = 'User'
    Action    = 'Create'
    Disable   = $true
    Key       = 'HKLM\SOFTWARE\Microsoft\ExampleKey'
    ValueName = 'ValueOne'
    Value     = 'SomeData'
    Type      = 'String'
}
Remove-GPPrefRegistryValue @removeGPPrefParams |
    Set-GPPrefRegistryValue @setGPPrefParams
```

此命令会在名为“TestGPO”的GPO的用户配置（User Configuration）中，为注册表值`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey ValueOne`创建一个处于“禁用”状态的注册表首选项项。`Remove-GPPrefRegistryValue`命令会删除所有用于配置该值的注册表首选项项。随后，`Remove-GPPrefRegistryValue`命令返回的GPO会被传递给`Set-GPPrefRegistryValue`命令，以设置这个处于“禁用”状态的注册表首选项项。执行完此命令后，用户配置中与该注册表值关联的唯一注册表首选项项就变成了这个被禁用的首选项项了。

如果 `TestGPO` 最初没有为指定的注册表值配置相应的注册表偏好设置项，将会出现一个无法终止的错误。你可以通过向 `Remove-GPPrefRegistryValue` 提供 **ErrorAction** 参数并将其值设置为 `SilentlyContinue` 来抑制错误消息。有关 **ErrorAction** 参数的更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

#### 示例 5：为所有组策略对象（GPO）配置一个用于注册表值的注册表偏好设置项

```powershell
$removeGPPrefParams = @{
    Context     = 'User'
    Key         = 'HKLM\SOFTWARE\Microsoft\ExampleKey'
    ValueName   = 'ValueOne'
    ErrorAction = 'SilentlyContinue'
}
$setGPPrefParams = @{
    Context   = 'User'
    Action    = 'Update'
    Key       = 'HKLM\SOFTWARE\Microsoft\ExampleKey'
    ValueName = 'ValueOne'
    Value     = 'SomeData'
    Type      = 'String'
}
Get-GPO -All | Remove-GPPrefRegistryValue @removeGPPrefParams |
    Set-GPPrefRegistryValue @setGPPrefParams
```

此命令配置了一个注册表偏好设置项，用于更新域中每个组策略对象（GPO）的注册表值 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey ValueOne`。在这些组策略对象中，之前在“用户配置”（User Configuration）部分已经为该值配置了相应的注册表偏好设置项。

该命令使用 **All** 参数来获取域中的所有组策略对象（GPO）。这些 GPO 被传递给 `Remove-GPPrefRegistryValue` cmdlet。如果某个 GPO 中包含为指定注册表键配置的任何注册表首选项项，那么这些首选项项将被删除。只有当 `Remove-GPPrefRegistryValue` 从某个 GPO 中成功删除了注册表首选项项时，才会将该 GPO 输出到后续的处理流程中。最后，这些 GPO 被传递给 `Set-GPPrefRegistryValue` cmdlet，以配置相应的注册表首选项项并更新注册表值。

如果传递给 `Remove-GPPrefRegistryValue` 的 GPO 没有为指定值配置任何注册表偏好设置项，那么将会出现一个无法终止的错误。为了抑制错误消息，**ErrorAction** 参数被设置为 `SilentlyContinue`。

### 示例 6：复制某个 GPO 中的注册表值的全部注册表首选项项

```powershell
$getGPPrefParams = @{
    Name    = 'TestGPO'
    Context = 'User'
    Key     = 'HKLM\Software\Microsoft\ExampleKey'
}
$setGPPrefParams = @{
    Name        = 'TestGPO-1'
    Context     = 'Computer'
    Order       = 1
    ErrorAction = 'SilentlyContinue'
}
Get-GPPrefRegistryValue @getGPPrefParams | Set-GPPrefRegistryValue @setGPPrefParams
```

```Output
DisplayName      : TestGPO-1
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : ef4d0f7e-1a1a-4fd1-b735-0bc6620e7f51
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 3/1/2009 11:14:06 AM
ModificationTime : 3/1/2009 11:15:16 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 1, SysVol Version: 1
WmiFilter        :


DisplayName      : TestGPO-1
DomainName       : contoso.microsoft.com
Owner            : CONTOSO\Domain Admins
Id               : ef4d0f7e-1a1a-4fd1-b735-0bc6620e7f51
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 3/1/2009 11:14:06 AM
ModificationTime : 3/1/2009 11:15:16 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 2, SysVol Version: 2
WmiFilter        :
```

此命令将所有用于配置注册表键 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey` 下一级别值的注册表首选项项，从名为 `TestGPO` 的源组策略对象（GPO）中的“用户配置”部分复制到名为 `TestGPO-1` 的目标 GPO 中的“计算机配置”部分。对于每一组注册表首选项项，都会返回一个对应的目标 GPO `TestGPO-1` 的副本。

`Get-GPPrefRegistryValue` 命令用于获取所有在源 GPO 的“用户配置”（User Configuration）下配置了相关值的注册表偏好设置项。该命令还会返回所有具有已配置值的一级子键（但不包括这些值对应的注册表偏好设置项本身）。这些注册表偏好设置项和子键随后会被传递给 `Set-GPPrefRegistryValue` cmdlet。

`Set-GPPrefRegistryValue` 命令用于配置目标 GPO 中注册表值的注册表偏好设置项。

- The subkeys returned by `Get-GPPrefRegistryValue` do not have an **Action** property, and so a
  non-terminating error occurs for each subkey. The **ErrorAction** parameter is specified to
  suppress these error messages.

- It is a good practice to specify an order of one `-Order 1` in `Set-GPPrefRegistryValue` when it
  accepts input from the pipeline. This is because Registry preference items passed on the pipeline
  have an **Order** property. If the **Order** property of a Registry preference item passed on the
  pipeline is greater than the number of Registry preference items currently configured in the
  destination GPO, an out of range error occurs and the Registry preference item is not configured
  in the destination GPO. By specifying the order as one in the `Set-GPPrefRegistryValue` command,
  you override the **Order** property of the source Registry preference item, and prevent such
  errors from occurring.

## 参数

### -Action

指定注册表偏好设置项的操作。

此参数的可接受值为：

- Create
- Update
- Replace
- Delete

The action specifies how the Registry preference item is applied to the registry key or registry
value on the client when Group Policy is processed.

```yaml
Type: PreferenceAction
Parameter Sets: (All)
Aliases:
Accepted values: Create, Replace, Update, Delete

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -Context

指定注册表首选项项是在组策略对象（GPO）中的“用户配置”还是“计算机配置”下进行配置的。该参数的可接受值为：`User` 或 `Computer`。

```yaml
Type: GpoConfiguration
Parameter Sets: (All)
Aliases:
Accepted values: User, Computer

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Disable

表示该cmdlet将注册表首选项设置为禁用状态。当在客户端应用组策略时，禁用的注册表首选项不会被执行，因此也不会修改客户端上现有的任何注册表键或值。

此参数并不会禁用 GPO 中已存在的注册表设置项，而是会创建一个新的、处于禁用状态的注册表设置项。当 GPO 在客户端上应用时，任何配置相同键或值的现有注册表设置项仍然会被执行。这种行为与使用 GPMC 禁用现有注册表设置项的方式不同。

你可以使用 `Remove-GPPrefRegistryValue` cmdlet 来删除与指定键或值相关联的所有现有注册表偏好设置项。这些偏好设置项可能存在于 GPO 的用户配置或计算机配置中。在创建新的禁用型注册表偏好设置项之前执行此操作，可以确保新创建的偏好设置项成为 GPO 中与该键或值关联的唯一注册表偏好设置项。

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

指定此 cmdlet 所使用的域名。您必须提供该域名的完全限定域名（FQDN）。

对于 `Set-GPPrefRegistryValue` cmdlet，需要为其配置注册表首选项的 GPO（组策略对象）必须存在于该域中。

如果您没有指定 **Domain** 参数，将使用当前会话运行用户的域信息。如果该 cmdlet 是从计算机启动或关闭脚本中运行的，则将使用计算机的域信息。有关更多详细信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域名与当前会话所运行的用户的域名不同（或者对于启动/关闭脚本来说，是与计算机所在的域不同），那么该域名与用户或计算机的域名之间必须存在信任关系。

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

通过其全局唯一标识符（GUID）指定用于配置注册表首选项项的组策略对象（GPO）。该 GUID 可唯一标识该 GPO。

您也可以通过其内置别名**Id**来引用**Guid**参数。

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

### -Key

指定用于注册表偏好设置项的注册表键；例如：`HKEY_CURRENT_USER\Control Panel\Colors`。

你可以指定以下注册表项中的任何一个：`HKEY_CLASSES_ROOT`（HKCR）、`HKEY_CURRENT_USER`（HKCU）、`HKEY_LOCAL_MACHINE`（HKLM）、`HKEY_USERS`（HKU）以及 `HKEY_CURRENT_CONFIG`（HKCC）。在“计算机配置”和“用户配置”中，都可以使用这些注册表项来设置偏好设置。

您可以为注册表键或注册表值配置一个偏好设置（即注册表项的属性）。

- To configure a setting for a registry key, specify the **Key** parameter without the *ValueName*,
  **Value**, or **Type** parameters.

- To configure a setting for a registry value, specify the **Key** parameter together with the
  **ValueName**, **Value**, and **Type** parameters.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: FullKeyPath

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

通过显示名称来指定用于配置注册表首选项项的 GPO（组策略对象）。

显示名称在域中并不保证是唯一的。如果域中存在另一个具有相同显示名称的 GPO，将会出现错误。您可以使用 **Guid** 参数来唯一地标识一个 GPO。

您也可以通过其内置别名 **DisplayName** 来引用 **Name** 参数。

```yaml
Type: System.String.String.String
Parameter Sets: ByName
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Order

该设置用于指定在将 GPO 应用到客户端计算机时，该注册表偏好项相对于 GPO 中其他注册表偏好项的处理顺序。如果 GPO 中有两个注册表偏好项会修改同一个注册表值，那么顺序最高的那个偏好项将在客户端最后修改该值。

默认情况下，如果未指定 `Order` 参数，则顺序会设置为 GPO 中当前注册表偏好项数量的值加 1。您可以指定任何大于 0 的值。如果您指定的值大于默认值，那么顺序将恢复为默认值。

当注册表偏好设置项被添加到组策略对象（GPO）中或从GPO中删除时，这些设置的顺序可能会发生变化。例如，如果一个GPO包含五个注册表偏好设置项，而你又添加了一个新的设置项，并将其顺序指定为“4”，那么原本排在第4位和第5位的设置项在修改后就会分别变为第5位和第6位。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Server

指定此 cmdlet 用于联系以完成操作的域控制器的名称。您可以指定完全qualified域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系主域控制器（PDC）仿真器。

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

### -Type

用于指定注册表首选项项中注册表值的数据类型。

此参数的可接受值为：

- String
- ExpandString
- Binary
- DWord
- MultiString
- ExpandString
- Qword

For more information about these data types, see
[Microsoft.Win32.RegistryValueKind Enumeration](https://go.microsoft.com/fwlink/?LinkID=143266) in
the MSDN library.

When you configure a Registry preference item for a registry key, do not specify this parameter.
When you configure a Registry preference item for a registry value, specify this parameter together
with the **Key**, **ValueName**, and **Value** parameters.

```yaml
Type: RegistryValueKind
Parameter Sets: (All)
Aliases:
Accepted values: Unknown, String, ExpandString, Binary, DWord, MultiString, QWord, None

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Value

用于指定注册表设置项中对应注册表值的实际数据内容。例如，注册表值 `HKEY_CURRENT_USER\Control Panel\Colors ActiveTitle` 的数据可能如下所示：`data: 10 36 106`。

在为注册表键配置注册表偏好设置项时，不要指定此参数。在为注册表值配置注册表偏好设置项时，请同时指定此参数以及 **Key**（键）、**ValueName**（值名称）和 **Type**（类型）参数。

```yaml
Type: PSObject
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ValueName

用于指定注册表偏好设置项中对应的注册表值的名称。例如，注册表键 `HKEY_CURRENT_USER\Control Panel\Colors` 可以包含一个名为 `ActiveTitle` 的值。对于注册表键的默认值，可以指定 `(default)` 或空字符串 `""`。

当你为注册表键配置注册表偏好设置项时，不要指定此参数。当你为注册表值配置注册表偏好设置项时，需要同时指定此参数以及 **Key**（键）、**Value**（值）和 **Type**（类型）这三个参数。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.GroupPolicy.Gpo

### Microsoft.GroupPolicyPreferenceRegistrySetting

你可以将一个 GPO 对象（用于配置指定的注册表设置）传递给此 cmdlet，或者一个 **PreferenceRegistrySetting** 对象（用于在指定的 GPO 中进行配置）。不支持包含来自不同域的 GPO 的集合。

## 输出

### Microsoft.GroupPolicy.Gpo

此cmdlet返回配置了注册表偏好设置项的GPO（组策略对象）。

## 备注

* You can use the **Domain** parameter to explicitly specify the domain for this cmdlet.

如果您没有明确指定域名，该 cmdlet 会使用默认域名。默认域名是指当前会话所运行的安全上下文用于访问网络资源时所使用的域名。这个域名通常是与运行该会话的用户相关的域名；例如，通过“程序文件”菜单启动 Windows PowerShell 的用户的域名，或者在 “runas” 命令中指定的用户的域名。然而，计算机启动和关闭脚本是在 LocalSystem 账户的上下文中运行的。LocalSystem 是一个内置的本地账户，它以计算机账户的权限来访问网络资源。因此，当从这个启动或关闭脚本中运行该 cmdlet 时，默认域名就是计算机所属的域名称。

## 相关链接

[Get-GPPrefRegistryValue](./Get-GPPrefRegistryValue.md)

[Remove-GPPrefRegistryValue](./Remove-GPPrefRegistryValue.md)

