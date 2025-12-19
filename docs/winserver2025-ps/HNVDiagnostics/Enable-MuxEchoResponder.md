---
description: 使用这个主题来借助 Windows PowerShell 帮助管理 Windows 和 Windows Server 技术。
external help file: MuxEchoResponder.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/enable-muxechoresponder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-MuxEchoResponder
---

# Enable-MuxEchoResponder

## 摘要
启用 ICMP 回显响应功能。此命令已被弃用。

## 语法

```
Enable-MuxEchoResponder [-TargetVIP] <String> [[-SequenceNumber] <Int32>] [<CommonParameters>]
```

## 描述
`Enable-MuxEchoResponder` cmdlet 可以在多路复用器（MUX）中启用 ICMP 回声响应功能。

你应该在 MUX 虚拟机上运行此 cmdlet，既可以是在本地操作，也可以通过远程 PowerShell 来执行。

## 示例

### 示例 1：启用一个回显响应器
```
PS C:\> Enable-MuxEchoResponder -TargetVIP "10.123.176.108" -SequenceNumber 27
```

此命令可启用指定的回显响应器（echo responder）。

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
指定要启用的 Echo 回应器的目标虚拟 IP 地址。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Disable-MuxEchoResponder](./Disable-MuxEchoResponder.md)

