---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/get-appxdefaultvolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppxDefaultVolume
---

# Get-AppxDefaultVolume

## 摘要
获取默认的 AppX 文件音量设置。

## 语法

```
Get-AppxDefaultVolume [<CommonParameters>]
```

## 描述

`Get-AppxDefaultVolume` cmdlet 用于获取默认的 **AppxVolume**。默认的 **AppxVolume** 是该计算机上所有部署操作的默认目标位置。您无法将默认的 **AppxVolume** 从卷列表中删除。

## 示例

### 示例 1：获取默认音量

```powershell
Get-AppxDefaultVolume
```

这个命令用于获取当前的默认部署目标。

## 参数

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.AppxPackageManager Commands.AppxVolume

## 备注

## 相关链接

[Set-AppxDefaultVolume](./Set-AppxDefaultVolume.md)
