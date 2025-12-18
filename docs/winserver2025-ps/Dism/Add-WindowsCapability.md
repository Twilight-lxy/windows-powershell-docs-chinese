---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
ms.date: 08/24/2021
online version: https://learn.microsoft.com/powershell/module/dism/add-windowscapability?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-WindowsCapability
---

# Add-WindowsCapability

## 摘要
在指定的操作系统镜像上安装一个 Windows 功能包。

## 语法

### 在线
```powershell
Add-WindowsCapability [-Name <String>] [-LimitAccess] [-Source <String[]>] [-Online]
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

### 离线模式
```powershell
Add-WindowsCapability [-Name <String>] [-LimitAccess] [-Source <String[]>] -Path <String>
 [-WindowsDirectory <String>] [-SystemDrive <String>] [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
`Add-WindowsCapability` cmdlet 从按优先级排序的源位置列表中获取一个 Windows 功能包，然后将该包安装到指定的操作系统镜像上。

## 示例

### 示例 1：通过 Windows 更新客户端将某个 Windows 功能包添加到正在运行的操作系统中
```powershell
PS C:\> Add-WindowsCapability -Online -Name "Msix.PackagingTool.Driver~~~~0.0.1.0"
```
此命令会将一个 Windows 功能包添加到正在运行的操作系统中。由于没有指定源文件，Windows 更新客户端会自动下载所需的软件包。执行此操作需要具备活跃的互联网连接，或者能够连接到本地的 Windows Server Update Services (WSUS) 服务器。

### 示例 2：使用本地存储的包文件，将一个 Windows 功能包添加到正在运行的操作系统中
```powershell
PS C:\> Add-WindowsCapability -Online -Name "Msix.PackagingTool.Driver~~~~0.0.1.0" -Source "E:\" -LimitAccess
```

此命令会将由 *Name* 参数指定的 Windows 功能包添加到正在运行的操作系统中。*Source* 参数用于指定所需文件的位置。例如，如果当前运行的操作系统是 Windows 10 版本 1809 的副本，则 `Msix-PackagingTool-Driver-Package~31bf3856ad364e35~amd64~~.cab` 文件必须位于 `E:\` 目录下。

如果由 *Name* 参数指定的软件包已经安装好了，那么无论所需的文件是否存在于 `E:\` 目录中，此命令都不会返回错误信息。

### 示例 3：将一个 Windows 功能包添加到镜像中
```powershell
PS C:\> Add-WindowsCapability -Path "C:\mount\Windows" -Name "Msix.PackagingTool.Driver~~~~0.0.1.0" -Source "E:\"
```

此命令会将由 *Name* 参数指定的 Windows 功能包添加到位于路径 C:\mount\Windows 的操作系统镜像中。*Source* 参数指定了所需文件的位置。例如，如果挂载点中包含 Windows 10 版本 1809 的副本，则 `Msix-PackagingTool-Driver-Package~31bf3856ad364e35~amd64~~.cab` 文件必须位于 `E:\` 目录下。

## 参数

### -LimitAccess
表示在维护正在运行的操作系统（live OS）时，此 cmdlet 不会从 Windows 更新中查询源程序包。仅当指定了 `-Online` 参数时才适用该规则。

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
指定要写入日志的完整路径和文件名。如果未设置，默认值为 `"$env:WINDIR\Logs\Dism\dism.log"`。在 Windows PE 中，默认目录是 RAMDISK scratch 空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件会在文件名后加上 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，在设置 DISM 日志的路径之前，请先使用 `net use` 命令并输入域凭据来设置访问权限。

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
用于指定要添加到操作系统镜像中的功能的标识信息。

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

### -Online
表示该 cmdlet 在本地主机上正在运行的操作系统中执行操作。

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
指定一个临时目录，该目录将在执行维护任务时用于解压文件。此目录必须存在于本地系统中。如果未指定临时目录，则会使用 `"$env:Temp"` 目录，并且每次运行 DISM 时都会为该目录生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的内容会被删除。不建议将网络共享位置作为用于解压安装包（.cab 或 .msu 文件）的临时目录；用于维护过程中临时解压文件的目录应始终是本地目录。

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
指定用于将 Windows 功能包添加到镜像文件中的文件的所在位置。如果您指定了多个 *Source* 参数，系统将从第一个找到这些文件的位置收集文件，而其他位置将被忽略。使用逗号分隔不同的源位置。

如果您没有指定*源文件路径*，系统会使用组策略设置的默认位置。如果该方法也无法获取所需文件，Windows Update也会被用来下载在线资源（除非指定了*LimitAccess*选项）。当所有尝试都失败时，该cmdlet会默默地结束执行，不会抛出任何异常。

“Source”功能仅适用于运行Windows 8或Windows Server 2012及以上操作系统的图像文件处理场景。

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
指定BootMgr文件所在的路径。只有当BootMgr文件位于与你运行命令的分区不同的分区上时，才需要指定该路径。使用 `-SystemDrive` 参数可以从Windows PE环境中对已安装的Windows镜像进行维护或操作。

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
指定相对于镜像路径的Windows目录的路径。该路径不能是完整的Windows目录路径，而应该是一个相对路径。如果未指定，默认值为离线镜像目录根目录下的Windows目录。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Dism Commands.ImageObject

## 备注

从 Windows 10 版本 1709 开始，您无法使用 Windows Server Update Services (WSUS) 来为 Windows 10 客户端提供按需功能（Features on Demand, FOD）和语言包。相反，您可以设置组策略，要求客户端直接从 Windows 更新中下载这些资源。虽然也可以将 FOD 和语言包存储在网络共享位置上，但从 Windows 10 版本 1809 开始，这些资源只能通过 Windows 更新进行安装。有关更多信息，请参阅 [如何在使用 WSUS/Configuration Manager 时提供按需功能和语言包](/windows/deployment/update/fod-and-lang-packs)。

## 相关链接

[Get-WindowsCapability](./Get-Windows Capability.md) [Remove-WindowsCapability](./Remove-Windowscapability.md)
