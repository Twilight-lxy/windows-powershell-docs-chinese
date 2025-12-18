---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 10/06/2021
online version: https://learn.microsoft.com/powershell/module/dism/save-windowsimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Save-WindowsImage
---

# 保存Windows镜像

## 摘要
将应用于已挂载镜像的更改应用到其WIM（Windows Imaging Module）或VHD（Virtual Hard Disk）文件中。

## 语法

```
Save-WindowsImage -Path <String> [-CheckIntegrity] [-Append] [-SupportEa] [-LogPath <String>]
 [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Save-WindowsImage` cmdlet 可以将应用于已挂载镜像的服务更改直接应用到其 WIM 或 VHD 文件中，而无需先卸载该镜像。

`Path` 参数指定了已挂载的 Windows 镜像的位置。

`Append` 参数指定了在保存时将 Windows 映像文件添加到的现有 `.wim` 文件的位置。

*CheckIntegrity* 参数用于检测和跟踪.wim文件的损坏情况。当DISM在使用**Mount-WindowsImage** cmdlet时检测到.wim文件已损坏时，*CheckIntegrity* 会停止相关操作。需要注意的是，*CheckIntegrity* 参数不适用于虚拟硬盘（VHD）文件。

## 示例

#### 示例 1：保存对已挂载镜像所做的服务更改
```
PS C:\> Save-WindowsImage -Path "c:\offline"
```

这条命令会将针对 Windows 镜像所做的服务相关更改保存到挂载在 `c:\offline` 路径下的文件中。该命令不会卸载该镜像。

## 参数

### -Append
这表示该cmdlet指定了一个现有的.wim文件的位置，在保存时将Windows镜像添加到该文件中。

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

### -CheckIntegrity
该cmdlet用于检测和跟踪.wim文件的损坏情况。当使用**Mount-WindowsImage** cmdlet时，如果DISM发现.wim文件已损坏，*CheckIntegrity*参数会立即停止相关操作。需要注意的是，*CheckIntegrity*参数不适用于虚拟硬盘（VHD）文件。

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
用于指定日志中显示的最大输出级别。默认的日志级别为 3。允许的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及常规信息  
- 4 = 包括上述所有信息，此外还显示调试输出

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘（其容量可能低至 32 MB）。日志文件会自动被归档；归档后的日志文件名称后会加上 `.bak` 扩展名，并且系统会生成一个新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件都会被覆盖。如果使用未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先通过 `net use` 命令结合域凭据来配置访问权限。

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
指定要保存的离线Windows镜像根目录的完整路径。

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
指定一个临时目录，用于在维护过程中提取文件以供使用。该目录必须存在于本地计算机上。如果未指定该目录，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时都会为该目录生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的文件都会被删除。不建议将网络共享位置作为临时目录来解压用于安装的包（.cab 或 .msu 文件）。在维护过程中用于提取文件的临时目录应为本地目录。

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

### -SupportEa
捕获扩展属性。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dism Commands.ImageObject

### Microsoft.Dismcommands.ImageObjectWithState

## 输出

### Microsoft.Dism Commands.ImageObject

## 备注

## 相关链接

[Mount-WindowsImage](./Mount-WindowsImage.md)

[Dismount-WindowsImage](./Dismount-WindowsImage.md)

[Get-WindowsImage](./Get-WindowsImage.md)

[修复Windows镜像](./Repair-WindowsImage.md)

