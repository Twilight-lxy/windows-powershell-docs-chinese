---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/remove-windowsimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-WindowsImage
---

# 删除 Windows 图像文件

## 摘要
从一个包含多个卷镜像的WIM文件中删除指定的卷镜像。

## 语法

### InputByFilePathAndName
```
Remove-WindowsImage -ImagePath <String> -Name <String> [-CheckIntegrity] [-LogPath <String>]
 [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

### InputByFilePathAndIndex
```
Remove-WindowsImage -ImagePath <String> -Index <UInt32> [-CheckIntegrity] [-LogPath <String>]
 [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Remove-WindowsImage` cmdlet 用于从包含多个卷镜像的 WIM 文件中删除指定的卷镜像。该 cmdlet 仅会删除元数据条目和 XML 条目，而不会删除流数据，也不会优化 WIM 文件本身。

此命令行选项不适用于虚拟硬盘（VHD）文件。

## 示例

### 示例 1：从 WIM 文件中删除第一张图片
```
PS C:\> Remove-WindowsImage -ImagePath "c:\imagestore\custom.wim" -Index 1 -CheckIntegrity
```

这个命令会删除 c:\imagestore\custom.wim 文件中的第一张图片。

### 示例 2：通过名称从 WIM 文件中删除图片
```
PS C:\> Remove-WindowsImage -ImagePath "c:\imagestore\custom.wim" -Name "Starter" -CheckIntegrity
```

此命令会删除位于 c:\imagestore\custom.wim 中的名为 “Starter” 的图像文件。

## 参数

### -CheckIntegrity
当使用 `Add-WindowsImage`、`Dismount-WindowsImage` 或 `Save-WindowsImage` cmdlet 时，该工具能够检测并追踪 `.wim` 文件的损坏情况。如果在使用 `Expand-WindowsImage` 或 `Mount-WindowsImage` cmdlet 时 DISM 发现 `.wim` 文件已损坏，`CheckIntegrity` 会立即停止相关操作。

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
指定 WIM 或 VHD 文件中某个 Windows 镜像的索引编号。对于 VHD 文件而言，索引编号必须是 1。

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
用于指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及信息性内容  
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
指定用于记录日志的完整路径和文件名。如果未设置，则默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 中，默认目录是 RAMDISK 虚拟磁盘（其容量可能低至 32 MB）。日志文件会自动被归档；归档后的日志文件会在原文件名后加上 `.bak` 扩展名进行保存，并同时生成一个新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先通过 `net use` 命令结合域凭据来配置访问权限。

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

### -ScratchDirectory
指定一个临时目录，用于在服务期间提取文件。该目录必须存在于本地计算机上。如果未指定临时目录，系统将使用 `\Windows\%Temp%\` 目录，并为每次运行 DISM 工具生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的文件都会被删除。不建议使用网络共享位置作为临时目录来解压用于安装的包文件（.cab 或 .msu 格式）。在服务期间用于提取文件的临时目录应为本地目录。

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

### Microsoft.DismCommands.ImageObject

### Microsoft.Dism Commands.ImageObjectWithState

## 输出

### Microsoft.DismCommands.ImageObject

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

[Save-WindowsImage](./Save-WindowsImage.md)

[Split-WindowsImage](./Split-WindowsImage.md)

