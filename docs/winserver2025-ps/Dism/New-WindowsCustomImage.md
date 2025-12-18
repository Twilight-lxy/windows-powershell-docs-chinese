---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/new-windowscustomimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-WindowsCustomImage
---

# 新Windows自定义镜像

## 摘要
在配置了 Windows 映像文件启动（WIMBoot）功能的设备上，捕获自定义或已维修的 Windows 组件的图像。

## 语法

```
New-WindowsCustomImage -CapturePath <String> [-ConfigFilePath <String>] [-CheckIntegrity] [-Verify]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`New-WindowsCustomImage` cmdlet 将自定义的图像设置捕获到一个新的 WIM（Windows Image File）文件中，该文件用于在基于 WIMBoot 的系统中启动 Windows 系统。

被捕获的目录包含所有的子文件夹和数据。

您无法捕获一个空的目录。

注意：此命令仅捕获自定义文件。

该命令不能用于将安装文件捕获到一个新的WIM（Windows Imaging File）文件中。

## 示例

### 示例 1：捕获图片自定义文件
```
PS C:\> New-WindowsCustomImage -CapturePath "c:\"
```

这个命令会将图像自定义文件捕获到一个WIM（Windows Imaging Module）文件中，并将这些文件保存到c:\目录下。

## 参数

### -CapturePath
指定要捕获到图像文件中的 Windows 操作系统的驱动器或路径。

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

### -CheckIntegrity
当使用 `Add-WindowsImage`、`Dismount-WindowsImage` 或 `Save-WindowsImage` cmdlet 时，该工具能够检测并跟踪 `.wim` 文件的损坏情况。如果在使用 `Expand-WindowsImage` 或 `Mount-WindowsImage` cmdlet 期间 DISM 发现 `.wim` 文件已损坏，`CheckIntegrity` 会立即停止相关操作。

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

### -ConfigFilePath
用于指定配置文件的位置，该文件列出了图像捕获和压缩命令的排除项。有关更多信息，请参阅[DISM 配置列表和 WimScript.ini 文件](https://go.microsoft.com/fwlink/?LinkID=313768)。

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘（其存储空间可能低至 32 MB）。日志文件会自动被归档；归档后的文件名会加上 `.bak` 扩展名，同时会生成一个新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，在设置 DISM 日志路径之前，请先使用 `net use` 命令并输入相应的域凭据来配置访问权限。

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
指定一个临时目录，用于在服务过程中提取文件。该目录必须存在于本地计算机上。如果未指定目录，则会使用 `\Windows\%Temp%\` 目录，其中子目录的名称是由 DISM 运行时生成的随机十六进制值。每次操作完成后，临时目录中的内容都会被删除。不建议将网络共享位置用作安装包（.cab 或 .msu 文件）的临时提取目录。用于在服务过程中临时提取文件的目录应为本地目录。

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

### -Verify
检查错误和文件重复情况。例如，在使用 `Add-WindowsImage` cmdlet 进行应用操作时，会检查待应用文件的大小和哈希值是否与原始镜像文件一致。同样，在使用 `New-WindowsImage` cmdlet 进行捕获操作时，文件被捕获到 Windows 镜像后，会将其写入临时文件，并与原始文件进行逐位比较。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.Dismcommands.ImageObject

## 备注

## 相关链接

