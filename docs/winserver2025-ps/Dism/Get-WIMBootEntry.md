---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/get-wimbootentry?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WIMBootEntry
---

# Get-WIMBootEntry

## 摘要
显示指定磁盘卷的Windows镜像文件引导（WIMBoot）配置项。

## 语法

```
Get-WIMBootEntry -Path <String> [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

## 描述
`Get-WIMBootEntry` cmdlet 可以显示指定磁盘卷的 Windows 映像文件启动（WIMBoot）配置信息。

## 示例

#### 示例 1：显示某个驱动器的 WIMBoot 配置信息
```
PS C:\> Get-WIMBootEntry -Path "C:\"
```

此命令显示C:\驱动器上的Windows镜像文件启动（WIMBoot）配置项。

## 参数

### -LogLevel
指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及信息性日志内容  
- 4 = 包含上述所有内容，同时还显示调试输出

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 内的临时存储空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件会在文件名后加上 `.bak` 扩展名，同时会生成一个新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 日志路径之前，先通过 `net use` 命令并输入相应的域凭据来设置访问权限。

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

### -Path
指定用于 Windows 镜像文件启动（WIMBoot）配置的磁盘卷路径。

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

### -ScratchDirectory
指定一个临时目录，用于在维护过程中提取文件以供使用。该目录必须存在于本地。如果没有指定，则会使用 `\Windows\%Temp%` 目录，并且每次运行 DISM 时都会为该目录生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的内容都会被删除。不建议将网络共享位置作为用于安装包（.cab 或 .msu 文件）的临时目录。在维护过程中用于提取文件的临时目录应该是本地目录。

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

## 输出

### Microsoft.Dism Commands.WimBootEntryObject

## 备注

## 相关链接

