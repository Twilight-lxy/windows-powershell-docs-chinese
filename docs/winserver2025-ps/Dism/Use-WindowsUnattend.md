---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/use-windowsunattend?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Use-WindowsUnattend
---

# 使用 Windows Unattend（自动安装脚本）

## 摘要
将一个无人值守的应答文件应用到Windows镜像上。

## 语法

### 离线状态
```
Use-WindowsUnattend -UnattendPath <String> [-NoRestart] -Path <String> [-WindowsDirectory <String>]
 [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

### 在线
```
Use-WindowsUnattend -UnattendPath <String> [-NoRestart] [-Online] [-WindowsDirectory <String>]
 [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

## 描述
`Use-WindowsUnattend` cmdlet 将一个无人参与安装的答案文件（Unattend.xml）应用到 Windows 镜像上。

如果您使用无人值守的应答文件来更新设备驱动程序，则必须将该应答文件应用到离线镜像上，并在离线服务（offlineServicing）配置阶段指定相应的设置。

如果您正在使用无人值守的应答文件来更新软件包或其他设置，可以将该应答文件应用到离线或在线镜像上。请在 `offlineServicing` 配置参数中指定相应的设置。

## 示例

### 示例 1：将答案文件应用到已挂载的镜像上
```
PS C:\> Use-WindowsUnattend -Path "c:\offline" -UnattendPath "c:\test\answerfiles\myunattend.xml"
```

这个命令将一个回答文件（myunattend.xml）应用到被挂载到 c:\offline 目录中的 Windows 镜像上。

### 示例 2：将答案文件应用于正在运行的操作系统
```
PS C:\> Use-WindowsUnattend -Online -UnattendPath "c:\test\answerfiles\myunattend.xml"
```

这个命令将一个回答文件（myunattend.xml）应用到在线Windows镜像上。

## 参数

### -LogLevel
指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及详细信息  
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
指定要记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 内的临时存储空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件名称会在原文件名后添加 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。如果使用未加入域的网络共享资源，请在使用 `DISM` 日志路径之前，先通过 `net use` 命令结合域凭据来设置访问权限。

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

### -NoRestart
此命令用于抑制系统重启。如果不需要重启，该命令将不会执行任何操作。通过使用此选项，可以防止应用程序提示用户进行重启，或者避免应用程序自动重启。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

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
指定一个临时目录，用于在服务过程中提取文件。该目录必须存在于本地系统中。如果未指定临时目录，则系统会使用 `\Windows\%Temp%` 目录，并为每次执行 DISM 命令生成一个随机十六进制数值作为子目录名称。每次操作完成后，临时目录中的所有内容都会被删除。不建议将网络共享位置用作提取文件或安装包（.cab 或 .msu 文件）的临时目录。用于服务过程中临时提取文件的目录应当是本地目录。

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
指定 BootMgr 文件所在的路径。只有当 BootMgr 文件位于与您执行命令的分区不同的分区上时，才需要设置此路径。使用 `-SystemDrive` 选项可以从 Windows PE 环境中管理服务已安装的 Windows 镜像。

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

### -UnattendPath
指定用于应用到镜像中的 unattend.xml 答案文件的位置。

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

### -WindowsDirectory
指定相对于图像路径的Windows目录的路径。这个路径不能是Windows目录的完整路径，而应该是一个相对路径。如果未指定，默认值是离线图像目录根目录下的Windows目录。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dism Commands.ImageObject

## 输出

### Microsoft.Dism Commands.ImageObject

## 备注

## 相关链接

