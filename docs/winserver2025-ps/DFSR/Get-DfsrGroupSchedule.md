---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsrgroupschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsrGroupSchedule
---

# Get-DfsrGroupSchedule

## 摘要
检索复制组的调度信息。

## 语法

```
Get-DfsrGroupSchedule [[-GroupName] <String[]>] [[-DomainName] <String>] [<CommonParameters>]
```

## 描述
`Get-DfsrGroupSchedule` cmdlet 用于从指定的复制组中检索调度信息。分布式文件系统（DFS）的复制调度机制用于控制复制的可用性和带宽使用情况。默认情况下，DFS 复制机制建议配置为每天 24 小时、每周 7 天持续进行复制，并且使用全部带宽。

DFS复制Get-*命令集对于管道操作或资源清单管理非常有用。

## 示例

### 示例 1：获取小组日程安排
```
PS C:\> Get-DfsrGroupSchedule -GroupName "RG01"
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

此命令使用 **Get-DfsrGroupSchedule** cmdlet 来显示名为 RG01 的资源组的复制组计划。

## 参数

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果未指定此参数，cmdlet 将使用用户的当前域。

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
指定一个复制组名称的数组。如果不指定此参数，该cmdlet将查询所有参与的复制组。你可以使用逗号分隔的列表以及通配符（*）。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 输出

### Microsoft.DistributedFileSystemReplication.DfsRGroupSchedule

## 备注

## 相关链接

[Set-DfsrGroupSchedule](./Set-DfsrGroupSchedule.md)

