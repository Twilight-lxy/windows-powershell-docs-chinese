---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetQosFlowControl.cdxml-help.xml
Module Name: DcbQos
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/dcbqos/enable-netqosflowcontrol?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-NetQosFlowControl
---

# 启用 NetQoS Flow Control（网络服务质量流量控制）

## 摘要
根据IEEE 802.1p优先级实现链路级别的流量控制功能。

## 语法

### 使用 ByIfAlias（默认值）
```
Enable-NetQosFlowControl [[-Priority] <Byte[]>] [[-InterfaceAlias] <String>] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 作者：ByIfIndex
```
Enable-NetQosFlowControl [[-Priority] <Byte[]>] [[-InterfaceIndex] <UInt32>] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Enable-NetQosFlowControl -InputObject <CimInstance[]> [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-NetQosFlowControl` cmdlet 可在 Windows Server® 2012 及更高版本中启用基于优先级的流控（PFC）功能。PFC 是 IEEE 数据中心桥接（DCB）标准的一部分。如果 Windows Server 2012 或更高版本被配置为“不愿意”接收来自远程设备的配置，那么该系统会自动使用支持 DCB 功能的网卡（NIC），从而在链路层实现 PFC 功能。

有关远程设备配置的更多信息，请参阅 **Set-NetQosDcbxSetting** cmdlet。

在链路的两端都启用流控制可以降低由于链路拥塞而导致数据包丢失的概率。某些高层协议甚至假设底层协议是无损的（即不会发生数据包丢失）。在这种情况下，务必确保启用了流控制功能。PFC（优先级流量控制，Priority Flow Control）允许针对某种特定类型的流量来单独启用流控制，这种流量类型通过IEEE 802.1p协议中的优先级来标识。在链路的两端保持一致的PFC配置非常重要；如果配置不匹配，实际上就相当于根本没有启用流控制功能一样。

## 示例

#### 示例 1：根据优先级为流量启用流控机制
```
PS C:\> Enable-NetQosFlowControl -Priority 3,6
```

此命令允许对标记为优先级3和优先级6的流量进行流控（即控制数据包的传输顺序或速率）。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 类型的 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（about_Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称或会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定要传递给此 cmdlet 的输入数据。你可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -InterfaceAlias
```yaml
Type: String
Parameter Sets: ByIfAlias
Aliases: IfAlias

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InterfaceIndex
```yaml
Type: UInt32
Parameter Sets: ByIfIndex
Aliases: IfIndex

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
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

### -Priority
```yaml
Type: Byte[]
Parameter Sets: ByIfAlias, ByIfIndex
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
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

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.UInt32

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[ Disable-NetQosFlowControl](./Disable-NetQosFlowControl.md)

[Get-NetQosFlowControl](./Get-NetQosFlowControl.md)

[Set-NetQosDcbxSetting](./Set-NetQosDcbxSetting.md)

[Set-NetQosFlowControl](./Set-NetQosFlowControl.md)

