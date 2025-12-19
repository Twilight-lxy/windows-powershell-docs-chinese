---
description: 从本地机器收集Windows本地管理员密码解决方案（LAPS）相关的日志和追踪数据。
external help file: LAPS-help.xml
Module Name: LAPS
online version: https://learn.microsoft.com/powershell/module/laps/get-lapsdiagnostics?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
Locale: en-US
ms.date: 04/10/2023
title: Get-LapsDiagnostics
---

# 获取圈数诊断信息

## 摘要
从本地机器收集 Windows 本地管理员密码解决方案（LAPS）的相关日志和跟踪数据。

## 语法

```
Get-LapsDiagnostics [[-OutputFolder] <String>] [-CollectNetworkTrace] [-ResetPassword]
 [<CommonParameters>]
```

## 描述

`Get-LapsDiagnostics` cmdlet 从本地机器收集 LAPS 日志和跟踪数据，并将它们复制到一个 `.zip` 文件中。该 cmdlet 主要用于支持性和测试场景，但当然也可以在任何时候使用。生成的 `.zip` 文件名称中包含机器名称和当前时间戳，默认情况下会被保存在 `$env:TEMP\LapsDiagnostics` 文件夹下。可以通过设置 `OutputFolder` 参数来自定义输出文件夹的位置。

## 示例

### 示例 1

```powershell
Get-LapsDiagnostics
```

```Output
Get-LapsDiagnostics: all data for this run was written to the following zip file:

C:\Users\ADMINI~1\AppData\Local\Temp\LapsDiagnostics\LapsDiagnostics_LAPSCLIENT_2023041004_072649.zip
```

这个示例展示了如何使用所有默认参数来收集LAPS诊断信息的基本内容。

### 示例 2

```powershell
Get-LapsDiagnostics -OutputFolder c:\LapsDiagFolder
```

```Output
Get-LapsDiagnostics: all data for this run was written to the following zip file:

c:\LapsDiagFolder\LapsDiagnostics_LAPSCLIENT_2023041004_072702.zip
```

这个示例演示了如何将LAPS诊断信息收集到指定的输出文件夹中。

### 示例 3

```powershell
Get-LapsDiagnostics -OutputFolder c:\LapsDiagFolder -ResetPassword
```

```Output
Get-LapsDiagnostics: all data for this run was written to the following zip file:

c:\LapsDiagFolder\LapsDiagnostics_LAPSCLIENT_2023041004_072709.zip
```

这个示例演示了如何在强制密码重置操作过程中收集LAPS诊断信息，并将这些信息保存到指定的输出文件夹中。

### 示例 4

```powershell
Get-LapsDiagnostics -CollectNetworkTrace
```

```Output
Get-LapsDiagnostics: all data for this run was written to the following zip file:

C:\Users\ADMINI~1\AppData\Local\Temp\LapsDiagnostics\LapsDiagnostics_LAPSCLIENT_2023041004_072719.zip
```

这个示例展示了如何收集基本的LAPS诊断信息，同时还进行网络追踪（network tracing）。

## 参数

### -CollectNetworkTrace

指定网络追踪数据也应被收集并包含在最终的`.zip`文件中。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OutputFolder

指定生成的`.zip`文件应放置在指定的文件夹中。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResetPassword

指定在强制重置当前管理的本地账户的密码时，应收集相关的日志和跟踪信息。在这种模式下，该cmdlet会在调用`Reset-LapsPassword` cmdlet的过程中收集跟踪数据。

如果未指定此参数，该cmdlet将在调用`Invoke-LapsProcessingCycle` cmdlet的过程中收集跟踪信息。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Windows LAPS概述](https://go.microsoft.com/fwlink/?linkid=2233901)
