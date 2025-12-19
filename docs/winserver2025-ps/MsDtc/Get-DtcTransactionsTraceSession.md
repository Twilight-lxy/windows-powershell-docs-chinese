---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DtcTransactionsTraceSessionTask_v1.0.cdxml-help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/get-dtctransactionstracesession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DtcTransactionsTraceSession
---

# Get-DtcTransactionsTraceSession

## 摘要
获取主机特定的 DTC 事务跟踪会话设置。

## 语法

```
Get-DtcTransactionsTraceSession [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-DtcTransactionsTraceSession` cmdlet 可以获取主机上分布式事务协调器（DTC）事务跟踪会话的特定设置。同一主机上的所有 DTC 实例都会共享这些跟踪设置。

## 示例

### 示例 1：获取 DTC 交易跟踪会话
```
PS C:\> Get-DtcTransactionsTraceSession
BufferCount SessionStatus               PSComputerName
----------- -------------               --------------
25          Stopped
```

此命令用于查询本地主机上事务追踪会话的摘要信息。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，使用的是本地计算机上的当前会话。

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

### -ThrottleLimit
该参数用于指定可以同时运行的命令行函数（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令行函数的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### DtcTransactionsTraceSession
此cmdlet返回一个**DtcTransactionsTraceSession**对象，其中包含跟踪设置信息。

## 备注

## 相关链接

[Set-DtcTransactionsTraceSession](./Set-DtcTransactionsTraceSession.md)

[Start-DtcTransactionsTraceSession](./Start-DtcTransactionsTraceSession.md)

[Stop-DtcTransactionsTraceSession](./Stop-DtcTransactionsTraceSession.md)

[Write-DtcTransactionsTraceSession](./Write-DtcTransactionsTraceSession.md)

