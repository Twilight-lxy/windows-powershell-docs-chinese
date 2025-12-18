---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/new-windowsimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-WindowsImage
---

# 新Windows镜像

## 摘要
将驱动器的图像捕获到一个新的WIM（Windows Imaging File）文件中。

## 语法

```
New-WindowsImage -ImagePath <String> -CapturePath <String> [-CompressionType <String>]
 [-ConfigFilePath <String>] [-Description <String>] -Name <String> [-CheckIntegrity] [-NoRpFix] [-Setbootable]
 [-Verify] [-WIMBoot] [-SupportEa] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

## 描述
`New-WindowsImage` cmdlet 可将驱动器的图像捕获到一个新的 WIM（Windows Imaging Manifest）文件中。被捕获的目录包括所有的子文件夹和数据。你无法捕获空目录；一个目录必须至少包含一个文件。

此cmdlet不适用于虚拟硬盘（VHD）文件。

## 示例

### 示例 1：为 WIM 文件捕获驱动器的图像
```
PS C:\> New-WindowsImage -ImagePath "c:\imagestore\custom.wim" -CapturePath "d:\" -Name "Drive D"
```

这个命令会将位于 d:\ 目录下的 Drive D 映像捕获到 WIM 文件中，并将其保存到 c:\imagestore\custom.wim 文件中。

## 参数

### -CapturePath
指定要捕获到图像文件中的Windows操作系统的驱动器或路径。

当指定的路径不是驱动器的根文件夹时，捕获的图像将继承父文件夹的安全描述符。如果您要捕获的是之前已经应用过的镜像，请将该镜像重新应用于驱动器的根文件夹，以确保新图像的安全描述符保持不变。

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
当与 **Add-WindowsImage**、**Dismount-WindowsImage** 或 **Save-WindowsImage** cmdlet 一起使用时，该工具能够检测并追踪 .wim 文件的损坏情况。如果 DISM 在使用 **Expand-WindowsImage** 或 **Mount-WindowsImage** cmdlet 时发现 .wim 文件已损坏，**CheckIntegrity** 会立即停止相关操作。

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
指定用于初始捕获操作的压缩类型：

- **Max** = This option provides the best compression but takes more time to capture the image.
- **Fast** = This option provides faster image compression but the resulting files are larger than those compressed using the maximum (max) option.
- **None** = This option does not compress the captured image at all.

当你将图像导出到现有的.wim文件时，*CompressionType*参数是无效的；只有在你将图像导出到新的.wim文件时，才能使用这个压缩类型。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: Fast
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ConfigFilePath
指定一个配置文件的位置，该文件列出了用于图像捕获命令和压缩命令的排除规则。有关更多信息，请参阅TechNet库中的[DISM配置列表和WimScript.ini文件](https://go.microsoft.com/fwlink/?LinkID=313768)。

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
指定 WIM 文件的位置。

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
指定日志中显示的最大输出级别。默认的日志级别为 WarningsInfo。允许的值如下：

- Errors = Errors only
- Warnings = Errors and warnings
- WarningsInfo = Errors, warnings, and information

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 中，默认目录是 RAMDISK 虚拟磁盘中的临时存储空间，其大小可能低至 32 MB。日志文件会自动被归档；归档后的日志文件会在文件名后添加 `.bak` 扩展名，并生成新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。如果使用未加入域的网络共享资源，请在使用 `DISM` 日志路径之前，先使用 `net use` 命令结合域凭据来设置访问权限。

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
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NoRpFix
禁用对重新解析点标签的修复功能。重新解析点是一种文件，它在文件系统中包含指向另一个文件的链接。如果未指定该参数，则系统将不会捕获那些指向 *ImagePath* 参数所指定路径之外的位置的重新解析点。

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
指定一个临时目录，该目录将在执行维护操作（如文件提取）时被使用。此目录必须存在于本地系统中。如果未指定临时目录，默认会使用 `\Windows\%Temp%` 目录，且每次运行 DISM 时该目录下的子目录名称会由随机生成的十六进制值决定。每次操作完成后，临时目录中的所有内容都会被删除。不建议将网络共享位置作为临时目录来用于展开安装包（.cab 或 .msu 文件）。用于文件提取的临时目录应始终是本地目录。

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
将一个卷镜像标记为可启动镜像。此参数仅适用于 Windows PE 镜像。在一个 .wim 文件中，只能有一个卷镜像被标记为可启动的。

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

### -SupportEa
可以捕获扩展属性。必须明确指定相应的开关才能捕获这些扩展属性。如果组件中设置了扩展属性位，并且这些组件需要被包含在WIM镜像中，DISM会将其捕获；如果没有设置这些属性位，DISM就不会对其进行处理。只有CAB包中的“收件箱”组件（inbox components）和驱动程序才会包含这些扩展属性位，而AppX包组件或Win32应用程序组件则不会包含这些属性位。名称中以 `$Kernel.` 为前缀的扩展属性会被忽略，因为系统只会捕获用户模式下的扩展属性。

如果您在 Windows 10（版本 1607 或更高版本）中使用 DISM 来捕获扩展属性，然后使用较早版本的 DISM 来应用映像，操作本身会成功完成，但扩展属性不会被设置到所应用的映像中。

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
检查错误和文件重复情况。例如，在执行“应用”操作时（使用 **Add-WindowsImage** cmdlet），会核对所应用文件的大小和哈希值与源镜像文件是否一致；而在执行“捕获”操作时（使用 **New-WindowsImage** cmdlet），在将文件捕获为Windows镜像后，会将该文件写入临时文件，并逐位与其原始文件进行比较。

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
指定该图像将被格式化，以便安装在支持 Windows 映像格式启动（WIMBoot）的系统上。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.DismCommands.ImageObject

### Microsoft.Dismcommands.ImageObjectWithState

## 输出

### Microsoft.Dism Commands.OfflineImageObject

## 备注

## 相关链接

[Dismount-WindowsImage](./Dismount-WindowsImage.md)

[展开 Windows 图像](./Expand-WindowsImage.md)

[Export-WindowsImage](./Export-WindowsImage.md)

[Get-WindowsImage](./Get-WindowsImage.md)

[Mount-WindowsImage](./Mount-WindowsImage.md)

[Remove-WindowsImage](./Remove-WindowsImage.md)

[修复Windows镜像](./Repair-WindowsImage.md)

[Save-WindowsImage](./Save-WindowsImage.md)

[Split-WindowsImage](./Split-WindowsImage.md)
