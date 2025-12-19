---
description: 将GPU的一个分区分配给虚拟机。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmgpupartitionadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMGpuPartitionAdapter
---

# 设置 VMGpuPartitionAdapter

## 摘要
将GPU的一个分区分配给虚拟机。

## 语法

### VMName（默认值）

```
Set-VMGpuPartitionAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [-Passthru] [-AdapterId <String>]
 [-MinPartitionVRAM <UInt64>] [-MaxPartitionVRAM <UInt64>] [-OptimalPartitionVRAM <UInt64>]
 [-MinPartitionEncode <UInt64>] [-MaxPartitionEncode <UInt64>] [-OptimalPartitionEncode <UInt64>]
 [-MinPartitionDecode <UInt64>] [-MaxPartitionDecode <UInt64>] [-OptimalPartitionDecode <UInt64>]
 [-MinPartitionCompute <UInt64>] [-MaxPartitionCompute <UInt64>] [-OptimalPartitionCompute <UInt64>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject

```
Set-VMGpuPartitionAdapter [-VM] <VirtualMachine[]> [-Passthru] [-AdapterId <String>]
 [-MinPartitionVRAM <UInt64>] [-MaxPartitionVRAM <UInt64>] [-OptimalPartitionVRAM <UInt64>]
 [-MinPartitionEncode <UInt64>] [-MaxPartitionEncode <UInt64>] [-OptimalPartitionEncode <UInt64>]
 [-MinPartitionDecode <UInt64>] [-MaxPartitionDecode <UInt64>] [-OptimalPartitionDecode <UInt64>]
 [-MinPartitionCompute <UInt64>] [-MaxPartitionCompute <UInt64>] [-OptimalPartitionCompute <UInt64>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 对象

```
Set-VMGpuPartitionAdapter [-VMGpuPartitionAdapter] <VMGpuPartitionAdapter[]> [-Passthru]
 [-MinPartitionVRAM <UInt64>] [-MaxPartitionVRAM <UInt64>] [-OptimalPartitionVRAM <UInt64>]
 [-MinPartitionEncode <UInt64>] [-MaxPartitionEncode <UInt64>] [-OptimalPartitionEncode <UInt64>]
 [-MinPartitionDecode <UInt64>] [-MaxPartitionDecode <UInt64>] [-OptimalPartitionDecode <UInt64>]
 [-MinPartitionCompute <UInt64>] [-MaxPartitionCompute <UInt64>] [-OptimalPartitionCompute <UInt64>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Set-VMGpuPartitionAdapter` cmdlet 用于将 GPU 的某个分区分配给虚拟机。当对该虚拟机执行此命令时，会为其分配整个 GPU 分区。此外，还存在其他参数，可以用来为虚拟机指定更具体的配置选项。

## 示例

### 示例 1

```powershell
$vm = Get-VM "Test"
Set-VMGpuPartitionAdapter -VM $vm
```

这个例子通过传递一个虚拟机（VM）对象来为该虚拟机分配一个分区。

## 参数

### -AdapterId

虚拟机（VM）的GPU分区标识号码用于显示分配给该虚拟机的GPU相关信息。

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

在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](/powershell/module/cimcmdlets/get-cimsession) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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

指定要从虚拟网络适配器中获取的一个或多个 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址和完全限定的域名作为标识符。默认值是本地计算机。可以使用 `localhost` 或一个点（`.`）来明确表示本地计算机。

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

### -MaxPartitionCompute

主机GPU分配的计算资源（如核心数或线程数）的最大值。该数值由制造商提供的驱动程序确定。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxPartitionDecode

主机GPU分配的解码器数量上限。该限制由制造商提供的驱动程序决定。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxPartitionEncode

主机GPU可以分配的最大编码器数量。该数值由制造商提供的驱动程序来决定。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxPartitionVRAM

主机GPU支持的最大VRAM容量（以字节为单位）。该数值由制造商提供的驱动程序确定。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinPartitionCompute

主机GPU分配的最小计算资源数量。该数值由制造商提供的驱动程序确定。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinPartitionDecode

主机GPU分配的解码器最小数量。该数量由制造商的驱动程序决定。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinPartitionEncode

主机GPU分配的编码器最小数量。该数值由制造商提供的驱动程序决定。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinPartitionVRAM

主机GPU支持的最小VRAM容量（以字节为单位）。该数值由制造商提供的驱动程序进行定义。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OptimalPartitionCompute

主机GPU分配的最佳计算资源数量由制造商提供的驱动程序来决定。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OptimalPartitionDecode

主机GPU分配的解码器的最佳数量由制造商提供的驱动程序来决定。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OptimalPartitionEncode

主机GPU分配的编码器的最佳数量由制造商的驱动程序确定。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OptimalPartitionVRAM

主机GPU支持的最大VRAM容量（以字节为单位）。该数值由制造商提供的驱动程序确定。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru

为cmdlet启动的每个进程返回一个对象。

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

指定要获取其虚拟网络适配器的虚拟机。星号（`*`）是一个通配符；如果指定了该虚拟机，此cmdlet将从系统中的所有虚拟机中返回相应的虚拟网络适配器信息。

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

指定要配置其网络适配器的虚拟机的名称。

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

### -Confirm

在运行 cmdlet 之前，会提示您进行确认。

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

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### System.String[]

### Microsoft.HyperV.PowerShell.VirtualMachine[]

### Microsoft.HyperV.PowerShell.VMGpuPartitionAdapter[]

## 输出

### Microsoft.HyperV.PowerShell.VMGpuPartitionAdapter

## 备注

## 相关链接

[Add-VMGpuPartitionAdapter](add-vmgpupartitionadapter.md)

[Get-VMGpuPartitionAdapter](get-vmgpupartitionadapter.md)

[Remove-VMGpuPartitionAdapter](remove-vmgpupartitionadapter.md)
