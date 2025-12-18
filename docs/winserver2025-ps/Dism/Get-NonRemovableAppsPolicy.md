---
description: 返回一个列表，其中包含已安装并配置为“不可卸载应用”的应用程序包。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 10/07/2021
online version: https://learn.microsoft.com/powershell/module/dism/get-nonremovableappspolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NonRemovableAppsPolicy
---

# Get-NonRemovableAppsPolicy

## 摘要
返回一个列表，其中包含已安装并配置为“不可卸载应用”的应用程序包。

## 语法

### 离线模式
```
Get-NonRemovableAppsPolicy -Path <String> [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 在线
```
Get-NonRemovableAppsPolicy [-Online] [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>]
 [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Get-NonRemovableAppsPolicy` cmdlet 可以获取已安装且被配置为不可卸载（即无法删除）的应用程序包列表。

## 示例

### 示例 1：获取所有已安装且无法卸载的应用程序包
```powershell
PS> Get-NonRemovableAppsPolicy -Online
```

这个命令可以获取所有已安装的应用程序包的信息，这些应用程序包之前被配置为无法卸载的。

### 示例 2：从离线的 Windows 镜像中获取所有无法卸载的应用程序
```powershell
PS> Get-NonRemovableAppsPolicy -Path ".\wim\image.wim"
```

此命令用于获取有关已加载到离线操作系统镜像中的应用程序包的信息，这些应用程序包之前已被配置为不可移除的。

## 参数

### -LogLevel
用于指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及常规信息  
- 4 = 包括上述所有信息，还包括调试输出

```yaml
Type: LogLevel
Parameter Sets: (All)
Aliases: LL
Accepted values: Errors, Warnings, WarningsInfo, Debug

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogPath
指定要写入日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 中，默认目录是 RAMDISK 资源池（其容量可能低至 32 MB）。日志文件会自动被归档；归档后的日志文件会在文件名后添加“.bak”扩展名，并生成新的日志文件。每次日志文件被归档时，原来的“.bak”文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先使用 `net use` 命令并输入相应的域凭据来配置访问权限。

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
指定一个临时目录，该目录将在执行服务维护操作时用于解压文件。此目录必须存在于本地计算机上。如果未指定临时目录，默认使用 `\Windows\%Temp%\` 目录，其中子目录的名称由 DISM 运行时生成的随机十六进制值决定。每次操作完成后，临时目录中的文件都会被删除。不建议将网络共享位置用作解压安装包（.cab 或 .msu 文件）的临时目录。用于服务维护期间临时解压文件的目录应为本地目录。

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
指定 BootMgr 文件所在的路径。只有当 BootMgr 文件位于与你运行命令的分区不同的分区时，才需要指定该路径。使用 `-SystemDrive` 选项可以从 Windows PE 环境中管理服务已安装的 Windows 镜像。

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
指定相对于图像路径的Windows目录的路径。该路径不能是Windows目录的完整路径，而应该是一个相对路径。如果未指定，默认值为离线图像目录根目录下的Windows目录。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.Management Automation.SwitchParameter

### Microsoft.Dism Commands.LogLevel

## 输出

### Microsoft.Dism Commands.ImageObject

## 备注

## 相关链接

[https://go.microsoft.com/fwlink/?LinkId=293633](https://go.microsoft.com/fwlink/?LinkId=293633)

