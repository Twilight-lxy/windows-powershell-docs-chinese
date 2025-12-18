---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/set-dfsrgroupschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DfsrGroupSchedule
---

# 设置 DFSR 组计划（Set-DfsrGroupSchedule）

## 摘要
修改复制组的调度计划。

## 语法

### ScheduleNameParameterSet（默认值）
```
Set-DfsrGroupSchedule [-GroupName] <String[]> [[-UseUTC] <Boolean>] [[-ScheduleType] <GroupScheduleType>]
 [[-DomainName] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### CustomScheduleParameterSet
```
Set-DfsrGroupSchedule [-GroupName] <String[]> [[-UseUTC] <Boolean>] [-Day] <DayOfWeek[]>
 [-BandwidthDetail] <String> [[-DomainName] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DfsrGroupSchedule` cmdlet 用于修改复制组的计划设置。分布式文件系统（DFS）的复制计划控制着复制的可用性以及带宽的使用情况。

默认情况下，DFS复制功能会以全带宽进行复制操作，每天24小时、每周7天不间断地执行复制任务。这种配置是推荐的使用方式。

## 示例

### 示例 1：修改一个小组的日程安排
```
PS C:\> Set-DfsrGroupSchedule -GroupName "RG01" -ScheduleType Always
GroupName            : RG01
DomainName           : corp.contoso.com
ReplicationGroupGuid : 1f06f8d4-a0ae-4221-99d2-0bd1bb27882b
UseUTC               : False
HoursReplicated      : 168
BandwidthDetail      : FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
```

此命令使用 **Set-DfsrGroupSchedule** cmdlet 来修改 RG01 复制组，使其能够实现全天候（24 小时/7 天）的完整数据复制。该命令还使用了 *ScheduleType* 参数，因此无需指定任何特定的带宽限制或复制日期。

### 示例 2：修改组计划以防止数据复制
```
PS C:\> Set-DfsrGroupSchedule -GroupName "RG01" -Day Monday,Tuesday,Wednesday,Thursday,Friday -BandwidthDetail ffffffffffffffffffffffffffffffffffff00000000000000000000000000000000ffffffffffffffffffffffffffff
GroupName            : RG01
DomainName           : corp.contoso.com
ReplicationGroupGuid : 1f06f8d4-a0ae-4221-99d2-0bd1bb27882b
UseUTC               : False
HoursReplicated      : 128
BandwidthDetail      : FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
```

该命令使用 **Set-DfsrGroupSchedule** cmdlet 来修改 RG01 复制组的调度规则，以便在周一至周五的上午 9 点到下午 5 点期间禁止所有复制操作，而在其他时间段内则允许全部数据以全带宽进行复制。

## 参数

### -BandwidthDetail
指定一个自定义的时间安排值字符串，该字符串用于定义每个 15 分钟时间间隔内的带宽设置。共有 4 个这样的时间间隔块组成一组，每组代表 1 小时，总共包含 24 组。时间范围从 00:00 开始到 24:00 结束。在 15 分钟的时间间隔内，有效的带宽设置值范围是 0 到 F，各设置的含义如下：

- 0 = No replication
- 1 = 16 kilobits per second (Kbps)
- 2 = 64 Kbps
- 3 = 128 Kbps
- 4 = 256 Kbps
- 5 = 512 Kbps
- 6 = 1 megabit per second (Mbps)
- 7 = 2 Mbps
- 8 = 4 Mbps
- 9 = 8 Mbps
- A = 16 Mbps
- B = 32 Mbps
- C = 64 Mbps
- D = 128 Mbps
- E = 256 Mbps
- F = Full bandwidth replication

您必须指定一个完整的值字符串，并包含所有24个小时内的4个区块组合（总共96个十六进制字符）。例如：`fffffffffff0000ffff0000ffff00004444000044440000444400004444000044440000ffff0000ffff0000ffffffff`

```yaml
Type: String
Parameter Sets: CustomScheduleParameterSet
Aliases:

Required: True
Position: 3
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

### -Day
指定一周中的某一天。您可以指定一个枚举字符串值或其对应的整数值。该参数的允许值为：

- Sunday (0)
- Monday (1)
- Tuesday (2)
- Wednesday (3)
- Thursday (4)
- Friday (5)
- Saturday (6)

```yaml
Type: DayOfWeek[]
Parameter Sets: CustomScheduleParameterSet
Aliases:
Accepted values: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果未指定此参数，cmdlet 将使用当前域。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 100
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GroupName
用于指定一组复制组的名称。如果未指定此参数，则该cmdlet将应用于所有参与的复制组。您可以使用逗号分隔的列表以及通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RG, RgName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### -ScheduleType
指定一种调度类型：一种是禁止复制的类型；另一种是全调度类型，该类型允许每周7天、每天24小时使用全部带宽进行复制。此参数的合法取值为“Never”（0）和“Always”（1）。您可以为该参数指定一个枚举字符串值或其对应的整数值。

```yaml
Type: GroupScheduleType
Parameter Sets: ScheduleNameParameterSet
Aliases:
Accepted values: Never, Always

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseUTC
用于指示目标计算机是否在其日程安排中使用协调世界时（UTC）。默认情况下，目标计算机会根据其本地时间来解释日程安排。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 输出

### Microsoft.DistributedFileSystemReplicationDfsrgroupSchedule

## 备注

## 相关链接

[Get-DfsrGroupSchedule](./Get-DfsrGroupSchedule.md)

