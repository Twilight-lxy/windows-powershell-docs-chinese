---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/get-windowscapability?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WindowsCapability
---

# Get-WindowsCapability

## 摘要
为图像或正在运行的操作系统获取Windows功能支持。

## 语法

### 离线
```
Get-WindowsCapability [-Name <String>] [-LimitAccess] [-Source <String[]>] -Path <String>
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 在线
```
Get-WindowsCapability [-Name <String>] [-LimitAccess] [-Source <String[]>] [-Online]
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Get-WindowsCapability` cmdlet 可以获取安装在镜像或正在运行的操作系统中的 Windows 功能，或者从远程源可安装的 Windows 功能。

## 示例

### 示例 1：获取图像对应的 Windows 功能信息
```
PS C:\> Get-WindowsCapability -Path "C:\offline" -Name "Language.TextToSpeech~~~fr-FR~0.0.1.0"
```

该命令会在路径 C:\offline 处安装由 *Name* 参数指定的操作系统镜像中包含的 Windows 功能。

### 示例 2：获取本地操作系统的 Windows 功能
```
PS C:\> Get-WindowsCapability -Online
```

此命令会在本地主机上安装与Windows相关的功能/组件。

## 参数

### -LimitAccess
防止DISM与Windows Update或Windows Server Update联系以获取功能源文件。

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
指定日志中显示的最大输出级别。默认的日志级别为 3。允许的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及信息性内容  
- 4 = 显示前面列出的所有信息，还包括调试输出

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
指定日志文件的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘（用于临时存储数据），其容量可能低至 32 MB。日志文件会自动被归档；归档后的文件名后会添加 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，原有的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先通过 `net use` 命令结合域凭据来设置访问权限。

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

### -Name
用于指定在操作系统中需要获取的某个功能的身份（或标识）。

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

### -Online
表示该cmdlet是在本地主机上正在运行的操作系统中执行的。

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
指定一个临时目录，用于在服务过程中提取文件。该目录必须存在于本地系统中。如果未指定临时目录，则系统会使用 `\Windows\%Temp%` 目录，并为每次执行 DISM 命令生成一个随机十六进制数值作为子目录名称。每次操作完成后，临时目录中的文件都会被删除。不建议将网络共享位置用作扩展安装包（.cab 或 .msu 文件）的临时目录。用于在服务过程中提取文件的目录应为本地目录。

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
允许你检查可以从某个包含用于安装各种功能的包的 위치（例如 FOD 仓库）中安装的功能。可以使用多个 **Source** 参数。

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
指定 BootMgr 文件所在的路径。只有当 BootMgr 文件位于与你执行命令的分区不同的分区上时，才需要设置此路径。使用 `-SystemDrive` 参数可以从 Windows PE 环境中对已安装的 Windows 镜像进行维护或操作。

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
指定相对于图像路径的 Windows 目录的路径。这不能是 Windows 目录的完整路径，而应该是一个相对路径。如果未指定，默认值将是离线图像目录根目录下的 Windows 目录。

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

## 输出

### Microsoft.Dism Commands.ImageObject

## 备注

## 相关链接

[Add-WindowsCapability](./Add-WindowsCapability.md)

[Remove-WindowsCapability](./Remove-Windows Capability.md)

