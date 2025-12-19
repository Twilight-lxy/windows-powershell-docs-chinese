---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/disable-wmsscheduledupdate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-WmsScheduledUpdate
---

# 禁用WMS计划更新

## 摘要
在启用磁盘保护功能且处于“丢弃”模式时，会禁用定时更新。

## 语法

```
Disable-WmsScheduledUpdate [-Server <String>] [<CommonParameters>]
```

## 描述
` Disable-WmsScheduledUpdate ` 这个 cmdlet 在磁盘保护功能启用且处于“丢弃模式”（discard mode）时，会禁用定时更新。

## 示例

### 示例 1：禁用本地计算机上的定时更新功能
```
PS C:\> Disable-WmsScheduledUpdate
```

此命令会禁用本地计算机上的定时更新功能。

### 示例 2：禁用指定计算机的计划更新功能
```
PS C:\> Disable-WmsScheduledUpdate -Server "sample.microsoft.com"
```

此命令将禁用对计算机 sample.microsoft.com 的计划更新。

## 参数

### -Server
指定该命令的目标（即MultiPoint Server）的完全限定主机名。默认值为localhost。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Enable-WmsScheduledUpdate](./Enable-WmsScheduledUpdate.md)

[Get-WmsScheduledUpdate](./Get-WmsScheduledUpdate.md)

[Set-WmsScheduledUpdate](./Set-WmsScheduledUpdate.md)

