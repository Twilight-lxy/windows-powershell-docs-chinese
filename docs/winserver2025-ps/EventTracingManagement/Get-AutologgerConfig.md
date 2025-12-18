---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_AutologgerConfig_v1.0.cdxml-help.xml
Module Name: EventTracingManagement
ms.date: 01/05/2017
online version: https://learn.microsoft.com/powershell/module/eventtracingmanagement/get-autologgerconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AutologgerConfig
---

# 获取自动记录器配置

## 摘要
列出现有的 AutoLogger 会话配置。

## 语法

```
Get-AutologgerConfig [[-Name] <String[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-AutologgerConfig` cmdlet 用于枚举现有的 AutoLogger 会话配置。

## 示例

#### 示例 1：获取配置信息
```
PS C:\> Get-AutologgerConfig -Name "WFP-IPsec Trace"
Name                       : WFP-IPsec Trace
BufferSize                 :
ClockType                  : 2
DisableRealtimePersistence :
FileCount                  :
FileName                   : %SystemRoot%\System32\LogFiles\WMI\wfp.etl
FileMax                    :
FlushTimer                 :
Guid                       : {0762bd13-14d5-4928-9db0-6c4e96312988}
LogFileMode                : 0x1202
MaximumFileSize                : 8
MaximumBuffers             :
MinimumBuffers             :
Start                      : 0
InitStatus                 : 0
```

这个命令用于获取名为“WFP-IPsec Trace”的自动记录器（AutoLogger）配置信息。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定 AutoLogger 会话的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的cmdlet操作的最大数量。如果省略此参数或输入值`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前正在执行的cmdlet，而不影响整个会话或计算机本身。

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

## 备注

## 相关链接

[配置并启动自动日志记录会话](https://msdn.microsoft.com/library/windowsdesktop/aa363687.aspx)

[日志记录模式常量](https://msdn.microsoft.com/library/windowsdesktop/aa364080.aspx)

[New-AutologgerConfig](./New-AutologgerConfig.md)

[Remove-AutologgerConfig](./Remove-AutologgerConfig.md)

[更新自动记录器配置](./Update-AutologgerConfig.md)

