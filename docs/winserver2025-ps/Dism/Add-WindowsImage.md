---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 08/25/2021
online version: https://learn.microsoft.com/powershell/module/dism/add-windowsimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-WindowsImage
---

# Add-WindowsImage

## 摘要
向现有的图像文件（.wim）中添加另一张图片。

## 语法

```
Add-WindowsImage -ImagePath <String> -CapturePath <String> [-ConfigFilePath <String>] [-Description <String>]
 -Name <String> [-CheckIntegrity] [-NoRpFix] [-Setbootable] [-Verify] [-WIMBoot] [-SupportEa]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Add-WindowsImage` cmdlet 可以将新的镜像文件添加到现有的 `.wim` 镜像文件中。该cmdlet 会新文件与现有 `.wim` 文件中的资源进行比较（这些资源的路径由 `Name` 和 `ImagePath` 参数指定），并仅保留每个唯一文件的副本，以确保每个文件不会被重复存储。`.wim` 文件只能使用一种压缩格式；因此，你只能向该文件添加具有相同压缩格式的文件。

`Add-WindowsImage` cmdlet 不适用于虚拟硬盘（VHD）文件。

需要注意的是，在运行 **Add-WindowsImage** 命令之前，你必须确保有足够的磁盘空间。如果在添加镜像文件的过程中磁盘空间不足，可能会导致 .wim 文件损坏。

## 示例

### 示例 1：将文件添加到图像中
```
PS C:\> Add-WindowsImage -ImagePath "C:\imagestore\custom.wim" -CapturePath d:\ -Name "Drive D"
```

该命令将位于“d:\Drive D”目录中的文件添加到现有的图像文件（路径为c:\imagestore\custom.wim）中。

## 参数

### -CapturePath
指定新文件的路径，这些新文件将与现有的.wim文件中的资源进行比较。

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
当与 **Add-WindowsImage**、**Dismount-WindowsImage** 或 **Save-WindowsImage** cmdlet 一起使用时，该功能可以检测并跟踪 .wim 文件是否损坏。如果在使用 **Expand-WindowsImage** 或 **Mount-WindowsImage** cmdlet 时 DISM 发现 .wim 文件已损坏，CheckIntegrity 会立即停止相关操作。

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
指定一个配置文件的位置，该文件列出了用于图像捕获和压缩命令的排除规则。有关更多信息，请参阅[DISM 配置列表和 WimScript.ini 文件](https://go.microsoft.com/fwlink/?LinkID=313768)。

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

### -Description
用于指定要捕获的图像的描述信息。

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

### -ImagePath
指定包含要与新文件进行比较的Windows镜像的WIM文件的位置。

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
- 3 = 显示错误信息、警告信息以及详细信息  
- 4 = 包含上述所有信息，还包括调试输出

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
指定要记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 的临时存储空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件会在文件名后加上 `.bak` 扩展名，同时会生成一个新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 日志路径之前，先通过 `net use` 命令结合域凭据来设置访问权限。

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
指定WIM文件中一张图片的名称。

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

### -NoRpFix
禁用重新解析点标签修复功能。重新解析点是一种文件，它在文件系统中包含指向另一文件的链接。如果未指定该参数，则系统将不会捕获那些指向 *ImagePath* 参数所指定路径之外的位置的重新解析点。

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
指定一个临时目录，用于在维护过程中提取文件以供使用。该目录必须存在于本地。如果未指定，则会使用 `\Windows\%Temp%` 目录，并且每次运行 DISM 时都会为该目录生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的内容都会被删除。不建议将网络共享位置用作用于安装包（.cab 或 .msu 文件）的临时目录。在维护过程中用于提取文件的临时目录应该是本地目录。

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
将一个卷图像标记为可启动图像。此参数仅适用于 Windows PE 图像。在一个.wim 文件中，只能有一个卷图像被标记为可启动图像。

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

### -SupportEa
附加一张带有扩展属性的图片。

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
会检查是否存在错误以及文件是否重复。例如，在使用 `Add-WindowsImage` cmdlet 进行应用操作时，会将所应用的文件的大小和哈希值与源镜像文件进行比对，以确保两者一致。同样，在使用 `New-WindowsImage` cmdlet 进行捕获操作时，捕获到的文件会被写入一个临时文件中，并与该文件的原始内容进行逐位比较。

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
指定要添加的离线图像将被格式化为适用于Windows图像格式引导（WIMBoot）系统的版本。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dismcommands.ImageObject

### Microsoft.Dism Commands.ImageObjectWithState

## 输出

### Microsoft.Dism Commands.OfflineImageObject

## 备注

## 相关链接

[Dismount-WindowsImage](./Dismount-WindowsImage.md)

[Expand-WindowsImage](./Expand-WindowsImage.md)

[Export-WindowsImage](./Export-WindowsImage.md)

[Get-WindowsImage](./Get-WindowsImage.md)

[Mount-WindowsImage](./Mount-WindowsImage.md)

[New-WindowsImage](./New-WindowsImage.md)

[Remove-WindowsImage](./Remove-WindowsImage.md)

[修复Windows镜像](./Repair-WindowsImage.md)

[Save-WindowsImage](./Save-WindowsImage.md)

[Split-WindowsImage](./Split-WindowsImage.md)

