---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsrconnectionschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsrConnectionSchedule
---

# Get-DfsrConnectionSchedule

## 摘要
获取复制组中各成员之间的连接调度信息。

## 语法

```
Get-DfsrConnectionSchedule [[-GroupName] <String[]>] [-SourceComputerName] <String>
 [-DestinationComputerName] <String> [[-DomainName] <String>] [<CommonParameters>]
```

## 描述
`Get-DfsrConnectionSchedule` cmdlet 用于获取连接计划信息。

分布式文件系统（DFS）复制连接是复制组中各成员之间的逻辑关联。DFS复制服务使用远程过程调用（RPC）协议在服务器之间进行通信。DFS复制计划负责控制复制的可用性以及带宽的使用情况。

## 示例

### 示例 1：获取连接计划
```
PS C:\> Get-DfsrConnectionSchedule -GroupName "RG24" -SourceComputerName "SRV02" -DestinationComputerName "SRV01"


GroupName               : RG24
SourceComputerName      : SRV02
DestinationComputerName : SRV1
DomainName              : corp.contoso.com
ConnectionGuid          : b3249896-e3ec-468b-a06a-31946d86e426
UseUTC                  : False
HoursReplicated         : 168
BandwidthDetail         : Using the replication group's schedule
```

该命令从名为 SRV02 的服务器获取到与名为 SRV01 的服务器之间的基于连接的复制计划。由于管理员没有为该连接指定自定义的复制计划，因此该连接会继承来自复制组的计划设置。

#### 示例 2：获取自定义的连接计划
```
PS C:\> Get-DfsrConnectionSchedule -GroupName "RG24" -SourceComputerName "SRV01" -DestinationComputerName "SRV02"


GroupName               : RG24
SourceComputerName      : SRV01
DestinationComputerName : SRV22
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

这个命令用于从名为 SRV01 的服务器获取到名为 SRV02 的服务器的基于连接的复制调度信息。该 cmdlet 返回一个自定义的连接调度方案：在周一至周五的上午 9 点到下午 5 点期间，复制操作被禁止（输出结果中对应这些时间段的部分显示为“0”）；而在其他所有时间范围内，复制操作可以使用全部带宽进行。

## 参数

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
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果您不指定此参数，该 cmdlet 将使用当前用户的域。

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
指定一个复制组名称的数组。您可以使用逗号分隔的列表以及通配符（*）。

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

### -SourceComputerName
指定发送计算机的名称。发送计算机也被称为外出计算机（outbound computer）或上游计算机（upstream computer）。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrConnectionSchedule

### 字符串

## 备注

## 相关链接

[Set-DfsrConnectionSchedule](./Set-DfsrConnectionSchedule.md)
