---
description: 从一个或多个用户账户中删除应用程序包。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/remove-appxpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AppxPackage
---

# 删除 Appx 包

## 摘要
从一个或多个用户账户中删除应用程序包。

## 语法

### RemoveByPackageSet（默认值）

```
Remove-AppxPackage [-Package] <String> [-PreserveApplicationData] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 使用 `RemoveByPackageForRoamingSet` 方法

```
Remove-AppxPackage [-Package] <String> [-PreserveRoamableApplicationData] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### AllUsersSet

```
Remove-AppxPackage [-Package] <String> [-AllUsers] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### UserSet

```
Remove-AppxPackage [-Package] <String> -User <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-AppxPackage` cmdlet 用于从用户账户中删除应用程序包。应用程序包的文件扩展名为 `.msix` 或 `.appx`。

## 示例

#### 示例 1：删除应用程序包

```powershell
Remove-AppxPackage -Package 'package1_1.0.0.0_neutral__8wekyb3d8bbwe'
```

此命令会从当前用户的账户中删除名为 `package1_1.0.0.0_neutral__8wekyb3d8bbwe` 的应用程序包。

## 参数

### -AllUsers

此参数会删除计算机上所有用户账户的应用程序包。该参数的生效依赖于父包类型；如果应用程序是以“捆绑包”（bundle）的形式存在的，需要使用 `Get-AppxPackage` 命令并结合 `PackageTypeFilter` 来指定相应的捆绑包。要使用此参数，必须以管理员权限运行该命令。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AllUsersSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

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

### -Package

指定一个 **AppxPackage** 对象或包的全名。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf

展示了如果该cmdlet被运行会发生的情景。但实际上，这个cmdlet并没有被运行。

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

### -PreserveApplicationData

该选项指定 cmdlet 在删除软件包时保留应用程序数据。这些数据可供后续使用。请注意，此功能仅适用于正在开发中的应用程序，因此只有通过文件布局方式注册的应用程序（即“松散文件格式”下的应用程序）才能设置此选项。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: RemoveByPackageSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PreserveRoamableApplicationData

在删除应用程序包时，保留应用程序数据中可跨设备使用的部分。此参数与 **PreserveApplicationData** 不兼容。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: RemoveByPackageForRoamingSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -User

如果您指定了此参数，该cmdlet将仅删除指定用户的应用程序包。如果要为当前用户之外的其他用户配置文件删除软件包，则必须以管理员权限运行此命令。

> [!注意] >> 该参数仅接受用户的SID（Security Identifier）。可以使用 **whoami /user** 命令来显示当前用户的SID。详情请参阅 [whoami 语法](/windows-server/administration/windows-commands/whoami)。

```yaml
Type: System.String
Parameter Sets: UserSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Windows.AppxPackageManagercommands.AppxPackage

一个 `AppxPackage` 对象，其中包含各种信息，包括应用程序包的完整名称。

## 输出

### 无

## 备注

## 相关链接

[PackageManager 类](https://go.microsoft.com/fwlink/?LinkId=245447)

[使用 DISM 侧载应用程序](https://go.microsoft.com/fwlink/?LinkID=231020)
