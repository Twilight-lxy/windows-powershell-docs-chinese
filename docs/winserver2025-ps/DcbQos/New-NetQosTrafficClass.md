---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetQosTrafficClass.cdxml-help.xml
Module Name: DcbQos
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/dcbqos/new-netqostrafficclass?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-NetQosTrafficClass
---

# 新的NetQos流量类别

## 摘要
创建一个流量类别。

## 语法

### 由 IfAlias（默认值）生成
```
New-NetQosTrafficClass [-Name] <String> [-Algorithm] <Algorithm> [-BandwidthPercentage <Byte>]
 [-Priority] <Byte[]> [-InterfaceAlias <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 作者：ByIfIndex
```
New-NetQosTrafficClass [-Name] <String> [-Algorithm] <Algorithm> [-BandwidthPercentage <Byte>]
 [-Priority] <Byte[]> [-InterfaceIndex <UInt32>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
这个 `New-NetQosTrafficClass` cmdlet 用于创建一个流量类。流量类的概念在 IEEE 数据中心桥接 (DCB) 标准中的增强传输选择 (ETS) 规范中有详细说明。在创建流量类时，用户需要指定哪些类型的流量（这些流量通过 IEEE 802.1p 优先级进行区分）会被映射到该流量类中，使用哪种传输算法，以及这些流量将获得多少带宽。如果 Windows Server® 2012 或更高版本设置为“不接受”来自远程设备的 DCB 配置，那么 Windows Server 2012 或更高版本会禁止支持 DCB 的网络适配器添加新的流量类。

有关远程设备配置的更多信息，请参阅 **Set-NetQosDcbxSetting** cmdlet。

Windows Server 2012及更高版本会创建一个默认的流量类别。所有8个优先级都被映射到这个默认流量类别上，该类别选择ETS（Enhanced Transmission Service）作为传输算法，并占用全部的总带宽。用户无法删除这个默认流量类别。由于一个流量类别至少需要有一种类型的流量被映射到它上面，而根据IEEE 802.1p标准，这样的流量类型最多只能有8种，因此最多只能再创建7个额外的流量类别。

实际上，支持DCB（Direct Connect Bus）的网络适配器可能只能支持少于8个流量类别。如果在Windows Server 2012或更高版本中配置的流量类别数量超过了网络适配器的支持范围，那么Windows Server 2012或更高版本将不会将这些配置发送给网络适配器。

## 示例

#### 示例 1：创建一个交通类别
```
PS C:\> New-NetQosTrafficClass -Name "SMB" -Priority 3 -Algorithm ETS -BandwidthPercentage 60

Name                      Algorithm Bandwidth(%) Priority
----                      --------- ------------ --------
SMB                       ETS       60           3
```

此命令为标记有 802.1p 值为 3 的流量创建了一个流量类别。这个名为 SMB 的流量类别将占用 60% 的带宽。

## 参数

### -Algorithm
```yaml
Type: Algorithm
Parameter Sets: (All)
Aliases: tsa
Accepted values: Strict, ETS

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -BandwidthPercentage
```yaml
Type: Byte
Parameter Sets: (All)
Aliases: Bandwidth, bw

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
在运行该cmdlet之前，会提示您进行确认。

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

### -InterfaceAlias
```yaml
Type: String
Parameter Sets: ByIfAlias
Aliases: IfAlias

Required: False
Position: Named
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
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Priority
```yaml
Type: Byte[]
Parameter Sets: (All)
Aliases: p, pri

Required: True
Position: 2
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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.UInt32

## 输出

### System.Object

## 备注

## 相关链接

[Get-NetQosTrafficClass](./Get-NetQosTrafficClass.md)

[Set-NetQosTrafficClass](./Set-NetQosTrafficClass.md)

