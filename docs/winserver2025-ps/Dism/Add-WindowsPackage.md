---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/add-windowspackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-WindowsPackage
---

# Add-WindowsPackage

## 摘要
将一个 `.cab` 或 `.msu` 文件添加到 Windows 镜像中。

## 语法

### 在线
```
Add-WindowsPackage -PackagePath <String> [-IgnoreCheck] [-PreventPending] [-NoRestart] [-Online]
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 离线模式
```
Add-WindowsPackage -PackagePath <String> [-IgnoreCheck] [-PreventPending] [-NoRestart] -Path <String>
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Add-WindowsPackage` cmdlet 可将指定的 `.cab` 或 `.msu` 包安装到镜像中。

## 示例

### 示例 1：将一个软件包添加到在线图片中
```
PS C:\> Add-WindowsPackage -Online -PackagePath "c:\packages\package.cab"
```

这个命令会将一个.cab包添加到在线镜像中。

### 示例 2：向已挂载的镜像中添加文件
```
PS C:\> Add-WindowsPackage -Path "c:\offline" -PackagePath "c:\packages\demo_package.msu" -PreventPending
```

此命令会向已挂载的Windows镜像中添加一个.msu文件，除非该软件包或镜像存在待处理的操作（即还有其他需要执行的步骤）。

### 示例 3：向已挂载的镜像中添加多个软件包
```
PS C:\> Add-WindowsPackage -Path "c:\offline" -PackagePath "c:\packages" -IgnoreCheck
```

该命令会将文件夹中的所有软件包添加到已挂载的Windows镜像中，而不会检查这些软件包是否适用于该镜像。

## 参数

### -IgnoreCheck
跳过对每个软件包的适用性检查。

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
指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘（其存储空间可能低至 32 MB）。日志文件会自动被归档；归档后的日志文件名称会加上 `.bak` 后缀，同时系统会生成一个新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在设置 DISM 日志路径之前，使用 `net use` 命令并输入相应的域凭据来设置访问权限。

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
抑制系统重启。如果不需要重启，该命令将不起任何作用。此选项可以防止应用程序提示用户进行重启，或者阻止应用程序自动重启。

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

### -PackagePath
指定要添加到镜像中的包的位置。

有效值为：

- A single .cab or .msu file.
- A folder that contains a single expanded .cab file.
- A folder that contains a single .msu file.
- A folder that contains multiple .cab or .msu files.

如果 *PackagePath* 是一个文件夹，并且其根目录下包含 `.cab` 或 `.msu` 文件，那么该文件夹下的所有子文件夹也会被递归地检查是否存在 `.cab` 或 `.msu` 文件。

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

### -PreventPending
如果该软件包或Windows镜像存在待处理的在线操作（例如需要从网络下载额外文件等），则跳过安装过程。

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
指定一个临时目录，用于在服务过程中提取文件。该目录必须存在于本地系统中。如果未指定目录，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时都会为该目录生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的所有内容都会被删除。不建议将网络共享位置作为临时目录来解压用于安装的包文件（.cab 或 .msu 格式）。在服务过程中用于提取文件的临时目录应为本地目录。

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
指定 BootMgr 文件所在的路径。只有当 BootMgr 文件位于与运行命令的分区不同的分区上时，才需要设置此路径。使用 `-SystemDrive` 选项可以从 Windows PE 环境中服务已安装的 Windows 镜像。

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
指定相对于图像路径的Windows目录的路径。该路径不能是Windows目录的完整路径，而应该是一个相对路径。如果未指定，默认值是离线图像目录根目录下的Windows目录。

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

### Microsoft.Dism Commands.BasicPackageObject

### Microsoft.Dismcommands.AdvancedPackageObject

## 输出

### Microsoft.Dism Commands.ImageObject

## 备注

## 相关链接

[Get-WindowsPackage](./Get-WindowsPackage.md)

[Remove-WindowsPackage](./Remove-WindowsPackage.md)

