---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/clear-windowscorruptmountpoint?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-WindowsCorruptMountPoint
---

# 清理损坏的 Windows 移动存储设备挂载点

## 摘要
删除与已损坏的挂载镜像相关的所有资源。

## 语法

```
Clear-WindowsCorruptMountPoint [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

## 描述
`Clear-WindowsCorruptMountPoint` cmdlet 会删除与已损坏的挂载镜像相关的所有资源。

## 示例

### 示例 1：删除与已挂载镜像关联的所有资源
```
PS C:\> Clear-WindowsCorruptMountPoint
```

此命令会删除计算机上所有与已损坏的挂载镜像相关联的资源。

## 参数

### -LogLevel
指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及常规信息  
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
指定要记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 中，默认目录是 RAMDISK 资源池（其容量可能低至 32 MB）。日志文件会自动被归档；归档后的日志文件会在文件名后加上 `.bak` 扩展名，同时会生成一个新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先通过 `net use` 命令结合域凭据来配置访问权限。

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

### -ScratchDirectory
指定一个临时目录，该目录将在执行维护操作（servicing）时用于提取文件。此目录必须存在于本地系统中。如果未指定目录，则系统会使用 `\Windows\%Temp%` 目录，并为每次运行 DISM 命令生成一个随机十六进制值的子目录名称。每次操作完成后，该临时目录中的所有内容都会被删除。不建议将网络共享位置作为用于解压安装包（.cab 或 .msu 文件）的临时目录；用于提取文件的临时目录应始终是本地目录。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dism Commands.BasicDismObject

## 输出

### Microsoft.Dismcommands.BaseDismObject

## 备注

## 相关链接

[Dismount-WindowsImage](./Dismount-WindowsImage.md)

