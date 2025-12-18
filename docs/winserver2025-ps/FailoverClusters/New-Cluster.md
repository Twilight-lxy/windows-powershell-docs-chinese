---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 03/13/2023
online version: https://learn.microsoft.com/powershell/module/failoverclusters/new-cluster?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-Cluster
---

# 新集群

## 摘要
创建一个新的故障转移集群。

## 语法

```
New-Cluster [-Name] <String> [-Node <StringCollection>] [-StaticAddress <StringCollection>]
 [-IgnoreNetwork <StringCollection>] [-NoStorage] [-S2D]
 [-ManagementPointNetworkType <AdminAccessPointResType>]
 [-AdministrativeAccessPoint <AdminAccessPoint>] [-Force] [<CommonParameters>]
```

## 描述

`New-Cluster` cmdlet 用于创建一个新的故障转移集群。在创建集群之前，必须先连接相关的硬件（服务器、网络和存储设备），并运行验证测试。

使用 Test-Cluster 来运行验证测试。这些测试将确认硬件和配置是否适合故障转移集群的需求。测试类型有多种，包括资源清单（Inventory）、系统配置（System Configuration）、网络（Network）、存储（Storage）以及其他类型的测试。

> [!提示] > 您应该从与集群节点相同版本的集群节点或客户端运行 `New-Cluster` 命令。如果从版本较低的客户端计算机运行 `New-Cluster`，则可能需要在运行 `New-Cluster` 之后再执行 `Update-ClusterFunctionalLevel` 命令。

## 示例

### 示例 1

```powershell
New-Cluster -Name cluster1 -Node node1,node2,node3,node4
```

这个示例创建了一个名为 `cluster1` 的四节点集群，并使用默认的IP地址设置。

### 示例 2

```powershell
New-Cluster -Name cluster1 -Node node1,node2 -NoStorage
```

这个示例创建了一个名为 `cluster1` 的两节点集群。该集群没有任何集群化的存储资源或磁盘资源。可以使用 `Get-ClusterAvailableDisk` cmdlet 结合 `Add-ClusterDisk` cmdlet 来添加存储资源。

### 示例 3

```powershell
New-Cluster -Name cluster1 -Node node1,node2,node3,node4 -StaticAddress 2.0.0.123
```

这个示例创建了一个名为 `cluster1` 的四节点集群，该集群使用静态 IP 地址 `2.0.0.123`。

### 示例 4

```powershell
New-Cluster -Name cluster1 -Node node1,node2,node3,node4 -StaticAddress 2.0.0.123,3.0.0.123
```

这个示例创建了一个名为 `cluster1` 的四节点集群，该集群使用静态 IP 地址 `2.0.0.123` 和 `3.0.0.123`。

### 示例 5

```powershell
New-Cluster -Name cluster1 -Node node1,node2,node3,node4 -IgnoreNetwork 2.0.0.0/8
```

这个示例创建了一个名为 `cluster1` 的四节点集群。该集群使用默认的 IP 地址设置，并没有使用 `2.0.0.0/8` 这个网络。

### 示例 6

```powershell
$parameters = @{
    Name = 'cluster1'
    Node = 'node1','node2','node3','node4'
    StaticAddress = '2.0.0.123'
    IgnoreNetwork = '3.0.0.0/8'
}
New-Cluster @parameters
```

这个示例创建了一个名为“cluster1”的四节点集群。该集群使用静态IP地址2.0.0.123，没有使用网络3.0.0.0/8。

这个示例使用了“拆分”（splatting）技术，将 `$Parameters` 变量中的参数值传递给命令。有关 [拆分](/powershell/module/microsoft.powershell.core/about/about_splatting) 的更多信息，请参阅相关文档。

## 参数

### -AdministrativeAccessPoint

指定 cmdlet 为集群创建的行政访问点的类型。该参数的可接受值包括：

- **ActiveDirectoryAndDns**. The cmdlet creates an administrative access point for the cluster. The
  administrative access point is registered in DNS and enabled in Active Directory Domain Services.

- **Dns**. The cmdlet creates an administrative access point for the cluster. The administrative
  access point is registered in DNS but isn't enabled in Active Directory Domain Services.

- **None**.

该 cmdlet 不会为集群创建一个管理访问点。如果没有管理访问点，某些集群角色和功能可能无法使用。此外，也无法使用故障转移集群管理器来管理没有管理访问点的集群。

```yaml
Type: AdminAccessPoint
Parameter Sets: (All)
Aliases: aap
Accepted values: None, ActiveDirectoryAndDns, Dns, ActiveDirectory

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令运行，而无需请求用户确认。

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

### -IgnoreNetwork

指定在运行该cmdlet时要忽略的一个或多个网络。启用了DHCP的网络始终会被包含在内，但其他网络需要使用**StaticAddress**参数来指定静态地址，或者应通过**IgnoreNetwork**参数明确地将其忽略。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagementPointNetworkType
指定用于确定IP地址设置的网络配置。

此参数的可接受值为：

- Automatic: Automatically detects the appropriate setting. If SQL Server is running in Azure, uses `Distributed`. If SQL Server is running on-premises, uses `Singleton`. (Default setting)
- Singleton: The traditional method of DHCP or static IP address.
- Distributed: Uses a Distributed Network Name by using Node IP addresses.

```yaml
Type: AdminAccessPointResType
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: Automatic
Accept pipeline input: False
Accept wildcard characters: False
```


### -Name

指定要创建的集群的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoStorage

指定在创建集群的过程中忽略共享存储。操作完成后生成的集群将不包含共享存储。之后可以通过将 `Get-ClusterAvailableDisk` cmdlet 返回的 **ClusterDiskInfo** 对象通过管道传递给 `Add-ClusterDisk` cmdlet 来添加共享存储。

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

### -Node

指定一个用逗号分隔的集群节点名称或服务器名称列表，在这些节点上创建集群。如果未指定此参数，则会在本地物理计算机上创建一个单节点集群。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -S2D

指定在创建集群时是否启用“Storage Spaces Direct”功能。

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

### -StaticAddress

指定一个或多个在运行该cmdlet时使用的静态地址。启用了DHCP的网络始终会被包含在内，但其他网络需要通过**StaticAddress**参数来指定静态地址；或者可以通过**IgnoreNetwork**参数明确忽略这些网络。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### MicrosoftFailoverClusters.PowerShell_cluster

## 备注

- This cmdlet cannot be run remotely without Credential Security Service Provider (CredSSP)
  authentication on the server computer.

## 相关链接

[添加集群节点](./Add-ClusterNode.md)

[Get-Cluster](./Get-Cluster.md)

[Remove-Cluster](./Remove-Cluster.md)

[启动集群](./Start-Cluster.md)

[停止集群操作](./Stop-Cluster.md)

[测试集群](./Test-Cluster.md)
