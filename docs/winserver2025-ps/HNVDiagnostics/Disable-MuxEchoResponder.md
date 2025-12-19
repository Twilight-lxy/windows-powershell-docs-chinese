---
description: 使用这个主题来借助 Windows PowerShell 帮助管理 Windows 和 Windows Server 技术。
external help file: MuxEchoResponder.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/disable-muxechoresponder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-MuxEchoResponder
---

# 禁用 MuxEchoResponder

## 摘要
禁用 ICMP 回显响应功能。此cmdlet已被弃用。

## 语法

```
Disable-MuxEchoResponder [-TargetVIP] <String> [[-SequenceNumber] <Int32>] [<CommonParameters>]
```

## 描述
` Disable-MuxEchoResponder ` 这个 cmdlet 用于禁用多路复用器（MUX）中的互联网控制消息协议（ICMP）回声响应功能。

## 示例

### 示例 1：禁用回显响应器
```
PS C:\> Disable-MuxEchoResponder -TargetVIP "10.123.176.108" -SequenceNumber 27
```

## 参数

### -SequenceNumber
指定要禁用的回显响应器的 ICMP 序列号。

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

### -TargetVIP
指定要禁用的 Echo 应答器的目标虚拟 IP 地址。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Enable-MuxEchoResponder](./Enable-MuxEchoResponder.md)

