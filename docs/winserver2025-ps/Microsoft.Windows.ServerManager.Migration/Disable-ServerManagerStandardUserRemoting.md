---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ServerManager-help.xml
Module Name: Microsoft.Windows.ServerManager.Migration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.servermanager.migration/disable-servermanagerstandarduserremoting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-ServerManagerStandardUserRemoting
---

# 禁用 ServerManagerStandardUserRemoting 功能

## 摘要
禁止指定的标准用户访问由服务器管理器为某台服务器收集的事件数据、服务信息、性能计数器数据以及角色和功能清单数据。

## 语法

```
Disable-ServerManagerStandardUserRemoting [-User] <String[]> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-ServerManagerStandardUserRemoting` cmdlet 可以禁止一个或多个非管理员用户（即普通用户）通过 Server Manager 访问服务器的事件数据、服务信息、性能计数器以及角色和功能清单。该 cmdlet 对指定用户的操作效果与 `Enable-ServerManagerStandardUserRemoting` cmdlet 的作用相反（即取消之前允许的访问权限）。

该cmdlet会恢复对该数据的默认访问权限（仅限管理员使用），并且必须在使用Server Manager管理的服务器上本地运行。该cmdlet通过执行以下操作来实现其功能：

- Deletes access rights for specified standard users to the root\cimv2 namespace on the local server (for access to role and feature inventory information).
- Removes specified standard users from user groups (Remote Management Users, Event Log Readers, and Performance Log Readers) that allow remote access to event and performance counter logs on the local server.
- Removes access rights in the Service Control Manager for specified standard users who have access to the status of services on the local server.

## 示例

#### 示例 1：禁止用户访问事件数据、性能计数器信息、服务状态以及角色和功能清单数据
```
PS C:\> Disable-ServerManagerStandardUserRemoting -User "PattiFul"
```

该命令会禁用对由本地或远程服务器管理器控制的服务的事件数据、性能计数器数据、服务状态数据以及角色和功能清单数据的访问权限。该服务的标准用户名为“PattiFul”。

### 示例 2：模拟禁用用户对事件、性能计数器、服务状态以及角色和功能清单数据的访问所带来的结果
```
PS C:\> Disable-ServerManagerStandardUserRemoting -User "EvanNar" -WhatIf
```

此命令用于查看执行相关操作的结果：该操作旨在拒绝名为 EvanNar 的普通用户访问由服务器管理器（Server Manager）控制的服务的相关数据，包括事件记录、性能计数器信息、服务状态以及角色和功能清单等。服务器管理器可以运行在本地计算机或远程计算机上。由于使用了 “WhatIf” 参数，因此实际并不会执行任何操作（即不会真正拒绝 EvanNar 的访问权限）。

### 示例 3：禁止用户访问事件数据、性能计数器数据、服务状态信息以及角色和功能清单数据
```
PS C:\> Disable-ServerManagerStandardUserRemoting -User "PattiFul" -Confirm
```

此命令禁止名为 PattiFul 的标准用户访问由服务器管理器控制台管理的服务器的事件、性能计数器、服务状态以及角色和功能清单数据。该控制台可以运行在本地计算机或远程计算机上。由于使用了 *Confirm* 参数，因此在执行操作之前系统会提示用户进行确认。

## 参数

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需请求用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -User
指定一组标准用户的账户名称，这些用户正在运行 Server Manager。对于通过本地或远程 Server Manager 控制台管理的服务器而言，他们不再需要访问与该服务器相关的事件数据、性能计数器数据、服务信息以及角色和功能清单数据。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-WindowsFeature](./Get-WindowsFeature.md)

[Install-WindowsFeature](./Install-WindowsFeature.md)

[卸载Windows功能](./Uninstall-WindowsFeature.md)

[Enable-ServerManagerStandardUserRemoting](./Enable-ServerManagerStandardUserRemoting.md)

