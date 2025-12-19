---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmsnapshot?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMSnapshot
---

# 删除VMS快照

## 摘要
删除虚拟机检查点。

## 语法

### SnapshotName（默认值）
```
Remove-VMSnapshot [-VMName] <String[]> [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [[-Name] <String[]>] [-IncludeAllChildSnapshots] [-AsJob] [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### VMObject
```
Remove-VMSnapshot [-VM] <VirtualMachine[]> [[-Name] <String[]>] [-IncludeAllChildSnapshots] [-AsJob]
 [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SnapshotObject
```
Remove-VMSnapshot [-VMSnapshot] <VMSnapshot[]> [-IncludeAllChildSnapshots] [-AsJob] [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-VMSnapshot` cmdlet 用于删除虚拟机检查点（即虚拟机的某个状态快照）。

注意：在 Windows Server 2012 R2 中，虚拟机快照被重新命名为“虚拟机检查点”。为便于理解，本文档将把虚拟机快照称为“检查点”。

## 示例

### 示例 1
```
PS C:\> Get-VM TestVM | Remove-VMSnapshot -Name Experiment*
```

删除所有名称以“Experiment”开头的虚拟机TestVM的所有检查点。

### 示例 2
```
PS C:\> Get-VMSnapshot -VMName TestVM | Where-Object {$_.CreationTime -lt (Get-Date).AddDays(-90) } | Remove-VMSnapshot
```

删除虚拟机TestVM中创建时间超过90天的所有检查点。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: SnapshotName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于删除检查点的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名来进行标识。默认值是本地计算机；可以通过使用 `localhost` 或`.` 来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: SnapshotName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值是当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: SnapshotName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeAllChildSnapshots
指定在删除检查点的同时，也要删除该检查点的所有子元素（即与该检查点相关联的所有数据或资源）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: IncludeAllChildCheckpoints

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要删除的检查点的名称。

```yaml
Type: String[]
Parameter Sets: SnapshotName
Aliases:

Required: False
Position: 1
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

```yaml
Type: String[]
Parameter Sets: VMObject
Aliases:

Required: False
Position: 1
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Passthru
这表示该 cmdlet 返回一个 **Microsoft.HyperV.PowerShell.VirtualMachine** 对象，该对象代表它所删除的检查点。

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

### -VM
指定要删除检查点的虚拟机。

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
指定要删除检查点的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: SnapshotName
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMSnapshot
指定要删除的检查点。

```yaml
Type: VMSnapshot[]
Parameter Sets: SnapshotObject
Aliases: VMCheckpoint

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.VirtualMachine
如果指定了 `-PassThru` 参数。

## 备注

## 相关链接

[Export-VMSnapshot](./Export-VMSnapshot.md)

[Get-VMSnapshot](./Get-VMSnapshot.md)

[ Rename-VMSnapshot](./Rename-VMSnapshot.md)

[Restore-VMSnapshot](./Restore-VMSnapshot.md)

[Get-VM](./Get-VM.md)

