---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/get-sbecdestination?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-SbecDestination
---

# Get-SbecDestination

## 摘要
获取目标数据文件。

## 语法

```
Get-SbecDestination [[-ComputerName] <String[]>] [[-CimSession] <CimSession[]>] [<CommonParameters>]
```

## 描述
`Get-SbecDestination` cmdlet 可以获取已知的目的地数据文件（这些信息来自状态日志）。

当转发器使用数据创建目标文件时，如果启用了状态日志，这些信息会被记录在状态日志中。随后可以利用这些信息来展示所有已知的目标数据文件列表，以及每个文件的创建者和相关创建时间信息。

状态日志中每个目标文件可能包含多条记录，这是因为该文件被多次覆盖，且自那时起日志未被压缩。不过，此函数始终返回压缩后的视图，即每个文件只显示一条记录。如果管理员在最后一次日志压缩后删除了某些文件，那么返回的文件可能已经不存在了。

如果在收集器配置中未启用状态日志功能，则不会返回任何数据。

## 示例

#### 示例 1：获取目标文件
```
PS C:\> $x = @(Get-SbecDestination)
```

这个命令会获取目标文件，然后将它们存储在 `$x` 变量中。

## 参数

### -CimSession
通过远程会话在远程计算机上运行该cmdlet。可以输入一个会话对象（例如`New-CimSession`或`Get-CimSession` cmdlet的输出结果），或者这些对象的数组。默认情况下，该cmdlet会在本地计算机上运行。有关更多信息，请参阅“About_CimSession”。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。

## 输出

### 类为 \Root\Microsoft\Windows\BootEventCollector\TargetForwardingDestination 的 CIM/WMI 对象
输出包含以下字段：

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
Otherwise will be empty.
- `<ConnectedSince>`: CIM timestamp of when the connection was established.
- `<DisconnectedSince>`: CIM timestamp of when the connection was dropped.
- `<WmiDateTime>`: CIM timestamp of when this state change was recorded.

## 备注

## 相关链接

[Get-SbecForwarding](./Get-SbecForwarding.md)

[Get-SbecHistory](./Get-SbecHistory.md)

