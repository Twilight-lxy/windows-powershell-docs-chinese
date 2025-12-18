---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/enable-sbecbootimage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-SbecBootImage
---

# 启用 SbecBootImage

## 摘要
在离线的 WinPE 安装镜像中启用自动日志记录（AutoLogger）功能。

## 语法

```
Enable-SbecBootImage [-Path] <String[]> [[-Logger] <String[]>] [[-PermLogger] <String[]>] [-NoDefaultLoggers]
 [[-DismLogPath] <String>] [<CommonParameters>]
```

## 描述
`Enable-SbecBootImage` 这个 cmdlet 可以启用 AutoLogger 功能，并在离线的 WinPE 安装镜像中创建 `Winpeshl.ini` 文件，以便将事件转发到安装和启动事件收集器（Setup and Boot Event Collector）。

默认情况下，用于将事件发送到“启动事件收集器”（Boot Event Collector）的事件日志会话包括 NT Kernel Logger、EventLog-System 和 SetupPlatform。您可以使用参数 *Logger* 和 *PermLogger* 来配置其他日志记录器。无论这些日志记录器之前是否曾将数据写入文件，它们总是会被设置为实时模式（即持续记录事件）。

AutoLogger设置允许在安装过程的第一阶段（即从WinPE镜像启动时）进行事件转发。Winpeshl.ini文件通过Unattend.xml文件来帮助配置HDD镜像上的事件处理规则。

## 示例

#### 示例 1：在 WIM 图像中启用启动事件收集器
```
PS C:\> Enable-SbecBootImage -Path "C:\Images\Boot.wim"
```

该命令为Boot.wim映像启用启动事件收集器（Boot Event Collector）。

## 参数

### -DismLogPath
指定用于挂载镜像时的部署映像服务与管理（DISM）日志文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Logger
指定要启用转发功能的 AutoLogger 会话。这些会话上的转发功能在操作系统启动后会自动关闭。如果在 *Logger* 或 *PermLogger* 中明确指定了某个会话，那么该会话的默认设置将被覆盖。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoDefaultLoggers
这表示该操作不会自动添加默认的日志记录器会话集。

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

### -Path
指定一个包含离线 Windows 镜像文件（WIM 或 VHD）完整路径的数组，这些设置将应用于这些文件。如果一个 WIM 文件包含多个镜像，则所有镜像都会被修改。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PermLogger
指定要启用数据转发的自动记录器（AutoLogger）会话。这些会话的数据转发功能在操作系统启动后仍会保持启用状态。如果在*Logger*或*PermLogger*中明确指定了某个会话，那么该会 session 的默认设置将被覆盖。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。

## 输出

### 没有（需要处理的内容）。

## 备注

## 相关链接

[Disable-SbecAutologger](./Disable-SbecAutologger.md)

[Enable-SbecAutologger](./Enable-SbecAutologger.md)

[Enable-SbecWdsBcd](./Enable-SbecWdsBcd.md)

[New-SbecUnattendFragment](./New-SbecUnattendFragment.md)

