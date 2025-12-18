---
description: 提供了关于如何配置 Windows 应用程序的自动更新和修复设置的指导。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/reset-appxpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AppxPackageAutoUpdateSettings
---

# 设置 AppX 包的自动更新设置

## 摘要

配置特定Windows应用程序的自动更新和修复设置。

## 语法

### SetAutoUpdateOptionsSet（默认值）

```
Set-AppxPackageAutoUpdateSettings [-PackageFamilyName] <String> -AppInstallerUri <String>
 [-UpdateUris <String[]>] [-RepairUris <String[]>] [-OptionalPackages <String[]>]
 [-DependencyPackages <String[]>] [-EnableAutomaticBackgroundTask] [-ForceUpdateFromAnyVersion]
 [-DisableAutoRepairs] [-CheckOnLaunch] [-ShowPrompt] [-UpdateBlocksActivation]
 [-UseSystemPolicySource] [-HoursBetweenUpdateChecks <UInt32>] [-Version <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### PauseAutoUpdateOptionsSet

```
Set-AppxPackageAutoUpdateSettings [-PackageFamilyName] <String> [-PauseUpdates]
 [-UseSystemPolicySource] -HoursToPause <UInt32> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Set-AppxPackageAutoUpdateSettings` cmdlet 允许您配置特定 Windows 应用的自动更新和修复设置。

## 示例

### 示例 1：更新某个应用的自动更新设置

```powershell
$params = @{
    AppInstallerUri           =  'https://website.com/PackageName.appinstaller '
    PackageFamilyName         =  'PackageName_8h66172c634n0 '
    CheckOnLaunch             =  $true
    ForceUpdateFromAnyVersion =  $true
    HoursBetweenUpdateChecks  =  2
    ShowPrompt                =  $true
    UpdateUris                =  'file://ComputerName/Share/PackageName_x64.appinstaller'
}
Set-AppxPackageAutoUpdateSettings @params
```

这个 cmdlet 会更新 `PackageName_8h66172c634n0` 这个 Windows 应用的自动更新设置，使其每两小时从网络上可访问的文件共享位置下载应用程序安装文件（AppInstaller 文件），同时向用户显示提示信息。这样一来，无论当前安装的 Windows 应用版本如何，该应用都可以更新到任何其他版本的软件（无论是更高版本还是更低版本）。

### 示例 2：禁用某个应用程序的自动修复功能

```powershell
$params = @{
    AppInstallerUri    = 'https://website.com/PackageName.appinstaller'
    PackageFamilyName  = 'PackageName_8h66172c634n0'
    DisableAutoRepairs = $true
}
Set-AppxPackageAutoUpdateSettings @params
```

这个cmdlet会禁用Windows应用程序的自动修复功能。

### 示例 3：暂停特定 Windows 应用的更新

```powershell
$params = @{
    HoursToPause      = 4320
    PackageFamilyName = 'PackageName_8h66172c634n0'
    PauseUpdates      = $true
}
Set-AppxPackageAutoUpdateSettings @params
```

此cmdlet将暂停Windows应用程序检查应用更新的功能，持续时间长达4320小时（即180天）。

## 参数

### -HoursToPause

指定Windows应用程序在多少小时内不会检查更新。时间以小时为单位。

```yaml
Type: System.UInt32
Parameter Sets: PauseAutoUpdateOptionsSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PauseUpdates

指定是否需要暂停Windows应用程序的更新。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: PauseAutoUpdateOptionsSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PackageFamilyName

指定正在修改的Windows应用程序的包系列名称（Package Family Name）。

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

### -AppInstallerUri

指定此Windows应用程序所针对的AppInstaller文件的位置。

```yaml
Type: System.String
Parameter Sets: SetAutoUpdateOptionsSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CheckOnLaunch

该设置表示：当Windows应用程序启动时，会自动检查是否有新的更新可用。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: SetAutoUpdateOptionsSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DependencyPackages

指定Windows应用程序所使用的任何依赖包（Dependency Packages）。

```yaml
Type: System.String[]
Parameter Sets: SetAutoUpdateOptionsSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableAutoRepairs

关闭对损坏的Windows应用程序进行自动修复的功能。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: SetAutoUpdateOptionsSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableAutomaticBackgroundTask

指定更新和修复的自动化操作将以后台任务的形式进行。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: SetAutoUpdateOptionsSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ForceUpdateFromAnyVersion

指定Windows应用程序的下一次更新可以是更高版本，也可以是更低版本。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: SetAutoUpdateOptionsSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HoursBetweenUpdateChecks

指定特定 Windows 应用程序允许在两次更新检查之间的时间间隔。

```yaml
Type: System.UInt32
Parameter Sets: SetAutoUpdateOptionsSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OptionalPackages

指定Windows应用程序所使用的可选软件包（Optional Packages）。

```yaml
Type: System.String[]
Parameter Sets: SetAutoUpdateOptionsSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RepairUris

指定在修复Windows应用程序时将从中获取资源的位置。

```yaml
Type: System.String[]
Parameter Sets: SetAutoUpdateOptionsSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ShowPrompt

指定如果Windows应用程序有任何操作发生，将会显示一个提示框。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: SetAutoUpdateOptionsSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UpdateBlocksActivation

该规定指出：如果某个Windows应用程序有可用的更新版本，那么在更新安装完成之前，该应用程序将无法被启动。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: SetAutoUpdateOptionsSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UpdateUris

指定在更新 Windows 应用程序时将从中获取资源的位置。

```yaml
Type: System.String[]
Parameter Sets: SetAutoUpdateOptionsSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseSystemPolicySource

指定可以对开发者配置的设置进行覆盖（即修改原有的设置）。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Version

指定所应用的“更新设置”（Update Settings）的版本号。

```yaml
Type: System.String
Parameter Sets: SetAutoUpdateOptionsSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[包管理器 API](http://go.microsoft.com/fwlink/?LinkId=245447)

[如何添加和删除应用程序](http://go.microsoft.com/fwlink/?LinkID=231020)

[Get-AppxPackage](Get-AppxPackage.md)

[Get-AppxPackageManifest](Get-AppxPackageManifest.md)

[Move-AppxPackage](Move-AppxPackage.md)

[Remove-AppxPackage](Remove-AppxPackage.md)
