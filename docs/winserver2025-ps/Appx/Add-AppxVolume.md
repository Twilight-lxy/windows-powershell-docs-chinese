---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/add-appxvolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AppxVolume
---

# 添加 Appx 卷（Add-AppxVolume）

## 摘要
向包管理器中添加一个 AppX 文件（即应用程序安装文件）。

## 语法

```
Add-AppxVolume [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Add-AppxVolume` cmdlet 为包管理器添加一个用于广告宣传的 **AppxVolume**。添加该卷后，Appx 部署操作可以使用该卷作为目标。此 cmdlet 会返回所添加的卷的信息。请注意，**Path** 参数必须指定为一个驱动器字母后跟 `WindowsApps` 作为目录路径。如果不使用这种格式，可能会导致应用程序模型子系统或卷本身出现不一致的行为。有关更多信息，请参阅示例部分。

## 示例

### 示例 1：添加音量（volume）

```powershell
Add-AppxVolume -Path "E:\WindowsApps"
```

此命令将 `E:\WindowsApps` 这个文件夹添加到包管理器（Package Manager）中。

## 参数

### -Path

指定此 cmdlet 所添加的卷的挂载点的路径。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: PSPath

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.AppxPackageManagercommands.AppxVolume

此cmdlet会返回它所添加的**AppxVolume**对象。

## 备注

## 相关链接

[Dismount-AppxVolume](./Dismount-AppxVolume.md)

[Get-AppxVolume](./Get-AppxVolume.md)

[Mount-AppxVolume](./Mount-AppxVolume.md)

[Remove-AppxVolume](./Remove-AppxVolume.md)
