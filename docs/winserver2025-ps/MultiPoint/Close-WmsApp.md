---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/close-wmsapp?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Close-WmsApp
---

# 关闭 WMS 应用程序

## 摘要
关闭一个应用程序。

## 语法

```
Close-WmsApp [-SessionId] <UInt32> [-ProcessId] <UInt32> [-WindowId] <UInt64> [-CreateTime] <UInt64>
 [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Close-WmsApp` cmdlet 使用指定的进程 ID 和窗口 ID 来关闭指定的应用程序。该 cmdlet 会首先尝试优雅地关闭应用程序；如果应用程序无法优雅地关闭，则会强制关闭它。

## 示例

### 示例 1：关闭一个应用程序
```
PS C:\> Close-WmsApp -SessionId 3 -ProcessId 852 -WindowId 65854 -CreateTime 45689009809823
```

这个命令会关闭在会话3中运行的应用程序，该应用程序的进程ID为852，窗口ID为65854。

使用 `Get-WmsApp` 命令来获取应用程序列表及其进程 ID 和窗口 ID。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -CreateTime
指定进程创建的时间。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ProcessId
指定要关闭的进程的ID。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

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
指定会话的ID。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WindowId
指定窗口的ID。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Get-WmsApp](./Get-WmsApp.md)

[Open-WmsApp](./Open-WmsApp.md)

