---
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
online version: https://learn.microsoft.com/powershell/module/dism/set-windowsreservedstoragestate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
---

# Set-WindowsReservedStorageState

## 摘要
设置图像的预留存储状态。

## 语法

```
Set-WindowsReservedStorageState -State <ReservedStorageState> [-LogPath <String>] [-ScratchDirectory <String>]
 [-LogLevel <LogLevel>] [<CommonParameters>]
```

## 描述
用于设置预留存储的状态。此命令行选项仅支持在线Windows镜像。如果预留存储正在被使用中，将无法将其禁用，并会返回以下错误：<i>当预留存储正在使用时，不支持此操作。请等待所有服务操作完成后再尝试。</i>对预留存储状态所做的更改会在Sysprep通用化的Windows镜像中体现出来。有关更多信息，请参阅[通过Sysprep（通用化）准备Windows安装](/windows-hardware/manufacture/desktop/sysprep--system-preparation--overview)。

## 示例

### 示例 1
```powershell
PS C:\> Set-WindowsReservedStorageState -State Enabled -Online
```

此命令启用本地主机上的Windows预留存储功能。

## 参数

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘（其存储空间可能小至 32 MB）。日志文件会自动被归档；归档后的日志文件会在原文件名后添加 `.bak` 扩展名，并生成一个新的日志文件。每次日志文件被归档时，对应的 `.bak` 文件都会被覆盖。当使用未加入域的网络共享资源时，请先使用 `net use` 命令并输入相应的域凭据来设置访问权限，然后再指定 DISM 日志的存储路径。

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

### -ScratchDirectory
指定一个临时目录，用于在维护过程中提取文件以供使用。该目录必须存在于本地系统中。如果未指定目录，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时都会为该目录生成一个随机十六进制值的子目录名称。每次操作完成后，临时目录中的内容都会被删除。不建议将网络共享位置作为用于解压安装包（.cab 或 .msu 文件）的临时目录。在维护过程中用于提取文件的临时目录应该是一个本地目录。

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

### -State
该图像的预留存储状态，分为“已禁用”或“已启用”。

```yaml
Type: ReservedStorageState
Parameter Sets: (All)
Aliases:
Accepted values: Disabled, Enabled

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Dism Commands.ReservedStorageState

### System.String

### Microsoft.Dism Commands.LogLevel

## 输出

### Microsoft.Dism Commands.ReservedStorageStateObject

## 备注
支持Windows 10操作系统（版本2004）。

## 相关链接
[Get-WindowsReservedStorageState](./Get-WindowsReservedStorageState.md)
