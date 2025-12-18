---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/remove-windowspackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-WindowsPackage
---

# 移除Windows软件包

## 摘要
从Windows镜像中删除一个软件包。

## 语法

### 离线模式
```
Remove-WindowsPackage [-PackagePath <String>] [-PackageName <String>] [-NoRestart] -Path <String>
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 在线
```
Remove-WindowsPackage [-PackagePath <String>] [-PackageName <String>] [-NoRestart] [-Online]
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Remove-WindowsPackage` cmdlet 用于从镜像中删除指定的 `.cab` 文件包。只能指定 `.cab` 文件；不能使用此命令来删除 `.msu` 文件。

使用此命令从离线镜像中删除某个软件包并不会减小镜像的大小。

## 示例

### 示例 1：从正在运行的操作系统镜像中删除某个软件包
```
PS C:\> Remove-WindowsPackage -Online -PackageName "Microsoft-Windows-Backup-Package~31bf3856ad364e35~x86~~6.1.7601.16525"
```

此命令会从正在运行的Windows操作系统中删除指定的软件包。

### 示例 2：从已挂载的操作系统镜像中删除一个软件包
```
PS C:\> Remove-WindowsPackage -Path "c:\offline" -PackagePath "c:\packages\package.cab"
```

此命令会从挂载到 c:\offline 的 Windows 映像中删除位于 c:\packages\package.cab 的程序包。

## 参数

### -LogLevel
指定日志中显示的最大输出级别。默认的日志级别为 3。允许的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及常规信息  
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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK scratch space（临时存储空间），其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件会在文件名后加上 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件都会被覆盖。如果使用未加入域的网络共享资源，请在使用 `DISM` 日志的路径设置之前，先使用 `net use` 命令并结合相应的域凭据来设置访问权限。

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

### -NoRestart
禁止重新启动。如果不需要重新启动，此命令将不会执行任何操作。该选项可以防止应用程序提示用户重新启动，或者阻止应用程序自动重新启动。

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
指定Windows镜像中一个软件包的名称。

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

### -PackagePath
指定一个.cab文件的路径。

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
指定一个临时目录，该目录将在执行服务操作（如文件提取）时被使用。该目录必须存在于本地系统中。如果未指定临时目录，则系统会使用 `\Windows\%Temp%\` 目录，并为每次 DISM 操作生成一个随机十六进制值的子目录名称。每次操作完成后，该临时目录中的所有内容都会被删除。不建议将网络共享位置作为用于解压安装包（.cab 或 .msu 文件）的临时目录；用于服务过程中文件提取操作的目录应始终是本地目录。

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
指定 BootMgr 文件所在的路径。仅当 BootMgr 文件位于与您运行命令的分区不同的分区上时，才需要指定该路径。使用 `-SystemDrive` 选项可以从 Windows PE 环境中管理服务已安装的 Windows 映像。

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
指定相对于图像路径的Windows目录的路径。该路径不能是Windows目录的完整路径，而应该是一个相对路径。如果未指定，则默认值为离线图像目录根目录下的Windows目录。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dism Commands.ImageObject

### Microsoft.DismCommands.BasicPackageObject

### Microsoft.Dismcommands.AdvancedPackageObject

## 输出

### Microsoft.Dism Commands.ImageObject

## 备注

## 相关链接

[Get-WindowsPackage](./Get-WindowsPackage.md)

[Add-WindowsPackage](./Add-WindowsPackage.md)

[Disable-WindowsOptionalFeature](./ Disable-WindowsOptionalFeature.md)

