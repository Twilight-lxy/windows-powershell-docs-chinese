---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DtcNetworkSettingTask_v1.0.cdxml-help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/get-dtcnetworksetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DtcNetworkSetting
---

# Get-DtcNetworkSetting

## 摘要
获取 DTC 的网络和安全配置设置。

## 语法

```
Get-DtcNetworkSetting [-DtcName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-DtcNetworkSetting` cmdlet 可以获取分布式事务协调器（DTC）实例的网络和安全配置信息。请使用 `DtcName` 参数来指定相应的 DTC 实例。

## 示例

### 示例 1：获取本地 DTC 实例的网络和安全配置设置
```
PS C:\> Get-DtcNetworkSetting -DtcName "Local"
AuthenticationLevel               : Mutual
InboundTransactionsEnabled        : True
LUTransactionsEnabled             : True
OutboundTransactionsEnabled       : True
RemoteAdministrationAccessEnabled : True
RemoteClientAccessEnabled         : True
XATransactionsEnabled             : True
```

这个命令用于获取本地DTC实例的网络和安全配置设置。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 类型的 cmdlets；要获取作业结果，则可以使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
用于指定一个 DTC（分布式事务协调器）实例。该 cmdlet 会获取该实例的网络和安全配置设置。如果您不指定此参数，或者指定的值为 “Local”，则该 cmdlet 会返回本地 DTC 实例的网络和安全配置信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行该cmdlet的最大操作数量。如果省略此参数或输入`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前执行的cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Set-DtcNetworkSetting](./Set-DtcNetworkSetting.md)

