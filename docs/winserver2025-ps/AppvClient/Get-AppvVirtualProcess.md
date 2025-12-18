---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: AppVClientCmdlets-help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/get-appvvirtualprocess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppvVirtualProcess
---

# Get-AppvVirtualProcess

## 摘要
显示在计算机上运行的虚拟进程。

## 语法

### 名称（默认值）
```
Get-AppvVirtualProcess [[-Name] <String[]>] [-ComputerName <String[]>] [-Module] [-FileVersionInfo]
 [<CommonParameters>]
```

### ID
```
Get-AppvVirtualProcess -Id <Int32[]> [-ComputerName <String[]>] [-Module] [-FileVersionInfo]
 [<CommonParameters>]
```

### InputObject
```
Get-AppvVirtualProcess [-ComputerName <String[]>] [-Module] [-FileVersionInfo] -InputObject <Process[]>
 [<CommonParameters>]
```

## 描述
`Get-AppvVirtualProcess` cmdlet 可以显示计算机上正在运行的每个虚拟进程。

## 示例

### 示例 1：显示所有正在运行的虚拟进程
```
PS C:\> Get-AppvVirtualProcess
```

这个命令会显示所有正在运行的虚拟进程。

### 示例 2：显示虚拟进程的文件信息
```
PS C:\> Get-AppvVirtualProcess -Name "myVirtualProcess" -FileVersionInfo
```

这个命令会显示名为“myVirtualProcess”的进程的文件信息。

### 示例 3：使用管道运算符显示虚拟进程的文件信息
```
PS C:\> Get-Process -Name "myVirtualProcess" | Get-AppvVirtualProcess -FileVersionInfo
```

这个命令会显示名为“myVirtualProcess”的进程的文件信息。

## 参数

### -ComputerName
指定一个包含计算机名称的数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: Cn

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -FileVersionInfo
表示此cmdlet会为每个`ProcessName`返回`ProductVersion`、`FileVersion`以及未虚拟化的`Filename`。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: FV, FVI

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Id
指定虚拟进程ID。

```yaml
Type: Int32[]
Parameter Sets: Id
Aliases: PID

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputObject
指定要输入到此cmdlet的数据。您可以使用这个参数，也可以将数据通过管道（pipe）传递给此cmdlet。

```yaml
Type: Process[]
Parameter Sets: InputObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Module
指定一个模块。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个进程的名称，该名称也被称为 **ProcessName**。

```yaml
Type: String[]
Parameter Sets: Name
Aliases: ProcessName

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.Diagnosis.Process

## 输出

## 备注

## 相关链接

[启动 AppV 虚拟进程](./Start-AppvVirtualProcess.md)

