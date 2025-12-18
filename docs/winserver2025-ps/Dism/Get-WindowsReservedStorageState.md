---
external help file: Microsoft.Dism.PowerShell.dll-Help.xml
Module Name: Dism
online version: https://learn.microsoft.com/powershell/module/dism/get-windowsreservedstoragestate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
---

# Get-WindowsReservedStorageState

## 摘要
获取图像的预留存储状态。

## 语法

```
Get-WindowsReservedStorageState [-LogPath <String>] [-ScratchDirectory <String>] [-LogLevel <LogLevel>]
 [<CommonParameters>]
```

## 描述
获取预留存储空间的当前状态。此命令仅支持在线Windows镜像。

## 示例

### 示例 1
```powershell
PS C:\> Get-WindowsReservedStorageState
```

此命令用于获取本地主机上的Windows预留存储空间状态。

## 参数

### -LogLevel
用于指定日志中显示的输出级别。可选的值如下：  
- Errors（或“0”）：显示错误事件。可以与其他级别（如Warnings或WarningsInfo）结合使用。  
- Warnings（或“1”）：显示警告事件。  
- WarningsInfo（或“2”）：显示信息日志记录。

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
指定用于记录日志的完整路径和文件名。如果未设置，默认值为 `%WINDIR%\Logs\Dism\dism.log`。在 Windows PE 环境中，默认目录是 RAMDISK 虚拟磁盘中的临时存储空间，其容量可能低至 32 MB。日志文件会自动被归档；归档后的日志文件名会加上 `.bak` 扩展名，同时系统会生成一个新的日志文件。每次日志文件被归档时，原来的 `.bak` 文件都会被覆盖。如果使用的是未加入域的网络共享资源，请在使用 `DISM` 命令设置日志路径之前，先通过 `net use` 命令并输入相应的域凭据来配置访问权限。


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
指定一个临时目录，该目录将在执行维护操作（如文件提取）时被使用。此目录必须存在于本地系统中。如果未指定临时目录，则会使用 `\Windows\%Temp%\` 目录，并且每次运行 DISM 时，该目录下的子目录名称都会是一个随机生成的十六进制值。每次维护操作完成后，临时目录中的内容都会被删除。不建议将网络共享位置用作用于展开安装包（.cab 或 .msu 文件）的临时目录。因此，在执行维护操作期间用于提取文件的临时目录应当是本地目录。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### Microsoft.Dismcommands.LogLevel

## 输出

### Microsoft.Dism Commands.ReservedStorageStateObject

## 备注
支持 Windows 10 的 2004 版本

## 相关链接
[Set-WindowsReservedStorageState](./Set-WindowsReservedStorageState.md)
