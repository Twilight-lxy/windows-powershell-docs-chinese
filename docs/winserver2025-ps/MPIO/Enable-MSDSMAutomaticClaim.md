---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Mpio-help.xml
Module Name: MPIO
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/mpio/enable-msdsmautomaticclaim?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-MSDSMAutomaticClaim
---

# 启用 MSDSMAutomaticClaim 功能

## 摘要
使 MSDSM 能够自动为 MPIO 功能申请使用 SAN 磁盘。

## 语法

```
Enable-MSDSMAutomaticClaim [-BusType] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-MSDSMAutomaticClaim` cmdlet 允许微软设备特定模块（Microsoft Device Specific Module，简称 MSDSM）自动为某种总线类型的磁盘申请存储区域网络（Storage Area Network，简称 SAN）资源，以便使用微软多路径 I/O（Microsoft Multipath I/O，简称 MPIO）技术。

你必须指定一个有效的总线类型，可以是串行连接存储（SAS）或互联网小型计算机系统接口（iSCSI）。你可以启用 MSDSM 以自动识别 SAS 和 iSCSI 磁盘。运行该 cmdlet 两次，一次用于 SAS，另一次用于 iSCSI。

## 示例

#### 示例 1：为 iSCSI 启用自动索赔功能
```
PS C:\> Enable-MSDSMAutomaticClaim -BusType "iSCSI"
```

此命令使 MSDSM 能够自动申请使用 iSCSI 总线类型的资源。如果需要使用 SAS 总线类型，请指定 “SAS” 代替 “iSCSI”。

## 参数

### -BusType
用于指定总线类型。该cmdlet使MSDSM能够自动为该总线类型申请SAN磁盘。此参数的可接受值为：SAS和iSCSI。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: SAS, iSCSI

Required: True
Position: 0
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[禁用-MSDSMAutomaticClaim](./Disable-MSDSMAutomaticClaim.md)

[Get-MSDSMAutomaticClaimSettings](./Get-MSDSMAutomaticClaimSettings.md)

