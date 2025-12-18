---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.Modernizer.Cmdlets.dll-Help.xml
Module Name: AppvSequencer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvsequencer/new-appvsequencerpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AppvSequencerPackage
---

# New-AppvSequencerPackage

## 摘要
创建一个新的App-V包。

## 语法

### 使用 ByInstallerFullLoad（默认设置）
```
New-AppvSequencerPackage [-FullLoad] [-Installer] <String[]> [-InstallerOptions <String[]>]
 [[-PrimaryVirtualApplicationDirectory] <String>] [-Name] <String> [-Path] <String>
 [-TemplateFilePath <String>] [<CommonParameters>]
```

### ByPackageAcceleratorInstallMedia
```
New-AppvSequencerPackage [-AcceleratorFilePath] <String> [-InstallMediaPath] <String> [-Name] <String>
 [-Path] <String> [<CommonParameters>]
```

### ByPackageAcceleratorInstalledFiles
```
New-AppvSequencerPackage [-AcceleratorFilePath] <String> [-InstalledFilesPath] <String> [-Name] <String>
 [-Path] <String> [<CommonParameters>]
```

## 描述
`New-AppvSequencerPackage` cmdlet 可用于创建一个新的 Microsoft 应用虚拟化 (App-V) 包。该 cmdlet 可以使用安装程序、App-V 加速器，或者带有已安装应用程序的加速器来生成新包。此外，它还接受一个模板文件，并提供了在运行包之前强制将整个包内容流式传输到目标计算机的选项。

## 示例

#### 示例 1：创建一个包
```
PS C:\> New-AppvSequencerPackage -Name "MyPackage" -OutputPath "C:\MyPackage" -PrimaryVirtualApplicationDirectory "C:\Program Files\MyApp" -Installer "C:\installers\MyApp\setup.exe"
```

这个命令为名为“MyApp”的应用程序创建了一个软件包。

### 示例 2：创建一个需要完整下载的包
```
PS C:\> New-AppvSequencerPackage -Name MyPackage2 -OutputPath C:\MyPackages -PrimaryVirtualApplicationDirectory "C:\Program Files\MyApp -Installer C:\installers\MyApp\setup.exe -FullLoad
```

此命令创建了一个软件包，需要将该软件包完全下载后才能使用名为“MyApp”的应用程序。

### 示例 3：使用预生成的加速器创建一个包
```
PS C:\> New-AppvSequencerPackage -Name "MyPackage" -OutputPath "C:\MyPackages" -AcceleratorFilePath "C:\MyAccelerators\MyAccelerator.cab" -PrimaryVirtualApplicationDirectory "C:\MyApp\" -InstalledMediaPath "C:\Installers\PreReq\" -Installer "C:\Installers\MyApp\setup.exe"
```

这个命令使用预先生成的安装包加速器来创建一个新的名为“MyApp”的安装包。

### 示例 4：使用模板文件创建一个软件包
```
PS C:\> New-AppvSequencerPackage -Name "MyPackage" -TemplateFilePath "C:\template.appvt" -OutputPath "C:\Packages\MyPackage" -PrimaryVirtualApplicationDirectory "C:\Program Files\MyApp" -Installer "C:\Installers\MyApp\setup.exe"
```

这个命令使用模板文件创建一个新的MyApp软件包。

## 参数

### -AcceleratorFilePath
指定该软件包对应的加速器文件的路径。如果加速器文件未经过签名，或者无法被Sequencer识别/接受，系统会返回错误信息。

```yaml
Type: String
Parameter Sets: ByPackageAcceleratorInstallMedia, ByPackageAcceleratorInstalledFiles
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FullLoad
表示在启动该软件包之前，必须先将其完整下载下来。

```yaml
Type: SwitchParameter
Parameter Sets: ByInstallerFullLoad
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InstalledFilesPath
指定已安装文件的位置，这些文件将用于借助 App-V Accelerator 创建一个新的 App-V 包。

```yaml
Type: String
Parameter Sets: ByPackageAcceleratorInstalledFiles
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Installer
指定一组MSI文件、安装程序或其他需要运行的可执行文件，这些文件用于创建App-V包。

```yaml
Type: String[]
Parameter Sets: ByInstallerFullLoad
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InstallerOptions
将一组安装程序命令行选项作为参数值指定，例如 `/quiet`、`/passive` 或 `/norestart`。

```yaml
Type: String[]
Parameter Sets: ByInstallerFullLoad
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InstallMediaPath
指定序列器所指向的安装介质的位置，并生成相应的加速器文件。

```yaml
Type: String
Parameter Sets: ByPackageAcceleratorInstallMedia
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定App-V包的名称。这也是序列化过程生成的所有文件的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定保存该软件包的文件夹位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases: OutputPath

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PrimaryVirtualApplicationDirectory
指定应用程序的安装位置。该路径必须位于本地计算机上。

```yaml
Type: String
Parameter Sets: ByInstallerFullLoad
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TemplateFilePath
指定用于此软件包的 App-V 包模板文件的路径。

```yaml
Type: String
Parameter Sets: ByInstallerFullLoad
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Expand-AppvSequencerPackage](./Expand-AppvSequencerPackage.md)

[New-AppvPackageAccelerator](./New-AppvPackageAccelerator.md)

[更新 AppvSequencerPackage](./Update-AppvSequencerPackage.md)

