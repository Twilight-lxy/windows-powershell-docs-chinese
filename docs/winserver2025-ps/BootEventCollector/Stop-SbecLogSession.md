---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/stop-sbeclogsession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-SbecLogSession
---

# 停止 SbecLogSession 会话

## 摘要
停止日志会话。

## 语法

### 对象
```
Stop-SbecLogSession -Session <TraceSessionInfo[]> [<CommonParameters>]
```

### 名称
```
Stop-SbecLogSession -Name <String[]> [<CommonParameters>]
```

## 描述
`Stop-SbecLogSession` cmdlet 用于停止日志会话。

## 示例


## 参数

### -Name
指定要停止的日志会话的名称。

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
指定要停止的会话对象。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### SbecEtwTrace.TraceSessionInfo
`SbecEtwTrace.TraceSessionInfo` 类定义在 `$PsHomeModules\BootEventCollector\SbecTrace Helpers.psm1` 文件中。

## 输出

### 没有（需要处理的内容）。

## 备注

## 相关链接

[Get-SbecLogSession](./Get-SbecLogSession.md)

[Save-SbecLogSession](./Save-SbecLogSession.md)

[Set-SbecLogSession](./Set-SbecLogSession.md)

[开始 SbecLogSession 会话](./Start-SbecLogSession.md)

[开始 SbecNtKernelLogSession 会话](./Start-SbecNtKernelLogSession.md)

[开始 SbecSimpleLogSession 会话](./Start-SbecSimpleLogSession.md)

