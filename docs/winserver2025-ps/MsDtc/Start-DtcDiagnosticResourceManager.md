---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dtc.PowerShell.dll-Help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/start-dtcdiagnosticresourcemanager?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-DtcDiagnosticResourceManager
---

# Start-DtcDiagnostic ResourceManager

## 摘要
启动一个用于诊断的资源管理器（Resource Manager）。

## 语法

```
Start-DtcDiagnosticResourceManager [[-Port] <Int32>] [[-Name] <String>] [<CommonParameters>]
```

## 描述
`Start-DtcDiagnostic ResourceManager` cmdlet 以 Windows PowerShell® 后台作业的形式启动一个诊断资源管理器（Resource Manager，简称 RM）。

## 示例

### 示例 1：启动诊断资源管理器
```
PS C:\> Start-DtcDiagnosticResourceManager -Port 17124 -Name "testRM"
```

这个示例启动了一个DTC诊断资源管理器。

## 参数

### -Name
指定要启动的诊断资源管理器的名称。之后您可以使用这个名称来引用该资源管理者（RM）。如果您不指定名称，系统会自动为资源管理者分配一个实例ID（通常是GUID），此时您可以凭该ID来引用它。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Port
指定测试RM（Real-Time Messaging）服务器的监听端口。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Join-DtcDiagnostic ResourceManager](./Join-DtcDiagnosticResourceManager.md)

[Stop-DtcDiagnostic ResourceManager](./Stop-DtcDiagnosticResourceManager.md)

