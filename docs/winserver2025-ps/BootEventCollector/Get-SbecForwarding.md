---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/get-sbecforwarding?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-SbecForwarding
---

# Get-SbecForwarding

## 摘要
获取当前的连接状态以及数据传输的方式。

## 语法

```
Get-SbecForwarding [[-ComputerName] <String[]>] [[-CimSession] <CimSession[]>] [<CommonParameters>]
```

## 描述
`Get-SbecForwarding` cmdlet 可以获取当前的连接状态以及数据是如何从设置和启动事件收集器（Setup and Boot Event Collector）转发出去的。该命令会为每个连接返回一个对象。

## 示例

### 示例 1：了解数据是如何被传输的
```
PS C:\> $x = @(Get-SbecForwarding)
```

这条命令获取转发信息，然后将其存储在变量 $x 中。

## 参数

### -CimSession
通过远程会话在远程计算机上运行该cmdlet。可以输入一个会话对象（例如`New-CimSession`或`Get-CimSession` cmdlet的输出结果），或者这些对象的数组。默认情况下，该cmdlet会在本地计算机上运行。有关更多信息，请参阅“关于_CimSession”。

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
指定您想要在其上执行操作的计算机的名称。对于每台计算机，您可以指定一个完全合格的域名（FQDN）、一个NetBIOS名称或一个IP地址。有关更多信息，请参阅MSDN上的[Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

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

### 类 \Root\Microsoft\Windows\BootEventCollector\TargetForwarding 的 CIM/WMI 对象。
这些对象包含以下字段：

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

## 备注

## 相关链接

[Get-SbecDestination](./Get-SbecDestination.md)

[Get-SbecHistory](./Get-SbecHistory.md)

