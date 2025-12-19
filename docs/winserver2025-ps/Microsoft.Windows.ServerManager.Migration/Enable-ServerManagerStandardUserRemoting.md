---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ServerManager-help.xml
Module Name: Microsoft.Windows.ServerManager.Migration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.servermanager.migration/enable-servermanagerstandarduserremoting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-ServerManagerStandardUserRemoting
---

# 启用 ServerManagerStandardUserRemoting 功能

## 摘要
通过使用 Server Manager，允许一个或多个标准的非管理员用户访问您所管理的服务器的事件、服务、性能计数器以及角色和功能清单数据。

## 语法

```
Enable-ServerManagerStandardUserRemoting [-User] <String[]> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-ServerManagerStandardUserRemoting` cmdlet 允许一个或多个非管理员用户（即普通用户）通过 Server Manager 访问你所管理的服务器的事件数据、服务信息、性能计数器数据，以及角色和功能的配置信息。该 cmdlet 必须在你要管理的服务器上本地运行。其工作原理如下：

- Adds access rights for specified standard users to the root\cimv2 namespace on the local server (for access to role and feature inventory information).
- Adds specified standard users to required user groups (Remote Management Users, Event Log Readers, and Performance Log Readers) that allow remote access to event and performance counter logs on the managed server.
- Changes access rights in the Service Control Manager to allow specified standard users remote access to the status of services on the managed server.This cmdlet does not provide standard users access to bpa (BPA) results, or allow standard users to run BPA scans.
Aside from the preceding list of changes, this cmdlet provides no additional access that a standard user does not already have, by default, on managed servers.

运行此cmdlet会对您的网络环境产生安全影响，因为它会赋予指定的非管理员用户访问某些信息的权限。而这些信息默认情况下仅限于本地计算机上的Administrators组成员才能访问。该cmdlet允许访问root\cimv2命名空间中的其他WMI提供程序，但仅限于那些标准用户可以使用的提供程序。我们建议您仅在确实需要通过Server Manager将某个特定标准用户添加到能够访问远程服务器数据的用户列表中时才运行此cmdlet。此外，一旦这些用户不再需要这种访问权限，应立即运行`Disable-ServerManagerStandardUserRemoting`命令来取消他们的访问权限。

## 示例

### 示例 1：允许用户访问事件数据、性能计数器信息、服务状态以及角色和功能清单数据
```
PS C:\> Enable-ServerManagerStandardUserRemoting -User "PattiFul"
```

该命令允许名为“PattiFul”的普通用户访问由服务器管理器（Server Manager）本地或远程管理的服务器上的事件数据、性能计数器信息、服务状态以及角色和功能清单信息。

### 示例 2：在用户确认后，允许其访问事件数据、性能计数器数据、服务状态信息以及角色和功能清单数据
```
PS C:\> Enable-ServerManagerStandardUserRemoting -User "PattiFul" -Confirm
```

该命令允许名为 PattiFul 的普通用户访问服务器上的事件数据、性能计数器信息、服务状态以及角色和功能清单信息。这些服务器可以是通过 Server Manager 在本地或远程进行管理的。由于使用了“Confirm”参数，因此在执行操作之前系统会提示用户进行确认。

## 参数

### -Confirm
在运行cmdlet之前会提示您进行确认。

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
指定一组标准用户账户名称，这些用户运行服务器管理器（Server Manager），并且需要访问事件数据、性能计数器信息、服务详情以及远程服务器的角色和功能库存信息。这些远程服务器是通过本地服务器管理器控制台进行管理的。

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
展示了如果该cmdlet运行会发生什么情况。但实际上该cmdlet并没有被运行。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-WindowsFeature](./Get-WindowsFeature.md)

[Install-WindowsFeature](./Install-WindowsFeature.md)

[卸载Windows功能](./Uninstall-WindowsFeature.md)

[禁用 ServerManager 标准用户远程访问功能](./Disable-ServerManagerStandardUserRemoting.md)

