---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/get-appxvolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppxVolume
---

# Get-AppxVolume

## 摘要
获取计算机的 AppX 容量信息。

## 语法

### DefaultParameterSet

```
Get-AppxVolume [[-Path] <String>] [<CommonParameters>]
```

### OnlineParameterSet

```
Get-AppxVolume [[-Path] <String>] [-Online] [<CommonParameters>]
```

### OfflineParameterSet

```
Get-AppxVolume [[-Path] <String>] [-Offline] [<CommonParameters>]
```

## 描述

`Get-AppxVolume` cmdlet 可以获取计算机上已知的所有 **AppxVolume** 对象的列表。这些卷可以由用户或设备添加，例如通过使用 Storage Sense 功能来添加。

## 示例

### 示例 1：获取所有卷

```powershell
Get-AppxVolume
```

该命令会获取计算机上所有的 **AppxVolume** 对象。

### 示例 2：获取指定路径下的文件体积（即文件大小）

```powershell
Get-AppxVolume -Path F:\
```

这个命令会获取位于路径 F:\ 下的 **AppxVolume** 文件。

#### 示例 3：获取已挂载的卷

```powershell
Get-AppxVolume -Online
```

该命令仅获取当前已挂载在计算机上的 **AppxVolume** 对象。

### 示例 4：获取未挂载的卷

```powershell
Get-AppxVolume -Offline
```

这个命令用于获取那些当前没有挂载到计算机上的 **AppxVolume** 对象。

## 参数

### -Offline

表示此cmdlet仅返回当前已卸载的卷。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: OfflineParameterSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Online

表示此 cmdlet 仅返回当前已挂载的卷。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: OnlineParameterSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

指定卷的挂载点的路径。此cmdlet会获取位于该参数所指定位置的卷。

```yaml
Type: String
Parameter Sets: DefaultParameterSet
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: OnlineParameterSet, OfflineParameterSet
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters

此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.AppxPackageManager.Commands.AppxVolume

## 备注

## 相关链接

[Add-AppxVolume](./Add-AppxVolume.md)

[Dismount-AppxVolume](./Dismount-AppxVolume.md)

[Mount-AppxVolume](./Mount-AppxVolume.md)

[Remove-AppxVolume](./Remove-AppxVolume.md)
