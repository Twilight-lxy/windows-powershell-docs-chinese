---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetQosTrafficClass.cdxml-help.xml
Module Name: DcbQos
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/dcbqos/set-netqostrafficclass?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NetQosTrafficClass
---

# 设置 NetQos 流量类别

## 摘要
设置流量类别的相关配置。

## 语法

### 由 IfAlias （默认值）生成
```
Set-NetQosTrafficClass [[-Name] <String[]>] [[-InterfaceAlias] <String>] [-Algorithm <Algorithm>]
 [-BandwidthPercentage <Byte>] [-Priority <Byte[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByIfIndex
```
Set-NetQosTrafficClass [[-Name] <String[]>] [[-InterfaceIndex] <UInt32>] [-Algorithm <Algorithm>]
 [-BandwidthPercentage <Byte>] [-Priority <Byte[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-NetQosTrafficClass -InputObject <CimInstance[]> [-Algorithm <Algorithm>] [-BandwidthPercentage <Byte>]
 [-Priority <Byte[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-NetQosTrafficClass` cmdlet 用于修改流量类的设置，例如 802.1p 优先级与流量类之间的映射关系、必须使用的传输算法以及分配给该流量类的带宽。如果 Windows Server® 2012 或更高版本被设置为“不愿意”接收来自远程设备的配置信息，那么它会将这些更新后的设置发送到计算机中支持数据中心桥接（DCB）功能的网络适配器上。

有关远程设备配置的更多信息，请参阅 **Set-NetQosDcbxSetting** cmdlet。

有关流量类别的更多信息，请参阅 **New-NetQosTrafficClass** cmdlet。

## 示例

### 示例 1：更改某个流量类别的带宽分配
```
PS C:\> Set-NetQosTrafficClass -Name "SMB" -BandwidthPercentage 50
```

此命令将名为“SMB”的流量类的带宽分配比例修改为50%。

### 示例 2：更改某个流量类的优先级映射
```
PS C:\> Get-NetQosTrafficClass -Name "SMB" | Set-NetQosTrafficClass -Priority 3,4
```

此命令使用 **Get-NetQosTrafficClass** cmdlet 来获取名为 “SMB” 的流量类的设置。该命令通过管道运算符将这些设置传递给当前正在执行的 cmdlet。然后，这个 cmdlet 会修改优先级映射设置，使得标记为 3 或 4 的流量被分配到名为 “SMB” 的流量类中。

## 参数

### -Algorithm
```yaml
Type: Algorithm
Parameter Sets: (All)
Aliases: tsa
Accepted values: Strict, ETS

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -InputObject
指定要传递给此cmdlet的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

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

### -Name
```yaml
Type: String[]
Parameter Sets: ByIfAlias, ByIfIndex
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
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
Parameter Sets: (All)
Aliases: p, pri

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.UInt32

### Microsoft.ManagementInfrastructure.CimInstance[]

### Microsoft.PowerShell CmdletizationGeneratedTypes.NetQosTrafficClass.Algorithm

### System Byte

### System Byte[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetQosTrafficClassSettingData

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows Management Instrumentation (WMI) 对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。此 cmdlet 返回一个 **MSFT_NetQosTrafficClassSettingData** 对象，该对象包含网络流量相关的数据。只有当你指定了 *PassThru* 参数时，cmdlet 才会返回这个 **MSFT_NetQosTrafficClassSettingData** 对象。

## 备注

## 相关链接

[Get-NetQosTrafficClass](./Get-NetQosTrafficClass.md)

[New-NetQosTrafficClass](./New-NetQosTrafficClass.md)

[Remove-NetQosTrafficClass](./Remove-NetQosTrafficClass.md)

[Set-NetQosDcbxSetting](./Set-NetQosDcbxSetting.md)

[Set-NetQosTrafficClass](./Set-NetQosTrafficClass.md)

