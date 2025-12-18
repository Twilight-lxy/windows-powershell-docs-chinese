---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/set-appxdefaultvolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AppxDefaultVolume
---

# 设置 AppX 的默认音量

## 摘要
指定一个默认的 AppX 容量（volume）。

## 语法

```
Set-AppxDefaultVolume [-Volume] <AppxVolume> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Set-AppxDefaultVolume` cmdlet 用于指定一个默认的 **AppxVolume**。这个默认的 **AppxVolume** 是该计算机上所有部署操作的默认目标。不过，部署操作也可以指定其他非默认的目标卷。

## 示例

### 示例 1：通过使用路径来设置默认音量

```powershell
Set-AppxDefaultVolume -Volume F:\
```

这个命令将默认卷设置为`F:\`卷。

### 示例 2：使用 ID 设置默认音量

```powershell
Set-AppxDefaultVolume -Volume {ef23c8d6-b13c-4c4c-ae3b-7d5a162de9b9}
```

这个命令将默认音量设置为具有指定媒体ID的那个音量。

## 参数

### -Volume

指定卷的路径。此cmdlet会将此参数指定的卷设置为计算机的默认部署目标。

```yaml
Type: AppxVolume
Parameter Sets: (All)
Aliases:

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

展示了如果该cmdlet运行会发生的结果。但实际上，该cmdlet并没有被执行。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-AppxDefaultVolume](./Get-AppxDefaultVolume.md)
