---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/set-dfsrconnectionschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DfsrConnectionSchedule
---

# Set-DfsrConnectionSchedule

## 摘要
更改复制组中成员之间连接调度的相关设置。

## 语法

### ScheduleNameParameterSet（默认值）
```
Set-DfsrConnectionSchedule [[-GroupName] <String[]>] [-SourceComputerName] <String>
 [-DestinationComputerName] <String> [[-UseUTC] <Boolean>] [[-ScheduleType] <ConnectionScheduleType>]
 [[-DomainName] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### CustomScheduleParameterSet
```
Set-DfsrConnectionSchedule [[-GroupName] <String[]>] [-SourceComputerName] <String>
 [-DestinationComputerName] <String> [[-UseUTC] <Boolean>] [-Day] <DayOfWeek[]> [-BandwidthDetail] <String>
 [[-DomainName] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DfsrConnectionSchedule` cmdlet 用于更改复制组中两个成员之间连接的计划和时间安排以及带宽限制设置。

分布式文件系统（DFS）的复制连接是复制组中各成员之间的逻辑关联。DFS复制服务使用远程过程调用（RPC）协议在服务器之间进行通信。默认情况下，DFS复制会按照推荐的计划和带宽配置创建连接：使用全部带宽，并确保每周7天、每天24小时均可正常使用。

## 示例

#### 示例 1：配置完整的连接计划
```
PS C:\> Set-DfsrConnectionSchedule -GroupName "RG24" -SourceComputerName "SRV01" -DestinationComputerName "SRV02" -ScheduleType Always
GroupName               : RG24
SourceComputerName      : SRV01
DestinationComputerName : SRV02
DomainName              : corp.contoso.com
ConnectionGuid          : fb4a502f-48d1-4926-ae29-c1e90b32c139
UseUTC                  : False
HoursReplicated         : 168
BandwidthDetail         : FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFF
```

此命令用于配置从名为 SRV01 的服务器到名为 SRV02 的服务器之间的连接计划，这两个服务器属于 RG24 复制组。参数 *ScheduleType* 指定了一个完整的复制计划，该计划允许在每天 24 小时、每周 7 天内进行复制操作，并且会使用全部带宽。

### 示例 2：设置连接计划
```
PS C:\> Set-DfsrConnectionSchedule -GroupName "RG24" -SourceComputerName "SRV01" -DestinationComputerName "SRV01" -Day Monday,Tuesday,Wednesday,Thursday,Friday - BandwidthDetail "ffffffffffffffffffffffffffffffffffff00000000000000000000000000000000ffffffffffffffffffffffffffff"


GroupName               : RG 1
SourceComputerName      : SRV1
DestinationComputerName : SRV2
DomainName              : corp.contoso.com
ConnectionGuid          : fb4a502f-48d1-4926-ae29-c1e90b32c139
UseUTC                  : False
HoursReplicated         : 128
BandwidthDetail         : FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000FFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000FFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000FFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000FFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFF
```

此命令用于配置从名为 SRV01 的服务器到 RG24 复制组中名为 SRV02 的服务器的连接计划。该命令规定：DFS 复制服务在周一至周五的上午 9 点至下午 5 点期间禁止所有复制操作；而在其他时间范围内，复制操作将允许以全带宽进行。

## 参数

### -BandwidthDetail
指定一个自定义的计划时间值字符串。

时间表中的值定义了每个15分钟时间段内的设置（包括该时间段的带宽），每组包含4个时间段，一组代表1小时。总共有24组这样的时间段。时间从00:00开始，到24:00结束。在15分钟的时间段内，有效的设置范围是从0（零）到F（使用十六进制表示）。以下是有效设置的对应关系：

请帮我将以下Markdown格式的内容翻译成中文：

0 = 不进行复制  
1 = 每秒16千比特（Kbps）  
2 = 64 Kbps  
3 = 128 Kbps  
4 = 256 Kbps  
5 = 512 Kbps  
6 = 每秒1兆比特（Mbps）  
7 = 2 Mbps  
8 = 4 Mbps  
9 = 8 Mbps  
A = 16 Mbps  
B = 32 Mbps  
C = 64 Mbps  
D = 128 Mbps  
E = 256 Mbps  
F = 全带宽复制

一个完整的值字符串必须包含所有24组数据，每组数据由4个块组成，总共需要96个十六进制字符。例如：`fffffffffff0000ffff0000ffff000044440000444400004444000044440000ffff0000ffff0000ffffffff`

```yaml
Type: String
Parameter Sets: CustomScheduleParameterSet
Aliases:

Required: True
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前，会提示您进行确认。

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
用于指定一周中的一系列天数。对于这个参数，你可以提供一个枚举字符串值或其对应的整数。该参数的可接受值为：

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
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DestinationComputerName
指定接收计算机的名称。接收计算机也被称为入站计算机或下游计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ReceivingMember, RMem

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果您不指定此参数，cmdlet 将使用当前用户的所在域。

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
指定一个复制组名称数组。您可以使用逗号分隔的列表以及通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RG, RgName

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### -ScheduleType
指定连接调度类型。您可以选择继承自复制组的调度方式、基于连接的“关闭”模式（该模式下不允许数据复制），或者基于连接的“全开”模式（该模式下支持全天候（24小时×7天）的数据复制，并使用全部带宽进行传输）。对于此参数，您既可以输入一个枚举字符串值，也可以输入相应的整数值。该参数的合法取值为：

- UseGroupSchedule (0)
- Never (1)
- Always (2)

```yaml
Type: ConnectionScheduleType
Parameter Sets: ScheduleNameParameterSet
Aliases:
Accepted values: UseGroupSchedule, Never, Always

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SourceComputerName
指定发送计算机的名称。发送计算机也被称为出站计算机或上游计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: SendingMember, SMem

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

### -UseUTC
该选项用于指示目标计算机是否使用协调世界时（UTC）来处理时间安排。默认情况下，目标计算机会按照自身的本地时间来解读这些时间安排。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### 字符串

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrConnectionSchedule

## 备注

## 相关链接

[Get-DfsrConnectionSchedule](./Get-DfsrConnectionSchedule.md)
