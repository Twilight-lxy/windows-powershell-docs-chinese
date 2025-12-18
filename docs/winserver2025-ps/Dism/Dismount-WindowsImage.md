---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/dismount-windowsimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Dismount-WindowsImage
---

# 卸载 Windows 映像文件

## 摘要
从映射到的目录中卸载Windows镜像文件。

## 语法

### DismountDiscard
```
Dismount-WindowsImage -Path <String> [-Discard] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

### DismountSave
```
Dismount-WindowsImage -Path <String> [-Save] [-CheckIntegrity] [-Append] [-LogPath <String>]
 [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Dismount-WindowsImage` cmdlet 会保存或丢弃对 Windows 镜像所做的更改，之后再卸载该镜像。

*Path* 参数指定了已挂载的 Windows 镜像的位置。

`Append` 参数用于指定一个现有的 `.wim` 文件的位置，以便在卸载该文件时将 Windows 镜像添加到该文件中，而不是覆盖原有的镜像。

`CheckIntegrity` 参数用于检测和跟踪 `.wim` 文件的损坏情况。当使用 `DISM` 并配合 `Mount-WindowsImage` cmdlet 时，如果发现 `.wim` 文件已损坏，`CheckIntegrity` 会立即停止相关操作。

*CheckIntegrity* 和 *Append* 参数不适用于虚拟硬盘（VHD）文件。

## 示例

### 示例 1：卸载操作系统镜像
```
PS C:\> Dismount-WindowsImage -Path "c:\offline" -Save
```

此命令会卸载映射到 c:\offline 的 Windows 镜像，并保存在对该镜像进行维护时所做的所有更改。

## 参数

### -Append
指定一个现有的.wim文件的位置，以便在卸载该文件时将Windows镜像添加到该文件中，而不是覆盖原有的镜像。

```yaml
Type: SwitchParameter
Parameter Sets: DismountSave
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CheckIntegrity
能够检测并追踪.wim文件的损坏情况。当DISM在使用**Mount-WindowsImage** cmdlet时发现.wim文件已损坏时，*CheckIntegrity*会停止相关操作。

```yaml
Type: SwitchParameter
Parameter Sets: DismountSave
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Discard
丢弃对Windows镜像所做的更改。

```yaml
Type: SwitchParameter
Parameter Sets: DismountDiscard
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogLevel
指定日志中显示的最大输出级别。默认的日志级别为 3。允许的值如下：  
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
指定要写入日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件名称会在原文件名后添加 `.bak` 扩展名，并且系统会生成一个新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先通过 `net use` 命令结合域凭据来设置访问权限。

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
指定要维护的离线 Windows 镜像的根目录的完整路径。如果名为 “Windows” 的目录不是根目录的子目录，则必须指定 “WindowsDirectory”。

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

### -Save
将所做的更改保存到Windows镜像文件中。

```yaml
Type: SwitchParameter
Parameter Sets: DismountSave
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScratchDirectory
指定一个临时目录，用于在服务过程中提取文件。该目录必须存在于本地。如果未指定，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时，子目录的名称都会是一个随机生成的十六进制值。每次操作后，临时目录中的内容都会被删除。不建议使用网络共享位置作为临时目录来解压安装包（.cab 或 .msu 文件）。用于在服务过程中提取文件的临时目录应该是本地目录。

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

### System.String[]

### Microsoft.Dism Commands.ImageObject

### Microsoft.Dism Commands.MountedImageInfoObject

### Microsoft.Dismcommands.ImageInfoObject

## 输出

### Microsoft.Dism Commands.BaseDismObject

## 备注

## 相关链接

[Save-WindowsImage](./Save-WindowsImage.md)

[修复Windows镜像](./Repair-WindowsImage.md)

[Mount-WindowsImage](./Mount-WindowsImage.md)

[Get-WindowsImage](./Get-WindowsImage.md)

