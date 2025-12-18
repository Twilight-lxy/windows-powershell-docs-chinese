---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/get-sbeclogsession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-SbecLogSession
---

# Get-SbecLogSession

## 摘要
获取运行日志会话信息。

## 语法

```
Get-SbecLogSession [[-Name] <String>] [-KdOnly] [[-SimulateError] <Int32>] [<CommonParameters>]
```

## 描述
`Get-SbecLogSession` cmdlet 用于获取当前正在运行的 ETW（Events Tracing Windows）日志会话。该操作不会检索注册表中为 AutoLogger 定义的日志会话信息。

此cmdlet会返回`SbecEtwTrace TRACESessionInfo`对象，这些对象的属性包含了大部分有用的信息。更多详细内容可以在`Trace`属性中找到。

## 示例


## 参数

### -KdOnly
表示此操作仅获取那些被配置为通过内核传输机制将事件转发到收集器的日志会话。

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
指定日志会话的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SimulateError
模拟一个Windows错误，导致函数抛出异常。你可以指定这个参数来测试错误处理机制。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。

## 输出

### SbecEtwTrace TRACESessionInfo
`SbecEtwTrace.TraceSessionInfo` 类定义在 `$PsHomeModules\BootEventCollector\SbecTrace Helpers.psm1` 中。

## 备注

## 相关链接

[Save-SbecLogSession](./Save-SbecLogSession.md)

[Set-SbecLogSession](./Set-SbecLogSession.md)

[开始 SbecLogSession 会话](./Start-SbecLogSession.md)

[Start-SbecNtKernelLogSession](./Start-SbecNtKernelLogSession.md)

[开始 SbecSimpleLogSession 会话](./Start-SbecSimpleLogSession.md)

[Stop-SbecLogSession](./Stop-SbecLogSession.md)

