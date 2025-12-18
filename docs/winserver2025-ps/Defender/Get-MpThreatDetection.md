---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_MpThreatDetection.cdxml-help.xml
Module Name: Defender
ms.date: 09/19/2018
online version: https://learn.microsoft.com/powershell/module/defender/get-mpthreatdetection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MpThreatDetection
---

# Get-MpThreatDetection

## 摘要
当Windows Defender检测到恶意软件威胁时，该功能会被激活并帮助系统避开这些威胁。

## 语法

### DefaultSet（默认设置）
```
Get-MpThreatDetection [<CommonParameters>]
```

### ById
```
Get-MpThreatDetection [-ThreatID <Int64[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-MpThreatDetection` 这个 cmdlet 用于获取 Windows Defender 在计算机上检测到的恶意软件威胁的相关信息。如果 Windows Defender 检测到了您指定的威胁，该 cmdlet 会返回一个列表，显示每次 Windows Defender 发现该威胁的具体时间。

## 示例

#### 示例 1：获取 Windows Defender 检测到的威胁
```
PS C:\> Get-MpThreatDetection
```

该命令会返回本地计算机过去检测到的恶意软件列表。

**错误代码**

下表列出了此 cmdlet 的十六进制和十进制错误代码。每个十六进制错误代码前都有一个 “0x8050” 前缀。因此，ERROR_mp_BAD_SCANID 错误对应于错误代码 0x80508012；ERR_MP_REMOVE_FAILED 错误对应于错误代码 0x80508017。

有关错误代码的列表，以及可能的原因和解决方法，请参阅[Windows Defender 防病毒客户端错误代码](/windows/security/threat-protection/windows-defender-antivirus/troubleshoot-windows-defender-antivirus#windows-defender-antivirus-client-error-codes)，该内容位于主题[查看事件日志和错误代码以排除 Windows Defender 防病毒的问题](/windows/security/threat-protection/windows-defender-antivirus/troubleshoot-windows-defender-antivirus#window-defense-antivirus-client-error-codes)中。

|Symbolic Name                       | Error Number (hexadecimal) | Error number (decimal) |
|------------------------------------|----------------------------|------------------------|
|ERROR_MP_UI_CONSOLIDATION_BASE      | 0x80501000                 | 2142236672             |
|ERROR_MP_ACTIONS_FAILED             | 0x80501001                 | 2142236671             |
|ERROR_MP_BAD_INIT_MODULES           | 0x80508001                 | 2142207999             |
|ERROR_MP_BAD_DATABASE               | 0x80508002                 | 2142207998             |
|ERROR_MP_BAD_UFS                    | 0x80508004                 | 2142207996             |
|ERROR_MP_NO_MEMORY                  | 0x80508007                 | 2142207993             |
|ERROR_MP_BAD_INPUT_DATA             | 0x8050800C                 | 2142288079             |
|ERROR_MP_BAD_GLOBAL_STORAGE         | 0x8050800D                 | 2142207987             |
|ERROR_MP_OBSOLETE                   | 0x8050800E                 | 2142207986             |
|ERROR_MP_NOT_SUPPORTED              | 0x8050800F                 | 2142207985             |
|ERROR_MP_NO_MORE_ITEMS              | 0x80508010                 | 2142207984             |
|ERROR_MP_DUPLICATE_SCANID           | 0x80508011                 | 2142207983             |
|ERROR_MP_BAD_SCANID                 | 0x80508012                 | 2142207982             |
|ERROR_MP_BAD_USERDB_VERSION         | 0x80508013                 | 2142207981             |
|ERROR_MP_RESTORE_FAILED             | 0x80508014                 | 2142207980             |
|ERROR_MP_FAILED_TO_SPYNET           | 0x80508015                 | 2142207979             |
|ERROR_MP_BAD_ACTION                 | 0x80508016                 | 2142207978             |
|ERROR_MP_REMOVE_FAILED              | 0x80508017                 | 2142207977             |
|ERROR_MP_SCAN_ABORTED               | 0x80508018                 | 2142207976             |
|ERROR_MP_NOT_FOUND                  | 0x80508019                 | 2142207975             |
|ERROR_MP_BAD_CONFIGURATION          | 0x80508020                 | 2142207968             |
|ERROR_MP_QUARANTINE_FAILED          | 0x80508021                 | 2142207967             |
|ERROR_MP_REBOOT_REQUIRED            | 0x80508022                 | 2142207966             |
|ERROR_MP_THREAT_NOT_FOUND           | 0x80508023                 | 2142207965             |
|ERROR_MP_FULL_SCAN_REQUIRED         | 0x80508024                 | 2142207964             |
|ERROR_MP_MANUAL_STEPS_REQUIRED      | 0x80508025                 | 2142207963             |
|ERROR_MP_REMOVE_NOT_SUPPORTED       | 0x80508026                 | 2142207962             |
|ERROR_MP_REMOVE_LOW_MEDIUM_DISABLED | 0x80508027                 | 2142207961             |
|ERR_MP_RESCAN_REQUIRED              | 0x80508029                 | 2142207959             |
|ERROR_RELO_BAD_EHANDLE              | 0x80509001                 | 2142203903             |
|ERROR_RELO_KERNEL_NOT_LOADED        | 0x80509003                 | 2142203901             |
|ERROR_MP_BADDB_OPEN                 | 0x8050A001                 | 2142199807             |
|ERROR_MP_BADDB_HEADER               | 0x8050A002                 | 2142199806             |
|ERROR_MP_BADDB_OLDENGINE            | 0x8050A003                 | 2142199805             |
|ERROR_MP_BADDB_CONTENT              | 0x8050A004                 | 2142199804             |
|ERROR_MP_BADDB_NOTSIGNED            | 0x8050A005                 | 2142199803             |

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: SwitchParameter
Parameter Sets: ById
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: ById
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThreatID
指定一个威胁ID数组。此cmdlet会获取您所指定的威胁信息。

```yaml
Type: Int64[]
Parameter Sets: ById
Aliases: ID

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: ById
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-MpThreat](./Get-MpThreat.md)

[Remove-MpThreat](./Remove-MpThreat.md)

[Get-MpThreatCatalog](./Get-MpThreatCatalog.md)
