---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/enable-windowsoptionalfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-WindowsOptionalFeature
---

# 启用 Windows 可选功能

## 摘要
启用Windows镜像中的某个功能。

## 语法

### 在线
```
Enable-WindowsOptionalFeature -FeatureName <String[]> [-PackageName <String>] [-All] [-LimitAccess]
 [-Source <String[]>] [-NoRestart] [-Online] [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 离线模式
```
Enable-WindowsOptionalFeature -FeatureName <String[]> [-PackageName <String>] [-All] [-LimitAccess]
 [-Source <String[]>] [-NoRestart] -Path <String> [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Enable-WindowsOptionalFeature` cmdlet 可以在 Windows 镜像中启用或恢复某个可选功能。

使用 *Online* 参数来指定您本地计算机上正在运行的操作系统，或者使用 *Path* 参数来指定已挂载的 Windows 镜像的位置。

`PackageName` 参数用于指定该功能所属的包。当所使用的包是 Windows Foundation 包时，此参数是可选的。

*FeatureName* 参数用于指定要添加的功能。您可以在同一个包中指定多个功能，只需用逗号将这些功能名称分隔开即可。

`Source` 参数指定了恢复已删除功能所需文件的位置。

`LimitAccess` 参数可阻止将 Windows 更新作为源来用于将功能恢复到在线映像中。`All` 参数在启用指定功能之前，会先启用该功能的全部父功能；这些父功能将使用默认值进行配置。

## 示例

### 示例 1：在正在运行的操作系统中启用一个可选功能
```
PS C:\> Enable-WindowsOptionalFeature -Online -FeatureName "Hearts" -All
```

此命令在正在运行的Windows操作系统中启用了可选功能“Hearts”及其父功能，以及该父功能的所有依赖项。

### 示例 2：在已挂载的操作系统镜像中启用一个可选功能
```
PS C:\> Enable-WindowsOptionalFeature -Path "c:\offline" -FeatureName "Calc" -PackageName "Microsoft.Windows.Calc.Demo~6595b6144ccf1df~x86~en~1.0.0.0"
```

此命令会在已挂载到 c:\offline 的 Windows 映像中，为指定的软件包启用可选功能“Calc”。

### 示例 3：恢复一个可选的功能
```
PS C:\> Enable-WindowsOptionalFeature -Online -FeatureName "MyFeature" -Source "c:\test\mount" -LimitAccess
```

此命令会将可选功能“MyFeature”恢复到已挂载到 c:\offline 的 Windows 映像中。该功能的恢复依赖于另一个 Windows 映像（挂载路径为 c:\test\mount）中的源文件。如果在源图像中找不到所需的文件，此命令会指定不通过 Windows Update 来查找这些源文件。

## 参数

### -All
启用指定功能的所有父级功能。如果某个父级功能是使该指定功能在图像中得以启用所必需的，那么“所有”选项将会同时启用该父级功能及其所有的默认依赖项。

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

### -FeatureName
指定要启用的功能的名称。如果您正在为运行Windows版本早于Windows® 8的Windows镜像提供服务，则功能名称区分大小写。您可以使用Get-WindowsOptionalFeature来查找该镜像中功能的名称。

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

### -LimitAccess
防止DISM在从在线镜像中查找用于恢复某个功能的源文件时与Windows Update进行通信。

“LimitAccess”功能仅能在使用 Windows 8、Windows Server® 2012、Windows® 预安装环境（Windows PE）4.0 或更高版本的系统上处理图像文件时使用。

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 中，默认目录是 RAMDISK 虚拟磁盘（其容量可能低至 32 MB）。日志文件会自动被归档；归档后的日志文件会在文件名后添加 `.bak` 扩展名，并生成新的日志文件。每次日志文件被归档时，原有的 `.bak` 文件都会被覆盖。如果使用未加入域的网络共享资源，请在使用 `DISM` 日志路径之前，通过 `net use` 命令结合相应的域凭据来设置访问权限。

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
抑制重启操作。如果不需要重新启动，该命令将不起任何作用。此选项可以防止应用程序提示用户重新启动，或者避免应用程序自动重启。

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
指定要维护的离线 Windows 镜像的根目录的完整路径。如果名为 “Windows” 的目录不是根目录的子目录，则必须指定 **WindowsDirectory**。

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
指定一个临时目录，用于在维护过程中提取文件以供使用。该目录必须存在于本地系统中。如果未指定临时目录，则系统会使用 `\Windows\%Temp%` 目录，并为每次运行 DISM 工具生成一个随机十六进制值的子目录名称。每次操作完成后，该临时目录中的文件都会被删除。不建议将网络共享位置作为用于安装包（.cab 或 .msu 文件）的临时目录。在维护过程中用于提取文件的临时目录应为本地目录。

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

### -Source
指定用于恢复从镜像中删除的功能所需的文件的位置。您可以指定已挂载的镜像对应的Windows目录，或者位于网络上并正在运行的Windows安装程序的目录。

如果您指定了多个*Source*参数，系统将从第一个找到这些文件的位置收集它们，而忽略其他位置。特征名称之间用逗号分隔。

如果您没有为已被删除的功能指定“源”（即该功能的下载位置），系统会使用组策略设置的默认位置。Windows Update 也会用于获取在线版本的软件资源（例如更新文件或安装包）。

只有在使用 Windows 8、Windows Server 2012 或更高版本的操作系统来处理图像时，才能使用 “*Source*” 功能。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SystemDrive
指定 BootMgr 文件所在路径。只有当 BootMgr 文件位于与你运行命令的分区不同的分区上时，才需要设置此路径。使用 `-SystemDrive` 选项可以从 Windows PE 环境中对已安装的 Windows 镜像进行维护或操作。

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
指定相对于图像路径的Windows目录的路径。这个路径不能是Windows目录的完整路径，而应该是一个相对路径。如果未指定，默认值是离线图像目录根目录下的Windows目录。

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

### Microsoft.Dism Commands.ImageObject

### Microsoft.Dism Commands.BasicFeatureObject

### Microsoft.DismCommands.AdvancedFeatureObject

## 输出

### Microsoft.Dism Commands.ImageObject

## 备注

## 相关链接

[ Disable-WindowsOptionalFeature](./Disable-WindowsOptionalFeature.md)

[Get-WindowsOptionalFeature](./Get-WindowsOptionalFeature.md)

[Add-WindowsPackage](./Add-WindowsPackage.md)

