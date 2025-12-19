---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DtcLogTask_v1.0.cdxml-help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/get-dtclog?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DtcLog
---

# Get-DtcLog

## 摘要
获取DTC日志文件设置信息。

## 语法

```
Get-DtcLog [-DtcName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-DtcLog` cmdlet 可用于获取分布式事务协调器（DTC）实例的日志文件设置。请使用 `DtcName` 参数来指定所需的 DTC 实例。

## 示例

### 示例 1：获取本地 DTC 实例的日志文件设置
```
PS C:\> Get-DtcLog
MaxSizeInMB      : 512
Path             : C:\Windows\system32\MSDtc
SizeInMB         : 4
```

这个命令用于获取本地DTC实例的DTC日志文件设置信息。

### 示例 2：获取指定 DTC 实例的日志文件设置
```
PS C:\> Get-DtcLog -DtcName "InstanceName"
MaxSizeInMB      : 512
Path             : G:\MSDTC\beb6d145-405e-47cd-b326-a5505a461229
SizeInMB         : 4
```

此命令用于获取指定DTC实例的DTC日志文件设置信息。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在该会话中操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，也可以输入会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -DtcName
用于指定一个 DTC（分布式事务协调器）实例。该 cmdlet 会显示该实例的日志文件设置信息。如果您未指定此参数，或者指定了 “Local” 值，则会显示本地 DTC 实例的日志文件设置信息。

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

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Reset-DtcLog](./Reset-DtcLog.md)

[Set-DtcLog](./Set-DtcLog.md)

