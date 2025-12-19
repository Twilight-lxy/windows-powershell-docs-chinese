---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/split-wmsstation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Split-WmsStation
---

# Split-WmsStation

## 摘要
将一个电台节目分成多个部分（或段）。

## 语法

### SplitById
```
Split-WmsStation [-StationId] <UInt32[]> [-Server <String>] [<CommonParameters>]
```

### SplitAll
```
Split-WmsStation [-All] [-Server <String>] [<CommonParameters>]
```

## 描述
`Split-WmsStation` cmdlet 将指定的气象站拆分为两个独立的气象站。

## 示例

#### 示例 1：分割一个车站
```
PS C:\> Split-WmsStation -StationId 01
```

这个命令会将ID为01的车站拆分为两个独立的车站。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: SplitAll
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定该命令的目标的多点服务器（MultiPoint Server）的完整主机名。默认值为 localhost。

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
指定一个车站ID数组。

```yaml
Type: UInt32[]
Parameter Sets: SplitById
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

[Clear-WmsStation](./Clear-WmsStation.md)

[Get-WmsStation](./Get-WmsStation.md)

[加入WMS站点](./Join-WmsStation.md)

[Set-WmsStation](./Set-WmsStation.md)

[更新 WMS 站点](./Update-WmsStation.md)

