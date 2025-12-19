---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/set-gpregistryvalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-GPRegistryValue
---

# Set-GPRegistryValue

## 摘要

在组策略对象（GPO）中，通过“计算机配置”或“用户配置”选项来设置一个或多个基于注册表的策略项。

## 语法

### ByGUID（默认值）

```
Set-GPRegistryValue -Guid <Guid> -Key <String> [-ValueName <String[]>] [-Value <PSObject>]
 [-Type <RegistryValueKind>] [-Domain <String>] [-Server <String>] [-Additive] [-Disable]
 [-ValuePrefix <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 按名称排序

```
Set-GPRegistryValue [-Name] <String> -Key <String> [-ValueName <String[]>] [-Value <PSObject>]
 [-Type <RegistryValueKind>] [-Domain <String>] [-Server <String>] [-Additive] [-Disable]
 [-ValuePrefix <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Set-GPRegistryValue` cmdlet 用于在组策略对象（GPO）的“计算机配置”或“用户配置”项下，配置基于注册表的策略设置。当该 GPO 被应用到客户端计算机时，这些策略设置会修改注册表中的相应键或值。

您可以通过名称或GUID来指定GPO，也可以将一个GPO对象通过管道（pipe）传递给该cmdlet。同样地，您也可以将一个PolicyRegistrySetting对象通过管道传递给该cmdlet。

您可以配置基于注册表的策略设置，用于：

- One or more registry values by passing the **Key**, **ValueName**, **Value**, and **Type**
  parameters. For multiple registry values, pass a comma-separated list for both the **ValueName**
  and **Value** parameters. When you specify multiple registry values, only the `String` and
  `ExpandString` data types are supported.

- A list of one or more registry values that share the same name prefix by passing the **Key** and
  **Type** parameters, and a single value or a comma-separated list for the **Value** parameter. You
  can optionally specify the value name prefix by using the **ValuePrefix** parameter. Only the
  `String` and `ExpandString` data types are supported for lists.

你可以使用 `Additive` 参数来确保在应用 GPO 时，该键的现有注册表值不会被新的策略设置覆盖。

当GPO应用到客户端时，您也可以通过使用“Disable”参数来禁用某个策略设置，从而删除相应的注册表值。您可以禁用的内容包括：

- All the registry values under a specified registry key by passing the **Key** parameter. No
  subkeys, or their values, are deleted on the client.

- A single registry value by passing the **Key** parameter and the **ValueName** parameter.

- Multiple registry values by passing the **Key** parameter and a comma-separated list for the
  **ValueName** parameter.

## 示例

#### 示例 1：为某个注册表值配置基于注册表的策略设置

```powershell
$params = @{
    Name      = 'TestGPO'
    Key       = 'HKCU\Software\Policies\Microsoft\Windows\Control Panel\Desktop'
    ValueName = 'ScreenSaveTimeOut'
    Value     = 900
    Type      = 'DWORD'
}
Set-GPRegistryValue @params
```

```Output
DisplayName      : TestGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 35c12ab3-956c-45d5-973b-46b17d225f47
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/24/2009 4:41:03 PM
ModificationTime : 2/25/2009 12:42:00 PM
UserVersion      : AD Version: 3, SysVol Version: 3
ComputerVersion  : AD Version: 34, SysVol Version: 34
WmiFilter        :
```

此命令为注册表值 `HKCU\Software\Policies\Microsoft\Windows\Control ScreenSaverTimeOut` 配置了一个基于注册表的策略设置。该注册表值的值为 `900`，数据类型为 `DWord`。当组策略应用于客户端时，此策略设置会将屏幕保护程序的超时时间设置为 900 秒（15 分钟）。

### 示例 1：为多个注册表值配置基于注册表的策略设置

```powershell
$params = @{
    Name      = 'TestGPO'
    Key       = 'HKCU\Software\Policies\Microsoft\ExampleKey'
    ValueName = 'ValueOne', 'ValueTwo', 'ValueThree'
    Value     = 'String 1', 'String 2', 'String 3'
    Type      = 'String'
}
Set-GPRegistryValue @params
```

此命令用于配置基于注册表的策略设置，以修改三个注册表值。这些策略设置在GPO的“用户”配置部分中进行配置。当GPO应用于客户端时，以下注册表值将会被修改：

`HKCU\Software\Policies\Microsoft\ExampleKeyValueOne` `字符串 1`

`HKCU\Software\Policies\Microsoft\ExampleKeyValueTwo` `String 2`

`HKCU\Software\Policies\Microsoft\ExampleKeyValueThree` `String 3`

### 示例 3：配置基于注册表的策略设置，以指定一组注册表值

```powershell
$params = @{
    Name        = 'TestGPO'
    Key         = 'HKCU\Software\Policies\Microsoft\ExampleKey'
    ValuePrefix = 'MyValue'
    Type        = 'String'
    Value       = 'String 1', 'String 2', 'String 3'
}
Set-GPRegistryValue @params
```

此命令配置了一个基于注册表的策略设置，用于设置三个注册表值的列表。这些策略设置在 GPO 的“用户”配置部分中进行配置。由于没有指定 “Additive” 参数，因此当 GPO 应用于客户端时，该键下的所有列表值都会被删除；之后，将设置以下注册表值：

`HKCU\Software\Policies\Microsoft\ExampleKey\MyValue1` `String 1`

`HKCU\Software\Policies\Microsoft\ExampleKey“MyValue2”` `String 2`

`HKCU\Software\Policies\Microsoft\ExampleKey\MyValue3` `字符串（长度为3）`

如果您指定了**Additive**参数，那么在应用GPO时，列表中的值将会被添加到客户端上已有的列表值中。分配给这些列表值的实际名称取决于客户端上现有列表值的数量。

### 示例 4：禁用针对特定注册表值的基于注册表的策略设置

```powershell
$params = @{
    Disable   = $true
    Name      = 'TestGPO'
    Key       = 'HKCU\Software\Policies\Microsoft\ExampleKey'
    ValueName = 'ValueOne', 'ValueTwo', 'ValueThree'
}
Set-GPRegistryValue @params
```

此命令会禁用“用户配置”部分中基于注册表的策略设置，针对指定的注册表值。当该组策略对象（GPO）应用于客户端时，这些注册表值将从客户端的注册表中删除。

### 示例 5：禁用针对特定注册表键的基于注册表的策略设置

```powershell
Set-GPRegistryValue -Disable -Name 'TestGPO' -Key 'HKCU\Software\Policies\Microsoft\ExampleKey'
```

此命令会禁用指定注册表键在“用户配置”部分中基于注册表的策略设置。当GPO应用于客户端时，该注册表键中的所有一级值都会被删除，但子键及其值不会被修改。

## 参数

### -Additive

表示当GPO应用于客户端时，注册表值应追加到该键下已存在的值中。

默认情况下，当在客户端上处理组策略时，系统会在将任何新值写入注册表之前删除该注册表键下的现有值。通过使用基于注册表的策略设置中的 **Additive** 参数，您可以指定新值应被添加到注册表键中，而不会删除现有值。

您不能使用这个参数来指定“禁用”（Disable）选项。

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

### -Disable

表示该 cmdlet 会禁用基于注册表的策略设置。

您可以禁用注册表键或值的策略设置：

- For a registry key, specify the **Key** parameter without the **ValueName** parameter. When the GPO
  is applied on the client, all of the values directly under the key are removed from the registry.
  The key itself is not removed from the registry, nor are any of its subkeys, or their values,
  removed.

- For a registry value, specify the **Key** parameter together with the **ValueName** parameter.
  When the GPO is applied on the client, only the specified value is removed from the registry.

要从组策略对象（GPO）中删除某个策略设置，同时不影响客户端上已存在的注册表键或值，请使用 `Remove-GPRegistryValue` cmdlet。

您不能在使用 `Disable` 参数的同时指定 `Additive`、`Type`、`Value` 或 `ValuePrefix` 这些参数。

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

指定此cmdlet所使用的域名。必须提供该域名的完全限定域名（FQDN）。

对于 `Set-GPRegistryValue` cmdlet 来说，需要配置基于注册表策略设置的 GPO 必须存在于该域中。

如果您没有指定 **Domain** 参数，那么将使用运行当前会话的用户所在的域。如果该 cmdlet 是从计算机启动或关闭脚本中运行的，则将使用计算机所属的域。有关更多信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域名与当前会话所使用的用户的域名不同（或者对于启动/关闭脚本而言，与该计算机的域名不同），那么该域名与用户或计算机的域名之间必须存在信任关系。

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

通过其全局唯一标识符（GUID）指定用于配置基于注册表的策略设置的组策略对象（GPO）。该 GUID 可唯一地识别该 GPO。

您也可以使用其内置别名 **Id** 来引用 **Guid** 参数。

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

指定基于注册表的策略设置的注册表键；例如，`HKLM\Software\Policies\Microsoft\Windows NT\DNSClient`。

该密钥必须存在于以下两个注册表项之一中：

- `HKEY_LOCAL_MACHINE` (HKLM) for a registry-based policy setting in Computer Configuration.

- `HKEY_CURRENT_USER` (HKCU) for a registry-based policy setting in User Configuration.

您也可以使用其内置别名 FullKeyPath 来引用 Key 参数。

```yaml
Type: System.String.String
Parameter Sets: (All)
Aliases: FullKeyPath

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

通过显示名称指定用于配置基于注册表的策略设置的组策略对象（GPO）。

显示名称在域中并不保证是唯一的。如果域中存在另一个具有相同显示名称的 GPO，将会发生错误。您可以使用 **Guid** 参数来唯一标识一个 GPO。

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

指定此cmdlet用于联系的域控制器的名称，以便完成操作。您可以指定完全限定域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将联系主域控制器（PDC）仿真器。

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

指定基于注册表的策略设置的数据类型。

此参数的可接受值为：

- String
- ExpandString
- Binary
- DWord
- MultiString
- QWord

For more information about these data types, see
[Microsoft.Win32.RegistryValueKind Enumeration](https://go.microsoft.com/fwlink/?LinkID=143266) in
the MSDN library.

Only the following data types are supported for list values: `String` and `ExpandString`.

You must specify this parameter when you configure a policy setting to set a registry value.
You cannot specify this parameter with the **Disable** parameter.

The following values are permitted for this object type.

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

用于指定基于注册表的策略设置的值数据。您可以指定一个单一的值或一组值。如果需要指定多个值，可以使用逗号分隔的列表来实现。对于值数组而言，仅支持 `String` 和 `ExpandString` 数据类型。

至少，您必须指定这个参数，同时还要指定*类型*（Type）和**键**（Key）参数，才能配置一个用于设置注册表值的策略。您不能将这个参数与**禁用**（Disable）参数一起使用。

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

用于为基于注册表的策略设置指定一个值名称或一组值名称。例如，注册表键 `HKLM\Software\Policies\Microsoft\Windows NT\DNSClient` 可以包含一个具有以下值名称的注册表值：`UseDomainNameDevolution`。若需指定多个值名称，请使用逗号分隔的列表。对于值数组，仅支持 `String` 和 `ExpandString` 数据类型。

您不能使用 **ValuePrefix** 参数来指定这个参数。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ValuePrefix

为基于注册表的策略设置指定一个值名称前缀，该前缀用于关联一组注册表值。

配置一个策略设置，当组策略应用于客户端时，该设置会创建以下注册表值：

`HKLM\SOFTWARE\Policies\ExampleKey\ExValue1` `100`

`HKLM\SOFTWARE\Policies\ExampleKey\ExValue2` `200`

`HKLM\SOFTWARE\Policies\ExampleKey\ExValue3` `300`

只有 `String` 和 `ExpandString` 数据类型支持使用 **ValuePrefix** 参数。

您不能使用 **ValueName** 参数或 **Disable** 参数来指定此参数。

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

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

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

### Microsoft.GroupPolicy.Gpo 或 Microsoft.GroupPolicy.PolicyRegistrySetting

你可以将一个GPO（其中包含基于注册表的策略设置）或一个**PolicyRegistrySetting**对象（表示基于注册表的策略设置，用于在指定的GPO中配置）传递给此cmdlet。不支持包含来自不同域的GPO的集合。

## 输出

### Microsoft.GroupPolicy.Gpo

这个 cmdlet 会返回配置了基于注册表的策略设置的组策略对象（GPO）。

## 备注

* The hive of the registry key that you specify, `HKEY_LOCAL_MACHINE` (HKLM) or `HKEY_CURRENT_USER`
  (HKCU), determines whether the registry-based policy setting is in Computer Configuration or User
  Configuration.

您可以使用 **Domain** 参数来明确指定此 cmdlet 的域名。

如果你没有明确指定域名，该 cmdlet 会使用默认域名。默认域名是指当前会话所运行的安全上下文用于访问网络资源时使用的域名。这个域名通常就是启动该会话的用户所属的域名；例如，通过“程序文件”菜单打开 Windows PowerShell 启动会话的用户所属的域名，或者在 “runas” 命令中指定的用户所属的域名。然而，计算机启动和关闭脚本是在 LocalSystem 计算机账户的上下文中运行的。LocalSystem 是一个内置的本地账户，它以计算机账户的身份访问网络资源。因此，当从这个启动或关闭脚本中运行该 cmdlet 时，默认域名就是计算机所连接的那个域名。

## 相关链接

[Get-GPRegistryValue](./Get-GPRegistryValue.md)

[Remove-GPRegistryValue](./Remove-GPRegistryValue.md)

