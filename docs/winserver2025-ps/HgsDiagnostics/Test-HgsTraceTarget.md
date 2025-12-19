---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.HostGuardianService.Diagnostics.Payload.dll-Help.xml
Module Name: HgsDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsdiagnostics/test-hgstracetarget?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-HgsTraceTarget
---

# 测试 HgsTraceTarget

## 摘要
验证是否可以打开到指定目标的远程 Windows PowerShell® 会话。

## 语法

```
Test-HgsTraceTarget -Target <InputTarget> [<CommonParameters>]
```

## 描述
`Test-HgsTraceTarget` cmdlet 用于验证是否能够连接到指定的远程 Windows PowerShell® 会话，并确认是否存在兼容版本的诊断模块。

## 示例

## 参数

### -Target
指定要测试的目标对象。

```yaml
Type: InputTarget
Parameter Sets: (All)
Aliases: InputObject

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### Microsoft.Windows.HostGuardianServiceDiagnosticPayload.InputTarget
你可以将使用 **New-HgsTraceTarget** cmdlet 创建的目标对象通过管道（pipe）传递出去。

## 输出

### System(Boolean)
如果可以建立连接，并且目标满足所需的条件，则此cmdlet会返回true；否则返回false。如果测试失败，该cmdlet会报告详细的错误信息。

## 备注

## 相关链接

[New-HgsTraceTarget](./New-HgsTraceTarget.md)

