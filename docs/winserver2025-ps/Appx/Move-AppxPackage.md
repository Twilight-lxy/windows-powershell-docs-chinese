---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/move-appxpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Move-AppxPackage
---

# 移动 AppxPackage 文件

## 摘要
将一个包从当前位置移动到另一个 AppX 卷中。

## 语法

```
Move-AppxPackage [-Package] <String[]> [-Volume] <AppxVolume> [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Move-AppxPackage` cmdlet 将一个应用程序包从当前位置移动到另一个 **AppxVolume**。新的位置必须是一个包管理器能够识别的、并且已经挂载的卷。此外，该 cmdlet 还会将你的应用程序数据也移至指定的卷中。

## 示例

#### 示例 1：将一个包移动到由路径指定的卷中

```powershell
Move-AppxPackage -Package "package1_1.0.0.0_neutral__8wekyb3d8bbwe" -Volume F:\
```

这个命令会将名称指定的包移动到`F:\`卷中。此外，该cmdlet还会将你的应用程序数据一并移动过去。

### 示例 2：将一个包移动到由 ID 指定的卷中

```powershell
$params = @{
    Package = 'package1_1.0.0.0_neutral__8wekyb3d8bbwe'
    Volume  = '{d2a4d1f4-f45a-46f3-a419-160ab52af091}'
}
Move-AppxPackage @params
```

此命令将名称指定的包移动到具有指定媒体ID的卷上。此外，该cmdlet还会将你的应用程序数据一并转移过去。

## 参数

### -Package

指定一个 `AppxPackage` 对象或包的全名。此 cmdlet 会移动由该参数指定的包。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Volume

指定一个 **AppxVolume** 对象。该 cmdlet 会将软件包移动到由此参数指定的卷上。

```yaml
Type: AppxVolume
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Confirm

在运行cmdlet之前会提示您进行确认。

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

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AppxPackage](./Add-AppxPackage.md)

[Get-AppxPackage](./Get-AppxPackage.md)

[Remove-AppxPackage](./Remove-AppxPackage.md)
