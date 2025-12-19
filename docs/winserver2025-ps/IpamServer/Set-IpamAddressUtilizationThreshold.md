---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamAddressUtilizationThreshold.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/set-ipamaddressutilizationthreshold?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IpamAddressUtilizationThreshold
---

# 设置 Ipam 地址利用率阈值

## 摘要
修改IPAM中的地址使用阈值。

## 语法

```
Set-IpamAddressUtilizationThreshold [-UnderUtilizationThreshold <UInt32>] [-OverUtilizationThreshold <UInt32>]
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-IpamAddressUtilizationThreshold` cmdlet 用于修改 IP 地址管理（IPAM）中地址过度使用和利用不足的阈值。请确保指定的过度使用阈值不低于利用不足的阈值。当某个地址块、子网或地址范围的利用率超过或低于这些阈值时，IPAM 会生成警报。

## 示例

### 示例 1：设置过度使用阈值
```
PS C:\> Set-IpamAddressUtilizationThreshold -OverUtilizationThreshold 70 -PassThru

UnderUtilizationThreshold                                   OverUtilizationThreshold

-------------------------                                   ------------------------

20                                                          70
```

这个命令将地址过度使用阈值设置为70。

该命令包含了 *PassThru* 参数，因此它会将结果显示在控制台上。

### 示例 2：设置资源利用率不足的阈值
```
PS C:\> Set-IpamAddressUtilizationThreshold -UnderUtilizationThreshold 40 -PassThru

UnderUtilizationThreshold                                   OverUtilizationThreshold

-------------------------                                   ------------------------

40                                                          70
```

该命令将地址利用率不足的阈值设置为40。

该命令包含了 *PassThru* 参数，因此它会将结果显示在控制台上。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -OverUtilizationThreshold
指定过度使用阈值的数值。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -ThrottleLimit
指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最优限制值。此限制仅适用于当前运行的cmdlet，而不适用于整个会话或计算机本身。

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

### -UnderUtilizationThreshold
指定未充分利用（underutilization）阈值的数值。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamAddressUtilizationThreshold
这个对象返回一个表示 IPAM 地址空间使用率阈值的对象。

## 备注

## 相关链接

[Get-IpamAddressUtilizationThreshold](./Get-IpamAddressUtilizationThreshold.md)

