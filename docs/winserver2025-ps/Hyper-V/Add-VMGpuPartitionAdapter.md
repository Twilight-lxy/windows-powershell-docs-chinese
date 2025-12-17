---
description: 向虚拟机添加一个GPU分区适配器。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmgpupartitionadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMGpuPartitionAdapter
---

# 添加 VMGpuPartitionAdapter

## 摘要
向虚拟机添加一个GPU分区适配器。

## 语法

### VMName（默认值）

```
Add-VMGpuPartitionAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [-Passthru] [-InstancePath <String>]
 [-MinPartitionVRAM <UInt64>] [-MaxPartitionVRAM <UInt64>] [-OptimalPartitionVRAM <UInt64>]
 [-MinPartitionEncode <UInt64>] [-MaxPartitionEncode <UInt64>] [-OptimalPartitionEncode <UInt64>]
 [-MinPartitionDecode <UInt64>] [-MaxPartitionDecode <UInt64>] [-OptimalPartitionDecode <UInt64>]
 [-MinPartitionCompute <UInt64>] [-MaxPartitionCompute <UInt64>] [-OptimalPartitionCompute <UInt64>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject

```
Add-VMGpuPartitionAdapter [-VM] <VirtualMachine[]> [-Passthru] [-InstancePath <String>]
 [-MinPartitionVRAM <UInt64>] [-MaxPartitionVRAM <UInt64>] [-OptimalPartitionVRAM <UInt64>]
 [-MinPartitionEncode <UInt64>] [-MaxPartitionEncode <UInt64>] [-OptimalPartitionEncode <UInt64>]
 [-MinPartitionDecode <UInt64>] [-MaxPartitionDecode <UInt64>] [-OptimalPartitionDecode <UInt64>]
 [-MinPartitionCompute <UInt64>] [-MaxPartitionCompute <UInt64>] [-OptimalPartitionCompute <UInt64>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Add-VMGpuPartitionAdapter` 这个 cmdlet 用于向虚拟机添加一个 GPU 分区适配器。如果不指定任何参数，它会将可用 GPU 中的一个完整分区分配给该虚拟机。

## 示例

### 示例 1

```powershell
$vm = Get-VM -Name "TestVM"
Add-VMGpuPartitionAdapter -VM $vm
```

这个示例将一个分区分配给特定的虚拟机对象。

### 示例 2

```powershell
$vm = Get-VM -Name "TestVM"
Add-VMGpuPartitionAdapter -VM $vm -InstancePath "GPUInstancePath"
```

这个示例将某个特定GPU上的分区分配给一个虚拟机（VM），其中该虚拟机的实例路径对应于主机上该GPU设备的ID名称。

## 参数

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 `[New-CimSession](/powershell/module/cimcmdlets/new-cimsession)` 或 `[Get-CimSession](/powershell/module/cimcmdlets/get-cimsession)` cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

指定一个或多个用于获取虚拟机的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行选择。默认值是本地计算机。可以使用 `localhost` 或点（`.`）来明确表示本地计算机。

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

### -InstancePath

表示主机中GPU的设备实例路径。该值可以通过执行`Get-VMHostPartitionableGpu`命令并查看其“Name”属性来获取。

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

### -MaxPartitionCompute

主机GPU所能分配的最大计算资源数量。这一数值由制造商提供的驱动程序来定义。

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

主机GPU可以分配的最大解码器数量。这一数值由制造商提供的驱动程序来定义。

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

主机GPU可分配的最大编码器数量。该数量由制造商提供的驱动程序进行定义。

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

主机GPU支持的最大VRAM容量（以字节为单位）。该数值由制造商提供的驱动程序进行定义。

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

主机GPU分配的最少计算资源数量。该数值由制造商提供的驱动程序进行定义。

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

主机GPU分配的解码器最小数量。该数量由制造商的驱动程序确定。

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

主机GPU分配的编码器数量的最小值。该数值由制造商提供的驱动程序确定。

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

主机GPU支持的最低VRAM容量（以字节为单位）。该数值由制造商提供的驱动程序确定。

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

主机GPU分配的最佳编码器数量由制造商的驱动程序确定。

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

主机GPU支持的最大VRAM容量（以字节为单位）。该数值由制造商提供的驱动程序进行定义。

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

对于cmdlet启动的每个进程，都会返回一个对象。

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

指定要添加网络适配器的虚拟机。

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

### -VMName

指定要添加网络适配器的虚拟机的名称。

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

在运行cmdlet之前，会提示您进行确认。

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

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### Microsoft.HyperV.PowerShell VirtualMachine[]

### System.String[]

## 输出

### Microsoft.HyperV POWERShell.VMGpuPartitionAdapter

## 备注

## 相关链接

[Get-VMGpuPartitionAdapter](get-vmgpupartitionadapter.md)

[Remove-VMGpuPartitionAdapter](remove-vmgpupartitionadapter.md)

[Set-VMGpuPartitionAdapter](set-vmgpupartitionadapter.md)
