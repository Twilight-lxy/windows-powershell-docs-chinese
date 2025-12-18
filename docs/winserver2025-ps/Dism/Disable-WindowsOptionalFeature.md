---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/disable-windowsoptionalfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-WindowsOptionalFeature
---

# 禁用 Windows 的可选功能

## 摘要
禁用Windows镜像中的某个功能。

## 语法

### 在线
```
Disable-WindowsOptionalFeature -FeatureName <String[]> [-PackageName <String>] [-Remove] [-NoRestart] [-Online]
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 离线状态
```
Disable-WindowsOptionalFeature -FeatureName <String[]> [-PackageName <String>] [-Remove] [-NoRestart]
 -Path <String> [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>]
 [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Disable-WindowsOptionalFeature` cmdlet 可以禁用或删除 Windows 镜像中的可选功能。

使用 *Online* 参数来指定您本地计算机上运行的操作系统，或者使用 *Path* 参数来指定已挂载的 Windows 映像文件的位置。

`PackageName` 参数指定了该功能所属的包。当该包属于 Windows Foundation 包时，此参数是可选的。

`FeatureName` 参数用于指定要删除的功能。你可以在同一个包中指定多个功能，只需用逗号分隔各个功能名称即可。

“Remove”参数用于删除某个可选功能的文件，但不会从镜像中移除该功能的相应配置信息（即功能清单）。使用此参数可以减少Windows镜像所占用的磁盘空间。在安装完镜像后，您可以随时通过远程资源（如Windows Update或网络共享）恢复被删除的功能。有关“按需功能”（Features on Demand）的更多信息，请参阅TechNet库中的[配置Windows修复源](https://go.microsoft.com/fwlink/?LinkId=243077)。

## 示例

#### 示例 1：禁用一个可选功能
```
PS C:\> Disable-WindowsOptionalFeature -Online -FeatureName "Hearts"
```

此命令会禁用运行中的Windows操作系统中的一个可选功能（名为“Hearts”）。

### 示例 2：禁用图像中的某个功能
```
PS C:\> Disable-WindowsOptionalFeature -Path "c:\offline" -FeatureName "Calc" -PackageName "Microsoft.Windows.Calc.Demo~6595b6144ccf1df~x86~en~1.0.0.0" -Remove
```

此命令会禁用指定软件包中的可选功能“Calc”，该软件包位于被挂载到 c:\offline 目录的 Windows 镜像中。同时，除了清单文件（manifest file）外，所有其他文件都会被删除，从而减小 Windows 镜像的大小。该功能可以通过 **Enable-WindowsOptionalFeature** cmdlet 在任何时候恢复，或者在镜像部署后通过“按需使用功能”（Features on Demand）的方式重新启用。

## 参数

### -FeatureName
指定要禁用的功能的名称。如果您服务的Windows映像版本不是Windows® 8或更高版本，那么功能名称是区分大小写的。您可以使用Get-WindowsOptionalFeature来查找该映像中功能的名称。

```yaml
Type: String[]
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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 中，默认目录是 RAMDISK 内的临时存储空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的文件名称会添加 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 日志路径之前，先使用 `net use` 命令结合域凭据来设置访问权限。

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
抑制重启功能。如果不需要重启，该命令将不会执行任何操作。此选项可以防止应用程序提示用户重新启动，或阻止应用程序自动重启。

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
指定 Windows 镜像中某个软件包的名称。

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
指定要维护的离线 Windows 镜像的根目录的完整路径。如果名为 “Windows” 的目录不是根目录的子目录，则必须指定 `WindowsDirectory`。

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

### -Remove
该操作会移除某个可选功能的相关文件，但不会从镜像中删除该功能的配置信息（即功能清单）。您可以使用“Remove”命令来减少Windows镜像所占用的磁盘空间。在镜像安装完成后，您可以随时通过远程源（如Windows Update或网络共享）恢复该功能。

“Remove”功能仅适用于处理安装了Windows 8、Windows Server 2012或更高版本的操作系统的图像文件。

> [!注意] > 从 Windows 10 开始，为了支持“一键重置”功能（Push-Button Reset），该有效载荷（payload）不会从 Windows 10 设备中删除。但是，该有效载荷会从所有版本的 Windows Server 中被删除。

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

### -ScratchDirectory
指定一个临时目录，用于在服务过程中提取文件。该目录必须存在于本地计算机上。如果未指定目录，则会使用 `\Windows\%Temp%\` 目录，其中每个 DISM 运行都会生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的文件都会被删除。不建议将网络共享位置作为用于展开安装包（.cab 或 .msu 文件）的临时目录。在服务过程中用于提取文件的目录应为本地目录。

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
指定 BootMgr 文件所在位置的路径。只有当 BootMgr 文件位于与执行命令的分区不同的分区时，才需要指定该路径。使用 `-SystemDrive` 参数可以从 Windows PE 环境中管理服务已安装的 Windows 镜像。

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
指定相对于图像路径的 Windows 目录的路径。这不能是 Windows 目录的完整路径，而应该是一个相对路径。如果未指定，默认值将是离线图像目录根目录中的 Windows 目录。

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

### Microsoft.Dism Commands.ImageObject

### Microsoft.DismCommands.BasicFeatureObject

### Microsoft.DismCommands.AdvancedFeatureObject

## 输出

### Microsoft.Dism Commands.ImageObject

## 备注

## 相关链接

[Enable-WindowsOptionalFeature](./Enable-WindowsOptionalFeature.md)

[Get-WindowsOptionalFeature](./Get-WindowsOptionalFeature.md)

[Remove-WindowsPackage](./Remove-WindowsPackage.md)

