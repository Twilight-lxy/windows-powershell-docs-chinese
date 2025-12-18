---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/get-windowspackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WindowsPackage
---

# Get-WindowsPackage

## 摘要
获取有关Windows镜像中包的信息。

## 语法

### 离线状态
```
Get-WindowsPackage [-PackagePath <String>] [-PackageName <String>] -Path <String> [-WindowsDirectory <String>]
 [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

### 在线
```
Get-WindowsPackage [-PackagePath <String>] [-PackageName <String>] [-Online] [-WindowsDirectory <String>]
 [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

## 描述
`Get-WindowsPackage` cmdlet 可以获取有关 Windows 映像中所有包的信息，或者获取作为 `.cab` 文件提供的特定包的信息。

使用 *Online* 参数来指定本地计算机上正在运行的操作系统，或者使用 *Path* 参数来指定已挂载的 Windows 镜像的位置。

使用 `PackageName` 或 `PackagePath` 参数来获取有关 Windows 镜像中特定包的更详细信息，例如该包是否可以在不启动镜像的情况下完全离线安装。

您不能使用此命令来获取.msu文件的详细包信息，仅适用于.cab文件。

## 示例

### 示例 1：列出已挂载镜像中的软件包
```
PS C:\> Get-WindowsPackage -Path "c:\offline"
```

这个命令会列出所有安装到 c:\offline 路径下的 Windows 镜像中的软件包。

### 示例 2：在已挂载的镜像中列出有关软件包的详细信息
```
PS C:\> Get-WindowsPackage -Path "c:\offline" -PackageName "Microsoft-Windows-Backup-Package~31bf3856ad364e35~x86~~6.1.7601.16525"
```

此命令会显示关于指定软件包的详细信息，该软件包位于已挂载到 c:\offline 的 Windows 镜像中。

## 参数

### -LogLevel
用于指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及常规信息  
- 4 = 包括上述所有信息，再加上调试输出

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘（其存储空间可能小至 32 MB）。日志文件会自动被归档；归档后的日志文件会在原文件名后加上 `.bak` 扩展名进行保存，并同时生成一个新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先通过 `net use` 命令结合相应的域凭据来设置访问权限。

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
指定在 Windows 镜像中列出的软件包的名称。可以使用 `PackageName` 参数来获取关于该软件包的更多详细信息，例如该软件包是否可以在不启动镜像的情况下完全离线安装。

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
指定 Windows 镜像中某个 `.cab` 文件的位置。可以使用 `*PackagePath*` 参数来获取有关该镜像中特定包的更多详细信息，例如该包是否可以在不启动镜像的情况下完全离线安装。

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
指定一个临时目录，该目录将在执行维护操作（如文件提取）时被使用。此目录必须存在于本地系统中。如果未指定临时目录，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时都会为该目录生成一个随机十六进制值的子目录名称。每次维护操作完成后，临时目录中的所有内容都会被删除。不建议将网络共享位置作为用于安装包（.cab 或 .msu 文件）的临时目录。在执行维护操作期间用于文件提取的临时目录应当是本地目录。

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
指定 BootMgr 文件所在的路径。仅当 BootMgr 文件位于与您运行命令的分区不同的分区时，才需要指定该路径。使用 `-SystemDrive` 选项可以从 Windows PE 环境中管理服务已安装的 Windows 镜像。

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
指定相对于镜像路径的Windows目录的路径。这个路径不能是Windows目录的完整路径，而应该是一个相对路径。如果未指定，默认值将是离线镜像目录根目录中的Windows目录。

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

### Microsoft.DismCommands.ImageObject

## 输出

### Microsoft.DismCommands.BasicPackageObject

### Microsoft.Dism Commands.AdvancedPackageObject

## 备注

## 相关链接

[Add-WindowsPackage](./Add-WindowsPackage.md)

[Remove-WindowsPackage](./Remove-WindowsPackage.md)

