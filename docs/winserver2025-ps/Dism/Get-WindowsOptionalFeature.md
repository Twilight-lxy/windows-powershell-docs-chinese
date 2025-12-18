---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/get-windowsoptionalfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WindowsOptionalFeature
---

# Get-WindowsOptionalFeature

## 摘要
获取有关Windows镜像中可选功能的信息。

## 语法

### 离线模式
```
Get-WindowsOptionalFeature [-FeatureName <String>] [-PackageName <String>] [-PackagePath <String>]
 -Path <String> [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>]
 [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 在线
```
Get-WindowsOptionalFeature [-FeatureName <String>] [-PackageName <String>] [-PackagePath <String>] [-Online]
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Get-WindowsOptionalFeature` cmdlet 可以获取有关 Windows Foundation 包或 Windows 镜像中指定包中所有功能的信息（这些功能包括可选的 Windows 基础功能）。

使用 `PackageName` 或 `PackagePath` 参数来获取有关 Windows 镜像中特定包内所有功能的信息。

*FeatureName* 参数可以获取有关 Windows 镜像中某个特定功能的更多详细信息。如果该功能不属于 Windows Foundation 包，那么必须使用 *PackageName* 或 *PackagePath* 参数来指定该功能的父包。

使用 *Online* 参数来指定您本地计算机上运行的操作系统，或者使用 *Path* 参数来指定已挂载的 Windows 镜像的位置。

## 示例

### 示例 1：列出当前操作系统中的可选功能
```powershell
PS C:\> Get-WindowsOptionalFeature -Online
```

此命令列出了正在运行的Windows操作系统中的所有可选功能。

### 示例 2：在已挂载的镜像中列出软件包中的可选功能
```powershell
PS C:\> Get-WindowsOptionalFeature -Path "c:\offline" -PackageName "Microsoft-Windows-Backup-Package~31bf3856ad364e35~x86~~6.1.7601.16525"
```

此命令会显示指定软件包中所有可选功能的列表，这些功能位于已挂载到 c:\offline 的 Windows 镜像文件中。

### 示例 3：获取已挂载镜像中某个功能的详细信息
```powershell
PS C:\> Get-WindowsOptionalFeature -Path "c:\offline" -FeatureName Hearts
```

此命令会显示有关“Hearts”这一功能的详细信息。该功能属于Windows Foundation Package的一部分，而这个包包含在已挂载到c:\offline目录的Windows镜像文件中。

### 示例 4：获取已挂载镜像中指定包中某个功能的详细信息
```powershell
PS C:\> Get-WindowsOptionalFeature -Path "c:\offline" -FeatureName "MyFeature" -PackagePath "c:\packages\package.cab"
```

该命令会显示关于名为“MyFeature”的功能的详细信息。该功能位于路径为“c:\package\package.cab” 的文件中，而这个文件属于安装在 “c:\offline” 路径下的 Windows 映像文件所包含的软件包中。

### 示例 5：使用通配符获取有关功能的详细信息
```powershell
PS C:\> Get-WindowsOptionalFeature -Online -FeatureName *Hyper-V*
```

该命令通过使用通配符形式的特性名称，返回有关正在运行的操作系统中Hyper-V可选特性的详细信息。

## 参数

### -FeatureName
指定要获取详细信息的功能的名称。如果您维护的是非 Windows 8 的 Windows 镜像，则功能名称区分大小写。

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
用于指定日志中显示的最大输出级别。默认的日志级别为 3。允许的值如下：  
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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK（随机存取存储器磁盘），其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件名称后会添加“.bak”后缀，同时会生成一个新的日志文件。每次日志文件被归档时，原有的“.bak”文件会被覆盖。如果使用未加入域的网络共享资源，请在设置 DISM 日志路径之前，先使用 `net use` 命令并结合域凭据来配置访问权限。

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
指定该操作应在当前正在本地计算机上运行的操作系统上执行。

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
指定在 Windows 镜像中列出的软件包的名称。使用 `PackageName` 参数可以获取该软件包中的所有功能；使用 `-featureName` 和 `PackageName` 参数可以获得关于软件包中特定功能的更详细信息。

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
指定Windows镜像中.cab文件的位置。可以使用*PackagePath*参数来获取包中的所有功能；使用*FeatureName*和*PackagePath*参数可以获取包中特定功能的更详细信息。

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
指定一个临时目录，该目录将在执行服务维护操作时用于解压文件。此目录必须存在于本地计算机上。如果未指定临时目录，则系统会使用 `\Windows\%Temp%\` 目录，并为每次 DISM 操作生成一个随机十六进制值的子目录名称。每次操作完成后，该临时目录中的所有内容都会被删除。不建议将网络共享位置作为用于解压安装包（.cab 或 .msu 文件）的临时目录；用于服务维护操作的临时文件解压目录应始终是本地目录。

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
指定BootMgr文件所在位置的路径。只有当BootMgr文件位于与您运行命令的分区不同的分区上时，才需要指定此路径。使用 `-SystemDrive` 参数可以从Windows PE环境中对已安装的Windows镜像进行维护或操作。

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
指定相对于图像路径的 Windows 目录的路径。该路径不能是 Windows 目录的完整路径，而应该是一个相对路径。如果未指定，则默认值为离线图像目录根目录下的 Windows 目录。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dism Commands.ImageObject

## 输出

### Microsoft.Dism Commands.BasicFeatureObject

### Microsoft.DismCommands.AdvancedFeatureObject

## 备注

## 相关链接

[Add-WindowsPackage](./Add-WindowsPackage.md)

[Enable-WindowsOptionalFeature](./Enable-WindowsOptionalFeature.md)

[Get-WindowsPackage](./Get-WindowsPackage.md)

