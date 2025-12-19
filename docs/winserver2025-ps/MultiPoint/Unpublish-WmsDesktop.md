---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/unpublish-wmsdesktop?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Unpublish-WmsDesktop
---

# 取消发布 WmsDesktop

## 摘要
停止共享指定的会话桌面。

## 语法

```
Unpublish-WmsDesktop [-SessionId] <UInt32> [-Server <String>] [<CommonParameters>]
```

## 描述
`Unpublish-WmsDesktop` 这个 cmdlet 用于停止指定会话桌面内容的共享功能。

## 示例

### 示例 1：停止共享桌面
```
PS C:\> Unpublish-WmsDesktop -SessionId 2
```

此命令会停止与会话ID为2的桌面共享功能。

## 参数

### -Server
指定作为该命令目标的多点服务器（MultiPoint Server）的完全限定主机名。默认值为 localhost。

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
指定用于停止共享的会话ID。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Publish-WmsDesktop](./Publish-WmsDesktop.md)

[Show-WmsDesktop](./Show-WmsDesktop.md)

