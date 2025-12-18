---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/remove-windowsdriver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-WindowsDriver
---

# 删除 Windows 驱动程序

## 摘要
从离线的Windows镜像中删除某个驱动程序。

## 语法

```
Remove-WindowsDriver -Driver <String> -Path <String> [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Remove-WindowsDriver` cmdlet 可以从离线的 Windows 镜像中删除第三方驱动程序包。

注意：删除对系统启动至关重要的驱动程序包可能会导致离线Windows镜像无法正常启动。

## 示例

### 示例 1：从图像中移除驱动程序相关的内容
```
PS C:\> Remove-WindowsDriver -Path "c:\offline" -Driver "OEM1.inf"
```

这个命令会从已挂载的Windows镜像中删除OEM1.inf驱动程序。

## 参数

### -Driver
请指定包含您想要添加的驱动程序对应的 `.inf` 文件的 `.inf` 文件或文件夹。当第三方驱动程序被添加到镜像中时，它们的名称会被设置为 `OEM0.inf`、`OEM1.inf` 等。要删除某个驱动程序，必须指定其对应的公开名称（例如 `OEM1.inf`）。默认驱动程序是无法被删除的。

当您指定一个文件夹时，那些无效的驱动程序包（即不符合要求的 `.inf` 文件）将被忽略。

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
指定日志中显示的最大输出级别。默认的日志级别为 3。允许的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误和警告信息  
- 3 = 显示错误、警告以及信息性内容  
- 4 = 显示上述所有信息，外加调试输出

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件名称后面会添加 `.bak` 扩展名，并且系统会生成一个新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先使用 `net use` 命令结合相应的域凭据来配置访问权限。

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
指定一个临时目录，用于在服务过程中提取文件以供使用。该目录必须存在于本地计算机上。如果未指定临时目录，则系统会使用 `\Windows\%Temp%\` 目录，并为每次 DISM 操作生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的内容都会被删除。不建议将网络共享位置作为临时目录来解压安装包（.cab 或 .msu 文件）。用于在服务过程中提取文件的临时目录应为本地目录。

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
指定 BootMgr 文件所在的路径。只有当 BootMgr 文件位于与运行命令的分区不同的分区时，才需要提供该路径。使用 `-SystemDrive` 选项可以从 Windows PE 环境中维护已安装的 Windows 映像。

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
指定相对于镜像路径的Windows目录的路径。这不能是Windows目录的完整路径，而应该是一个相对路径。如果未指定，默认值是离线镜像目录根目录下的Windows目录。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dism Commands.ImageObject

### Microsoft.Dism Commands.BasicDriverObject

### Microsoft.DismCommands.AdvancedDriverObject

## 输出

### Microsoft.Dism Commands.ImageObject

## 备注

## 相关链接

[Get-WindowsDriver](./Get-WindowsDriver.md)

[Add-WindowsDriver](./Add-WindowsDriver.md)

