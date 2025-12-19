---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/measure-vmresourcepool?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Measure-VMResourcePool
---

# Measure-VMResourcePool

## 摘要
报告一个或多个资源池的资源利用数据。

## 语法

```
Measure-VMResourcePool [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String[]> [[-ResourcePoolType] <VMResourcePoolType[]>] [<CommonParameters>]
```

## 描述
` Measure-VMResourcePool ` cmdlet 可报告一个或多个虚拟机资源池的处理器使用情况、内存使用情况、网络流量以及磁盘容量等相关数据。

注意：只有在为虚拟机资源池启用了资源计量功能后，才能通过 **Measure-VMResourcePool** cmdlet 获取用于报告的数据。

这个cmdlet也可以使用具有相同名称的资源池数组来调用。在这种情况下，不同资源类型的资源利用数据将被汇总在一份报告中。

该报告包含以下字段：

    -- ComputerName: The name of the virtual machine host.

    -- ResourcePoolType: The type of the virtual machine resource pool.

    -- ResourcePoolName: The name of the resource pool.

    -- MeteringDuration: The duration over which resource utilization data is being reported.

    -- AverageProcessorUsage: The sum of the average processor usage, in megahertz, of the virtual machines under the specified resource pool over the time period reported in the MeteringDuration field.

    -- AverageMemoryUsage: The sum of the average memory usage, in megabytes, of the virtual machines under the specified resource pool over the time period reported in the MeteringDuration field.

    -- MaximumMemoryUsage: The maximum memory usage, in megabytes, of any virtual machine under the specified resource pool over the time period reported in the MeteringDuration field.

    -- MinimumMemoryUsage: The minimum memory usage, in megabytes, of any virtual machine under the specified resource pool over the time period reported in the MeteringDuration field.

    -- TotalDiskAllocation: The maximum disk capacity, in gigabytes, allocated to any virtual machine under the specified resource pool over the time period reported in the MeteringDuration field.

    -- NetworkMeteredTrafficReport: An array whose elements report the traffic through each NetworkAdapterAcl on the virtual machines under the specified resource pool over the time period reported in the MeteringDuration field.

每个数组元素都具有以下属性：

    -- LocalAddress: for an inbound packet, the destination IP address in the packet header; for an outbound packet, the source IP address in the packet header.

    -- RemoteAddress: for an inbound packet, the source IP address in the packet header; for an outbound packet, the destination IP address in the packet header.

-- 方向：ACL适用的网络流量方向。允许的值包括 Inbound（入站）、Outbound（出站）或 Both（两者均可）。

    -- TotalTraffic: the amount of network traffic, in megabytes, through the NetworkAdapterAcl.

注释：

    -- The disk capacity allocated to the virtual machine is reported as the sum of the virtual capacity of the virtual machine's virtual hard disks, together with the sum of the physical disk capacity of the virtual machine's virtual hard disk snapshots.

    -- Resource utilization information is not available for resource pool types of FiberChannelConnection, FibreChannelPort, VFD, and ISO.

    -- If the virtual machines under the specified resource pool are configured with the same values for LocalAddress, RemoteAddress, and Direction, the information from each of these NetworkAdapterAcl objects is aggregated in the TotalTraffic property specified by the NetworkMeteredTrafficReport of the object returned by the **Measure-VMResourcePool** cmdlet.

资源池利用率报告的默认显示内容包括以下列：

    -- Name: the name of the resource pool.

    -- ResourcePoolType: the type of the virtual machine resource pool.

    --AvgCPU(Mhz): the sum of the average processor usage, in megahertz, of the virtual machines under the specified resource pool.

    -- AvgRAM(M): the sum of the average memory usage, in megabytes, of the virtual machines under the specified resource pool.

    -- TotalDisk(G): the maximum disk capacity, in gigabytes, allocated to any virtual machine under the specified resource pool.

    -- NetworkInbound(M): total incoming traffic, in megabytes, to the virtual machines under the specified resource pool.

    -- NetworkOutbound(M): total outgoing network traffic, in megabytes, to the virtual machines under the specified resource pool.

## 示例

### 示例 1
```
PS C:\> Measure-VMResourcePool -Name TestResourcePool -ResourcePoolType Memory
```

这个示例报告了一个名为 TestResourcePool 的资源池的资源利用数据。

### 示例 2
```
PS C:\> $UtilizationReport = Get-VMResourcePool -Name "TestResourcePool" -ResourcePoolType @("Processor","VHD","Ethernet","Memory") | Measure-VMResourcePool
PS C:\> Get-VMResourcePool -ResourcePoolType @("Processor","VHD","Ethernet","Memory") | Reset-VMResourceMetering
```

这个示例使用了两个命令以及管道（pipeline）机制。第一个命令通过 `Get-VMResourcePool` cmdlet 获取一组资源池的资源利用率数据，将该数据对象传递给 `Measure-VMResourcePool` cmdlet，并将结果存储在名为 `$UtilizationReport` 的变量中。第二个命令会重置这些资源池的资源利用率数据，从而让 Hyper-V 开始重新收集这些资源池的新数据。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个虚拟机主机，以便报告这些主机的资源使用情况。允许使用 NetBIOS 名称、IP 地址和完全限定域名。默认值为本地计算机。可以使用 `localhost` 或点号（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值是当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定用于报告资源利用情况的资源池的友好名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ResourcePoolType
指定要报告资源使用情况的虚拟机资源池的资源类型。有效值为：

- Ethernet
- Memory
- Processor
- VHD

```yaml
Type: VMResourcePoolType[]
Parameter Sets: (All)
Aliases:
Accepted values: Ethernet, Memory, Processor, VHD

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.HyperV.PowerShell.VMResourcePoolType[]

## 输出

### Microsoft.HyperV POWERShell.VMMeteringReportForResourcePool

## 备注

## 相关链接

[Add-VMNetworkAdapterAcl](./Add-VMNetworkAdapterAcl.md)

[禁用虚拟机资源计量功能](./Disable-VMResourceMetering.md)

[Enable-VMResourceMetering](./Enable-VMResourceMetering.md)

[Remove-VMNetworkAdapterAcl](./Remove-VMNetworkAdapterAcl.md)

[重置虚拟机资源计量功能](./Reset-VMResourceMetering.md)

