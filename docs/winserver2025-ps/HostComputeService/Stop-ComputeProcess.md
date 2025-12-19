---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HostCompute.PowerShell.Cmdlets.dll-Help.xml
Module Name: HostComputeService
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/hostcomputeservice/stop-computeprocess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-ComputeProcess
---

# 停止计算进程

## 摘要
在 Hyper-V 主机计算服务中停止正在运行的计算系统。

## 语法

### ID（默认值）
```
Stop-ComputeProcess [-Id] <String> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 对象
```
Stop-ComputeProcess -ComputeProcess <ComputeProcess[]> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Stop-ComputeProcess` cmdlet 用于停止 Hyper-V 主机计算服务中正在运行的计算系统。

## 示例


## 参数

### -ComputeProcess
指定一个计算系统数组，该cmdlet会停止这些系统的运行。要获取一个**ComputeProcess**对象，请使用**Get-ComputeProcess** cmdlet。

```yaml
Type: ComputeProcess[]
Parameter Sets: Object
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而不会询问用户的确认。

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

### -Id
指定该cmdlet将要停止运行的计算系统的ID。

```yaml
Type: String
Parameter Sets: Id
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-ComputeProcess](./Get-ComputeProcess.md)

