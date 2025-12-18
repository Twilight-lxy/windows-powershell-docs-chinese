---
description: 提供了关于如何查看Windows应用程序的自动更新和修复设置的指导。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/Get-AppxPackageAutoUpdateSettings?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
---

# Get-AppxPackageAutoUpdateSettings

## 摘要

提供了对为特定 Windows 应用程序配置的设置的可见性（即让用户能够查看这些设置）。

## 语法

```
Get-AppxPackageAutoUpdateSettings [[-PackageFullName] <String>] [-ShowUpdateAvailability]
 [-AllUsers] [<CommonParameters>]
```

## 描述

`Get-AppxPackageAutoUpdateSettings` PowerShell cmdlet 可以返回为特定已安装的 Windows 应用程序或所有已安装的 Windows 应用程序配置的与自动更新和修复相关的设置。

## 示例

### 示例 1：获取所有应用程序包自动更新的设置

```powershell
Get-AppxPackageAutoUpdateSettings
```

这将返回设备上所有已配置和安装的Windows应用程序的自动更新及修复设置信息，这些应用程序都是为用户注册的。

### 示例 2：获取所有用户的应用包自动更新设置

```powershell
Get-AppxPackageAutoUpdateSettings -AllUsers
```

这将返回所有已配置和安装的Windows应用程序的自动更新和修复设置，这些设置适用于所有用户。

### 示例 3：获取单个应用包的自动更新设置

```powershell
Get-AppxPackageAutoUpdateSettings -PackageFullName publisher.package1_1.0.0.0_neutral__8wekyb3d8bbwe
```

这将返回已安装并注册到该登录用户的特定Windows应用程序的“自动更新”和“修复”设置。

### 示例 4：获取所有已安装的 Windows 应用程序的自动更新设置

```powershell
Get-AppxPackageAutoUpdateSettings -ShowUpdateAvailability
```

显示所有已安装的Windows应用程序的可用更新信息。

## 参数

### -PackageFullName

指定正在查询的应用程序的完整包名（Package Full Name）。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: True
```

### -ShowUpdateAvailability

用于指定显示特定Windows应用程序的可用更新信息。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -AllUsers

指定为所有用户显示已安装的所有Windows应用程序的自动更新和修复设置。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```


### CommonParameters

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.Management Automation.SwitchParameter

## 输出

### System.Object

## 备注

## 相关链接

[包管理器 API](http://go.microsoft.com/fwlink/?LinkId=245447)

[如何添加和删除应用程序](http://go.microsoft.com/fwlink/?LinkID=231020)

[Get-AppxPackage](./Get-AppxPackage.md)

[Get-AppxPackageManifest](./Get-AppxPackageManifest.md)

[Move-AppxPackage](./Move-AppxPackage.md)

[Remove-AppxPackage](./Remove-AppxPackage.md)
