---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/get-windowsdriver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WindowsDriver
---

# Get-WindowsDriver

## 摘要
显示有关Windows镜像中驱动程序的信息。

## 语法

### 离线
```
Get-WindowsDriver [-All] [-Driver <String>] -Path <String> [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 在线
```
Get-WindowsDriver [-All] [-Driver <String>] [-Online] [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Get-WindowsDriver` cmdlet 可以显示在线或离线 Windows 镜像中驱动程序包的相关信息。你可以查看镜像中所有驱动程序的基本信息，也可以查看某个特定驱动程序的详细信息。

## 示例

### 示例 1：获取在线图片中的所有驱动程序信息
```
PS C:\> Get-WindowsDriver -Online -All
```

这个命令可以获取在线Windows镜像中的所有驱动程序。

### 示例 2：从已挂载的镜像中获取第三方驱动程序
```
PS C:\> Get-WindowsDriver -Path "c:\offline"
```

这个命令用于从已挂载的Windows镜像中获取第三方驱动程序。

### 示例 3：获取已挂载镜像中某个驱动程序的详细信息
```
PS C:\> Get-WindowsDriver -Path "c:\offline" -Driver "OEM1.inf"
```

这个命令可以获取已挂载的Windows镜像中OEM1.inf驱动程序的详细信息。

### 示例 4：获取已挂载镜像中指定位置上的驱动程序的详细信息
```
PS C:\> Get-WindowsDriver -Path "c:\offline" -Driver "c:\drivers\Usb\Usb.inf"
```

这个命令可以获取关于已挂载的Windows镜像中Usb.inf驱动程序的详细信息。

## 参数

### -All
显示有关默认驱动程序的信息。如果您不指定此参数，则仅会显示第三方驱动程序和已列出的驱动程序。

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

### -Driver
指定包含所需详细信息的驱动程序的 `.inf` 文件的 `.inf` 文件或文件夹。当您指定一个文件夹时，无效的驱动程序包（即不符合 `.inf` 格式的文件）将被忽略。

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

### -LogLevel
用于指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及常规信息  
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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 中，默认目录是 RAMDISK 虚拟磁盘（其可用空间可能低至 32 MB）。日志文件会自动被归档；归档后的日志文件名称后会添加 `.bak` 扩展名，并且系统会生成新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先通过 `net use` 命令结合域凭据来配置访问权限。

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

### -Online
指定该操作应在当前在本地计算机上运行的操作系统上执行。

```yaml
Type: SwitchParameter
Parameter Sets: Online
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path
指定要维护的离线 Windows 镜像的根目录的完整路径。如果名为 “Windows” 的目录不是根目录的子目录，则必须指定 “WindowsDirectory”。

```yaml
Type: String
Parameter Sets: Offline
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScratchDirectory
指定一个临时目录，用于在服务过程中提取文件。该目录必须存在于本地系统中。如果未指定目录，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时，该目录下的子目录名称都会生成一个随机十六进制值。每次操作完成后，临时目录中的所有内容都会被删除。不建议将网络共享位置作为临时目录来解压用于安装的包文件（.cab 或 .msu 文件）。在服务过程中用于提取文件的临时目录应始终是本地目录。

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
指定BootMgr文件所在的路径。只有在BootMgr文件位于与执行命令的分区不同的分区上时，才需要指定该路径。使用 `-SystemDrive` 参数可以从Windows PE环境中对已安装的Windows镜像进行维护（即对Windows系统进行更新或修复操作）。

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
指定相对于图像路径的 Windows 目录的路径。该路径不能是 Windows 目录的完整路径，而应该是一个相对路径。如果未指定，默认值为离线图像目录根目录中的 Windows 目录。

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

## 输出

### Microsoft.DismCommands.BasicDriverObject

### Microsoft.Dism Commands.AdvancedDriverObject

## 备注

## 相关链接

[Add-WindowsDriver](./Add-WindowsDriver.md)

[Remove-WindowsDriver](./Remove-WindowsDriver.md)

