---
description: Windows允许用户卸载当前版本的操作系统，并恢复到之前的版本。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 10/07/2021
online version: https://learn.microsoft.com/powershell/module/dism/start-osuninstall?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-OSUninstall
---

# 开始卸载操作系统

## 摘要
Windows 允许用户卸载当前版本并恢复到之前的 Windows 版本。你可以使用 DISM 来启动卸载过程。

## 语法

### 离线模式
```
Start-OSUninstall [-NoRestart] -Path <String> [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 在线
```
Start-OSUninstall [-NoRestart] [-Online] [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Start-OSUninstall` cmdlet 允许你卸载 Windows 并恢复到之前安装的版本。

`Start-OSUninstall` cmdlet 仅支持 Windows 11 客户端操作系统。

## 示例

### 示例 1：卸载操作系统
```powershell
Start-OSUninstall -Online
```

卸载当前在本地计算机上运行的操作系统，并恢复到之前安装的Windows版本。

## 参数

### -LogLevel
指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及信息性内容  
- 4 = 包括上述所有信息，此外还显示调试输出

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 暂存空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件会在文件名后加上 `.bak` 扩展名，并生成新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件都会被覆盖。当使用未加入域的网络共享资源时，请先使用 `net use` 命令并输入域凭据来设置访问权限，然后再为 DISM 日志指定路径。

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
会抑制重新启动的提示信息，并且需要手动进行重启操作。

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
指定该操作应在当前正在本地计算机上运行的操作系统上执行。

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
指定一个临时目录，用于在维护过程中提取文件。该目录必须存在于本地系统中。如果未指定目录，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时都会为该目录生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的内容都会被删除。不建议将网络共享位置用作安装包（.cab 或 .msu 文件）的临时提取目录。用于在维护过程中临时提取文件的目录应为本地目录。

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
指定 BootMgr 文件所在的路径。只有当 BootMgr 文件位于与执行命令的分区不同的分区时，才需要提供该路径。使用 `-SystemDrive` 选项可以从 Windows PE 环境中服务已安装的 Windows 镜像。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.Management Automation.SwitchParameter

### System.String

### Microsoft.Dismcommands.LogLevel

## 输出

### Microsoft.Dism Commands.BaseDismObject

## 备注

## 相关链接
