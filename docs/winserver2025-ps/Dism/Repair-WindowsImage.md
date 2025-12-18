---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/repair-windowsimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Repair-WindowsImage
---

# 修复Windows镜像

## 摘要
修复WIM或VHD文件中的Windows镜像。

## 语法

### 离线模式
```
Repair-WindowsImage [-CheckHealth] [-ScanHealth] [-RestoreHealth] [-StartComponentCleanup] [-LimitAccess]
 [-ResetBase] [-Defer] [-Source <String[]>] [-NoRestart] -Path <String> [-WindowsDirectory <String>]
 [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

### 在线
```
Repair-WindowsImage [-CheckHealth] [-ScanHealth] [-RestoreHealth] [-StartComponentCleanup] [-LimitAccess]
 [-ResetBase] [-Defer] [-Source <String[]>] [-NoRestart] [-Online] [-WindowsDirectory <String>]
 [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

## 描述
`Repair-WindowsImage` cmdlet 可以修复 WIM 或 VHD 文件中的 Windows 镜像。

使用 *Online* 参数来指定您本地计算机上正在运行的操作系统，或者使用 *Path* 参数来指定已挂载的 Windows 镜像的位置。

*LimitAccess* 参数用于阻止将 Windows 更新（WU）作为修复在线镜像的来源进行访问。

*CheckHealth* 参数用于检查图像是否因某个进程失败而被标记为损坏，以及这种损坏是否能够被修复。

*ScanHealth* 参数用于扫描图像中是否存在组件存储损坏的情况。此操作可能需要几分钟时间才能完成。

`RestoreHealth` 参数会扫描图像以检测组件存储是否损坏，然后自动执行修复操作。这个过程需要几分钟时间。

*Source* 参数指定了可用于修复的已知正常版本的文件的位置，例如挂载映像的根目录路径。

*CheckHealth*、*ScanHealth*、*RestoreHealth*、*Source* 和 *LimitAccess* 这些功能仅能用于处理运行在 Windows 8 或 Windows Server 2012 及更高版本操作系统上的图像文件。

## 示例

### 示例 1：扫描图像以检测是否存在损坏
```
PS C:\> Repair-WindowsImage -Path "C:\offline\Mount" -ScanHealth
```

该命令会扫描指定的图像，以检查组件存储是否出现损坏。

### 示例 2：检查图像是否损坏以及是否需要修复该图像
```
PS C:\> Repair-WindowsImage -Path "C:\offline\Mount" -CheckHealth
```

此命令用于检查指定的图像是否因某个失败的进程而被标记为损坏状态，以及该损坏问题是否可以修复。

### 示例 3：检查图像是否损坏，并修复该图像
```
PS C:\> Repair-WindowsImage -Online -RestoreHealth -Source "C:\Mounted\VHD\Windows\WinSxS", "C:\Windows\TEMP" -LimitAccess
```

该命令会扫描指定的图像，检查是否存在组件存储损坏的情况，然后自动执行修复操作。

## 参数

### -CheckHealth
检查图像是否因某个进程失败而被标记为损坏，以及该损坏是否可以修复。

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

### -Defer
将清理操作推迟到下一次自动维护时再进行。

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

### -LimitAccess
防止DISM在搜索用于修复在线镜像的源文件时与Windows Update（WU）进行通信。

*LimitAccess* 只能用于处理运行在 Windows 8、Windows Server 2012 或 Windows 预安装环境（Windows PE）4.0 等操作系统上的图像文件。

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘（其容量可能低至 32 MB）。日志文件会自动被归档；归档后的日志文件会在文件名后附加 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。当使用未加入域的网络共享资源时，请先使用 `net use` 命令并输入相应的域凭据来设置访问权限，然后再设置 DISM 日志的路径。

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
抑制重新启动。如果不需要重新启动，该命令将不会执行任何操作。此选项可以防止应用程序提示用户进行重启，或者阻止应用程序自动重新启动。

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

### -ResetBase
将已被替换的组件的基础状态重置，以进一步减小组件存储的大小。

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

### -RestoreHealth
扫描图像以检测组件存储是否损坏，然后自动执行修复操作。此过程需要几分钟时间。

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

### -ScanHealth
扫描图像以检查组件存储是否损坏。此操作需要几分钟时间。

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
指定一个临时目录，该目录将在执行维护操作（servicing）时用于提取文件。此目录必须存在于本地计算机上。如果未指定目录，则系统会使用 `\Windows\%Temp%` 目录，并为每次 DISM 操作生成一个随机的十六进制值作为子目录名称。每次操作完成后，临时目录中的所有内容都会被删除。不建议将网络共享位置用作用于安装包（.cab 或 .msu 文件）的临时目录。在执行维护操作时用于提取文件的目录应为本地目录。

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
指定用于修复图像所需的文件的位置。您可以指定已挂载的图像对应的Windows目录，或者是在网络中共享的正在运行的Windows系统所在的目录。

如果您指定了多个 *Source* 参数，系统将从第一个找到这些文件的 위치收集文件，其余的位置将被忽略。使用逗号分隔不同的来源位置。

如果您没有指定*来源*，则会使用组策略设置的默认位置。Windows Update（WU）也会用于获取在线更新所需的图像文件。

“Source”功能仅适用于运行Windows 8或Windows Server 2012及以上操作系统的系统上的图像处理任务。

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

### -StartComponentCleanup
清理已被替换的组件，以减小组件存储空间的大小。

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

### -SystemDrive
指定包含 BootMgr 文件的路径。只有当 BootMgr 文件位于与你运行命令的分区不同的分区上时，才需要提供该路径。使用 `-SystemDrive` 选项可以从 Windows PE 环境中管理服务已安装的 Windows 镜像。

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
指定相对于图像路径的 Windows 目录的路径。该路径不能是 Windows 目录的完整路径，而应该是一个相对路径。如果未指定，默认值是离线图像目录根目录下的 Windows 目录。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dismcommands.ImageObject

### Microsoft.Dism Commands.ImageInfoObject

### Microsoft.Dismcommands.MountedImageInfoObject

## 输出

### Microsoft.DismCommands.ImageObjectWithState

## 备注

## 相关链接

[Mount-WindowsImage](./Mount-WindowsImage.md)

[Dismount-WindowsImage](./Dismount-WindowsImage.md)

[Get-WindowsImage](./Get-WindowsImage.md)

[Save-WindowsImage](./Save-WindowsImage.md)

