---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/join-wmsstation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Join-WmsStation
---

# 连接WMS站点

## 摘要
将一个车站拆分为多个独立的部分。

## 语法

### JoinById
```
Join-WmsStation [-StationId] <UInt32[]> [-Server <String>] [<CommonParameters>]
```

### JoinAll
```
Join-WmsStation [-All] [-Server <String>] [<CommonParameters>]
```

## 描述
`Join-WmsStation` cmdlet 用于将当前被分割为两个逻辑显示区的指定物理显示区重新合并为一个单一的显示区。

## 示例

### 示例 1：车站接驳信息显示
```
PS C:\> Join-WmsStation -StationId 1,2,5
```

此命令会将当前被分割为两个逻辑显示器的指定物理显示器重新合并为一个单一的显示器。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: JoinAll
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定该命令的目标（即MultiPoint Server）的完全限定主机名。默认值为localhost。

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
指定一个车站ID数组。有效值为1（表示车站的数量）。

```yaml
Type: UInt32[]
Parameter Sets: JoinById
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32[]

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Clear-WmsStation](./Clear-WmsStation.md)

[Get-WmsStation](./Get-WmsStation.md)

[Set-WmsStation](./Set-WmsStation.md)

[Split-WmsStation](./Split-WmsStation.md)

[更新 WMS 站点](./Update-WmsStation.md)

