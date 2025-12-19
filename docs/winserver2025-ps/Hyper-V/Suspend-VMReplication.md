---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/suspend-vmreplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Suspend-VMReplication
---

# 暂停虚拟机复制（Suspend-VMReplication）

## 摘要
暂停虚拟机的复制操作。

## 语法

### VMName（默认值）
```
Suspend-VMReplication [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-ReplicationRelationshipType <VMReplicationRelationshipType>] [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### VMObject
```
Suspend-VMReplication [-VM] <VirtualMachine[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 虚拟机复制（VMReplication）
```
Suspend-VMReplication [-VMReplication] <VMReplication[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Suspend-VMReplication` cmdlet 可以暂停虚拟机的复制过程。要恢复复制，可以使用 `Resume-VMReplication` cmdlet 来继续复制操作。当复制重新开始后，自暂停复制以来所做的所有更改都会被传输到目标虚拟机。

## 示例

### 示例 1
```
PS C:\> Suspend-VMReplication VM01
```

暂停虚拟机VM01的复制操作。

### 示例 2
```
PS C:\> Suspend-VMReplication *
```

暂停本地Hyper-V主机上所有虚拟机的复制操作。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于暂停虚拟机复制的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址或完全限定域名进行标识。默认值是本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定要将一个 **VMReplication** 对象传递到流水线中，该对象表示要暂停的复制操作。

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
用于指定虚拟机的复制关系类型。需要明确该复制关系是属于简单的主从模式，还是扩展的复制链结构。该命令会暂停具有所指定复制类型的虚拟机的复制过程。

```yaml
Type: VMReplicationRelationshipType
Parameter Sets: VMName
Aliases: Relationship
Accepted values: Simple, Extended

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要暂停复制的虚拟机。

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
指定要暂停复制的虚拟机的名称。

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
指定要暂停的虚拟机复制操作。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被运行。

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

### 虚拟机复制（VMReplication）
如果指定了 `-PassThru`。

## 备注

## 相关链接

