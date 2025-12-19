---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/unlock-wmsusbstorage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Unlock-WmsUsbStorage
---

# 解锁 WMS USB 存储

## 摘要
解锁USB存储设备。

## 语法

### UnlockById
```
Unlock-WmsUsbStorage [-StationId] <UInt32[]> [-Server <String>] [<CommonParameters>]
```

### 解锁全部（UnlockAll）
```
Unlock-WmsUsbStorage [-All] [-Server <String>] [<CommonParameters>]
```

## 描述
`Unlock-WmsUsbStorage` cmdlet 可以启用指定工作站上的 USB 存储功能。如果某个 USB 存储设备被隐藏了，这个 cmdlet 会将其重新显示出来，使其可用。

## 示例

### 示例 1：解除对 USB 存储设备的限制（即取消对其使用的禁止）
```
PS C:\> Unlock-WmsUsbStorage -StationId 2
```

此命令会解封指定工作站上的USB存储设备。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: UnlockAll
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定作为命令目标的多点服务器（MultiPoint Server）的完全限定主机名。默认值为 localhost。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ComputerName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StationId
指定一个站点ID数组。

```yaml
Type: UInt32[]
Parameter Sets: UnlockById
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32[]

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Lock-WmsUsbStorage](./Lock-WmsUsbStorage.md)

