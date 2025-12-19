---
description: 从虚拟机中删除已分配的GPU分区。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmgpupartitionadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMGpuPartitionAdapter
---

# 移除 VMGpuPartitionAdapter

## 摘要
从虚拟机中删除已分配的GPU分区。

## 语法

### VMName（默认值）

```
Remove-VMGpuPartitionAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [-Passthru] [-AdapterId <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### VMObject

```
Remove-VMGpuPartitionAdapter [-VM] <VirtualMachine[]> [-Passthru] [-AdapterId <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 对象

```
Remove-VMGpuPartitionAdapter [-VMGpuPartitionAdapter] <VMGpuPartitionAdapter[]> [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-VMGpuPartitionAdapter` cmdlet 用于从虚拟机中移除分配的图形处理单元（GPU）分区，并将该分区释放回主机上的 GPU。

## 示例

### 示例 1

```powershell
$testvm = Get-VM "TestVM"
Remove-VMGpuPartitionAdapter -VM $testvm
```

这个示例用于删除分配给特定虚拟机对象的分区。

### 示例 2

```powershell
$testvm = Get-VM "TestVM"
$GPUpartition = Get-VMGpuPartitionAdapter -VM $testvm
Remove-VMGpuPartitionAdapter -VM $testvm -AdapterId $GPUpartiton[0].id
```

这个示例从特定的虚拟机中删除一个特定的分区对象。

## 参数

### -AdapterId

这是一个用于识别虚拟机（VM）中GPU分区的编号，通过该编号可以将GPU从虚拟机中移除。

```yaml
Type: String
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession

在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如 `[New-CimSession](/powershell/module/cimcmdlets/new-cimsession)` 或 `[Get-CimSession](/powershell.module/cimcmdlets/get-cimsession)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName

指定一个或多个需要在虚拟网络适配器上获取的Hyper-V主机。允许使用NetBIOS名称、IP地址和完全限定域名作为标识。默认值是本地计算机。可以使用`localhost`或点（`.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru

对于 cmdlet 启动的每个进程，都会返回一个对象。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM

指定要获取其虚拟网络适配器的虚拟机。星号（`*`）是通配符；如果指定了该虚拟机，此cmdlet将从系统中的所有虚拟机中返回相应的虚拟网络适配器。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMGpuPartitionAdapter

从 `Get-VMGpuPartitionAdapter` 获取到的 GPU 分区对象。

```yaml
Type: VMGpuPartitionAdapter[]
Parameter Sets: Object
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName

指定要删除其网络适配器的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果该cmdlet被运行会发生的情景。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction和-WarningVariable。有关更多信息，请参阅[about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### Microsoft.HyperV.PowerShell.VirtualMachine[]

### Microsoft.HyperV POWERShell.VMGpuPartitionAdapter[]

## 输出

### Microsoft.HyperV POWERShell.VMGpuPartitionAdapter

## 备注

## 相关链接

[Add-VMGpuPartitionAdapter](add-vmgpupartitionadapter.md)

[Get-VMGpuPartitionAdapter](get-vmgpupartitionadapter.md)

[Set-VMGpuPartitionAdapter](set-vmgpupartitionadapter.md)
