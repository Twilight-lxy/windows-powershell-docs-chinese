---
description: 将Windows应用程序恢复到其初始配置状态。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/reset-appxpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Reset-AppxPackage
---

# 重置 AppxPackage

## 摘要

将Windows应用程序恢复到其初始配置状态。

## 语法

```
Reset-AppxPackage
 [-Package] <string>
 [-WhatIf]
 [-Confirm]
 [<CommonParameters>]
```

## 描述

`Reset-AppxPackage` cmdlet 将应用程序恢复到其原始设置，此时该应用程序的表现将如同刚刚安装过一样。

在重置应用程序后，应用程序会首次提示用户进行输入操作。

## 示例

### 示例 1：重置应用程序包

```powershell
Reset-AppxPackage -Package publisher.package1_1.0.0.0_neutral__8wekyb3d8bbwe
```

这个cmdlet会将`publisher.package1_1.0.0.0_neutral__8wekyb3d8bbwe`应用程序重置回其原始设置。

## 参数

### -Confirm

在运行 cmdlet 之前会提示您确认是否要执行该操作。

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

### -Package

指定需要重置的应用程序的完整包名（Package Full Name，简称PFuN）。

```yaml
Type: System.String
Parameter Sets: None
Aliases: None

Required: True
Position: 0
Default value: None
Accept pipeline input: True
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### System.IO.FileInfo

## 输出

### 无

## 备注

## 相关链接

[包管理器 API](http://go.microsoft.com/fwlink/?LinkId=245447)

[如何添加和删除应用程序](http://go.microsoft.com/fwlink/?LinkID=231020)

[Get-AppxPackage](./Get-AppxPackage.md)

[Get-AppxPackageManifest](./Get-AppxPackageManifest.md)

[Move-AppxPackage](./Move-AppxPackage.md)

[Remove-AppxPackage](./Remove-AppxPackage.md)
