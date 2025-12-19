---
description: 获取分配给虚拟机的GPU分区信息。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmgpupartitionadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMGpuPartitionAdapter
---

# Get-VMGpuPartitionAdapter

## 摘要
获取分配给虚拟机的GPU分区信息。

## 语法

### VMName（默认值）

```
Get-VMGpuPartitionAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [-AdapterId <String>] [<CommonParameters>]
```

### VMObject

```
Get-VMGpuPartitionAdapter [-VM] <VirtualMachine[]> [-AdapterId <String>] [<CommonParameters>]
```

## 描述

`Get-VMGpuPartitionAdapter` cmdlet 可以获取分配给虚拟机的图形处理单元（GPU）分区的信息。

## 示例

### 示例 1

```powershell
$testvm = Get-VM "TestVM"
Get-VMGpuPartitionAdapter -VM $testvm
```

这个示例将分配给GPU的信息关联到一个虚拟机（VM）对象上。

### 示例 2

```powershell
Get-VMGpuPartitionAdapter -VMName "TestVM" | FL InstancePath, Id, SupportsOutgoingLiveMigration
```

该命令用于检索名为**TestVM**的虚拟机所使用的GPU分区适配器的信息，并显示`InstancePath`、`Id`以及`SupportsOutgoingLiveMigration`这三个属性的值。

在实时迁移带有 GPU 分区适配器的虚拟机时，源主机和目标主机都必须满足某些硬件和软件条件。可以使用 `SupportsOutgoingLiveMigration` 字段来预先验证实时迁移过程，确保在尝试迁移之前所有必要的条件都得到满足。

## 参数

### -AdapterId

这是一个虚拟机（VM）的GPU分区标识号码，用于显示分配给该虚拟机的GPU相关信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](/powershell/module/cimcmdlets/get-cimsession) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

指定一个或多个需要在虚拟网络适配器上检索的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址和完全限定的域名作为标识。默认值是本地计算机。可以使用 `localhost` 或点号（`.`）来明确表示本地计算机。

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

### -VM

指定要获取其虚拟网络适配器的虚拟机。星号（`*`）是通配符；如果指定了该虚拟机，此 cmdlet 将从系统中的所有虚拟机中返回相应的虚拟网络适配器。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: True
```

### -VMName

指定要获取其网络适配器信息的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### System.String[]

### Microsoft.HyperV.PowerShell.VirtualMachine[]

## 输出

### Microsoft.HyperV.PowerShell.VMGpuPartitionAdapter

## 备注

## 相关链接

[Add-VMGpuPartitionAdapter](add-vmgpupartitionadapter.md)

[Remove-VMGpuPartitionAdapter](remove-vmgpupartitionadapter.md)

[Set-VMGpuPartitionAdapter](set-vmgpupartitionadapter.md)
