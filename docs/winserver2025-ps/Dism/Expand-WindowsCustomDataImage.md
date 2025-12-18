---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/expand-windowscustomdataimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Expand-WindowsCustomDataImage
---

# 扩展 Windows 自定义数据镜像

## 摘要
展开一个自定义的数据图像。

## 语法

```
Expand-WindowsCustomDataImage -ImagePath <String> -CustomDataImage <String> [-SingleInstance]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Expand-WindowsCustomDataImage` cmdlet 用于展开自定义数据镜像。这些单实例文件适用于设备恢复文件夹中的自定义数据镜像所包含的操作系统分区。

## 示例

### 示例 1：展开自定义数据图像
```
PS C:\> Expand-WindowsCustomDataImage -CustomDataImage "C:\oem.ppkg" -ImagePath "C:\" -SingleInstance
```

此命令将自定义数据镜像文件 C:\oem.ppkg 解压到指定的镜像路径。该命令指定了 *SingleInstance* 参数。

## 参数

### -CustomDataImage
用于指定在 WIM 容器中捕获的 Windows 镜像的自定义数据。

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

### -ImagePath
指定WIM文件的位置。

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK（一种临时存储空间），其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件会在原文件名后添加 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件都会被覆盖。如果使用未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先通过 `net use` 命令结合域凭据来配置访问权限。

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
指定一个临时目录，该目录将在执行服务维护操作时用于解压文件。此目录必须存在于本地计算机上。如果未指定临时目录，则系统会使用 `\Windows\%Temp%\` 目录，并为每次 DISM 操作生成一个随机十六进制数值作为子目录的名称。每次操作完成后，该临时目录中的所有文件都会被删除。切勿将网络共享位置用作解压安装包（.cab 或 .msu 文件）的临时目录；用于服务维护过程中临时解压文件的目录应始终是本地目录。

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

### -SingleInstance
这表示该cmdlet会修改应用于操作系统分区上的自定义数据文件，使其变为由自定义数据镜像中的文件载荷所备份的文件指针。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]、Microsoft.Dism Commands.ImageObject、Microsoft.DismCommands.ImageObjectWithState

## 输出

### Microsoft.Dism Commands.OfflineImageObject

## 备注

## 相关链接

[Expand-WindowsImage](./Expand-WindowsImage.md)

