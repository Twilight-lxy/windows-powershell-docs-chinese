---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/split-windowsimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Split-WindowsImage
---

# Split-WindowsImage

## 摘要
将现有的.wim文件分割成多个只读的独立.wim文件。

## 语法

```
Split-WindowsImage -ImagePath <String> -SplitImagePath <String> -FileSize <UInt64> [-CheckIntegrity]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Split-WindowsImage` cmdlet 会在指定的目录中创建 `.swm` 文件，每个文件的名称都与 `path_to_swm` 的值相同，只是在文件名后加上一个数字。例如，如果你将 `path_to_swm` 设置为 `c:\Data.swm`，那么该命令会创建 `Data.swm`、`Data2.swm`、`Data3.swm` 等文件，这些文件分别对应分割后的 `.wim` 文件的不同部分，并将它们保存到 `C:` 目录中。

如果某个文件的体积超过了 *FileSize* 参数中指定的值，那么生成的多个分割后的 `.swm` 文件中至少会有一个文件的体积也会超过该参数指定的值，这样就能容纳这个较大的文件了。

此cmdlet不适用于虚拟硬盘（VHD）文件。

## 示例

### 示例 1：分割一个.wim 文件
```
PS C:\> Split-WindowsImage -ImagePath "c:\imagestore\install.wim" -SplitImagePath "c:\imagestore\splitfiles\split.swm" -FileSize 1024 -CheckIntegrity
```

此命令使用位于 c:\imagestore\install.wim 的图像文件来创建 split.swm、split2.swm、split3.swm 等文件。每个分割后的 .wim 文件的最大大小被设置为 1024 MB，并将这些文件保存到 C:\imagestore\splitfiles\ 目录中。

## 参数

### -CheckIntegrity
当与 **Add-WindowsImage**、**Dismount-WindowsImage** 或 **Save-WindowsImage** cmdlet 一起使用时，该工具能够检测并跟踪 .wim 文件的损坏情况。如果 DISM 在使用 **Expand-WindowsImage** 或 **Mount-WindowsImage** cmdlet 时发现 .wim 文件已损坏，CheckIntegrity 会立即停止相关操作。

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

### -FileSize
指定每个创建的.swm文件的最大大小（以兆字节MB为单位）。

```yaml
Type: UInt64
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
- 3 = 显示错误信息、警告信息以及详细信息  
- 4 = 显示前面列出的所有信息，还包括调试输出

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
指定日志文件的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘，其容量可能低至 32 MB。日志文件会自动被归档；归档后的文件名称会加上 `.bak` 扩展名，并且会生成一个新的日志文件。每次日志文件被归档时，原有的 `.bak` 文件都会被覆盖。如果使用的网络共享未加入域，请在使用 `DISM` 日志路径之前，先通过 `net use` 命令并输入域凭据来设置访问权限。

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
指定一个临时目录，用于在维护过程中提取文件。该目录必须存在于本地系统中。如果未指定临时目录，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时都会为该目录生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的文件都会被删除。不建议将网络共享位置用作扩展安装包（.cab 或 .msu 文件）的临时目录。用于在维护过程中提取文件的目录应为本地目录。

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

### -SplitImagePath
指定位置以及基础分割图像文件的名称。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dism Commands.ImageObject

### Microsoft.Dism Commands.ImageObjectWithState

## 输出

### Microsoft.Dism Commands.OfflineImageObject

## 备注

## 相关链接

[Add-WindowsImage](./Add-WindowsImage.md)

[Dismount-WindowsImage](./Dismount-WindowsImage.md)

[Expand-WindowsImage](./Expand-WindowsImage.md)

[Export-WindowsImage](./Export-WindowsImage.md)

[Get-WindowsImage](./Get-WindowsImage.md)

[Mount-WindowsImage](./Mount-WindowsImage.md)

[New-WindowsImage](./New-WindowsImage.md)

[修复Windows镜像](./Repair-WindowsImage.md)

[Remove-WindowsImage](./Remove-WindowsImage.md)

[Save-WindowsImage](./Save-WindowsImage.md)

