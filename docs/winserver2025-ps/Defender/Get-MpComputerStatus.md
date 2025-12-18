---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_MpComputerStatus.cdxml-help.xml
Module Name: Defender
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/defender/get-mpcomputerstatus?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MpComputerStatus
---

# 获取计算机状态信息

## 摘要
获取计算机上反恶意软件软件的状态。

## 语法

```
Get-MpComputerStatus [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
[<CommonParameters>]
```

## 描述

`Get-MpComputerStatus` cmdlet 可以获取计算机上安装的反恶意软件的状态信息。

## 示例

#### 示例 1：获取计算机状态

```
PS C:\> Get-MpComputerStatus
AMEngineVersion                 : 1.1.9700.0
AMProductVersion                : 4.3.9463.0
AMRunningMode                   : Normal
AMServiceEnabled                : True
AMServiceVersion                : 4.3.9463.0
AntispywareEnabled              : True
AntispywareSignatureAge         : 0
AntispywareSignatureLastUpdated : 7/30/2013 3:01:45 AM
AntispywareSignatureVersion     : 1.155.1107.0
AntivirusEnabled                : True
AntivirusSignatureAge           : 0
AntivirusSignatureLastUpdated   : 7/30/2013 3:01:45 AM
AntivirusSignatureVersion       : 1.155.1107.0
BehaviorMonitorEnabled          : True
ComputerID                      : A69DA5B8-06B3-4A00-B2C1-D18ED66BAD40
ComputerState                   : 0
FullScanAge                     : 4294967295
FullScanEndTime                 :
FullScanStartTime               :
IoavProtectionEnabled           : True
LastFullScanSource              : 0
LastQuickScanSource             : 2
NISEnabled                      : False
NISEngineVersion                : 2.1.9700.0
NISSignatureAge                 : 0
NISSignatureLastUpdated         : 7/30/2013 1:30:46 PM
NISSignatureVersion             : 106.0.0.0
OnAccessProtectionEnabled       : True
QuickScanAge                    : 0
QuickScanEndTime                : 7/30/2013 1:50:24 PM
QuickScanStartTime              : 7/30/2013 1:49:15 PM
RealTimeProtectionEnabled       : True
RealTimeScanDirection           : 0
```

这个命令用于获取计算机上安装的反恶意软件保护程序的状态。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或整个计算机。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。 ## 输入内容

## 输出

## 备注

## 相关链接

[获取-MpComputerStatus的属性](/previous-versions/windows/desktop/defender/msft-mpcomputerstatus#properties)
