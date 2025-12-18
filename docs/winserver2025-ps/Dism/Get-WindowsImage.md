---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/get-windowsimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WindowsImage
---

# Get-WindowsImage

## 摘要
获取关于WIM或VHD文件中Windows镜像的信息。

## 语法

### InputByFilePath
```
Get-WindowsImage -ImagePath <String> [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

### InputByFilePathAndName
```
Get-WindowsImage -ImagePath <String> -Name <String> [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

### InputByFilePathAndIndex
```
Get-WindowsImage -ImagePath <String> -Index <UInt32> [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

### InputByMounted
```
Get-WindowsImage [-Mounted] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

## 描述
`Get-WindowsImage` cmdlet 可以获取 WIM（Windows Imaging Format）或 VHD（Virtual Hard Disk）文件中包含的 Windows 镜像的相关信息。

使用 *Mounted* 参数来获取有关映射到本地计算机目录上的任何 Windows 镜像的信息。

使用 *ImagePath* 参数来获取特定 WIM 或 VHD 文件中图像的相关信息。

使用 *Index* 或 *Name* 参数可以获取 WIM 或 VHD 文件中特定图像的详细信息。对于 VHD 文件，*Index* 的值必须为 1。

## 示例

### 示例 1：获取所有已挂载图像的信息
```
PS C:\> Get-WindowsImage -Mounted
```

此命令可获取有关本地计算机上所有已挂载的Windows镜像的信息，包括挂载路径等详细信息。

### 示例 2：获取关于某个已挂载镜像的信息
```
PS C:\> Get-WindowsImage -ImagePath "c:\imagestore\install.wim" -Name Ultimate
```

这个命令可以获取关于名为“Ultimate”的Windows镜像的详细信息，该镜像位于c:\imagestore目录下的install.wim文件中。

### 示例 3：获取关于特定图像的信息
```
PS C:\> Get-WindowsImage -ImagePath "c:\imagestore\install.vhd"
```

这个命令可以获取关于位于 c:\imagestore 目录下的 install.vhd 文件中所包含的 Windows 镜像的基本信息。

## 参数

### -ImagePath
指定 WIM 或 VHD 文件的位置。

```yaml
Type: String
Parameter Sets: InputByFilePath, InputByFilePathAndName, InputByFilePathAndIndex
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Index
用于指定 Windows 映像在 WIM 或 VHD 文件中的索引编号。对于 VHD 文件，索引值必须为 1。

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
Default value: 3
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogPath
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 擦除空间，其容量可能低至 32 MB。日志文件会自动归档；归档后的日志文件会在文件名后添加 `.bak` 扩展名，并生成新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。当使用未加入域的网络共享资源时，请先使用 `net use` 命令并输入域凭据来设置访问权限，然后再设置 DISM 日志的路径。

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

### -Mounted
获取所有映射到本地计算机上目录中的图像的相关信息，包括这些图像的安装路径（即挂载路径）。

```yaml
Type: SwitchParameter
Parameter Sets: InputByMounted
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定 WIM 或 VHD 文件中图像的名称。

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

### -ScratchDirectory
指定一个临时目录，该目录将在执行服务维护操作时用于提取文件。此目录必须存在于本地计算机上。如果未指定临时目录，默认使用 `\Windows\%Temp%\` 目录，且每次运行 DISM 时，该目录下的子目录名称会生成一个随机的十六进制值。每次操作完成后，临时目录中的文件都会被删除。不建议将网络共享位置用作用于安装软件包（.cab 或 .msu 文件）的临时目录。在执行服务维护操作时用于提取文件的临时目录应为本地目录。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dism CommandsIMAGEObject

## 输出

### Microsoft.DismCommands.ImageInfoObject

### Microsoft.Dism Commands.MountedImageInfoObject

### Microsoft.Dism Commands.WimImageInfoObject

### Microsoft.Dism Commands.BasicImageInfoObject

## 备注

## 相关链接

[Dismount-WindowsImage](./Dismount-WindowsImage.md)

[Mount-WindowsImage](./Mount-WindowsImage.md)

[修复Windows映像](./Repair-WindowsImage.md)

[保存Windows镜像](./Save-WindowsImage.md)

