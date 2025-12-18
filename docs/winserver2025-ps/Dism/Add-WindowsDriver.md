---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/add-windowsdriver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-WindowsDriver
---

# Add-WindowsDriver

## 摘要
向一个离线的Windows镜像中添加驱动程序。

## 语法

```
Add-WindowsDriver [-Recurse] [-ForceUnsigned] [-Driver <String>] [-BasicDriverObject <BasicDriverObject>]
 [-AdvancedDriverObject <AdvancedDriverObject>] -Path <String> [-WindowsDirectory <String>]
 [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

## 描述
`Add-WindowsDriver` cmdlet 可将第三方驱动程序包添加到离线的 Windows 镜像中。

使用 *Path* 参数来指定已挂载的 Windows 镜像的位置。

使用 *Driver* 参数来指定 .inf 驱动程序文件的位置，或者指定包含一个或多个 .inf 驱动程序文件的文件夹的位置。

使用 *ForceUnsigned* 参数将未签名的 `.inf` 文件添加到基于 x64 的镜像中。

## 示例

### 示例 1：向图像中添加驱动程序
```
PS C:\> Add-WindowsDriver -Path "c:\offline" -Driver "c:\test\drivers" -Recurse
```

该命令会将位于 `c:\test\drivers` 文件夹或其任意子目录中的所有驱动程序添加到已挂载到 `c:\offline` 的 Windows 操作系统镜像中。

### 示例 2：添加一个未签名的驱动程序包
```
PS C:\> Add-WindowsDriver -Path "c:\offline" -Driver "c:\test\drivers\Usb\Usb.inf" -ForceUnsigned
```

此命令将未签名的驱动程序包（Usb.inf）添加到挂载在 c:\offline 路径下的 Windows 镜像中。

## 参数

### -AdvancedDriverObject
指定一个对象，其中包含有关您想要添加的驱动程序的详细信息。该对象可以从 `Export-WindowsDriver` 或 `Get-WindowsDriver` 的输出中获取。

```yaml
Type: AdvancedDriverObject
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -BasicDriverObject
提供了一个对象，其中包含了您想要添加的驱动程序的基本信息。该对象可以从 **Export-WindowsDriver** 或 **Get-WindowsDriver** 的输出结果中获取。

```yaml
Type: BasicDriverObject
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Driver
指定包含您想要添加的驱动程序对应的 `.inf` 文件的 `.inf` 文件或文件夹。当您指定一个文件夹时，系统中会忽略那些无效的（即不符合驱动程序格式要求的）`.inf` 文件。在命令执行过程中，这些无效文件会在控制台中被显示出来，并且日志文件中也会包含相应的警告信息。不过您不会收到错误提示消息。

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

### -ForceUnsigned
将未签名的驱动程序添加到 x64 架构的映像中。*ForceUnsigned* 参数会覆盖这样一个要求：即安装在基于 X64 的计算机上的驱动程序必须具有数字签名。有关驱动程序签名要求的更多信息，请参阅 TechNet 文库中的 [Windows 部署选项](https://go.microsoft.com/fwlink/?LinkId=214574)。

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
指定日志文件的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认的日志存储目录是 RAMDISK（临时存储空间），其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件会在原文件名后加上 `.bak` 扩展名进行保存，并同时生成一个新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先通过 `net use` 命令结合域凭据来配置访问权限。

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

### -Recurse
在搜索要添加的驱动程序时，会包含所有子文件夹。

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
指定一个临时目录，用于在维护过程中提取文件。该目录必须存在于本地系统中。如果未指定临时目录，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时，该目录下的子目录名称都会是一个随机生成的十六进制值。每次操作完成后，临时目录中的内容都会被删除。不建议将网络共享位置作为临时目录来解压安装包（.cab 或 .msu 文件）。用于在维护过程中临时提取文件的目录应该是一个本地目录。

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
指定 BootMgr 文件所在的路径。只有当 BootMgr 文件位于与执行命令的分区不同的分区上时，才需要指定该路径。使用 `-SystemDrive` 选项可以从 Windows PE 环境中管理服务已安装的 Windows 镜像。

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
指定相对于图像路径的Windows目录的路径。这不能是Windows目录的完整路径，而应该是一个相对路径。如果未指定，默认值是离线图像目录根目录下的Windows目录。

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

### Microsoft.Dismcommands.ImageObject

### Microsoft.Dism Commands.BasicDriverObject

### Microsoft.DismCommands.AdvancedDriverObject

## 输出

### Microsoft.Dism Commands.BasicDriverObject

### Microsoft.Dismcommands.ImageObject

## 备注

## 相关链接

[Get-WindowsDriver](./Get-WindowsDriver.md)

[Remove-WindowsDriver](./Remove-WindowsDriver.md)

