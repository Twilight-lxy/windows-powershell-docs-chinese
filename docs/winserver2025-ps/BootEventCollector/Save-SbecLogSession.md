---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/save-sbeclogsession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Save-SbecLogSession
---

# 保存 SbecLogSession

## 摘要
将日志会话中的缓冲区数据刷新到磁盘上。

## 语法

### 对象
```
Save-SbecLogSession -Session <TraceSessionInfo[]> [<CommonParameters>]
```

### 名称
```
Save-SbecLogSession -Name <String[]> [<CommonParameters>]
```

## 描述
`Save-SbecLogSession` cmdlet 将日志会话中的缓冲区内容刷新到磁盘上。该会话可以通过名称或对象来标识。

## 示例


## 参数

### -Name
指定一个会话名称数组。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Session
指定一个包含 **SbecEtwTrace.TraceSessionInfo** 对象的数组。

```yaml
Type: TraceSessionInfo[]
Parameter Sets: Object
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### SbecEtwTrace.TraceSessionInfo
此 cmdlet 接受 **SbecEtwTrace TRACESessionInfo** 对象作为需要刷新缓冲区的会话。

## 输出

### 没有（需要特别说明的内容）。

## 备注

## 相关链接

[Get-SbecLogSession](./Get-SbecLogSession.md)

[Set-SbecLogSession](./Set-SbecLogSession.md)

[Start-SbecLogSession](./Start-SbecLogSession.md)

[开始 SbecSimpleLogSession 会话](./Start-SbecSimpleLogSession.md)

[开始 SbecNtKernelLogSession 会话](./Start-SbecNtKernelLogSession.md)

[Stop-SbecLogSession](./Stop-SbecLogSession.md)

