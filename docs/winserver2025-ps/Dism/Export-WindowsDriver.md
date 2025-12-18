---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/export-windowsdriver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-WindowsDriver
---

# 导出 Windows 驱动程序

## 摘要
将Windows镜像中的所有第三方驱动程序导出到目标文件夹中。

## 语法

### 离线模式
```
Export-WindowsDriver [-Destination <String>] -Path <String> [-WindowsDirectory <String>]
 [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

### 在线
```
Export-WindowsDriver [-Destination <String>] [-Online] [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Export-WindowsDriver` 这个 cmdlet 可以将 Windows 映像中的所有第三方驱动程序导出到指定的目标文件夹中。

## 示例

### 示例 1：从正在运行的操作系统中导出驱动程序
```
PS C:\> Export-WindowsDriver -Online -Destination d:\drivers
```

此命令会从正在运行的Windows版本中导出第三方驱动程序。

### 示例 2：从离线镜像中导出驱动程序
```
PS C:\> Export-WindowsDriver -Path c:\offline-image -Destination d:\drivers
```

此命令用于从挂载在 `c:\offline-image` 目录下的离线镜像中导出第三方驱动程序。

## 参数

### -Destination
指定一个目录，用于存放导出的第三方驱动程序。

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

### -LogLevel
用于指定日志中显示的最大输出级别。默认的日志级别为 3。允许的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及常规信息  
- 4 = 显示前面列出的所有信息，还包括调试输出

```yaml
Type: LogLevel
Parameter Sets: (All)
Aliases: LL
Accepted values: Errors, Warnings, WarningsInfo

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogPath
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘（其存储空间可能低至 32 MB）。日志文件会自动被归档；归档后的日志文件会在原文件名后加上 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，相应的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，在设置 DISM 日志路径之前，请先使用 `net use` 命令并输入相应的域凭据来设置访问权限。

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
指定一个临时目录，该目录将在执行服务维护操作时用于提取文件。此目录必须存在于本地系统中。如果未指定临时目录，则系统会使用 `\Windows\%Temp%\` 目录，并为每次 DISM 操作生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的所有内容都会被删除。不建议将网络共享位置作为临时目录来解压用于安装的包文件（.cab 或 .msu 格式）。在执行服务维护操作时用于提取文件的临时目录应为本地目录。

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
指定 BootMgr 文件所在的路径。只有当 BootMgr 文件位于与你运行命令的分区不同的分区上时，才需要指定该路径。使用 `-SystemDrive` 选项可以从 Windows PE 环境中对已安装的 Windows 映像进行维护或操作。

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
指定相对于图像路径的 Windows 目录的路径。这不能是 Windows 目录的完整路径，而应该是一个相对路径。如果未指定，默认值是离线图像目录根目录下的 Windows 目录。

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

### System.String[], Microsoft.Dismcommands.ImageObject

## 输出

### Microsoft.DismCommands.AdvancedDriverObject

## 备注

## 相关链接

[Add-WindowsDriver](./Add-WindowsDriver.md)

[Get-WindowsDriver](./Get-WindowsDriver.md)

[Remove-WindowsDriver](./Remove-WindowsDriver.md)

