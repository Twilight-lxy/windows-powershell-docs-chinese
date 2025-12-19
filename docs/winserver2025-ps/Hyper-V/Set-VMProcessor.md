---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmprocessor?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMProcessor
---

# 设置虚拟机处理器

## 摘要
配置虚拟机中虚拟处理器的设置。这些设置会统一应用于属于该虚拟机的所有虚拟处理器。

## 语法

### VMName（默认值）
```
Set-VMProcessor [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-Count <Int64>] [-CompatibilityForMigrationEnabled <Boolean>]
 [-CompatibilityForOlderOperatingSystemsEnabled <Boolean>] [-HwThreadCountPerCore <Int64>] [-Maximum <Int64>]
 [-Reserve <Int64>] [-RelativeWeight <Int32>] [-MaximumCountPerNumaNode <Int32>]
 [-MaximumCountPerNumaSocket <Int32>] [-ResourcePoolName <String>] [-Perfmon <String>] [-EnableHostResourceProtection <Boolean>]
 [-ExposeVirtualizationExtensions <Boolean>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Set-VMProcessor [-VM] <VirtualMachine[]> [-Count <Int64>] [-CompatibilityForMigrationEnabled <Boolean>]
 [-CompatibilityForOlderOperatingSystemsEnabled <Boolean>] [-HwThreadCountPerCore <Int64>] [-Maximum <Int64>]
 [-Reserve <Int64>] [-RelativeWeight <Int32>] [-MaximumCountPerNumaNode <Int32>]
 [-MaximumCountPerNumaSocket <Int32>] [-ResourcePoolName <String>] [-EnableHostResourceProtection <Boolean>]
 [-ExposeVirtualizationExtensions <Boolean>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMProcessor
```
Set-VMProcessor [-VMProcessor] <VMProcessor[]> [-Count <Int64>] [-CompatibilityForMigrationEnabled <Boolean>]
 [-CompatibilityForOlderOperatingSystemsEnabled <Boolean>] [-HwThreadCountPerCore <Int64>] [-Maximum <Int64>]
 [-Reserve <Int64>] [-RelativeWeight <Int32>] [-MaximumCountPerNumaNode <Int32>]
 [-MaximumCountPerNumaSocket <Int32>] [-ResourcePoolName <String>] [-EnableHostResourceProtection <Boolean>]
 [-ExposeVirtualizationExtensions <Boolean>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Set-VMProcessor** cmdlet 用于配置虚拟机的虚拟处理器。

## 示例

### 示例 1
```
PS C:\> Set-VMProcessor TestVM -Count 2 -Reserve 10 -Maximum 75 -RelativeWeight 200
```

配置虚拟机TestVM，使其拥有两个虚拟处理器、10%的预留资源使用率、75%的资源使用上限以及200的相对权重。

### 示例 2
```
PS C:\> Set-VMProcessor TestVM -CompatibilityForMigrationEnabled $true
```

配置虚拟机TestVM，以实现处理器兼容性从而支持实时迁移（live migration）。

### 示例 3
```
PS C:\> Set-VMProcessor TestVM -CompatibilityForOlderOperatingSystemsEnabled $true
```

配置虚拟机TestVM，使其能够兼容运行较旧版本的操作系统。

### 示例 4
```
PS C:\> Set-VMProcessor TestVM -ExposeVirtualizationExtensions $true
```

配置虚拟机 TestVM，并启用其内置的 Hyper-V 功能。

### 示例 5
```
PS C:\> Set-VMProcessor TestVM -Perfmon pmu,pebs,lbr
```

配置您的虚拟机（VM），以便暴露性能监测（Performance Monitoring）所需的设备，如光电式电流互感器（PMU）、光电式电压互感器（PEBS）以及线路边界路由器（LBR）。





## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -CompatibilityForMigrationEnabled
指定在将虚拟机迁移到另一台主机时，是否需要限制虚拟处理器的功能以确保兼容性。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CompatibilityForOlderOperatingSystemsEnabled
指定是否需要限制虚拟处理器的功能，以便与旧版本的操作系统兼容。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
用于指定一个或多个需要配置处理器的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名来进行识别。默认值为本地计算机；可以通过使用 `localhost` 或点号（.`）来明确表示本地计算机。

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

### -Count
指定虚拟机的虚拟处理器数量。

```yaml
Type: Int64
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
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableHostResourceProtection
指定是否在虚拟机上启用主机资源保护功能。当该功能被启用后，主机将对虚拟机的某些操作进行限制，以防止其过度消耗主机计算资源。受此设置控制的虚拟机操作包括与虚拟机部分虚拟设备相关的 VMbus 管道消息，以及由虚拟机生成的拦截信息。受影响的虚拟设备包括视频、键盘、鼠标和动态内存 VDEV（Virtual Device Express）等设备。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExposeVirtualizationExtensions
指定管理程序是否应该向虚拟机暴露虚拟化扩展的存在，这样可以支持嵌套虚拟化功能。


```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HwThreadCountPerCore
指定暴露给虚拟机的虚拟SMT线程的数量。将此值设置为0表示虚拟机将继承主机每个核心的线程数量。该设置不得超过主机每个核心的线程数量。

注意：Windows Server 2016 不支持将 `HwThreadCountPerCore` 设置为 0。有关更多详细信息，请参阅 [使用 PowerShell 配置虚拟机 SMT 设置](/windows-server/virtualization/hyper-v/manage/about-hyper-v-scheduler-type-selection#configuring-vm-smt-settings-using-powershell)。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Maximum
指定可以配置给虚拟机处理器的资源的最大百分比。允许的值范围是 0 到 100。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumCountPerNumaNode
指定每个 NUMA 节点上可以为虚拟机配置的最大处理器数量。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumCountPerNumaSocket
指定每个 NUMA 节点上为虚拟机配置的最大套接字数量。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Perfmon
指定用于性能监控的硬件。有关要求的更多信息，请访问[在Hyper-V虚拟机中启用Intel性能监控硬件](/windows-server/virtualization/hyper-v/manage/performance-monitoring-hardware)。


```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```



### -Passthru
指定需要将一个 `Microsoft.HyperV POWERShell.Processor` 对象传递给管道，该对象代表将要配置的处理器。

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

### -RelativeWeight
指定在分配物理计算机的处理能力时，该虚拟机相对于其他虚拟机的优先级。允许的值范围是从1到10000。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Reserve
指定要为此虚拟机预留的处理器资源的百分比。允许的值范围是从0到100。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourcePoolName
指定要使用的处理器资源池的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定用于配置处理器的虚拟机。

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
指定要配置处理器的虚拟机的名称。

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

### -VMProcessor
指定需要配置虚拟机的虚拟处理器相关设置。

```yaml
Type: VMProcessor[]
Parameter Sets: VMProcessor
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被运行。

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

### Microsoft.HyperV.PowerShell.VMProcessor
如果指定了 **-PassThru**。

## 备注

## 相关链接
