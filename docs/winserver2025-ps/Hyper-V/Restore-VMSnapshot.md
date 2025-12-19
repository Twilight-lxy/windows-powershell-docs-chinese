---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/restore-vmsnapshot?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Restore-VMSnapshot
---

# 恢复虚拟机快照

## 摘要
恢复虚拟机检查点。

## 语法

### SnapshotName（默认值）
```
Restore-VMSnapshot [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> [-VMName] <String> [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SnapshotObject
```
Restore-VMSnapshot [-VMSnapshot] <VMSnapshot> [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 虚拟机（VM）
```
Restore-VMSnapshot [-VM] <VirtualMachine> [-Name] <String> [-AsJob] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Restore-VMSnapshot` cmdlet 可以恢复虚拟机的检查点状态。

注意：在 Windows Server 2012 R2 中，虚拟机快照被重新命名为“虚拟机检查点”。为便于理解，本文档将把虚拟机快照称为“检查点”。

## 示例

### 示例 1
```
PS C:\> Restore-VMSnapshot -Name 'Base image' -VMName TestVM
Confirm
Are you sure you want to perform this action?
Restore-VMSnapshot will restore checkpoint "Base image".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help
(default is "Y"): Y
```

恢复虚拟机 TestVM 的检查点，并使用其基础镜像进行操作。

### 示例 2
```
PS C:\> Get-VM | Foreach-Object { $_ | Get-VMSnapshot | Sort CreationTime | Select -Last 1 | Restore-VMSnapshot -Confirm:$false }
```

将最新的检查点应用到所有虚拟机上，且不会显示任何确认提示。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: SnapshotName
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于恢复虚拟机检查点的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址或完全限定域名作为主机标识。默认值为本地计算机；可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: SnapshotName
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
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
默认值；常规设置 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: SnapshotName
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要恢复的检查点的名称。

```yaml
Type: String
Parameter Sets: SnapshotName, VM
Aliases:

Required: True
Position: 0
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 **VMSnapshot** 传递给流水线，该 **VMSnapshot** 表示要恢复的检查点。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要恢复的虚拟机。

```yaml
Type: VirtualMachine
Parameter Sets: VM
Aliases:

Required: True
Position: 0
默认值；常规设置 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要恢复的虚拟机的名称。

```yaml
Type: String
Parameter Sets: SnapshotName
Aliases:

Required: True
Position: 1
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMSnapshot
指定一个 **VMSnapshot** 对象数组。要获取一个 **VMSnapshot** 对象，可以使用 **Get-VMSnapshot** cmdlet。该 cmdlet 会恢复您指定的虚拟机检查点。

```yaml
Type: VMSnapshot
Parameter Sets: SnapshotObject
Aliases: VMCheckpoint

Required: True
Position: 0
默认值；常规设置 value: None
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
默认值；常规设置 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值；常规设置

### 虚拟机（VM）Snapshot
如果指定了 **-PassThru**，则……

## 备注

## 相关链接

[Get-VMSnapshot](./Get-VMSnapshot.md)

