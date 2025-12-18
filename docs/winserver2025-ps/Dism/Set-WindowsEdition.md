---
description: 使用此主题来帮助您使用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/set-windowsedition?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WindowsEdition
---

# Set-WindowsEdition

## 摘要
将Windows镜像升级到更高版本。

## 语法

```
Set-WindowsEdition -Edition <String> -Path <String> [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Set-WindowsEdition` cmdlet 可将 Windows 镜像升级为更高版本的操作系统。你可以使用 `Get-WindowsEdition` 并配合 `Target` 参数来查看某张镜像中支持哪些操作系统版本。

你不应该在对某个系统镜像进行了更高版本升级之后再使用 `Set-WindowsEdition` 命令。建议你在该版本系列中可用的最低版本上使用这个选项。

您只能更改正在运行的操作系统上的Windows Server镜像的版本，而不能更改在线Windows客户端镜像的版本。

## 示例

#### 示例 1：更改图片的版本
```
PS C:\> Set-WindowsEdition -Path "c:\offline" -Edition "Ultimate"
```

这个命令会将挂载到 c:\offline 目录中的 Windows 镜像的版本更改为“Ultimate”版本。

## 参数

### -Edition
指定要将Windows镜像更改为的目标版本。

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
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogPath
指定日志文件的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 施工区（其大小可能低至 32 MB）。日志文件会自动被归档；归档后的日志文件会在原文件名后加上 `.bak` 扩展名进行保存，并同时生成一个新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。当使用未加入域的网络共享资源时，请先使用 `net use` 命令结合相应的域凭据来设置访问权限，然后再指定 DISM 日志文件的路径。

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

### -Path
指定要维护的离线 Windows 镜像的根目录的完整路径。如果名为 “Windows” 的目录不是根目录的子目录，则必须指定 “WindowsDirectory”。

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

### -ScratchDirectory
指定一个临时目录，用于在服务过程中提取文件以供使用。该目录必须存在于本地系统中。如果未指定此目录，则会使用 `\Windows\%Temp%` 目录，并且每次运行 DISM 时都会为其生成一个随机十六进制值的子目录名称。每个操作完成后，临时目录中的内容会被删除。不建议将网络共享位置作为临时目录来用于展开安装包（.cab 或 .msu 文件）。在服务过程中用于提取文件的临时目录应是一个本地目录。

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

### -SystemDrive
指定BootMgr文件所在的路径。只有当BootMgr文件位于与你运行命令的分区不同的分区上时，才需要设置此参数。使用-SystemDrive选项可以从Windows PE环境中对已安装的Windows镜像进行维护或操作。

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

### -WindowsDirectory
指定相对于图像路径的 Windows 目录的路径。该路径不能是 Windows 目录的完整路径，而应该是一个相对路径。如果未指定，默认值为离线图像目录根目录下的 Windows 目录。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dismcommands.ImageObject

### Microsoft.Dism Commands.EditionObject

## 输出

### Microsoft.Dismcommands.ImageObject

## 备注

## 相关链接

[Get-WindowsEdition](./Get-WindowsEdition.md)

[Set-WindowsProductKey](./Set-WindowsProductKey.md)

