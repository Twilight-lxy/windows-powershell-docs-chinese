---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/get-sbechistory?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-SbecHistory
---

# Get-SbecHistory

## 摘要
获取连接状态变化的最新记录。

## 语法

```
Get-SbecHistory [[-ComputerName] <String[]>] [[-CimSession] <CimSession[]>] [<CommonParameters>]
```

## 描述
`Get-SbecHistory` cmdlet 用于从设置和启动事件收集器中获取连接状态变化的近期历史记录。

该命令返回的、存储在“Collector”中的历史记录的长度是受到绝对数值限制的。当历史记录的长度超过这个限制后，新的事件会导致旧的事件被覆盖（即旧事件从记录中消失）。因此，返回的历史记录并不完整，而只包含最近的事件。阅读这些历史记录并不会删除它们本身。

类似的信息（以精简的形式）可以由收集者写入状态日志文件中。这种精简体现在：状态日志仅会记录在为新ETL文件建立连接时发生的事件。可以通过`Get-SbecDestination`命令获取状态日志文件中的信息。

## 示例

### 示例 1：获取连接历史记录
```
PS C:\> $x = @(Get-SbecHistory)
```

这个命令可以获取连接历史记录。

## 参数

### -CimSession
通过远程会话在远程计算机上运行该 cmdlet。可以输入一个会话对象（例如 **New-CimSession** 或 **Get-CimSession** cmdlet 的输出结果），或者这些对象的数组。默认情况下，该 cmdlet 会在本地计算机上运行。有关更多信息，请参阅 About_CimSession。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定您想要在其上执行操作的计算机的名称。您可以分别为每台计算机指定一个完全合格的域名（FQDN）、NetBIOS 名称或 IP 地址。有关更多信息，请参阅 MSDN 上的 [Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。

## 输出

### 类为 \Root\Microsoft\Windows\BootEventCollector\TargetForwardingHistory 的 CIM/WMI 对象
CIM/WMI对象包含以下字段：

- `<TargetEndpoint>`: The target computer's endpoint information in human-readable format, as its host:port string (for example, 127.0.0.1:50000).
- `<TargetMac>`: The target computer's MAC address (if known).
- `<TargetGuid>`: The target computer's SMBIOS GUID (if known).
- `<CollectorEndpoint>`: The host:port information of the endpoint on the collector side.
- `<Computer>`: Target computer name, as determined by the collector according to its configuration.
- `<ForwarderType>`: Type of the forwarder (such as 'etl').
- `<Destination>`: Destination of the data.
The meaning depends on the forwarder type.
A file name (such as for the ETL forwarder), or some other identification.
- `<DestinationPattern>`: Pattern used to generate the destination of the data.
The meaning depends on the forwarder type and configuration.
For a fixed destination, would be the same as the destination itself.
For the destination with rotation of the files would contain the pattern characters that will be replaced with the actual index in the destination.
- `<Error>`: Error message if an error was encountered.
Otherwise will be empty.`<ConnectedSince>`: CIM timestamp of when the connection was established.
- `<DisconnectedSince>`: CIM timestamp of when the connection was dropped.
- `<WmiDateTime>`: CIM timestamp of when this state change was recorded.

## 备注

## 相关链接

[Get-SbecDestination](./Get-SbecDestination.md)

[Get-SbecForwarding](./Get-SbecForwarding.md)

