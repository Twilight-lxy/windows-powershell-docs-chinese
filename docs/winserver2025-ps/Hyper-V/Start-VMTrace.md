---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/start-vmtrace?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-VMTrace
---

# 启动虚拟机跟踪（Start-VMTrace）

## 摘要
从某个文件开始进行跟踪。

## 语法

```
Start-VMTrace [-Level] <TraceLevel> [-TraceVerboseObjects] [-Path <String>] [<CommonParameters>]
```

## 描述
`Start-VMTrace` cmdlet 用于将跟踪日志写入文件中。您可以利用这些日志信息进行高级调试。

## 示例

### 示例 1：启动错误追踪
```
PS C:\> Start-VMTrace -Level Error
```

此命令从“Error”（错误）级别开始进行跟踪。

## 参数

### -Level
指定跟踪的级别。此参数的可接受值为：

- Off
- Error
- Warning
- Info
- Verbose

```yaml
Type: TraceLevel
Parameter Sets: (All)
Aliases:
Accepted values: Error, Warning, Info, Verbose

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
Specifies the path of the file where this cmdlet stores the trace information.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TraceVerboseObjects
Specifies that tracing uses verbose objects.

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

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[Stop-VMTrace](./Stop-VMTrace.md)

