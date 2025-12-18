---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/get-windowsimagecontent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WindowsImageContent
---

# Get-WindowsImageContent

## 摘要
显示指定图像中的文件和文件夹列表。

## 语法

### InputByFilePathAndName
```
Get-WindowsImageContent -ImagePath <String> -Name <String> [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

### InputByFilePathAndIndex
```
Get-WindowsImageContent -ImagePath <String> -Index <UInt32> [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Get-WindowsImageContent` cmdlet 可以显示指定 Windows 镜像中的文件和文件夹列表。

此cmdlet不适用于虚拟硬盘（VHD）文件。

## 示例

### 示例 1：列出图像文件和文件夹
```
PS C:\> Get-WindowsImageContent -ImagePath "c:\imagestore\install.wim" -Index 1
```

该命令会列出位于 c:\imagestore\install.wim 文件中的第一个镜像所包含的文件和文件夹。

### 示例 2：列出指定图像文件所在的文件夹中的所有文件和文件夹
```
PS C:\> Get-WindowsImageContent -ImagePath "c:\imagestore\install.wim" -Name "Windows Pro"
```

此命令会列出位于 `c:\imagestore\install.wim` 文件夹中的名为 “Windows Pro” 的镜像文件及文件夹内容。

## 参数

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
指定 WIM 或 VHD 文件中某个 Windows 镜像的索引编号。对于 VHD 文件而言，该索引号必须为 1。

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘（其存储空间可能小至 32 MB）。日志文件会自动被归档；归档后的文件名会在原文件名后添加 `.bak` 扩展名，并生成新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先通过 `net use` 命令结合相应的域凭据来配置访问权限。

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
Parameter Sets: InputByFilePathAndName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScratchDirectory
指定一个临时目录，用于在服务期间提取文件。该目录必须存在于本地系统中。如果未指定目录，则会使用 `\Windows\%Temp%` 目录，并且每次运行 DISM 时都会为该目录生成一个随机十六进制数值作为子目录名称。每次操作完成后，临时目录中的内容会被删除。不建议使用网络共享位置作为临时目录来解压用于安装的包文件（.cab 或 .msu 文件）。在服务期间用于提取文件的临时目录应该是本地目录。

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

### System.String[]

### Microsoft.Dism Commands.ImageObject

### Microsoft.Dism Commands.ImageObjectWithState

## 输出

### System.String[]

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

