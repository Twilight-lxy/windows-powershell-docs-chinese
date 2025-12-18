---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/get-sbeclocalizedmessage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-SbecLocalizedMessage
---

# Get-Sbec Localization

## 摘要
获取一个本地化的消息字符串。

## 语法

```
Get-SbecLocalizedMessage [-Name] <String> [<CommonParameters>]
```

## 描述
`Get-SbeclocalizedMessage` cmdlet 可以根据名称获取相应的本地化消息字符串。

由于“设置”（Setup）和“启动事件收集器”（Boot Event Collector）的错误消息字符串是经过本地化处理的，因此在脚本中识别这些命令返回的错误时，你必须能够理解这些本地化文本的含义。

文件 `$PsHomeModules\BootEventCollector\$PsCulture\BootEventCollectorStrings.psd1` 中包含了本地化后的字符串及其对应的名称。如果您需要获取某条本地化消息的内容，请指定该消息的名称即可。

如果名称未知，该cmdlet会抛出一个错误。

## 示例


## 参数

### -Name
指定要获取的本地化消息的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。

## 输出

### 字符串
这个cmdlet用于获取本地化消息的文本内容。

## 备注

## 相关链接

