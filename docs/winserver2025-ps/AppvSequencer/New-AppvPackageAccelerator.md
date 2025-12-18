---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.Modernizer.Cmdlets.dll-Help.xml
Module Name: AppvSequencer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvsequencer/new-appvpackageaccelerator?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AppvPackageAccelerator
---

# New-AppvPackageAccelerator

## 摘要
生成一个包加速器（package accelerator）。

## 语法

### 从安装程序（默认方式）
```
New-AppvPackageAccelerator [-InputPackagePath] <String> [-Installer] <String>
 [-AcceleratorDescriptionFile <String>] [-Path] <String> [<CommonParameters>]
```

### FromInstalledMedia
```
New-AppvPackageAccelerator [-InputPackagePath] <String> [-InstalledFilesPath] <String>
 [-AcceleratorDescriptionFile <String>] [-Path] <String> [<CommonParameters>]
```

## 描述
`New-AppvPackageAccelerator` cmdlet 用于生成一个包加速器对象。该 cmdlet 接受一个现有的应用程序虚拟化（App-V）5.0 包文件，以及已正确安装的文件或安装介质，然后生成一个新的包加速器文件。

## 示例

### 示例 1：创建一个软件包加速器
```
PS C:\> New-AppvPackageAccelerator -AppvPackageFilePath "C:\MyPackages\Package1\Package1.appv" -Installer "C:\MyPackages\Package1" -OutputPath "C:\Output\packages\Package1.cab"
```

这个命令使用一个安装程序文件夹来创建一个包加速器（package accelerator），该文件夹中可能包含例如 MSI 安装程序等文件。

### 示例 2：创建一个带有使用说明表的软件包加速器
```
PS C:\> New-AppvPackageAccelerator -AppvPackageFilePath "C:\MyPackages\Package1\Package1.appv" -InstalledFilesPath "C:\Program Files\Package1InstallFolder" -OutputPath "C:\Output\packages\Package1.cab" -AcceleratorDescriptionFilePath "C:\MyPackages\Package1\Package1Description.rtf"
```

这个命令会创建一个用于加速软件包发布的工具，并插入一份关于如何使用该工具来加快发布过程的说明书。

## 参数

### -AcceleratorDescriptionFile
指定软件包加速器描述文件。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputPackagePath
指定用于生成加速器的 App-V 包的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InstalledFilesPath
指定包含该软件包安装目录的文件夹路径，以便为其生成加速器文件。

```yaml
Type: String
Parameter Sets: FromInstalledMedia
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Installer
指定应用程序安装程序所在文件夹的路径，以便从中生成加速器文件。该安装程序必须采用 MSI、CAB 或 ZIP 格式。如果您没有这种格式的安装程序，请改用 *InstalledFilesPath* 参数。

```yaml
Type: String
Parameter Sets: FromInstaller
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定.cab包加速器输出文件的完整路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: OutputPath

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Expand-AppvSequencerPackage](./Expand-AppvSequencerPackage.md)

[更新 AppvSequencerPackage](./Update-AppvSequencerPackage.md)

