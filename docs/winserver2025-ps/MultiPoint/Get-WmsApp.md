---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/get-wmsapp?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WmsApp
---

# Get-WmsApp

## 摘要
获取当前会话中正在运行的应用程序集合。

## 语法

```
Get-WmsApp [-SessionId] <UInt32> [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-WmsApp` cmdlet 可以获取指定会话中当前正在运行的应用程序集合，同时还会获取这些应用程序的进程 ID、窗口 ID 以及进程创建时间。

## 示例

#### 示例 1：获取正在运行的应用程序
```
PS C:\> Get-WmsApp -SessionId 3
Name                                                               ProcessId                                WindowId                           CreateTime
----                                                               ------                                   ----                               ----------
Calculator                                                         4228                                     197108                             129937600254314944
```

这个命令可以获取在会话3中运行的应用程序。


## 参数

### -Server
指定作为该命令目标的 MultiPoint Server 的完全限定主机名。默认值为 localhost。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ComputerName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SessionId
指定远程桌面会话（Remote Desktop Session，简称RDS）的ID。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32

### System.String

## 输出

### Microsoft.WindowsServerSolutions.MultipointServer.PowerShellcommands.Library.WmsRunningApp

## 备注

## 相关链接

[Close-WmsApp](./Close-WmsApp.md)

[Open-WmsApp](./Open-WmsApp.md)

