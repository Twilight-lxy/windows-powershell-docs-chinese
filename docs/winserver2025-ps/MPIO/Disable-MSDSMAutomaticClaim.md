---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Mpio-help.xml
Module Name: MPIO
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/mpio/disable-msdsmautomaticclaim?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-MSDSMAutomaticClaim
---

# 禁用 MSDSA 自动声明功能

## 摘要
防止MSDSM为某种总线类型自动将SAN磁盘分配给MPIO（多路径I/O）。

## 语法

```
Disable-MSDSMAutomaticClaim [-BusType] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
` Disable-MSDSMAutomaticClaim` 这个cmdlet可以阻止特定的Microsoft设备特定模块（MSDSM）自动为指定的总线类型，申请存储区域网络（SAN）磁盘以用于Microsoft多路径I/O（MPIO）功能。

有效的总线类型是串行连接存储（SAS）和互联网小型计算机系统接口（iSCSI）。此cmdlet不会更改之前已标记的SAN磁盘。

## 示例

### 示例 1：禁用 iSCSI 的自动索赔功能
```
PS C:\> Disable-MSDSMAutomaticClaim -BusType "iSCSI"
```

此命令可阻止MSDSM自动为iSCSI总线类型申请SAN磁盘以用于MPIO（多路径I/O）。该命令不会影响之前已申请的磁盘。

该命令不会影响SAS总线类型的设置。如果您希望同时禁用两种总线类型的自动声明功能，请再次使用此cmdlet，并指定“SAS”作为类型参数。

## 参数

### -BusType
用于指定总线类型。此cmdlet会禁用对该总线类型自动获取SAN磁盘的功能。该参数的允许值为：SAS和iSCSI。

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
在运行 cmdlet 之前会提示您进行确认。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Enable-MSDSMAutomaticClaim](./Enable-MSDSMAutomaticClaim.md)

[Get-MSDSMAutomaticClaimSettings](./Get-MSDSMAutomaticClaimSettings.md)

