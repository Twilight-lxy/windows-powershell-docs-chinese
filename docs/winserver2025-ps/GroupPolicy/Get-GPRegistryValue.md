---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/get-gpregistryvalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-GPRegistryValue
---

# Get-GPRegistryValue

## 摘要

在组策略对象（GPO）中，“计算机配置”或“用户配置”下可以找到一个或多个基于注册表的策略设置。

## 语法

### GetByGUID（默认值）

```
Get-GPRegistryValue -Guid <Guid> -Key <String> [-ValueName <String>] [-Domain <String>]
 [-Server <String>] [<CommonParameters>]
```

### GetByName

```
Get-GPRegistryValue [-Name] <String> -Key <String> [-ValueName <String>] [-Domain <String>]
 [-Server <String>] [<CommonParameters>]
```

## 描述

`Get-GPRegistryValue` cmdlet 可以从组策略对象（Group Policy Object, GPO）中的“计算机配置”（Computer Configuration）或“用户配置”（User Configuration）部分检索一个或多个基于注册表的策略设置。

你可以为特定的注册表值获取基于注册表的策略设置，或者为某个键下的所有注册表值获取这样的设置。

- To get the registry-based policy setting that configures a specific registry value, specify both
  the **Key** and the **ValueName** parameters.

- To get all the registry-based policy settings that configure values directly under a registry key,
  specify the **Key** parameter without the **ValueName** parameter.

如果您仅指定一个键，那么除了用于配置该键下值的策略设置外，系统还会返回该键的以下一级子键：

- first-level subkeys that have a policy setting that configures a value.

- first-level subkeys that have a subkey, at any level, with a policy setting that configures a
  value.

你可以利用这些信息来查找基于注册表的策略设置。

## 示例

### 示例 1：从指定的键中获取组策略注册表值

```powershell
$params = @{
    ValueName = 'ValueOne'
    Key       = 'HKEY_CURRENT_USER\Software\Policies\Microsoft\ExampleKey'
    Name      = 'TestGPO'
}
Get-GPRegistryValue @params
```

```Output
KeyPath     : Software\Policies\Microsoft\ExampleKey
FullKeyPath : HKEY_CURRENT_USER\Software\Policies\Microsoft\ExampleKey
Hive        : CurrentUser
PolicyState : Set
Value       : TestGPO
Type        : String
ValueName   : ValueOne
HasValue    : True
```

此命令从名为“TestGPO”的组策略对象（GPO）中的“用户配置”部分，获取用于配置注册表值 `HKEY_CURRENT_USER\Software\Policies\Microsoft\ExampleKey:ValueOne` 的基于注册表的策略设置。

### 示例 2：从指定的注册表键中获取所有组策略值

```powershell
Get-GPRegistryValue -Name "TestGPO" -Key "HKCU\Software\Policies\Microsoft\ExampleKey"
```

```Output
KeyPath     : Software\Policies\Microsoft\ExampleKey
FullKeyPath : HKEY_CURRENT_USER\Software\Policies\Microsoft\ExampleKey
Hive        : CurrentUser
PolicyState : Set
Value       : TestGPO
Type        : String
ValueName   : ValueOne
HasValue    : True

KeyPath     : Software\Policies\Microsoft\ExampleKey
FullKeyPath : HKEY_CURRENT_USER\Software\Policies\Microsoft\ExampleKey
Hive        : CurrentUser
PolicyState : Delete
Value       :
Type        : String
ValueName   : ValueTwo
HasValue    : True


KeyPath     : Software\Policies\Microsoft\ExampleKey\Subkey1
FullKeyPath : HKEY_CURRENT_USER\Software\Policies\Microsoft\ExampleKey\Subkey1
Hive        : CurrentUser

KeyPath     : Software\Policies\Microsoft\ExampleKey\SubKey2
FullKeyPath : HKEY_CURRENT_USER\Software\Policies\Microsoft\ExampleKey\SubKey2
Hive        : CurrentUser
```

这个命令会从名为“TestGPO”的组策略对象（GPO）中的“用户配置”部分，获取所有基于注册表的策略设置。这些策略设置用于配置位于 `HKEY_CURRENT_USER\Software\Policies\Microsoft\ExampleKey` 键下的注册表值。该键的所有子键中包含的基于注册表的策略设置也会被一并返回。其中第二个基于注册表的策略设置（ValueTwo）已被禁用（其 **PolicyState** 属性被设置为 “Delete”）。

## 参数

### -Domain

指定此 cmdlet 的域。您必须提供该域的完全限定域名（FQDN），例如：sales.contoso.com。

对于 `Get-GPRegistryValue` cmdlet 来说，需要获取基于注册表策略设置的 GPO 必须存在于该域中。

如果您没有指定 **Domain** 参数，那么将使用当前会话所运行的用户的域信息。如果该 cmdlet 是通过计算机启动或关闭脚本来执行的，那么将使用计算机的域信息。有关更多详细信息，请参阅完整帮助文档中的“注释”部分。

如果您指定的域名与当前会话所使用的用户的域名不同（或者对于启动/关闭脚本来说，是与计算机相关的域名不同），那么该域名与用户或计算机的域名之间必须存在信任关系。

您也可以使用该域的内置别名 **DomainName** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

通过其全局唯一标识符（GUID）指定要从哪个组策略对象（GPO）中检索基于注册表的策略设置。该 GUID 可唯一地标识该 GPO。

您也可以使用 **Guid** 参数的内置别名 **Id** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

指定此cmdlet获取基于注册表的策略设置的注册表键。例如：`HKLM\Software\Policies\Microsoft\Windows NT\DNSClient`。

该密钥必须位于以下两个注册表项之一中：

- HKEY_LOCAL_MACHINE (HKLM) for a registry-based policy setting in Computer Configuration.

- HKEY_CURRENT_USER (HKCU) for a registry-based policy setting in User Configuration.

您可以指定：

- The **Key** parameter without the **ValueName** parameter to get all the registry-based policy
  settings that configure values directly under that key.

- The Key parameter together with the **ValueName** parameter to get the registry-based policy
  setting that configures a specific registry value.

您也可以使用内置别名 `FullKeyPath` 来引用 `Key` 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

指定此cmdlet根据其显示名称从哪个GPO中获取基于注册表的策略设置。

显示名称在域中并不保证是唯一的。如果域中存在另一个具有相同显示名称的组策略对象（GPO），则会出现错误。你可以使用 **Guid** 参数来唯一标识一个 GPO。

您也可以使用其内置别名 **DisplayName** 来引用 **Name** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

### -Server

指定此cmdlet用于联系以完成操作的域控制器的名称。您可以指定完全合格的域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系主域控制器（Primary Domain Controller，简称 PDC）的仿真器。

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

指定一个注册表值的名称，该 cmdlet 会从这个注册表值中获取基于注册表的策略设置。例如，注册表键 `HKLM\Software\Policies\Microsoft\Windows NT\DNSClient` 可以包含一个名为 `UseDomainNameDevolution` 的值。对于注册表键的默认值，请指定“(default)”或空字符串 (“”)。

您还必须使用这个参数来指定**Key**参数。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.GroupPolicy.Gpo

您可以将需要获取基于注册表策略设置的 GPO 传递给此 cmdlet。不支持包含来自不同域的 GPO 的集合。

## 输出

### Microsoft.GroupPolicy.PolicyRegistrySetting

此cmdlet返回**PolicyRegistrySetting**对象，这些对象表示基于注册表的策略设置。这些对象可以传递给以下cmdlets：

- `Set-GPRegistryValue`

- `Remove-GPRegistryValue`

## 备注

* The hive of the registry key that you specify (HKLM or HKCU) indicates whether the registry-based
  policy setting is retrieved from Computer Configuration or User Configuration.

如果在策略中找不到指定的注册表键（即该注册表键未被配置），则会显示相应的错误消息。

你可以使用 **Domain** 参数来明确指定此 cmdlet 的域名。

如果您没有明确指定域名，该 cmdlet 会使用默认域名。默认域名是指当前会话运行的安全上下文用于访问网络资源所使用的域名。这个域名通常就是启动该会话的用户所在的域名（例如，通过打开 Windows PowerShell 启动会话的用户所属的域名，或者在 runas 命令中指定的用户所属的域名）。然而，计算机启动和关闭脚本是在 LocalSystem 账户的上下文中运行的。LocalSystem 是一个内置的本地账户，它以计算机账户的身份来访问网络资源。因此，当从这个启动或关闭脚本中运行该 cmdlet 时，默认域名就是计算机所加入的域名称。

## 相关链接

[Remove-GPRegistryValue](./Remove-GPRegistryValue.md)

[Set-GPRegistryValue](./Set-GPRegistryValue.md)

