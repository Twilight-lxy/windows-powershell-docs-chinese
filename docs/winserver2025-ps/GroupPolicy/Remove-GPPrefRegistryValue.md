---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/remove-gpprefregistryvalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-GPPrefRegistryValue
---

# 移除 GPPREF 注册表值

## 摘要

从组策略对象（GPO）中的“计算机配置”或“用户配置”中删除一个或多个注册表偏好设置项。

## 语法

### GetByGUID（默认值）

```
Remove-GPPrefRegistryValue -Guid <Guid> -Context <GpoConfiguration> -Key <String>
 [-ValueName <String>] [-Order <Int32>] [-Domain <String>] [[-Server] <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### GetByName

```
Remove-GPPrefRegistryValue [-Name] <String> -Context <GpoConfiguration> -Key <String>
 [-ValueName <String>] [-Order <Int32>] [-Domain <String>] [[-Server] <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Remove-GPPrefRegistryValue` cmdlet 可以从组策略对象（GPO）的“计算机配置”或“用户配置”中删除一个或多个注册表首选项项。您必须指定 `Context` 参数，以指明是要从“计算机配置”还是“用户配置”中删除该注册表首选项项。您可以按 GPO 的显示名称或其 GUID 来标识该 GPO。

你可以指定键（key）或值（value）中的任意一个：

- If you specify a key, all Registry preference items that configure that registry key or any of its
  first-level values are removed from the specified configuration in the GPO. Registry preference
  items that configure subkeys of that key or their values are not affected. For a key, specify the
  **Key** parameter without the *ValueName* parameter.

- If you specify a value, all Registry preference items that configure that registry value are
  removed from the specified configuration in the GPO. For a value, specify the **Key** parameter
  without the **ValueName** parameter.

这个cmdlet可以从管道中接收输入数据：

- You can pipe GPO objects to this cmdlet to remove a specified Registry preference item from one or
  more GPOs.

- You can pipe **PreferencRegistrySetting** objects to this cmdlet to remove one or more Registry
  preference items from a specified GPO.

## 示例

### 示例 1：删除指定注册表项下的所有注册表偏好设置项

```powershell
$params = @{
    Name      = 'TestGPO'
    Context   = 'User'
    Key       = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey'
    ValueName = 'ValueOne'
}
Remove-GPPrefRegistryValue @params
```

```Output
DisplayName      : TestGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 92f79f6c-61ce-47d9-8dc6-f78c5cea93ac
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/28/2009 5:15:04 PM
ModificationTime : 2/28/2009 5:15:32 PM
UserVersion      : AD Version: 5, SysVol Version: 5
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :
```

此命令会从名为“TestGPO”的组策略对象（GPO）的用户配置中，删除所有用于配置注册表值 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey ValueOne` 的注册表偏好设置项。

### 示例 2：删除用于配置一级值的注册表偏好设置项

```powershell
$params = @{
    Name    = "TestGPO"
    Context = "Computer"
    Key     = "HKLM\SOFTWARE\Microsoft\ExampleKey"

}
Remove-GPPrefRegistryValue @params
```

```Output
DisplayName      : TestGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 92f79f6c-61ce-47d9-8dc6-f78c5cea93ac
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/28/2009 5:15:04 PM
ModificationTime : 2/28/2009 5:15:32 PM
UserVersion      : AD Version: 5, SysVol Version: 5
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :
```

此命令会删除注册表中的某些偏好设置项。这些偏好设置项用于配置位于注册表键 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey` 下的所有一级值，或者直接从名为 `TestGPO` 的组策略对象（GPO）的 “计算机配置” 设置中删除该注册表键本身。

### 示例 3：删除所有组策略对象（GPO）中的注册表偏好设置项

```powershell
$params = @{
    Context     = 'User'
    Key         = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey'
    ValueName   = 'ValueOne'
    ErrorAction = 'SilentlyContinue'
}
Get-GPO -All | Remove-GPPrefRegistryValue @params
```

```Output
DisplayName      : TestGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : a83ad1da-9fd4-4005-96b1-7e98042d04de
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/28/2009 5:21:05 PM
ModificationTime : 2/28/2009 5:21:17 PM
UserVersion      : AD Version: 5, SysVol Version: 5
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :


DisplayName      : TestGPO-1
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 277eafe8-5dbf-4e3f-86dc-557eee14d0a4
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/28/2009 2:35:24 PM
ModificationTime : 2/28/2009 5:21:17 PM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :
```

此命令会删除所有域中GPO的“用户”配置设置中，用于配置注册表值`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExampleKey ValueOne`的所有注册表偏好项。命令会返回每一个至少有一个注册表偏好项被删除的GPO。

对于每个没有与指定注册表值相关联的注册表偏好设置的GPO（组策略对象），此cmdlet都会返回一个非终止性的错误。在本命令中，通过将**ErrorAction**参数设置为`SilentlyContinue`来抑制这些错误消息。有关**ErrorAction**参数的更多信息，请参阅[about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 参数

### -Confirm

在运行该cmdlet之前，会提示您确认是否要执行该操作。

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

指定是否从指定的组策略对象（GPO）中的“计算机配置”或“用户配置”中删除相应的注册表偏好设置项。必须明确选择“用户”或“计算机”其中之一作为操作目标。

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

指定此 cmdlet 执行操作的域名。您必须提供该域的完全限定域名（FQDN）。

对于 `Remove-GPPrefRegistryValue` cmdlet 来说，需要从中删除注册表首选项项的 GPO（组策略对象）必须存在于该域中。

如果您没有指定 **Domain** 参数，那么将使用当前会话所运行的用户的域名。（如果该 cmdlet 是通过计算机启动或关闭脚本来执行的，则会使用计算机的域名。）有关更多信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域名与当前会话所使用的用户的域名不同，则该域名与用户或计算机的域名之间必须存在信任关系。

您也可以使用该参数的内置别名 **DomainName** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

通过其全局唯一标识符（GUID）指定要从其中删除注册表首选项项目的组策略对象（GPO）。该 GUID 可唯一标识该 GPO。

您也可以使用其内置别名 **Id** 来引用 **Guid** 参数。

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
指定一个注册表键，以便从中删除一个或多个注册表偏好设置项；例如：HKCU\Control Panel\Colors。

您可以指定以下注册表项中的任意一个：`HKEY_CLASSES_ROOT`（HKCR）、`HKEY_CURRENT_USER`（HKCU）、`HKEY_LOCAL_MACHINE`（HKLM）、`HKEY_USERS`（HKU）以及 `HKEY_CURRENT_CONFIG`（HKCC）。在“计算机配置”和“用户配置”中，都可以使用这些注册表项来设置注册表偏好设置。

`Key` 参数可以单独指定，也可以与 `ValueName` 参数一起指定：

- If the **ValueName** parameter is specified, all Registry preference items that configure the
  registry value are removed.

- If the **ValueName** parameter is not specified, all Registry preference items that configure the
  registry key and any of its first-level values are removed.

您也可以使用其内置别名 FullKeyPath 来引用 **Key** 参数。

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

根据显示名称指定要从其中删除注册表首选项项的 GPO（组策略对象）。

显示名称在域内并不保证是唯一的。如果该域中存在另一个具有相同显示名称的 GPO，将会发生错误。您可以使用 Guid 参数来唯一标识一个 GPO。

您也可以通过其内置别名 **DisplayName** 来引用 **Name** 参数。

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

指定当GPO应用于客户端计算机时，某个注册表偏好设置项相对于GPO中的其他注册表偏好设置项的处理顺序。

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

指定此 cmdlet 用于联系以完成操作的域控制器的名称。您可以指定完全 Qualified Domain Name（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统会联系主域控制器（PDC）模拟器。

您也可以使用其内置别名**DC**来引用**Server**参数。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DC

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ValueName

指定要删除所有注册表偏好设置的注册表值的名称。如果您指定了 **ValueName** 参数，那么还必须指定 **Key** 参数。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft(GroupPolicy.Gpo)

### Microsoft.GroupPolicy PreferenceRegistrySetting

此 cmdlet 接受一个 GPO 或一个 **PreferenceRegistrySetting** 对象作为输入。你可以通过管道传输一个或多个 **PreferenceRegistrySetting** 对象，从而从一个指定的 GPO 中删除一个或多个注册表偏好设置项；你也可以通过管道传输一个或多个 GPO 对象（例如使用 `Get-GPO` 命令获取的 GPO），以便从每个 GPO 中删除指定的注册表偏好设置项。不支持包含来自不同域的 GPO 的集合。

## 输出

### Microsoft(GroupPolicy.Gpo)

此cmdlet会返回从中移除了注册表首选项（一个或多个）的GPO（组策略对象）。

## 备注

* You can use the **Domain** parameter to explicitly specify the domain for this cmdlet.

如果您没有明确指定域名，该cmdlet会使用默认域名。默认域名是指当前会话运行的安全上下文用于访问网络资源时所使用的域名。这个域名通常就是运行该会话的用户的域名；例如，通过“Program Files”菜单打开Windows PowerShell来启动会话的用户对应的域名，或者在“runas”命令中指定的用户对应的域名。然而，计算机启动和关闭脚本是在“LocalSystem”账户的上下文中运行的。“LocalSystem”是一个内置的本地账户，它以计算机账户的权限访问网络资源。因此，当从这个启动或关闭脚本中运行该cmdlet时，默认域名就是计算机所隶属于的域名。

## 相关链接

[Get-GPO](./Get-GPO.md)

[Get-GPPrefRegistryValue](./Get-GPPrefRegistryValue.md)

[Set-GPPrefRegistryValue](./Set-GPPrefRegistryValue.md)
