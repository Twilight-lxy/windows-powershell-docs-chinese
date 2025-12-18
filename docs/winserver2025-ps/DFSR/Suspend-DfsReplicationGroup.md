---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/suspend-dfsreplicationgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Suspend-DfsReplicationGroup
---

# 暂停 DFS 复制组

## 摘要
无论原计划如何，都会暂停计算机之间的数据复制过程。

## 语法

```
Suspend-DfsReplicationGroup [-GroupName] <String[]> [-SourceComputerName] <String>
 [-DestinationComputerName] <String> [-DurationInMinutes] <UInt32> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Suspend-DfsReplicationGroup` cmdlet 会暂停计算机之间的复制操作，无论这种复制操作是由复制组还是连接来安排的。

此cmdlet会在指定的时间内忽略复制调度。通常来说，这种做法比临时更改复制调度更为合适，因为该cmdlet无需依赖Active Directory的复制机制或LDAP轮询功能。

## 示例

### 示例 1：暂停服务器之间的复制操作
```
PS C:\> Suspend-DfsReplicationGroup -GroupName "RG01" -SourceComputerName "SRV01" -DestinationComputerName "SRV02" -DurationInMinutes 15
```

此命令会暂停 RG01 复制组中从 SRV01 到 SRV02 的复制过程，持续时间為 15 分钟。即使在正常复制计划进行期间发生复制操作，该命令也同样会生效。

### 示例 2：暂停服务器之间的复制操作，并显示详细的输出信息
```
PS C:\> Suspend-DfsReplicationGroup -GroupName "RG01" -SourceComputerName "SRV01" -DestinationComputerName "SRV02" -DurationInMinutes 5 -Verbose
VERBOSE: Performing operation "Suspend-DfsReplicationGroup" on Target "SRV01".
VERBOSE: The **Suspend-DfsReplicationGroup** cmdlet completed successfully.
```

此命令会暂停RG01复制组中从SRV01到SRV02的复制操作，持续时间為5分钟。即使在正常的复制计划执行期间发生复制操作，该命令也会继续执行，并显示相应的输出结果。

## 参数

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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

### -DestinationComputerName
指定接收计算机的名称。目标计算机也被称为入站计算机或下游计算机。该计算机会覆盖自身的复制计划，并停止入站数据复制操作。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ReceivingMember, RMem

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DurationInMinutes
指定暂停复制操作的分钟数。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: Time

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GroupName
指定一个复制组名称的数组。如果您不指定此参数，该 cmdlet 会查询所有参与的复制组。您可以使用逗号分隔的列表以及通配符（*）。

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

### -SourceComputerName
指定发送计算机的名称。源计算机也被称为出站计算机或上游计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: SendingMember, SMem

Required: True
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### UInt

### 字符串（String）

## 输出

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 备注

## 相关链接

[Get-DfsReplicationGroup](./Get-DfsReplicationGroup.md)

[New-DfsReplicationGroup](./New-DfsReplicationGroup.md)

[Remove-DfsReplicationGroup](./Remove-DfsReplicationGroup.md)

[Set-DfsReplicationGroup](./Set-DfsReplicationGroup.md)

[Sync-DfsReplicationGroup](./Sync-DfsReplicationGroup.md)

