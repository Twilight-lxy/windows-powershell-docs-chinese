---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 08/25/2021
online version: https://learn.microsoft.com/powershell/module/dism/expand-windowsimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Expand-WindowsImage
---

# 扩展 Windows 映像文件

## 摘要
将一张图片应用到指定的位置。

## 语法

### 输入方式：通过文件路径和名称
```
Expand-WindowsImage -ImagePath <String> -Name <String> [-SplitImageFilePattern <String>] -ApplyPath <String>
 [-CheckIntegrity] [-ConfirmTrustedFile] [-NoRpFix] [-Verify] [-WIMBoot] [-Compact] [-SupportEa]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

### InputByFilePathAndIndex
```
Expand-WindowsImage -ImagePath <String> -Index <UInt32> [-SplitImageFilePattern <String>] -ApplyPath <String>
 [-CheckIntegrity] [-ConfirmTrustedFile] [-NoRpFix] [-Verify] [-WIMBoot] [-Compact] [-SupportEa]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Expand-WindowsImage` cmdlet 将一个镜像应用到指定的位置。

此命令行工具不适用于虚拟硬盘（VHD）文件。

## 示例

### 示例 1：将文件中的图像应用到某个分区
```
PS C:\> Expand-WindowsImage -ImagePath "c:\imagestore\custom.wim" -ApplyPath "d:\" -Index 1
```

这个命令会将位于路径 `c:\imagestore\custom.wim` 中、索引为 1 的图像应用到分区 `d:` 上。

### 示例 2：应用分割图像技术
```
PS C:\> Expand-WindowsImage -ImagePath "c:\imagestore\split\custom.swm" -SplitImageFilePattern "c:\imagestore\split\custom*.swm" -ApplyPath "d:\" -Name "Windows Pro" -Verify
```

此命令会将名为 `c:\imagestore\split\custom*.swm` 的分割图像（对应于 Windows Pro 操作系统）应用到分区 d: 上。在应用该图像的过程中，请检查是否存在错误或文件重复的情况。

## 参数

### -ApplyPath
指定图像应用的位置。

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
当使用 `Add-WindowsImage`、`Dismount-WindowsImage` 或 `Save-WindowsImage` cmdlet 时，该工具能够检测并跟踪 `.wim` 文件的损坏情况。如果在使用 `Expand-WindowsImage` 或 `Mount-WindowsImage` cmdlet 期间 DISM 检测到 `.wim` 文件已损坏，`CheckIntegrity` 会立即停止相关操作。

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

### -Compact
表示此cmdlet会将操作系统镜像应用到指定的驱动器上，同时压缩其中的各个操作系统文件。如果不指定该参数，此cmdlet会将镜像中的所有文件原样（未经压缩）复制到驱动器上。

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

### -ConfirmTrustedFile
该cmdlet用于验证图像是否适用于Windows 8或Windows 8.1上的“可信桌面”功能。此选项仅能在运行Windows预安装环境（Windows PE）4.0或更高版本的计算机上使用。

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

### -Index
指定 WIM 或 VHD 文件中 Windows 镜像的索引编号。对于 VHD 文件，索引值必须为 1。

```yaml
Type: UInt32
Parameter Sets: InputByFilePathAndIndex
Aliases:

Required: True
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
指定要记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 中，默认目录是 RAMDISK 故障恢复空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件名称会添加 `.bak` 扩展名，并且会生成一个新的日志文件。每次日志文件被归档时，原有的 `.bak` 文件都会被覆盖。当使用未加入域的网络共享资源时，请先使用 `net use` 命令并输入域凭据来设置访问权限，然后再设置 DISM 日志的路径。

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
指定 WIM 文件中一张图片的名称。

```yaml
Type: String
Parameter Sets: InputByFilePathAndName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NoRpFix
禁用对重新解析点标签的修复功能。重新解析点是一种文件，它在文件系统中包含指向另一文件的链接。如果未指定该参数，则系统将不会捕获那些指向 *ImagePath* 参数所指定路径之外的位置的重新解析点。

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

### -ScratchDirectory
指定一个临时目录，用于在服务过程中提取文件以供使用。该目录必须存在于本地。如果未指定，则会使用 `\Windows\%Temp%` 目录，并且每次运行 DISM 时都会为该目录生成一个随机十六进制值的子目录名称。每次操作结束后，临时目录中的内容都会被删除。不建议将网络共享位置作为临时目录来解压用于安装的包文件（.cab 或 .msu 文件）。在服务过程中用于提取文件的临时目录应为本地目录。

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

### -SplitImageFilePattern
指定基础分割图像文件的位置和名称。

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

### -SupportEa
应用具有扩展属性的图像。

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

### -Verify
检查错误和文件重复情况。例如，在使用 `Add-WindowsImage` cmdlet 进行应用操作时，会检查所应用文件的大小和哈希值是否与镜像文件相匹配。又例如，在使用 `New-WindowsImage` cmdlet 进行捕获操作时，文件被捕获到 Windows 镜像后，会将其写入临时文件，并逐位与原始文件进行比较。

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

### -WIMBoot
指定要添加的离线图像将被格式化，以便在基于 Windows 图像格式启动（WIMBoot）的系统上安装。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dism Commands.ImageObject

### Microsoft.Dism Commands.ImageObjectWithState

## 输出

### Microsoft.Dism Commands.OfflineImageObject

## 备注

## 相关链接

[Dismount-WindowsImage](./Dismount-WindowsImage.md)

[Export-WindowsImage](./Export-WindowsImage.md)

[Get-WindowsImage](./Get-WindowsImage.md)

[Mount-WindowsImage](./Mount-WindowsImage.md)

[New-WindowsImage](./New-WindowsImage.md)

[Remove-WindowsImage](./Remove-WindowsImage.md)

[Repair-WindowsImage](./Repair-WindowsImage.md)

[Save-WindowsImage](./Save-WindowsImage.md)

[Split-WindowsImage](./Split-WindowsImage.md)

