---
description: 通过用硬链接替换重复的文件来优化镜像中已配置包的总文件大小。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 10/13/2021
online version: https://learn.microsoft.com/powershell/module/dism/optimize-appxprovisionedpackages?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Optimize-AppXProvisionedPackages
---

# 优化 AppXProvisionedPackages

## 摘要
通过用硬链接替换重复的文件来优化镜像中已配置包的总文件大小。

## 语法

### 离线模式
```
Optimize-AppXProvisionedPackages -Path <String> [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
通过用硬链接替换重复的文件来优化镜像中已配置包的总文件大小。

在构建镜像时，首先挂载磁盘镜像，接着添加 AppX 包，优化已配置的包，最后卸载磁盘镜像。

一旦包含已配置的AppX包的镜像上线，**Optimize-AppXProvisionedPackages** 将无法对这些已配置的AppX包进行优化。如果您将镜像下线并添加新的包，那么只有那些在镜像下线之后新增的包才会被优化。

## 示例

### 示例 1：优化离线 Windows 镜像中预配置的软件包
```powershell
PS> Optimize-AppXProvisionedPackages -Path ".\wim\image.wim"
```

这个命令用于优化名为*image.wim*的镜像中所有已配置软件包的总文件大小。

## 参数

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
Accepted values: Errors, Warnings, WarningsInfo, Debug

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogPath
指定要记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 的临时存储空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件会在文件名后添加 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，`.bak` 文件都会被覆盖。如果使用未加入域的网络共享资源，请在使用 `DISM` 日志路径之前，先通过 `net use` 命令结合域凭据来设置访问权限。

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
请勿使用该功能。如果应用程序镜像是在线状态（即可以从网络下载），则 **Optimize-AppXProvisionedPackages** 无法对这些已配置好的 AppX 包进行优化处理。

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
指定一个临时目录，用于在服务过程中提取文件。该目录必须存在于本地。如果未指定，默认使用 `\Windows\%Temp%\` 目录，每次运行 DISM 时，该目录下的子目录名称会生成一个随机十六进制值。每次操作完成后，临时目录中的内容都会被删除。请不要使用网络共享位置作为临时目录来解压安装包（.cab 或 .msu 文件）。用于在服务过程中提取文件的临时目录应为本地目录。

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
指定BootMgr文件所在的路径。只有当BootMgr文件位于与你运行命令的分区不同的分区上时，才需要提供该路径。使用 `-SystemDrive` 参数可以从Windows PE环境中管理服务已安装的Windows镜像。

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
指定相对于图像路径的 Windows 目录的路径。这个路径不能是 Windows 目录的完整路径，而应该是一个相对路径。如果未指定，默认值是离线图像目录根目录下的 Windows 目录。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.Management.Automation.SwitchParameter

### Microsoft.Dism Commands.LogLevel

## 输出

### Microsoft.Dism Commands.ImageObject

## 备注

## 相关链接

[https://go.microsoft.com/fwlink/?LinkId=293633]

