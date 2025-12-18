---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/save-sbecinstance?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Save-SbecInstance
---

# 保存 Sbec 实例

## 摘要
将内存缓冲区中的数据写入磁盘。

## 语法

```
Save-SbecInstance [[-ComputerName] <String[]>] [[-CimSession] <CimSession[]>] [<CommonParameters>]
```

## 描述
`Save-SbecInstance` cmdlet 将正在运行的 Setup 和 Boot Event Collector 的内存缓冲区数据写入磁盘。

当命令执行完毕返回结果后，设置事件收集器（Setup Event Collector）和启动事件收集器（Boot Event Collector）中的转发器（forwarders）所持有的缓冲区数据会被保存到磁盘上；这样一来，所有在接收到写入请求之前的数据都会被完整地保存下来。

你必须具有内置管理员（Built-in Administrator）权限才能运行此 cmdlet。

这个cmdlet的别名是**Flush-SbecInstance**。

## 示例


## 参数

### -CimSession
通过远程会话在远程计算机上运行相应的cmdlet。可以提供一个会话对象（例如`New-CimSession`或`Get-CimSession` cmdlet的输出结果），或者提供这些对象的数组。默认情况下，该cmdlet会在本地计算机上执行。有关更多信息，请参阅“About_CimSession”。

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
指定您想要在其上执行操作的计算机的名称。您可以分别为每台计算机指定一个完全限定的域名（FQDN）、NetBIOS 名称或 IP 地址。有关更多信息，请参阅 MSDN 上的 [Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

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

### 无。

## 输出

### 无。

## 备注

## 相关链接

[Get-SbecActiveConfig](./Get-SbecActiveConfig.md)

[Set-SbecActiveConfig](./Set-SbecActiveConfig.md)

[Stop-SbecInstance](./Stop-SbecInstance.md)

[Test-SbecActiveConfig](./Test-SbecActiveConfig.md)

[测试-SbecConfig配置](./Test-SbecConfig.md)

