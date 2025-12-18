---
description: 将某个应用包设置为不可移除（即无法卸载）的状态。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 10/07/2021
online version: https://learn.microsoft.com/powershell/module/dism/set-nonremovableappspolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NonRemovableAppsPolicy
---

# Set-NonRemovableAppsPolicy

## 摘要
将某个应用包设置为不可移除（即无法卸载）的状态。

## 语法

### 离线模式
```
Set-NonRemovableAppsPolicy -PackageFamilyName <String> -NonRemovable <Int32> -Path <String>
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 在线
```
Set-NonRemovableAppsPolicy -PackageFamilyName <String> -NonRemovable <Int32> [-Online]
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Set-NonRemovableAppsPolicy` cmdlet 用于将已安装的应用程序包设置为可移除（能够被卸载）或不可移除（无法被卸载）的状态。

## 示例

### 示例 1：将应用包 `Application1` 设置为不可移除的
```powershell
PS> Set-NonRemovableAppsPolicy -Online -PackageFamilyName Application1_1.0.0.0+x64__ms7gsqeatfeb6 -NonRemovable 1
```

此命令将应用程序包“Application1”设置为不可移除的（即用户无法删除该应用程序）。

### 示例 2：将应用程序包 Application1 设置为可移除的
```powershell
PS> Set-NonRemovableAppsPolicy -Online -PackageFamilyName Application1_1.0.0.0+x64__ms7gsqeatfeb6 -NonRemovable 0
```
此命令将应用程序包“Application1”设置为可移除的（即用户可以将其从设备上卸载）。

### 示例 3：将应用程序包 Application1 设置为在离线 Windows 系统上无法删除的状态
```powershell
PS> Set-NonRemovableAppsPolicy -Path ".\wim\image.wim" -PackageFamilyName Application1_1.0.0.0+x64__ms7gsqeatfeb6 -NonRemovable 1
```

此命令将应用程序包“Application1”设置为无法卸载的（即用户无法从已安装的离线Windows镜像“image/win”中删除该应用程序包）。

## 参数

### -LogLevel
用于指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及详细信息  
- 4 = 包含上述所有信息，还包括调试输出

```yaml
Type: LogLevel
Parameter Sets: (All)
Aliases: LL
Accepted values: Errors, Warnings, WarningsInfo, Debug

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogPath
指定日志文件的全路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘（其容量可能低至 32 MB）。日志文件会自动被归档；归档后的日志文件会在文件名后添加 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，在设置 DISM 日志文件的路径之前，请先使用 `net use` 命令并输入相应的域凭据来设置访问权限。

```yaml
Type: String
Parameter Sets: (All)
Aliases: LP

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NonRemovable
将应用程序包配置为可移除或不可移除的状态。

允许的值如下：  
- 0：将应用程序设置为可移除的（即可以卸载）。  
- 1：将应用程序设置为不可移除的（即无法卸载）。


```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Online
指定该操作应在当前在本地计算机上运行的操作系统上执行。

```yaml
Type: SwitchParameter
Parameter Sets: Online
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PackageFamilyName
指定应用程序包的“包系列名称”，并将其设置为不可移除的（即用户无法删除该应用包）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path
指定要维护的离线 Windows 镜像的根目录的完整路径。如果名为 “Windows” 的目录不是根目录的子目录，则必须指定 “WindowsDirectory”。

```yaml
Type: String
Parameter Sets: Offline
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScratchDirectory
指定一个临时目录，该目录将在执行维护任务时用于提取文件。此目录必须存在于本地系统上。如果未指定临时目录，系统将使用 `\Windows\%Temp%` 目录，并为每次 DISM 操作生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的所有内容都会被删除。不建议使用网络共享位置作为提取文件或安装包（.cab 或 .msu 文件）的临时目录；用于维护任务的临时文件提取操作的目录应为本地目录。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SystemDrive
指定包含 BootMgr 文件的路径。仅当 BootMgr 文件位于与运行命令的分区不同的分区上时，才需要设置此参数。使用 `-SystemDrive` 可以通过 Windows PE 环境来管理服务已安装的 Windows 镜像。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WindowsDirectory
指定相对于图像路径的Windows目录的路径。该路径不能是Windows目录的完整路径，而应该是一个相对路径。如果未指定，默认值为离线图像目录根目录下的Windows目录。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.Management Automation.SwitchParameter

### Microsoft.Dism Commands.LogLevel

## 输出

### Microsoft.DismCommands.ImageObject

## 备注

## 相关链接

[https://go.microsoft.com/fwlink/?LinkId=293633]

