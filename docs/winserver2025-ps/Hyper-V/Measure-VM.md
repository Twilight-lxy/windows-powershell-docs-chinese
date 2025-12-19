---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/measure-vm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Measure-VM
---

# Measure-VM

## 摘要
报告一个或多个虚拟机的资源利用情况数据。

## 语法

### 名称（默认值）
```
Measure-VM [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String[]> [<CommonParameters>]
```

### VMObject
```
Measure-VM [-VM] <VirtualMachine[]> [<CommonParameters>]
```

## 描述
`Measure-VM` cmdlet 可报告一个或多个虚拟机的处理器使用情况、内存使用情况、网络流量以及磁盘容量等数据。

注意：只有当为虚拟机启用资源计量功能后，才能通过 **Measure-VM** cmdlet 获取用于报告的数据。

该报告包含以下字段：

-- ComputerName：虚拟机主机的名称。

-- VMId：虚拟机的唯一标识符。

-- VMName：虚拟机的友好名称。

-- HardDiskMetrics：关于存储子系统性能和吞吐量的信息。

-- MeteringDuration：资源使用数据报告所覆盖的时间段。

-- AverageProcessorUsage：在 MeteringDuration 字段所指定的时间段内，虚拟机的平均处理器使用率（以兆赫兹为单位）。

-- AverageMemoryUsage：虚拟机在报告时间段内的平均内存使用量（以兆字节为单位），该时间段由 MeteringDuration 字段指定。

-- MaximumMemoryUsage：在MeteringDuration字段所指定的时间段内，虚拟机的最大内存使用量（以兆字节为单位）。

-- MinimumMemoryUsage：在MeteringDuration字段所指定的时间范围内，虚拟机的最低内存使用量（以兆字节为单位）。

-- TotalDiskAllocation：在MeteringDuration字段所报告的时间段内，分配给虚拟机的最大磁盘容量（以兆字节为单位）。有关更多信息，请参阅该字段描述后的“注释”。

-- NetworkMeteredTrafficReport：一个数组，其元素用于报告在计量时间长度（MeteringDuration字段中指定的时间段内）虚拟机或各台机器上每个NetworkAdapterAcl的流量情况。该数组的每个元素具有以下属性：

-- NetworkAdapter：用于配置 NetworkAdapterAcl 的虚拟机网络适配器对象。

-- LocalAddress：对于入站数据包，指的是数据包头部中的目标IP地址；对于出站数据包，指的是数据包头部中的源IP地址。

-- RemoteAddress：对于入站数据包，是指数据包头部中的源IP地址；对于出站数据包，是指数据包头部中的目的IP地址。

-- 方向：ACL适用的网络流量方向。允许的值有“Inbound”（入站）、“Outbound”（出站）或“Both”（两者）。

-- TotalTraffic：通过NetworkAdapterAcl的网络流量总量（以兆字节为单位）。

注释：

分配给虚拟机的磁盘容量被报告为两个数值的总和：所有连接的虚拟硬盘的总存储容量，以及虚拟机快照所消耗的物理存储空间总量。

-- 如果虚拟机拥有多个虚拟硬盘，则 TotalDiskAllocation 属性显示分配给所有虚拟硬盘的磁盘容量的总和。

对于通过虚拟光纤通道连接附加的磁盘，或者配置为使用单根I/O虚拟化（SR-IOV）的网络适配器，其资源利用率不会被报告。

-- 如果虚拟机配置的是静态内存而不是动态内存，那么 AverageMemoryUsage、MinimumMemoryUsage 和 MaximumMemoryUsage 这些指标的值将等于为该虚拟机配置的内存容量。

资源池资源利用报告的默认显示内容包括以下列：

-- VMName：虚拟机的名称。

-- AvgCPU(Mhz)：虚拟机的平均处理器使用率，单位为兆赫（MHz）。

-- TotalDisk(M)：虚拟机的平均磁盘使用量（以兆字节为单位）。有关更多信息，请参阅该字段描述后面的“备注”部分。

-- NetworkInbound(M)：虚拟机器接收到的总网络流量，单位为兆字节（MB）。

-- NetworkOutbound(M)：虚拟机发出的总网络流量（以兆字节为单位）。

## 示例

#### 示例 1
```
PS C:\> Measure-VM -VMName TestVM
```

这个示例报告了一台名为TestVM的虚拟机的资源利用数据。

### 示例 2
```
PS C:\> $UtilizationReport = Get-VM TestVM | Measure-VM
PS C:\> Get-VM TestVM | Reset-VMResourceMetering
```

这个示例使用了两个命令以及管道（pipeline）机制。第一个命令使用了 **Get-VM** cmdlet，并将获取到的虚拟机对象传递给 **Measure-VM** cmdlet，以收集名为 TestVM 的虚拟机的资源使用情况数据，并将这些数据存储在变量 $UtilizationReport 中。第二个命令使用了 **Reset-VMResourceMetering** cmdlet 来清除现有的数据，从而使 Hyper-V 重新开始收集新的数据。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个需要报告资源使用情况的虚拟机主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行标识。默认值为本地计算机。可以通过使用 `localhost` 或点号（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: Name
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
Parameter Sets: Name
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要报告其资源利用数据的虚拟机的友好名称。

```yaml
Type: String[]
Parameter Sets: Name
Aliases: VMName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VM
指定要报告其资源使用情况的虚拟机。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.HyperV.PowerShell_virtualMachine[]

## 输出

### Microsoft.HyperV.PowerShell.VMMeteringReportForVirtualMachine

## 备注

## 相关链接

[Add-VMNetworkAdapterAcl](./Add-VMNetworkAdapterAcl.md)

[禁用虚拟机资源计量功能](./Disable-VMResourceMetering.md)

[启用虚拟机资源计量功能](./Enable-VMResourceMetering.md)

[Remove-VMNetworkAdapterAcl](./Remove-VMNetworkAdapterAcl.md)

[重置虚拟机资源计量数据](./Reset-VMResourceMetering.md)

