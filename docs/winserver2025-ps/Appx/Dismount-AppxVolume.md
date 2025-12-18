---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/dismount-appxvolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Dismount-AppxVolume
---

# 卸载 AppxVolume

## 摘要
卸载一个 appx 卷（即一个包含应用程序数据的文件）。

## 语法

```
Dismount-AppxVolume [-Volume] <AppxVolume[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Dismount-AppxVolume` cmdlet 用于卸载一个 **AppxVolume**。卸载卷后，所有部署到该目标上的应用程序都将无法访问。

## 示例

#### 示例 1：使用路径卸载卷

```powershell
Dismount-AppxVolume -Volume E:\
```

这个命令会卸载路径为 `E:\` 的卷。

### 示例 2：使用卷ID卸载卷

```powershell
Dismount-AppxVolume -Volume {7e62a691-398e-4fbe-819a-64f1e407777a}
```

此命令用于卸载具有指定媒体ID的卷。

## 参数

### -Volume

指定要卸载的 **AppxVolume** 对象。

```yaml
Type: AppxVolume[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Confirm

在运行该cmdlet之前，会提示您确认是否要继续执行。

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

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AppxVolume](./Add-AppxVolume.md)

[Get-AppxVolume](./Get-AppxVolume.md)

[Mount-AppxVolume](./Mount-AppxVolume.md)

[Remove-AppxVolume](./Remove-AppxVolume.md)
