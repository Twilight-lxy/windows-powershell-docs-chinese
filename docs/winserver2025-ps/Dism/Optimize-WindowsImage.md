---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/optimize-windowsimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Optimize-WindowsImage
---

# 优化 Windows 镜像

## 摘要
配置一个包含指定优化设置的Windows镜像文件。

## 语法

```
Optimize-WindowsImage -OptimizationTarget <String> -Path <String> [-WindowsDirectory <String>]
 [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

## 描述
`Optimize-WindowsImage` cmdlet 会对离线映像执行指定的配置操作。

`Optimize-WindowsImage` 仅适用于已捕获或导出为 Windows 映像文件（WIMBoot 文件）的 Windows 8.1 Update 镜像。请仅将该工具用于将用于支持 WIMBoot 的系统的镜像。如果在不支持 WIMBoot 的系统镜像上使用 `Optimize-WindowsImage`，安装后 Windows 可能无法正常运行。

## 示例

### 示例 1：将一张图片配置为 WIMBoot 系统
```
PS C:\> Optimize-WindowsImage -Path "c:\" -OptimizationTarget "WIMBoot"
```

此命令将位于 c:\ 目录中的 Windows 镜像配置为 WIMBoot 系统。

## 参数

### -LogLevel
指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误和警告信息  
- 3 = 显示错误、警告以及信息内容  
- 4 = 显示上述所有信息，外加调试输出

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK scratch 空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件会在原文件名后添加 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。如果使用未加入域的网络共享资源，请在使用 `DISM` 日志路径之前，先通过 `net use` 命令并输入域凭据来设置访问权限。

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

### -OptimizationTarget
指定 Windows 镜像优化类型。可接受的值如下：“WIMBoot”。注意：此值必须以字符串形式输入。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: WIMBoot

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path
指定你要维护的离线 Windows 镜像的根目录的完整路径。如果名为 “Windows” 的目录不是根目录的子目录，那么必须指定 “WindowsDirectory”。

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

### -ScratchDirectory
指定一个临时目录，用于在服务过程中提取文件。该目录必须存在于本地系统中。如果未指定目录，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时，该目录下的子目录名称都会由随机生成的十六进制数值来确定。每次操作完成后，临时目录中的所有内容都会被删除。不建议将网络共享位置作为临时目录来用于解压安装包（.cab 或 .msu 文件）。在服务过程中用于临时提取文件的目录应该是一个本地目录。

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
指定 BootMgr 文件所在的路径。只有当 BootMgr 文件位于与您运行命令的分区不同的分区上时，才需要指定该路径。使用 `-SystemDrive` 参数可以从 Windows PE 环境中管理服务已安装的 Windows 镜像。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DismCommands.ImageObject

## 输出

### Microsoft.DismCommands.ImageObject

## 备注

## 相关链接

