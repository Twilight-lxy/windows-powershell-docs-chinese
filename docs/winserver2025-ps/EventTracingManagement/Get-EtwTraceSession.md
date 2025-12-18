---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_EtwTraceSession_v1.0.cdxml-help.xml
Module Name: EventTracingManagement
ms.date: 01/05/2017
online version: https://learn.microsoft.com/powershell/module/eventtracingmanagement/get-etwtracesession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-EtwTraceSession
---

# 获取 EtwTraceSession

## 摘要
枚举系统上的 ETW（事件跟踪）会话。

## 语法

```
Get-EtwTraceSession [-Name] <String[]> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-EtwTraceSession` cmdlet 用于枚举系统上的 Windows 事件跟踪（ETW）会话。

## 示例

### 示例 1：获取跟踪会话
```
PS C:\> Get-EtwTraceSession -Name "NetCfgTrace"
```

这个命令用于获取名为 NetCfgTrace 的 ETW（Event Tracking Windows）跟踪会话。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定 ETW 会话的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行该 cmdlet 的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或整个计算机。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[New-EtwTraceSession](./New-EtwTraceSession.md)

[Save-EtwTraceSession](./Save-EtwTraceSession.md)

[Send-EtwTraceSession](./Send-EtwTraceSession.md)

[开始 ETW 跟踪会话](./Start-EtwTraceSession.md)

[Stop-EtwTraceSession](./Stop-EtwTraceSession.md)

[更新-EtwTraceSession](./Update-EtwTraceSession.md)

