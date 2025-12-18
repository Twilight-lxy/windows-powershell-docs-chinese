---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/sync-dfsreplicationgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Sync-DfsReplicationGroup
---

# Sync-DfsReplicationGroup

## 摘要
无论时间安排如何，都能在计算机之间同步复制过程。

## 语法

```
Sync-DfsReplicationGroup [-GroupName] <String[]> [-SourceComputerName] <String>
 [-DestinationComputerName] <String> [-DurationInMinutes] <UInt32> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Sync-DfsReplicationGroup` cmdlet 可以在源计算机和目标计算机之间同步数据复制过程，即使这种复制过程并未由任何复制组或连接机制进行调度。

此cmdlet会在指定的时间内忽略复制的调度安排。你可以使用此cmdlet暂时更改复制调度，以便进行数据复制操作；因为该cmdlet不需要Active Directory的复制功能或LDAP轮询机制。

## 示例

### 示例 1：在服务器之间进行数据复制，持续时间为 15 分钟
```
PS C:\> Sync-DfsReplicationGroup -GroupName "RG01" -SourceComputerName "SRV01" -DestinationComputerName "SRV02" -DurationInMinutes 15
```

此命令允许在RG01复制组中，从SRV01服务器向SRV02服务器进行15分钟的复制操作，即使复制发生在关闭的复制计划期间也是如此。

### 示例 2：在服务器之间进行复制，并显示详细的输出信息
```
PS C:\> Sync-DfsReplicationGroup -GroupName "RG01" -SourceComputerName "SRV01" -DestinationComputerName "SRV02" -DurationInMinutes 5 -Verbose
VERBOSE: Performing operation "Sync-DfsReplicationGroup" on Target "SRV01".
VERBOSE: The **Sync-DfsReplicationGroup** cmdlet completed successfully.
```

此命令允许在RG01复制组中，从SRV01服务器向SRV02服务器进行数据复制，持续时间为5分钟。

## 参数

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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
指定接收计算机的名称。目标计算机也被称为入站计算机或下游计算机。这台计算机会覆盖自身的计划，并复制传入的数据。

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
指定允许复制操作的分钟数。

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
指定一个复制组名称的数组。如果您不指定此参数，该cmdlet将查询所有参与的复制组。您可以使用逗号分隔的列表以及通配符（*）。

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
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### uint（无符号整数）

### 字符串

## 输出

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 备注

## 相关链接

[Get-DfsReplicationGroup](./Get-DfsReplicationGroup.md)

[New-DfsReplicationGroup](./New-DfsReplicationGroup.md)

[Remove-DfsReplicationGroup](./Remove-DfsReplicationGroup.md)

[Set-DfsReplicationGroup](./Set-DfsReplicationGroup.md)

[Suspend-DfsReplicationGroup](./Suspend-DfsReplicationGroup.md)
