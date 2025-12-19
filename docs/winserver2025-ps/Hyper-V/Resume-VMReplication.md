---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/resume-vmreplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Resume-VMReplication
---

# 简历 - 虚拟机复制技术（Resume-VMReplication）

## 摘要
恢复处于“暂停”（Paused）、“错误”（Error）、“需要重新同步”（Resynchronization Required）或“挂起”（Suspended）状态的虚拟机复制操作。

## 语法

### VMName（默认值）
```
Resume-VMReplication [-ComputerName <String[]>] [-VMName] <String[]>
 [-ReplicationRelationshipType <VMReplicationRelationshipType>] [-ResynchronizeStartTime <DateTime>]
 [-Resynchronize] [-AsJob] [-Continue] [-Passthru] [-CimSession <CimSession[]>] [-Credential <PSCredential[]>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Resume-VMReplication [-VM] <VirtualMachine[]> [-ReplicationRelationshipType <VMReplicationRelationshipType>]
 [-ResynchronizeStartTime <DateTime>] [-Resynchronize] [-AsJob] [-Continue] [-Passthru]
 [-CimSession <CimSession[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 虚拟机复制（VMReplication）
```
Resume-VMReplication [-VMReplication] <VMReplication[]> [-ResynchronizeStartTime <DateTime>] [-Resynchronize]
 [-AsJob] [-Continue] [-Passthru] [-CimSession <CimSession[]>] [-Credential <PSCredential[]>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Resume-VMReplication` cmdlet 用于恢复处于“暂停”（Paused）、“错误”（Error）、“需要重新同步”（Resynchronization Required）或“挂起”（Suspended）状态的虚拟机的复制过程。

## 示例

### 示例 1
```
PS C:\> Resume-VMReplication VM01
```

这个示例恢复了虚拟机VM01的复制过程。

### 示例 2
```
PS C:\> Resume-VMReplication VM01 -Resynchronize
```

这个示例用于重新同步虚拟机VM01的复制过程。

### 示例 3
```
PS C:\> Resume-VMReplication VM01 -Resynchronize -ResynchronizeStartTime "8/1/2012 05:00 AM"
```

这个示例安排了虚拟机VM01的复制同步操作在2012年8月1日上午5:00开始执行。

### 示例 4
```
PS C:\> Resume-VMReplication *
```

这个示例会恢复所有已暂停复制的虚拟机的复制过程。

## 参数

### -AsJob
将该cmdlet作为后台作业运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于恢复虚拟机复制的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名来进行指定。默认值是本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
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
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Continue
这表示，在您恢复虚拟机复制时，Hyper-V Replica会从上次停止的位置继续执行同步比较操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
表示此 cmdlet 返回一个 **VMReplication** 对象。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicationRelationshipType
用于指定虚拟机的复制关系类型。需要明确该复制关系是简单的主从复制关系，还是扩展的复制链关系。此cmdlet会恢复那些具有所指定复制类型的虚拟机的复制过程。

```yaml
Type: VMReplicationRelationshipType
Parameter Sets: VMName, VMObject
Aliases: Relationship
Accepted values: Simple, Extended

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Resynchronize
指定要为虚拟机启动重新同步操作。重新同步需要大量的存储、处理器和网络资源，因此建议在非高峰时段执行此操作。可以使用 **Set-VMReplication** cmdlet 来设置是否在未来自动重新同步该虚拟机。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: Resync

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResynchronizeStartTime
指定重新同步应开始的时间。如果未指定，则重新同步会立即启动。您可以安排重新同步在最多7天后开始。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases: ResyncStart

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要恢复复制的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要恢复复制的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMReplication
指定一个虚拟机复制对象，该对象代表需要恢复的虚拟机复制操作。

```yaml
Type: VMReplication[]
Parameter Sets: VMReplication
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
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
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### 虚拟机复制（VMReplication）
如果指定了 **-PassThru**。

## 备注

## 相关链接

