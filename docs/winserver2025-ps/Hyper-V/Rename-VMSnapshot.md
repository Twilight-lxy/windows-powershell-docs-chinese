---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/rename-vmsnapshot?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Rename-VMSnapshot
---

# 重命名VMS快照

## 摘要
重命名虚拟机检查点。

## 语法

### SnapshotName（默认值）
```
Rename-VMSnapshot [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> [-VMName] <String> [-NewName] <String> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SnapshotObject
```
Rename-VMSnapshot [-VMSnapshot] <VMSnapshot> [-NewName] <String> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 虚拟机（VM）
```
Rename-VMSnapshot [-VM] <VirtualMachine> [-Name] <String> [-NewName] <String> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Rename-VMSnapshot` cmdlet 用于重命名虚拟机检查点（即虚拟机的备份状态）。

注意：在 Windows Server 2012 R2 中，虚拟机快照被重新命名为“虚拟机检查点”。为避免混淆，本文档将把虚拟机快照称为“检查点”。

## 示例

### 示例 1
```
PS C:\> Rename-VMSnapshot -VMName TestVM -Name "Configuration 2" -NewName "Configuration 2: applied all updates"
```

将虚拟机 TestVM 的检查点配置 2 重命名为配置 2：已应用所有更新。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定一个或多个用于重命名虚拟机检查点的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行标识。默认值是本地计算机；可以通过使用 `localhost` 或点号（.）来明确表示本地计算机。

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
在运行 cmdlet 之前会提示您确认是否要执行该操作。

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
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

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

### -Name
指定要重命名的虚拟机检查点的名称。

```yaml
Type: String
Parameter Sets: SnapshotName, VM
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewName
指定虚拟机检查点要重命名的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定要将一个 **VMSnapshot** 对象传递给流水线，该对象代表需要重命名的虚拟机检查点。

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
指定要重命名检查点的虚拟机。

```yaml
Type: VirtualMachine
Parameter Sets: VM
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要重命名检查点的虚拟机的名称。

```yaml
Type: String
Parameter Sets: SnapshotName
Aliases:

Required: True
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMSnapshot
指定要重命名的虚拟机检查点。

```yaml
Type: VMSnapshot
Parameter Sets: SnapshotObject
Aliases: VMCheckpoint

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### 虚拟机（VM）Snapshot
如果指定了 **-PassThru**。

## 备注

## 相关链接

