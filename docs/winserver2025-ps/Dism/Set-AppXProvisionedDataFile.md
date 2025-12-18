---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/set-appxprovisioneddatafile?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AppXProvisionedDataFile
---

# 设置 AppXProvisionedDataFile 文件

## 摘要
将自定义数据添加到已经在 Windows 映像中配置好的指定应用程序（.appx）包中。

## 语法

### 离线模式
```
Set-AppXProvisionedDataFile -PackageName <String> -CustomDataPath <String> -Path <String>
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 在线
```
Set-AppXProvisionedDataFile -PackageName <String> -CustomDataPath <String> [-Online]
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Set-AppXProvisionedDataFile` cmdlet 可将自定义数据添加到已预先配置在 Windows 镜像中的指定应用程序（.appx）包中。在添加自定义数据之前，必须先将该应用程序（.appx）包添加到该镜像中。

你不能在不支持应用程序的操作系统上安装应用程序包（.appx）。Windows Server 的 Server Core 安装版、Windows PE，以及任何早于 Windows 8 和 Windows Server 2012 的 Windows 版本都不支持此类应用程序。

要在 Windows Server 上安装和运行应用程序，必须先安装 [桌面体验组件](https://go.microsoft.com/fwlink/?LinkId=247330)。

使用 *Online* 参数来指定您本地计算机上运行的操作系统，或者使用 *Path* 参数来指定已挂载的 Windows 镜像的位置。

## 示例

### 示例 1：将自定义数据文件添加到应用程序包中，以便在当前运行的操作系统中使用
```
PS C:\> Set-AppXProvisionedDataFile -Online -PackageName "MyAppxPkg" -CustomDataPath "c:\Appx\myCustomData.dat"
```

此命令将自定义数据文件 `c:\Appx\myCustomData.dat` 添加到已经添加到正在运行的 Windows 操作系统中的应用程序包 `MyAppxPkg` 中。

### 示例 2：为已挂载的镜像添加自定义数据文件到应用程序包中
```
PS C:\> Set-AppxProvisionedDataFile -Path c:\offline -PackageName MyAppxPkg -CustomDataPath c:\Appx\myCustomData.dat
```

此命令将自定义数据文件 `c:\Appx\myCustomData.dat` 添加到应用程序包 `MyAppxPkg` 中，该应用程序包已被添加到挂载在 `c:\offline` 的 Windows 镜像中。

## 参数

### -CustomDataPath
为应用程序指定一个可选的自定义数据文件。您可以指定任何文件名。当该文件被添加到镜像中时，其名称会更改为“Custom.dat”。如果已经存在一个“Custom.dat”文件，则现有的文件将被覆盖。

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 中，默认目录是 RAMDISK 存储空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件名称后会加上 `.bak` 扩展名，并会生成一个新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件都会被覆盖。当使用未加入域的网络共享资源时，请先使用 `net use` 命令并输入域凭据来设置访问权限，然后再设置 DISM 日志的路径。

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

### -PackageName
指定Windows镜像中某个软件包的名称。

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
指定一个临时目录，用于在服务期间提取文件以供使用。该目录必须存在于本地系统中。如果未指定目录，则会使用 `\Windows\%Temp%` 目录，并且每次运行 DISM 时都会为该目录生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的内容都会被删除。不建议将网络共享位置作为用于安装包（.cab 或 .msu 文件）的临时目录。在服务期间用于提取文件的临时目录应为本地目录。

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
指定 BootMgr 文件所在的路径。仅当 BootMgr 文件位于与执行命令的分区不同的分区上时，才需要设置此路径。使用 `-SystemDrive` 选项可以从 Windows PE 环境中管理服务已安装的 Windows 镜像。

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
指定相对于图像路径的 Windows 目录的路径。这个路径不能是 Windows 目录的完整路径，而应该是一个相对路径。如果未指定，默认值将是离线图像目录根目录下的 Windows 目录。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dismcommands.ImageObject

### Microsoft.Dism Commands.AppxPackageObject

## 输出

### Microsoft.Dismcommands.ImageObject

## 备注

## 相关链接

[Add-AppxProvisionedPackage](./Add-AppxProvisionedPackage.md)

[Get-AppxProvisionedPackage](./Get-AppxProvisionedPackage.md)

[Remove-AppxProvisionedPackage](./Remove-AppxProvisionedPackage.md)

