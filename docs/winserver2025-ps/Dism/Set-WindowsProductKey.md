---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/set-windowsproductkey?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WindowsProductKey
---

# Set-WindowsProductKey

## 摘要
用于设置Windows镜像的产品密钥。

## 语法

```
Set-WindowsProductKey -ProductKey <String> -Path <String> [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Set-WindowsProductKey` cmdlet 用于将指定的产品密钥设置到当前 Windows 版本对应的镜像中。

## 示例

### 示例 1：在已挂载的镜像上设置产品密钥
```
PS C:\> Set-WindowsProductKey -Path "c:\offline" -ProductKey "12345-12345-12345-12345-12345"
```

此命令将产品密钥设置到挂载在 c:\offline 目录下的 Windows 镜像上。

## 参数

### -LogLevel
用于指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
- 1 = 仅显示错误信息  
- 2 = 显示错误信息和警告信息  
- 3 = 显示错误信息、警告信息以及相关信息  
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
指定要写入日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 临时存储空间，其大小可能低至 32 MB。日志文件会自动被归档；归档后的日志文件名称后会添加“.bak”后缀，并生成新的日志文件。每次日志文件被归档时，对应的“.bak”文件都会被覆盖。如果使用未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先使用 `net use` 命令并输入相应的域凭据来配置访问权限。

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

### -ProductKey
指定用于Windows镜像的产品密钥。

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
指定一个临时目录，用于在维护过程中提取文件。该目录必须存在于本地。如果未指定，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时都会生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的内容都会被删除。不建议将网络共享位置作为用于解压安装包（.cab 或 .msu 文件）的临时目录。在维护过程中用于提取文件的临时目录应是一个本地目录。

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
指定 BootMgr 文件所在的路径。只有当 BootMgr 文件位于与您执行命令的分区不同的分区上时，才需要提供该路径。使用 `-SystemDrive` 选项可以从 Windows PE 环境中对已安装的 Windows 镜像进行维护或操作。

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
指定相对于图像路径的 Windows 目录的路径。这个路径不能是 Windows 目录的完整路径，而应该是一个相对路径。如果未指定，则默认值为离线图像目录根目录下的 Windows 目录。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Dism Commands.ImageObject

## 输出

### Microsoft.Dism Commands.ImageObject

## 备注

## 相关链接

[Get-WindowsEdition](./Get-WindowsEdition.md)

[Set-WindowsEdition](./Set-WindowsEdition.md)

