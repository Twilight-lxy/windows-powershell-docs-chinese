---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/remove-windowscapability?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-WindowsCapability
---

# 移除 Windows 功能

## 摘要
从一个镜像文件中卸载Windows功能包。

## 语法

### 在线
```
Remove-WindowsCapability -Name <String> [-Online] [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 离线模式
```
Remove-WindowsCapability -Name <String> -Path <String> [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Remove-WindowsCapability` cmdlet 会从指定的镜像中卸载相应的 Windows 功能包。

## 示例

#### 示例 1：从图像中移除与 Windows 相关的功能
```
PS C:\> Remove-WindowsCapability -Name "Language.TextToSpeech~~~fr-FR~0.0.1.0" -Path "C:\offline"
```

此命令会卸载在由 *Name* 参数指定的操作系统映像（路径为 C:\offline）中安装的 Windows 功能。

### 示例 2：移除本地操作系统的 Windows 功能
```
PS C:\> Remove-WindowsCapability -Name "Language.TextToSpeech~~~fr-FR~0.0.1.0" -Online
```

此命令会卸载本地主机上安装的Windows相关功能。

## 参数

### -LogLevel
用于指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及相关信息  
- 4 = 显示上述所有信息，还包括调试输出

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 的临时存储空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的文件名称会添加 `.bak` 扩展名，同时系统会生成一个新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件都会被覆盖。如果使用未加入域的网络共享资源，请先使用 `net use` 命令并输入相应的域凭据来设置访问权限，然后再指定 DISM 日志的路径。

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

### -Name
指定要从操作系统镜像中删除的功能的标识信息。

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

### -Online
表示该cmdlet在本地主机上正在运行的操作系统中执行。

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
指定一个临时目录，该目录将在执行维护任务时用于解压文件。此目录必须存在于本地系统中。如果未指定临时目录，则系统会使用 `\Windows\%Temp%` 目录，并为每次运行 DISM 命令生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的所有内容都会被删除。不建议将网络共享位置作为用于解压安装包（.cab 或 .msu 文件）的临时目录；用于维护任务的文件解压操作的目录应始终是本地目录。

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
指定BootMgr文件所在的路径。只有当BootMgr文件位于与您运行命令的分区不同的分区上时，才需要指定该路径。使用-SystemDrive选项可以从Windows PE环境中对已安装的Windows镜像进行维护（即对该镜像执行相关操作）。

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
指定相对于图像路径的 Windows 目录的路径。这不能是 Windows 目录的完整路径，而应该是一个相对路径。如果未指定，默认值将是离线图像目录根目录下的 Windows 目录。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.DismCommands.ImageObject

## 备注

## 相关链接

[Add-WindowsCapability](./Add-WindowsCapability.md)

[Get-WindowsCapability](./Get-WindowsCapability.md)

