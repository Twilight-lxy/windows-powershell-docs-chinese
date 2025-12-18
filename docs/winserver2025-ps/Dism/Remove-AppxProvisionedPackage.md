---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/remove-appxprovisionedpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AppxProvisionedPackage
---

# 移除 AppxProvisionedPackage

## 摘要
从Windows镜像中删除一个应用程序包（.appx文件）。

## 语法

### 在线
```
Remove-AppxProvisionedPackage -PackageName <String> [-AllUsers] [-Online] [-WindowsDirectory <String>]
 [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

### 离线模式
```
Remove-AppxProvisionedPackage -PackageName <String> -Path <String> [-WindowsDirectory <String>]
 [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

## 描述
`Remove-AppxProvisionedPackage` cmdlet 用于从 Windows 镜像中删除应用包（.appx 格式）。当创建新的用户账户时，这些应用包将不会被安装；同时，现有的用户账户中的应用包也不会被删除。如果您想要删除未被预配置的应用包，或者仅针对某个特定用户删除某个应用包，请使用 `Remove-AppxPackage` 命令。

## 示例

### 示例 1：从图像中删除应用程序包
```
PS C:\> Remove-AppxProvisionedPackage -Path c:\offline -PackageName MyAppxPkg
```

这个命令会从被挂载到 c:\offline 的 Windows 镜像中删除应用程序包（.appx）以及 MyAppxPkg 文件。

## 参数

### -LogLevel
指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
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
指定要记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 中，默认目录是 RAMDISK 内存空间（大小可能低至 32 MB）。日志文件会自动被归档；归档后的日志文件名称后会加上“.bak”后缀，并且系统会生成新的日志文件。每次日志文件被归档时，原来的“.bak”文件都会被覆盖。如果使用的是未加入域的网络共享资源，在设置 DISM 日志的路径之前，请先使用 `net use` 命令并结合域凭据来设置访问权限。

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
指定要从Windows镜像中删除的应用程序包（.appx）的名称。

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
指定一个临时目录，用于在服务过程中提取文件。该目录必须存在于本地系统中。如果未指定目录，则会使用 `\Windows\%Temp%` 目录，并且每次运行 DISM 时，该目录下的子目录名称会是一个随机生成的十六进制值。每次操作完成后，临时目录中的文件都会被删除。不建议将网络共享位置作为临时目录来解压用于安装的软件包（.cab 或 .msu 文件）。在服务过程中用于提取文件的临时目录应该是一个本地目录。

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
指定 BootMgr 文件所在的路径。只有当 BootMgr 文件位于与你运行命令的分区不同的分区上时，才需要指定该路径。使用 `-SystemDrive` 可以从 Windows PE 环境中对已安装的 Windows 镜像进行维护或修复操作。

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
指定相对于图像路径的 Windows 目录的路径。这不能是 Windows 目录的完整路径，而应该是一个相对路径。如果未指定，则默认值为离线图像目录根目录中的 Windows 目录。

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

### -AllUsers
将此命令执行给所有用户。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dismcommands.ImageObject

### Microsoft.DismCommands.AppxPackageObject

## 输出

### Microsoft.Dismcommands.ImageObject

## 备注

## 相关链接

[Remove-AppxPackage](https://go.microsoft.com/fwlink/?LinkId=215772)

[Add-AppxProvisionedPackage](./Add-AppxProvisionedPackage.md)

[Get-AppxProvisionedPackage](./Get-AppxProvisionedPackage.md)

[Set-AppXProvisionedDataFile](./Set-AppXProvisionedDataFile.md)

