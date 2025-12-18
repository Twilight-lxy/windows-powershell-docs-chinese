---
description: 使用此主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/dism/get-appxprovisionedpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppxProvisionedPackage
---

# 获取已配置的应用程序包（Get-AppxProvisionedPackage）

## 摘要
获取有关应用程序包（.appx）的信息，这些应用程序包将安装在每位新用户的设备上。

## 语法

### 离线模式
```
Get-AppxProvisionedPackage -Path <String> [-WindowsDirectory <String>] [-SystemDrive <String>]
 [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 在线
```
Get-AppxProvisionedPackage [-Online] [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>]
 [-ScratchDirectory <String>] [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Get-AppxProvisionedPackage` cmdlet 可用于获取镜像中关于应用程序包（.appx）的信息，这些应用程序包被设置为会随每个新用户的登录而自动安装。对于那些未被预先配置（即未设置自动安装）的应用程序包（.appx），请使用 `Get-AppxPackage` cmdlet 进行查询。

使用 *Online* 参数来指定您本地计算机上正在运行的操作系统，或者使用 *Path* 参数来指定已挂载的 Windows 镜像的位置。

## 示例

#### 示例 1：列出挂载后的镜像中为每个账户需要安装的应用包
```
PS C:\> Get-AppxProvisionedPackage -Path "c:\offline"
```

此命令列出了安装在Windows镜像中的应用程序包（.appx文件），这些镜像被挂载到了c:\offline目录下，将会为新创建的用户账户进行安装。

## 参数

### -LogLevel
指定日志中显示的最大输出级别。默认的日志级别为 3。可接受的值如下：  
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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK（即临时存储空间），其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件名称会加上 `.bak` 扩展名，并会生成新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件会被覆盖。如果使用的网络共享未加入域，请在使用 `DISM` 命令设置日志路径之前，先通过 `net use` 命令结合域凭据来设置访问权限。

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
指定要维护的离线 Windows 镜像的根目录的完整路径。如果名为 “Windows” 的目录不是根目录的子目录，则必须指定 **WindowsDirectory**。

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
指定一个临时目录，用于在服务期间提取文件以供使用。该目录必须存在于本地系统中。如果未指定，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时，该目录下的子目录名称会由随机生成的十六进制值决定。每次操作完成后，临时目录中的内容都会被删除。不建议将网络共享位置作为用于展开安装包（.cab 或 .msu 文件）的临时目录；用于在服务期间临时提取文件的目录应为本地目录。

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
指定包含 BootMgr 文件的路径。只有当 BootMgr 文件位于与执行命令的分区不同的分区上时，才需要设置此参数。使用 `-SystemDrive` 可以从 Windows PE 环境中维护已安装的 Windows 映像。

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
指定相对于镜像路径的Windows目录的路径。这个路径不能是Windows目录的完整路径，而应该是一个相对路径。如果未指定，默认值将是离线镜像目录根目录下的Windows目录。

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

### Microsoft.Dism Commands.ImageObject

## 输出

### Microsoft.Dism Commands.AppxPackageObject

## 备注

## 相关链接

[获取 AppX 包](https://go.microsoft.com/fwlink/?LinkId=215770)

[Add-AppxProvisionedPackage](./Add-AppxProvisionedPackage.md)

[Remove-AppxProvisionedPackage](./Remove-AppxProvisionedPackage.md)

[Set-AppXProvisionedDataFile](./Set-AppXProvisionedDataFile.md)

