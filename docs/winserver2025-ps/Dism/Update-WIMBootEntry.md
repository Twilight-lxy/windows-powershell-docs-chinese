---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/update-wimbootentry?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-WIMBootEntry
---

# 更新 WIM 启动项（Update-WIMBootEntry）

## 摘要
更新与指定的数据源ID、重命名的图像文件路径或移动后的图像文件路径相关联的Windows镜像文件引导（WIMBoot）配置项。

## 语法

```
Update-WIMBootEntry -Path <String> -ImagePath <String> -DataSourceID <Int64> [-LogPath <String>]
 [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Update-WIMBootEntry` cmdlet 用于更新与指定的数据源 ID、重命名的图像文件路径或移动后的图像文件路径相关联的 Windows 镜像文件启动（WIMBoot）配置条目。

## 示例

### 示例 1：更新 `.wim` 文件的配置条目
```
PS C:\> Update-WIMBootEntry -Path "C:\" -DataSourceID 0 -ImagePath "D:\Windows Images\install.wim"
```

此命令会更新数据源ID对应的（WIMBoot）配置项，使其新的图像文件路径变为D:\Windows Images\install.wim。

## 参数

### -DataSourceID
指定数据源ID。可以使用Get-WIMBootEntry命令来显示数据源ID。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ImagePath
指定被重命名或移动的图像文件的完整路径。

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 暂存空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件名称会加上“.bak”后缀，并且会生成一个新的日志文件。每次日志文件被归档时，原来的“.bak”文件都会被覆盖。当使用未加入域的网络共享资源时，在设置 DISM 日志的路径之前，请先使用 `net use` 命令并结合相应的域凭据来配置访问权限。

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
指定 WIMBoot 配置对应的磁盘分区的路径。

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
指定一个临时目录，用于在服务期间提取文件以供使用。该目录必须存在于本地系统中。如果未指定目录，则会使用 `\Windows\%Temp%` 目录，并且每次运行 DISM 时，该目录下的子目录名称都会是一个随机生成的十六进制值。每次操作完成后，临时目录中的文件都会被删除。不建议将网络共享位置用作用于解压安装包（.cab 或 .msu 文件）的临时目录。在服务期间用于提取文件的临时目录应该是一个本地目录。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Dism Commands.BaseDismObject

## 备注

## 相关链接

[Get-WIMBootEntry](./Get-WIMBootEntry.md)

