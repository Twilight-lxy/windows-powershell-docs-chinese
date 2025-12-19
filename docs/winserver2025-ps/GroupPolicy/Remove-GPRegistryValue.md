---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/remove-gpregistryvalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-GPRegistryValue
---

# 删除GPRegistry值

## 摘要

从GPO中的“计算机配置”或“用户配置”中删除一个或多个基于注册表的策略设置。

## 语法

### GetByGUID（默认值）

```
Remove-GPRegistryValue [-Guid] <Guid> [-Key] <String> [[-ValueName] <String>] [[-Domain] <String>]
 [[-Server] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### GetByName

```
Remove-GPRegistryValue [-Name] <String> [-Key] <String> [[-ValueName] <String>] [[-Domain] <String>]
 [[-Server] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-GPRegistryValue` cmdlet 可以从组策略对象（GPO）中的“计算机配置”或“用户配置”部分删除一个或多个基于注册表的策略设置。您可以通过显示名称或 GUID 来指定该 GPO。

你可以指定键（key）或值（value）中的任意一个：

- If you specify a key, registry-based policy settings that configure any of its first-level values
  are removed. However, if there are registry-based policy settings that configure any subkeys or
  their values, an error occurs and no policy settings are removed, including those for first-level
  values of the key. For a key, specify the **Key** parameter without the *ValueName* parameter.

- If you specify a value, the registry-based policy setting that configures that registry value is
  removed. For a value, specify the **Key** parameter without the *ValueName* parameter.

这个cmdlet可以从管道中接收输入数据：

- You can pipe GPO objects to this cmdlet to remove a specified registry-based policy setting from
  one or more GPOs.

- You can pipe **PolicyRegistrySetting** objects to this cmdlet to remove one or more registry-based
  policy settings from a specified GPO.

## 示例

### 示例 1：删除指定注册表键下的基于注册表的策略设置

```powershell
$params = @{
    Name      = 'TestGPO'
    Key       = 'HKCU\Software\Policies\Microsoft\Windows\Control Panel\Desktop'
    ValueName = 'ScreenSaveTimeOut'
}
Remove-GPRegistryValue @params
```

```Output
DisplayName      : TestGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 35c12ab3-956c-45d5-973b-46b17d225f47
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/24/2009 4:41:03 PM
ModificationTime : 2/25/2009 12:45:52 PM
UserVersion      : AD Version: 4, SysVol Version: 4
ComputerVersion  : AD Version: 34, SysVol Version: 34
WmiFilter        :
```

此命令会从名为“TestGPO”的组策略对象（GPO）中删除与注册表值`HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Control Panel\Desktop ScreenSaveTimeout`相关的注册表策略设置。当该GPO应用于客户端时，该注册表值将不再被修改。不过，删除策略设置并不会从客户端上删除相应的注册表值。如果希望在GPO应用于客户端时也删除该注册表值，必须使用`Set-GPRegistryValue` cmdlet来禁用该策略设置。

### 示例 2：删除指定注册表键下的所有基于注册表的策略设置

```powershell
Remove-GPRegistryValue -Name "TestGPO" -Key "HKCU\Software\Policies\Microsoft\ExampleKey"
```

此命令会从名为 `TestGPO` 的组策略对象（GPO）的 “用户配置” 部分中，删除所有基于注册表的策略设置。这些策略设置用于配置位于键 `HKEY_CURRENT_USER\Software\Policies\Microsoft\ExampleKey` 下的一级注册表值。如果 “用户配置” 中存在其他基于注册表的策略设置（它们用于配置该键的子键对应的注册表值），则会导致错误发生，此时将不会有任何一级策略设置被删除。

## 参数

### -Confirm

在运行cmdlet之前，会提示您进行确认。

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

对于 `Remove-GPRegistryValue` cmdlet 来说，要从中删除基于注册表的策略设置的 GPO 必须存在于该域中。

如果您没有指定 **Domain** 参数，将使用当前会话所运行的用户的域名。如果该 cmdlet 是从计算机启动或关闭脚本中运行的，则将使用计算机的域名。有关更多信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域与当前会话所使用的用户的域不同（或者对于启动/关闭脚本来说，是与计算机所在的域不同），那么该域与用户或计算机所在域之间必须存在信任关系。

您也可以使用其内置别名 **DomainName** 来引用 **Domain** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DomainName

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Guid

通过其全局唯一标识符（GUID）指定要从其中删除基于注册表的策略设置的组策略对象（GPO）。该 GUID 可唯一地识别该 GPO。

您也可以通过其内置别名 **Id** 来引用 **Guid** 参数。

```yaml
Type: Guid
Parameter Sets: GetByGUID
Aliases: Id

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Key

指定一个注册表键，以便从中删除一个或多个基于注册表的策略设置（例如：`HKLM\Software\Policies\Microsoft\WindowsNT\DNSClient\UseDomainNameDevolution`）。

该密钥必须存在于以下两个注册表 hive 之一中：

- `HKEY_LOCAL_MACHINE` (HKLM) for a registry-based policy setting in Computer Configuration.

- `HKEY_CURRENT_USER` (HKCU) for a registry-based policy setting in User Configuration.

`Key` 参数可以单独指定，也可以与 `ValueName` 参数一起指定：

- If the **ValueName** parameter is specified, the registry-based policy setting that configures
  that registry value is removed.

- If the **ValueName** parameter is not specified, all registry-based policy settings that configure
  any of the first-level values of the registry key are removed. If there are registry-based policy
  settings that configure any subkeys or their values, an error occurs.

您也可以使用其内置别名 FullKeyPath 来引用 Key 参数。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: FullKeyPath

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

根据显示名称指定要从其中删除基于注册表的策略设置的组策略对象（GPO）。

显示名称在该域中并不保证是唯一的。如果该域中存在另一个具有相同显示名称的组策略对象（GPO），则会发生错误。您可以使用 **Guid** 参数来唯一标识一个 GPO。

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

### -Server

指定此cmdlet用于联系的域控制器的名称，以便完成操作。您可以指定完整的域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系主域控制器（PDC）仿真器。

您也可以通过其内置别名“DC”来引用**Server**参数。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DC

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ValueName

指定要删除基于注册表的策略设置的注册表值的名称。如果您指定了**ValueName**参数，则还必须指定**Key**参数。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
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

此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft(GroupPolicy.Gpo)

### Microsoft.GroupPolicy.PolicyRegistrySetting

你可以使用管道操作（pipe）来获取一个GPO，然后从中移除基于注册表的策略设置；或者直接使用一个表示基于注册表策略设置的**PolicyRegistrySetting**对象。不支持包含来自不同域的GPO的集合。

## 输出

### Microsoft(GroupPolicy.Gpo)

此cmdlet返回了从中删除了基于注册表的策略设置（或多个设置）的GPO（组策略对象）。

## 备注

* The hive of the registry key that you specify -- `HKEY_LOCAL_MACHINE` (HKLM) or
  `HKEY_CURRENT_USER` (HKCU) indicates whether the registry-based policy setting is removed from
  Computer Configuration or User Configuration.

如果找不到注册表键的值（即该注册表键未被配置），或者存在子键，就会发生错误，并显示相应的错误消息。

你可以使用 **Domain** 参数来明确指定此 cmdlet 的域名。

如果您没有明确指定域名，该 cmdlet 会使用默认域名。默认域名是指当前会话所运行的安全上下文用于访问网络资源的那个域名。这个域名通常就是启动该会话的用户所在的域；例如，通过“程序文件”菜单打开 Windows PowerShell 启动会话的用户所属的域，或者在 `runas` 命令中指定的用户所属的域。然而，计算机启动和关闭脚本是在 `LocalSystem` 账户的上下文中运行的。`LocalSystem` 是一个内置的本地账户，它以计算机的身份来访问网络资源。因此，当从这个启动或关闭脚本中运行该 cmdlet 时，默认域名就是计算机所加入的那个域。

## 相关链接

[Get-GPRegistryValue](./Get-GPRegistryValue.md)

[Set-GPRegistryValue](./Set-GPRegistryValue.md)
