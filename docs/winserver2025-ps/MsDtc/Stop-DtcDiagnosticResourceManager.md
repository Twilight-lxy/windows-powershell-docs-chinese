---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dtc.PowerShell.dll-Help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/stop-dtcdiagnosticresourcemanager?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-DtcDiagnosticResourceManager
---

# Stop-DtcDiagnostic ResourceManager

## 摘要
停止并删除一个诊断性的资源管理器作业（Resource Manager job）。

## 语法

### ParameterSetInstance（默认值）
```
Stop-DtcDiagnosticResourceManager [[-Job] <DtcDiagnosticResourceManagerJob>] [<CommonParameters>]
```

### ParameterSetName
```
Stop-DtcDiagnosticResourceManager [[-Name] <String>] [<CommonParameters>]
```

### ParameterSetInstanceId
```
Stop-DtcDiagnosticResourceManager [[-InstanceId] <Guid>] [<CommonParameters>]
```

## 描述
`Stop-DtcDiagnostic ResourceManager` cmdlet 用于停止并删除作为 Windows PowerShell® 后台作业运行的 `DiagnosticResourceManagerJob`。要停止默认的 Resource Manager，必须明确指定该默认 Resource Manager 的名称。

## 示例

### 示例 1：停止一个诊断资源管理器
```
PS C:\> Stop-DtcDiagnosticResourceManager -Name "testRM"
```

此命令用于停止名为“testRM”的DTC诊断资源管理器。

## 参数

### -InstanceId
指定要停止的 **DtcDiag ResourceManagerJob** 实例 ID。

```yaml
Type: Guid
Parameter Sets: ParameterSetInstanceId
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Job
指定要停止的 **DtcDiag ResourceManagerJob** 实例。此参数接受管道输入（pipeline input）。

```yaml
Type: DtcDiagnosticResourceManagerJob
Parameter Sets: ParameterSetInstance
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name
指定要停止的诊断资源管理器的名称。

```yaml
Type: String
Parameter Sets: ParameterSetName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Join-DtcDiagnostic ResourceManager](./Join-DtcDiagnosticResourceManager.md)

[Start-DtcDiagnostic ResourceManager](./Start-DtcDiagnosticResourceManager.md)

