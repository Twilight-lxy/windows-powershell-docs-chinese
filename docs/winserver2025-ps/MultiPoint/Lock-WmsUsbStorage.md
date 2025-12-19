---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/lock-wmsusbstorage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Lock-WmsUsbStorage
---

# Lock-WmsUsbStorage

## 摘要
防止使用USB存储设备。

## 语法

### LockById
```
Lock-WmsUsbStorage [-StationId] <UInt32[]> [-Server <String>] [<CommonParameters>]
```

### LockAll
```
Lock-WmsUsbStorage [-All] [-Server <String>] [<CommonParameters>]
```

## 描述
`Lock-WmsUsbStorage` 这个 cmdlet 会阻止使用任何连接到工作站上的 USB 存储设备。如果在运行 `Lock-WmsUsbStorage` 时已经有设备连接到了工作站上，这些设备将会被“逻辑上”移除（即系统不再认为它们是可用的）。此后任何新添加到工作站上的 USB 设备都会被系统隐藏起来（无法被正常使用）。

## 示例

#### 示例 1：锁定 USB 存储设备
```
PS C:\> Lock-WmsUsbStorage -StationId 2
```

此命令可阻止在指定工作站上使用所有USB存储设备。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: LockAll
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定该命令的目标（即MultiPoint Server）的完整主机名。默认值为localhost。

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
指定一个包含多点站ID的数组。该参数的可接受值为：1到站点总数之间的任意整数。

```yaml
Type: UInt32[]
Parameter Sets: LockById
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32[]

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[解锁 WMS USB 存储功能](./Unlock-WmsUsbStorage.md)

