---
description: 将Windows镜像（存储在WIM或VHD文件中）安装到本地计算机的某个目录中。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 10/06/2021
online version: https://learn.microsoft.com/powershell/module/dism/mount-windowsimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Mount-WindowsImage
---

# Mount-WindowsImage

## 摘要
将Windows镜像（存储在WIM或VHD文件中）安装到本地计算机的某个目录中。

## 语法

### OfflineIndex
```
Mount-WindowsImage -Path <String> -ImagePath <String> -Index <UInt32> [-ReadOnly] [-Optimize] [-CheckIntegrity]
 [-SupportEa] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

### OfflineName
```
Mount-WindowsImage -Path <String> -ImagePath <String> -Name <String> [-ReadOnly] [-Optimize] [-CheckIntegrity]
 [-SupportEa] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 重新挂载（文件系统或设备）
```
Mount-WindowsImage -Path <String> [-Remount] [-SupportEa] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Mount-WindowsImage` cmdlet 将 WIM 或 VHD 文件中的 Windows 镜像映射到指定的目录中，以便对其进行维护或修复操作。

*Path* 参数指定了您想要挂载 Windows 镜像的位置。

`ImagePath` 参数指定了包含您想要挂载的 Windows 镜像的 WIM 或 VHD 文件的位置。

使用 *Index* 或 *Name* 参数来指定您想要挂载的 WIM 或 VHD 文件中的哪张图片。对于 VHD 文件，*Index* 必须为 1。

“Optimize”参数可以减少初始挂载图像所需的时间。但是，那些通常在挂载过程中会执行的操作将改为在你第一次访问某个目录时才完成。因此，在使用“Optimize”参数挂载图像后，首次访问该目录所需的时间可能会变长。

`Remount` 参数用于重新挂载一个位于 WIM 或 VHD 文件中的镜像。该镜像之前已经被挂载到指定的路径上，但由于某些原因无法被正常访问（例如需要进行维护或修复操作）。

`CheckIntegrity` 参数用于检测和跟踪 `.wim` 文件的损坏情况。如果 `DISM` 在使用 `Mount-WindowsImage` cmdlet 时发现 `.wim` 文件已损坏，`CheckIntegrity` 会立即停止相关操作。

*CheckIntegrity* 参数不适用于虚拟硬盘（VHD）文件。

## 示例

### 示例 1：将来自 `install.vhd` 文件的镜像挂载到某个目录中
```
PS C:\> Mount-WindowsImage -ImagePath "c:\imagestore\install.vhd" -Index 1 -Path "c:\offline"
```

此命令会将install.vhd文件中包含的Windows镜像安装到c:\offline目录中。

### 示例 2：以只读权限将镜像挂载到文件的某个索引位置
```
PS C:\> Mount-WindowsImage -ImagePath "c:\imagestore\install.wim" -Index 2 -Path "c:\offline" -ReadOnly
```

此命令会将 install.wim 文件中索引为 2 的 Windows 镜像以只读权限挂载到 c:\offline 目录下。

### 示例 3：在文件的某个索引位置挂载一个镜像
```
PS C:\> Mount-WindowsImage -ImagePath "c:\imagestore\install.wim" -Index 2 -Path "c:\offline" -Optimize
```

此命令会将安装.wim文件中索引为2的Windows镜像挂载到c:\offline目录下，从而实现更快的初始挂载速度。不过后续的操作可能会变慢一些。

### 示例 4：重新挂载之前已挂载到某个无法访问目录上的镜像
```
PS C:\> Mount-WindowsImage -Path "c:\offline" -Remount
```

此命令用于重新挂载一个已经挂载到 `c:\offline` 目录中的 Windows 镜像，但由于某些原因无法对其进行维护或修复操作（因此变得无法访问）。

### 示例 5：在文件的指定索引处挂载镜像，并使用 `checkintegrity` 和优化参数
```PowerShell
PS C:\> Mount-WindowsImage -Checkintegrity -ImagePath "c:\imagestore\install.wim" -Index 2 -Path "c:\offline" -Logpath C:\install.log -Optimize
```

此命令会将位于 `install.wim` 文件第 2 位置的 Windows 镜像安装到 `c:\offline` 目录中，同时使用 `Checkintegrity` 参数。该参数会要求系统生成日志文件，并加快初始安装过程的速度。不过，后续的操作可能会变得相对较慢。


## 参数

### -CheckIntegrity
当使用 **Dismount-WindowsImage** 或 **Save-WindowsImage** cmdlet 时，该功能可以检测并跟踪 .wim 文件的损坏情况。如果 DISM 在使用 **Mount-WindowsImage** cmdlet 时发现 .wim 文件已损坏，*CheckIntegrity* 会停止相关操作。不过，*CheckIntegrity* 参数不适用于虚拟硬盘（VHD）文件。

```yaml
Type: SwitchParameter
Parameter Sets: OfflineIndex, OfflineName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ImagePath
指定包含您想要挂载的Windows镜像的WIM或VHD文件的位置。

```yaml
Type: String
Parameter Sets: OfflineIndex, OfflineName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Index
用于指定 WIM 或 VHD 文件中 Windows 镜像的索引编号。对于 VHD 文件，该索引值必须为 1。

```yaml
Type: UInt32
Parameter Sets: OfflineIndex
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogLevel
用于指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及常规信息  
- 4 = 包括上述所有信息，此外还显示调试输出

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 内的临时存储空间，其大小可能低至 32 MB。日志文件会自动被归档；归档后的日志文件会在文件名后加上 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，原有的 `.bak` 文件都会被覆盖。如果使用未加入域的网络共享资源，请在使用 `DISM` 日志的路径设置之前，先通过 `net use` 命令并输入相应的域凭据来设置访问权限。

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
指定 WIM 或 VHD 文件中一张图片的名称。

```yaml
Type: String
Parameter Sets: OfflineName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Optimize
这种方式可以缩短初次挂载图像所需的时间。不过，那些通常在挂载过程中才会执行的操作，现在会改为在你第一次访问某个目录时才进行。因此，在使用“优化”（Optimize）参数挂载图像后，首次访问该目录所花费的时间可能会增加。

```yaml
Type: SwitchParameter
Parameter Sets: OfflineIndex, OfflineName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path
指定您希望在本地计算机上挂载 Windows 镜像的位置。

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

### -ReadOnly
指定该图像应以只读权限进行挂载。

```yaml
Type: SwitchParameter
Parameter Sets: OfflineIndex, OfflineName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Remount
将一张图像挂载到一个已经挂载在指定路径（*Path*）上的WIM或VHD文件中，但该文件因无法正常访问而无法进行维护或修复。

```yaml
Type: SwitchParameter
Parameter Sets: Remount
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScratchDirectory
指定一个临时目录，用于在服务过程中提取文件以供使用。该目录必须存在于本地计算机上。如果未指定目录，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时都会为该目录生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的内容都会被删除。不建议将网络共享位置作为用于解压安装包（.cab 或 .msu 文件）的临时目录；用于服务过程中临时提取文件的目录应该是本地目录。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dism Commands.ImageObject

### Microsoft.Dismcommands.ImageInfoObject

## 输出

### Microsoft.Dism Commands.ImageObject

## 备注

## 相关链接

[Dismount-WindowsImage](./Dismount-WindowsImage.md)

[Save-WindowsImage](./Save-WindowsImage.md)

[Get-WindowsImage](./Get-WindowsImage.md)

[修复Windows镜像](./Repair-WindowsImage.md)
