---
description: 使用此主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/export-windowsimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-WindowsImage
---

# Export-WindowsImage

## 摘要
将指定的图像复制到另一个图像文件中。

## 语法

### 输入方式：通过文件路径和名称
```
Export-WindowsImage [-CheckIntegrity] [-CompressionType <String>] -DestinationImagePath <String>
 [-DestinationName <String>] [-Setbootable] -SourceImagePath <String> -SourceName <String>
 [-SplitImageFilePattern <String>] [-WIMBoot] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

### InputByFilePathAndIndex
```
Export-WindowsImage [-CheckIntegrity] [-CompressionType <String>] -DestinationImagePath <String>
 [-DestinationName <String>] [-Setbootable] -SourceImagePath <String> -SourceIndex <UInt32>
 [-SplitImageFilePattern <String>] [-WIMBoot] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Export-WindowsImage` cmdlet 将指定的 Windows 映像文件复制到另一个图像文件中。源文件和目标文件必须使用相同的压缩格式。

您还可以使用 `Export-WindowsImage` 命令将图像导出为新的图像文件来优化它。当您修改图像时，DISM 会存储额外的资源文件，这些文件会增加图像的总大小。通过导出图像，可以删除不必要的资源文件。

此cmdlet不适用于虚拟硬盘（VHD）文件。

## 示例

### 示例 1：导出一张图片
```
PS C:\> Export-WindowsImage -SourceImagePath C:\imagestore\custom.wim -SourceIndex 1 -DestinationImagePath c:\imagestore\export.wim -DestinationName "Exported Image"
```

该命令将文件 C:\imagestore\custom.wim 中索引为 1 的镜像导出到文件 c:\imagestore\export.wim 中，并将其命名为 “Exported Image”。

## 参数

### -CheckIntegrity
当与 `Add-WindowsImage`、`Dismount-WindowsImage` 或 `Save-WindowsImage` cmdlet 一起使用时，该工具能够检测并跟踪 `.wim` 文件是否损坏。如果在使用 `Expand-WindowsImage` 或 `Mount-WindowsImage` cmdlet 时 DISM 发现 `.wim` 文件已损坏，`CheckIntegrity` 会立即停止相关操作。

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

### -CompressionType
指定用于初始捕获操作的压缩类型。可选值包括：

- **"max" or "maximum":** Provides the high compression, but takes more time to capture the image
- **"fast:"** Provides faster image compression, but the resulting files are larger than those compressed by using the maximum option.
- **"none":** No compression is used at all. This is the default.

> [!注意] > 该cmdlet不支持“recovery”压缩类型，请使用 `dism.exe` 代替。

当你将图像导出到现有的.wim文件时，*CompressionType*参数是无效的；只有在你将图像导出到一个新的.wim文件时，才能使用这个压缩类型。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: "none"
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DestinationImagePath
指定导出图像文件的位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases: DIP

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DestinationName
指定导出图像文件中导出图像的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: DN

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogLevel
用于指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
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
Default value: 3
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogPath
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 中，默认目录是 RAMDISK 磁盘上的临时存储空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件名称会在原文件名后加上 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先使用 `net use` 命令并结合相应的域凭据来配置访问权限。

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
指定一个临时目录，用于在维护过程中提取文件。该目录必须存在于本地系统中。如果未指定临时目录，则会使用 `\Windows\%Temp%` 目录，并且每次运行 DISM 时，该目录下的子目录名称都会是一个随机生成的十六进制值。每次操作完成后，临时目录中的文件都会被删除。不建议将网络共享位置用作安装包（.cab 或 .msu 文件）的临时提取目录。用于在维护过程中临时提取文件的目录应该是本地目录。

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

### -Setbootable
将卷图像标记为可启动图像。此参数仅适用于 Windows PE 图像。在一个.wim 文件中，只能有一个卷图像被标记为可启动图像。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: SB

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SourceImagePath
指定源图像文件的位置。必须与 `-SourceIndex` 或 `-SourceName` 一起使用。如果源文件是 SWM 文件，则还需要使用 `-SplitImageFilePattern`。

```yaml
Type: String
Parameter Sets: (All)
Aliases: SIP

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SourceIndex
指定 Windows 镜像在 WIM 或 VHD 文件中的索引编号。对于 VHD 文件，该索引编号必须为 1。

```yaml
Type: UInt32
Parameter Sets: InputByFilePathAndIndex
Aliases: SI

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SourceName
指定源图像文件中源图像的名称。

```yaml
Type: String
Parameter Sets: InputByFilePathAndName
Aliases: SN

Required: True
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

### -WIMBoot
指定该图像将被格式化，以便用于安装在基于 Windows 映像文件启动（WIMBoot）的系统上。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.DismCommands.ImageObject

### Microsoft.DismCommands.ImageObjectWithState

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

[修复Windows镜像](./Repair-WindowsImage.md)

[Save-WindowsImage](./Save-WindowsImage.md)

[Split-WindowsImage](./Split-WindowsImage.md)

