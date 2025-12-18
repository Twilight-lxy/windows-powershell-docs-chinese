---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/stop-sbecinstance?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-SbecInstance
---

# 停止 SbecInstance 实例

## 摘要
停止设置过程以及启动事件收集器的运行。

## 语法

### 服务
```
Stop-SbecInstance [-Service] [-Force] [<CommonParameters>]
```

### 直接
```
Stop-SbecInstance [-Direct] [-ComputerName <String[]>] [-CimSession <CimSession[]>] [-Force]
 [<CommonParameters>]
```

## 描述
**Stop-SbecInstance** cmdlet 用于停止 Setup and Boot Event Collector 的一个实例。

您必须具有内置管理员（Builtin Administrator）权限才能运行此cmdlet。

## 示例

### 示例 1：停止 Boot Event Collector 服务
```
PS C:\> Stop-SbecInstance -Service
```

此命令会停止“启动事件收集器”（Boot Event Collector）服务。

### 示例 2：停止一个启动事件收集器（Boot Event Collector）实例
```
PS C:\> Stop-SbecInstance -Direct
```

此命令用于停止通过命令行启动的“Boot Event Collector”实例。

### 示例 3：立即停止一个启动事件收集器（Boot Event Collector）实例
```
PS C:\> Stop-SbecInstance -Direct -Force
```

此命令会停止通过命令行启动的“Boot Event Collector”实例，并丢弃所有已缓冲但尚未处理的数据。

## 参数

### -CimSession
通过远程会话在远程计算机上运行该 cmdlet。可以输入一个会话对象（例如 **New-CimSession** 或 **Get-CimSession** cmdlet 的输出结果），或者这些对象的数组。默认情况下，该 cmdlet 会在本地计算机上运行。有关更多信息，请参阅 About_CimSession。

```yaml
Type: CimSession[]
Parameter Sets: Direct
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定您想要在其上执行操作的计算机的名称。您可以指定一个完全 qualified domain name (FQDN)、一个 NetBIOS 名称或一个 IP 地址。有关更多信息，请参阅 MSDN 上的 [Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

```yaml
Type: String[]
Parameter Sets: Direct
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Direct
通过 WMI/CIM 接口直接停止 Setup and Boot Event Collector 实例。如果该实例是通过命令提示符启动的，可以指定此参数来将其关闭。

如果有多个实例正在运行（包括该服务），指定此参数会停止其中一个随机选择的实例，因为WMI会连接到任意一个随机运行的实例。请不要在服务中使用这个参数，否则服务控制器会将其视为服务故障并重新启动该服务。

```yaml
Type: SwitchParameter
Parameter Sets: Direct
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
使用 `Service` 参数时，该参数作为 **Stop-Service** 命令的传递参数，使 cmdlet 能够停止某个服务，即使该服务有依赖的其他服务。当使用 `Direct` 选项时，则会请求快速停止服务，此时会丢弃尚未完全处理但已被缓冲的数据。

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

### -Service
停止当前计算机上的“设置和启动事件收集器”服务。

```yaml
Type: SwitchParameter
Parameter Sets: Service
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。

## 输出

### 没有（需要处理的内容）。

## 备注

## 相关链接

[Get-SbecActiveConfig](./Get-SbecActiveConfig.md)

[Save-SbecInstance](./Save-SbecInstance.md)

[Set-SbecActiveConfig](./Set-SbecActiveConfig.md)

[启动 Sbec 实例](./Start-SbecInstance.md)

[Test-SbecActiveConfig](./Test-SbecActiveConfig.md)

