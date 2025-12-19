---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/get-gpprefregistryvalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-GPPrefRegistryValue
---

# Get-GPPrefRegistryValue

## 摘要

从一个GPO中的“计算机配置”或“用户配置”部分获取一个或多个注册表偏好设置项。

## 语法

### GetByGUID（默认值）

```
Get-GPPrefRegistryValue -Guid <Guid> -Context <GpoConfiguration> -Key <String>
 [-ValueName <String>] [-Order <Int32>] [-Domain <String>] [-Server <String>] [<CommonParameters>]
```

### GetByName

```
Get-GPPrefRegistryValue [-Name] <String> -Context <GpoConfiguration> -Key <String>
 [-ValueName <String>] [-Order <Int32>] [-Domain <String>] [-Server <String>] [<CommonParameters>]
```

## 描述

`Get-GPPrefRegistryValue` cmdlet 可以从组策略对象（GPO）中的“计算机配置”或“用户配置”部分获取一个或多个注册表偏好设置项。您必须指定 `Context` 参数（该参数用于指明是要从“计算机配置”还是“用户配置”中获取这些偏好设置项）。您可以按照 GPO 的显示名称或其 GUID 来识别它。

你可以获取特定注册表值的偏好设置项，或者获取某个键及其所有一级注册表值的偏好设置项。

- To get any Registry preference items that configure a specific registry value, specify both the
  **Key** and the *ValueName* parameters.

- To get all the Registry preference items that configure a registry key and any first-level
  registry values directly under the key, specify the **Key** parameter without the *ValueName*
  parameter.

如果您只指定一个键，该cmdlet还会返回其一级子键（即那些具有注册表偏好设置项的子键），以及这些子键的值或它们的任何子键及其值。您可以使用这些信息来浏览注册表偏好设置项。

## 示例

#### 示例 1：获取注册表首选项的值

```powershell
$params = @{
    ValueName = 'ValueOne'
    Context   = 'User'
    Key       = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey'
    Name      = 'TestGPO'
}
Get-GPPrefRegistryValue @params
```

```Output
KeyPath            : SOFTWARE\Microsoft\ExampleKey
FullKeyPath        : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey
Hive               : LocalMachine
Action             : Create
Order              : 1
DisabledDirectly   : False
DisabledByAncestor : False
Value              : TestGPO
Type               : String
ValueName          : ValueOne
HasValue           : True
```

这个命令用于从名为“TestGPO”的组策略对象（GPO）中的“用户配置”部分，获取为注册表值`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey`以及该值的名称“ValueOne”所配置的注册表偏好设置项。

### 示例 2：获取所有注册表首选项项

```powershell
$params = @{
    Context = 'User'
    Key     = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey'
    Name    = 'TestGPO'
}
Get-GPPrefRegistryValue @params
```

```Output
KeyPath            : SOFTWARE\Microsoft\ExampleKey
FullKeyPath        : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey
Hive               : LocalMachine
Action             : Create
Order              : 1
DisabledDirectly   : False
DisabledByAncestor : False
Value              : NewData1
Type               : String
ValueName          : ValueOne
HasValue           : True

KeyPath            : SOFTWARE\Microsoft\ExampleKey
FullKeyPath        : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey
Hive               : LocalMachine
Action             : Create
Order              : 2
DisabledDirectly   : False
DisabledByAncestor : False
Value              : NewData2
Type               : String
ValueName          : Valuetwo
HasValue           : True



KeyPath     : SOFTWARE\Microsoft\ExampleKey\Subkey1
FullKeyPath : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey\Subkey1
Hive        : LocalMachine

KeyPath     : SOFTWARE\Microsoft\ExampleKey\SubKey2
FullKeyPath : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey\SubKey2
Hive        : LocalMachine
```

此命令会从名为 TestGPO 的组策略对象（GPO）的用户配置部分中，获取所有为注册表键 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey 及其一级子键所配置的注册表偏好设置项。

在这个例子中，返回了用于配置注册表键中以下两个一级值的注册表偏好设置项：ValueOne 和 ValueTwo。同时，还返回了该键下的两个子键。这是因为在用户配置（User Configuration）中存在与每个子键相关联的注册表偏好设置项。

## 参数

### -Context

指定该 cmdlet 是从 GPO 的“用户配置”还是“计算机配置”中获取注册表偏好设置项。

该参数的可接受值为：User（用户）或Computer（计算机）。

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

### -Domain

指定此 cmdlet 的域。必须提供该域的完全限定域名（FQDN）。

对于 `Get-GPPrefRegistryValue` cmdlet 来说，要获取其注册表偏好设置项的 GPO（组策略对象）必须存在于该域中。

如果您没有指定 **Domain** 参数，那么将使用当前会话所运行用户的域信息。如果该 cmdlet 是从计算机启动或关闭脚本中运行的，则会使用计算机的域信息。有关更多详细信息，请参阅完整帮助文档中的“备注”部分。

如果你指定的域与当前会话的用户所使用的域不同（或者对于启动/关闭脚本来说，是与计算机所在的域不同），那么该域与用户或计算机所在域之间必须存在信任关系。

您也可以通过其内置别名 **DomainName** 来引用 **Domain** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

该参数用于指定此cmdlet通过其全局唯一标识符（GUID）从哪个GPO中获取注册表首选项项。该GUID能够唯一地标识该GPO。

您也可以使用该参数的内置别名 **Id** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: Guid
Parameter Sets: GetByGUID
Aliases: Id

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Key

指定此 cmdlet 所获取的注册表偏好设置项对应的注册表键；例如：`HKEY_CURRENT_USER\Control Panel\Colors`。

该参数的可接受值包括：

- HKEY_CLASSES_ROOT (HKCR)
- HKEY_CURRENT_USER (HKCU)
- HKEY_LOCAL_MACHINE (HKLM)
- HKEY_USERS (HKU)
- HKEY_CURRENT_CONFIG (HKCC)

这些注册表项中的任何一个都可以被指定用于“计算机配置”和“用户配置”中的注册表偏好设置。

`Key` 参数可以单独指定，也可以与 `ParameterValue` 参数一起指定：

- If the **ValueName** parameter is specified, all Registry preference items that configure the
  registry value are retrieved.

- If the **ValueName** parameter is not specified, all Registry preference items that configure the
  registry key and any of its first-level values are retrieved.

您也可以使用其内置别名 `FullKeyPath` 来引用 `Key` 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: FullKeyPath

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

指定此 cmdlet 根据显示名称从哪个 GPO 中获取注册表首选项项。

显示名称在域内不保证是唯一的。如果域中存在另一个具有相同显示名称的组策略对象（GPO），则会发生错误。您可以使用 **Guid** 参数来唯一标识一个 GPO。

您也可以通过其内置别名 **DisplayName** 来引用 **Name** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: GetByName
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Order

指定注册表偏好设置项在客户端上应用的顺序，该顺序是相对于组策略对象（GPO）中的其他注册表偏好设置项而言的。

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

指定此cmdlet用于联系以完成操作的域控制器的名称。您可以指定完全 Qualified Domain Name（FQDN）或主机名。

如果您没有通过 **Server** 参数指定名称，系统将会联系主域控制器（PDC）仿真器。

您也可以使用服务器参数的内置别名“DC”来引用它。有关更多信息，请参阅[关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

### -ValueName

指定一个注册表值的名称，该 cmdlet 会从这个值中获取所有的注册表偏好设置项。例如，注册表键 `HKEY_CURRENT_USER\Control Panel\Colors` 可能包含一个名为 `ActiveTitle` 的值。要获取某个注册表键的默认值，可以指定“(default)”或空字符串 (“”)。

当你需要获取某个注册表键及其所有一级值的注册表偏好设置项时，不要指定此参数。当你仅需要获取某个特定注册表值的注册表偏好设置项时，请同时指定此参数和**Key**参数。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftGROUPPolicy.Gpo

此cmdlet接受一个GPO作为输入。不支持包含来自不同域的GPO的集合。

## 输出

### Microsoft.GroupPolicy PreferenceRegistrySetting

此cmdlet返回**PreferenceRegistrySetting**对象。您可以将这些对象传递给以下cmdlet：

- `Set-GPPrefRegistryValue`

- `Remove-GPPrefRegistryValue`

## 备注

* If a Registry preference item for the specified registry key or value is not found, a
  non-terminating error occurs.

你可以使用 **Domain** 参数来明确指定此 cmdlet 的域名。

如果您没有明确指定域名，该cmdlet会使用默认域名。默认域名是指当前会话所运行的安全上下文用于访问网络资源的那个域名。这个域名通常就是启动该会话的用户所属的域名（例如，通过Windows PowerShell打开会话的用户所在的域，或者在“runas”命令中指定的用户所在的域）。然而，计算机启动和关闭脚本是在LocalSystem账户的上下文中运行的。LocalSystem是一个内置的本地账户，它以计算机的身份来访问网络资源。因此，当从这个启动或关闭脚本中运行该cmdlet时，默认域名就是计算机所属的域名。

## 相关链接

[Remove-GPPrefRegistryValue](./Remove-GPPrefRegistryValue.md)

[Set-GPPrefRegistryValue](./Set-GPPrefRegistryValue.md)

