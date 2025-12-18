---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 10/07/2021
online version: https://learn.microsoft.com/powershell/module/dism/add-appxprovisionedpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AppxProvisionedPackage
---

# 添加 AppxProvisionedPackage

## 摘要
将一个应用程序包（.appx）添加到Windows镜像中，该程序包会在每个新用户登录时自动安装。

## 语法

### 离线状态
```
Add-AppxProvisionedPackage [-FolderPath <String>] [-PackagePath <String>] [-DependencyPackagePath <String[]>]
 [-OptionalPackagePath <String[]>] [-LicensePath <String[]>] [-SkipLicense] [-CustomDataPath <String>]
 [-Regions <String>] [-StubPackageOption <StubPackageOption>] -Path <String> [-WindowsDirectory <String>]
 [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

### 在线
```
Add-AppxProvisionedPackage [-FolderPath <String>] [-PackagePath <String>] [-DependencyPackagePath <String[]>]
 [-OptionalPackagePath <String[]>] [-LicensePath <String[]>] [-SkipLicense] [-CustomDataPath <String>]
 [-Regions <String>] [-StubPackageOption <StubPackageOption>] [-Online] [-WindowsDirectory <String>]
 [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

## 描述
**Add-AppxProvisionedPackage** cmdlet 用于将一个应用程序包（.appx）添加到 Windows 镜像中，以便每个新用户都能安装该应用程序。如果该应用程序包包含依赖于特定架构的组件，则必须在目标镜像上安装这些依赖组件对应的相应架构版本。例如，如果该应用程序包依赖于 x86 架构的组件，就必须确保在 x86 架构的镜像上也安装了相应的组件。

您无法在不支持 Windows 8 应用的操作系统中安装应用程序包（.appx）。Windows Server 2012 的 Server Core 版本、Windows 预安装环境（Windows PE）4.0，以及任何早于 Windows 8 和 Windows Server 2012 的 Windows 版本都不支持应用程序的安装。

要在 Windows Server 2016 上安装和运行应用程序，您必须先安装 [“带有桌面体验的服务器安装”选项](/windows-server/get-started/getting-started-with-server-with-desktop-experience)。

使用 *Online* 参数来指定您本地计算机上正在运行的操作系统，或者使用 *Path* 参数来指定已挂载的 Windows 镜像的位置。

使用 *PackagePath*、*DependencyPackagePath* 和 *LicensePath* 参数来指定添加所提供应用程序包（.appx）所需的所有文件的位置。利用这些参数来为业务线应用程序进行配置（即设置应用程序所需的各项资源）。

使用 *FolderPath* 参数来指定解压后的应用程序包（.appx）文件所在文件夹的位置。该文件夹中包含所有依赖包以及许可证文件。

如果要为特定用户添加应用程序包（.appx），或者在开发应用程序时测试某个包，请使用 **Add-AppxPackage** cmdlet。

如需更多信息（包括应用程序包提供的要求），请参阅 MicrosoftDocs 中的 [使用 DISM 侧载应用程序](/windows-hardware/manufacture/desktop/sideload-apps-with-dism-s14) 和 [如何开发使用自定义文件的原厂设备 (OEM) 应用程序](/windows/win32/appxpkg/how-to-develop-oem-app-with-custom-file)。

## 示例

### 示例 1：将一个应用程序包添加到正在运行的操作系统中
```powershell
PS C:\> Add-AppxProvisionedPackage -Online -FolderPath "c:\Appx"
```

此命令会将位于 `c:\Appx` 文件夹中的应用程序包、依赖包以及许可证文件添加到正在运行的 Windows 操作系统中。该软件包将同时安装给当前用户以及在计算机上创建的任何新用户账户。

### 示例 2：添加应用程序包和操作系统镜像
```powershell
PS C:\> Add-AppxProvisionedPackage -Path c:\offline -PackagePath c:\Appx\myPackage.appx -DependencyPackagePath c:\Appx\dependency1\dependencyPackage.appx -LicensePath c:\Appx\myLicense.xml
```

这个命令将应用程序包 `myPackage.appx` 添加到挂载在 `c:\offline` 目录下的 Windows 镜像中。

## 参数

### -CustomDataPath
指定自定义数据文件的位置。该自定义数据文件将被重命名为 `custom.data`，并保存在应用程序的数据存储中。

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

### -DependencyPackagePath
指定依赖包的位置。

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

### -FolderPath
指定一个用于存放解压后的应用程序包文件的文件夹，其中包含主程序包以及所有依赖包。该文件夹还必须包含您的应用程序许可证。

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

### -LicensePath
指定包含应用程序许可证的.xml文件的位置。

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

### -LogLevel
指定日志中显示的最大输出级别。

```yaml
Type: LogLevel
Parameter Sets: (All)
Aliases: LL
Accepted values: Errors, Warnings, WarningsInfo

Required: False
Position: Named
Default value: WarningsInfo
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogPath
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘中的临时存储空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件会在文件名后添加“.bak”扩展名，并生成一个新的日志文件。每次日志文件被归档时，对应的“.bak”文件都会被覆盖。如果使用的是未加入域的网络共享资源，在设置 DISM 日志的路径之前，请先使用 `net use` 命令并输入相应的域凭据来配置访问权限。

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

### -OptionalPackagePath
指定一个可选包的路径，该包也会被配置（provisioned）。有关可选包的更多信息，请参阅[可选包及相关设置创作](/windows/msix/package/optional-packages)。

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

### -PackagePath
指定要添加到 Windows 镜像中的应用程序包（.appx）的位置。此包将会为每个新用户账户自动添加。如果要为特定用户添加应用程序包（.appx），或者在开发应用程序时测试某个包，请使用 **Add-AppxPackage** cmdlet。

`PackagePath` 参数仅支持离线维修操作，前提是技术人员使用的计算机运行的是支持 Windows 8 应用的 Windows 版本。

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

### -Regions
该参数用于指定应用程序包（.appx 或 .appxbundle）必须在哪些地区进行部署。`region` 参数可以是 “all”，表示该应用程序应在所有地区都可用；也可以是一个用半冒号分隔的地区列表。这些地区的编码格式为 [ISO 3166-1 Alpha-2 或 ISO 3166-1 Alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1)。例如，美国可以表示为 “US” 或 “USA”（不区分大小写）。如果未指定地区列表，则该应用程序包仅会在被设置为启动布局（start layout）时才会被部署。

注意：此选项在客户端操作系统上是可用的。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: false
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScratchDirectory
指定一个临时目录，该目录将在执行服务操作时用于解压文件。此目录必须存在于本地系统中。如果未指定目录，则系统会使用 `\Windows\%Temp%\` 目录，并为每次 DISM 运行生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的所有内容都会被删除。不建议将网络共享位置作为用于解压安装包（.cab 或 .msu 文件）的临时目录；用于服务操作期间临时解压文件的目录应始终是本地目录。

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

### -SkipLicense
添加一个没有许可证文件的应用程序包。

只有在操作系统的企业版或服务器版本中不需要许可证的应用程序上，才使用*SkipLicense*。在其他情况下使用*SkipLicense*可能会损坏系统镜像（即导致系统无法正常运行）。

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
### -StubPackageOption
指定该包的代码存根（stub）配置偏好。如果未指定任何代码存根相关的选项，则提供的包版本将使用预设的代码存根配置设置。

```yaml
Type: StubPackageOption
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SystemDrive
指定BootMgr文件所在的路径。只有当BootMgr文件位于与你运行命令的分区不同的分区上时，才需要指定该路径。使用 `-SystemDrive` 选项可以从Windows PE环境对已安装的Windows镜像进行维护或操作。

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
指定相对于图像路径的Windows目录的路径。这个路径不能是Windows目录的完整路径，而应该是一个相对路径。如果未指定，默认值将是离线图像目录根目录下的Windows目录。

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

### System.String[]

### Microsoft.DismCommands.ImageObject

### Microsoft.Dismcommands.AppxPackageObject

## 输出

### Microsoft.DismCommands.ImageObject

## 备注

## 相关链接

[添加 AppxPackage 文件](https://go.microsoft.com/fwlink/?LinkId=215769)

[Get-AppxProvisionedPackage](./Get-AppxProvisionedPackage.md)

[Remove-AppxProvisionedPackage](./Remove-AppxProvisionedPackage.md)

[Set-AppXProvisionedDataFile](./Set-AppXProvisionedDataFile.md)
