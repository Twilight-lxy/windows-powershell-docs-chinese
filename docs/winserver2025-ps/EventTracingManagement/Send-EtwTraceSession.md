---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_EtwTraceSession_v1.0.cdxml-help.xml
Module Name: EventTracingManagement
ms.date: 01/05/2017
online version: https://learn.microsoft.com/powershell/module/eventtracingmanagement/send-etwtracesession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Send-EtwTraceSession
---

# Send-EtwTraceSession

## 摘要
将指定的 ETW 会话的日志文件发送到目标位置。

## 语法

### 按名称排序（默认设置）
```
Send-EtwTraceSession [-Name] <String[]> -DestinationFolder <String> [-DeleteAfterSend]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Send-EtwTraceSession -InputObject <CimInstance[]> -DestinationFolder <String> [-DeleteAfterSend]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Send-EtwTraceSession` cmdlet 将指定的 Windows 事件追踪（ETW）会话的日志文件发送到目标位置。

对于文件模式的ETW会话，会话将会被更新为写入一个新文件，而之前的文件将被复制到指定的目标位置。

对于采用缓冲模式的ETW会话，该会话数据将会被刷新到指定的目标位置。

## 示例

### 示例 1：将跟踪会话发送到文件夹
```
PS C:\> Send-EtwTraceSession -Name "WFP-IPsec Trace" -DestinationFolder "\\server17\traces\" -DeleteExistingFileAfterSend
```

该命令将一个名为“WFP-IPsec Trace”的ETW跟踪会话发送到目标文件夹“\\server17\traces”中。在成功复制原始跟踪文件后，该命令会删除本地副本。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的任务。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值为本地计算机上的当前会话。

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

### -Confirm
在运行cmdlet之前会提示您确认是否要继续。

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

### -DeleteAfterSend
在将文件复制到目标位置后，删除ETW会话原本写入的那个原始文件。

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

### -DestinationFolder
指定输出.etl文件的目标路径。

如果 ETW 会话处于缓冲模式，那么此参数必须是一个完整的文件路径，而不是一个文件夹的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: RemoteShare

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定要输入到此 cmdlet 的数据。您可以使用这个参数，也可以将数据通过管道（pipe）传递给此 cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name
指定 ETW 会话的名称。

```yaml
Type: String[]
Parameter Sets: ByName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最优限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -WhatIf
展示了如果该cmdlet被运行会发生的后果。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注
* The return values consist of a Win32 error code and a value returned by the cmdlet. The codes have the following meanings:

- 0: **Success**. New file created. Existing file copied to the destination folder. Existing file deleted, if specified.
- 1: **CreateNewFileFailed**. Operation halts at this point if a new file is not created.
- 2: **CopyFileFailed**. New file created.
- 3: **DeleteOldFileFailed**. New file created. Existing file copied to the destination folder.

## 相关链接

[Get-EtwTraceSession](./Get-EtwTraceSession.md)

[New-EtwTraceSession](./New-EtwTraceSession.md)

[Save-EtwTraceSession](./Save-EtwTraceSession.md)

[开始 ETW 跟踪会话](./Start-EtwTraceSession.md)

[Stop-EtwTraceSession](./Stop-EtwTraceSession.md)

[Update-EtwTraceSession](./Update-EtwTraceSession.md)

