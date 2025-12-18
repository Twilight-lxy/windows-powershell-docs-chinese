---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/23/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/test-cluster?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-Cluster
---

# 测试集群

## 摘要
运行验证测试，以检查故障转移集群的硬件和配置是否正常。

## 语法

```
Test-Cluster [[-Node] <StringCollection>] [-Disk <Object[]>] [-Pool <Object[]>]
 [-ReportName <String>] [-List] [-Include <StringCollection>] [-Ignore <StringCollection>] [-Force]
 [-InputObject <PSObject>] [-Cluster <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Test-Cluster` cmdlet 用于对故障转移集群的硬件和设置进行验证测试。这些测试可以在集群搭建之前或之后执行。

测试结果会被保存在一个由您指定的文件名所命名的文件中。通过运行这些验证测试，您可以确认您的硬件配置和设置是否与故障转移集群（Failover Clustering）兼容。测试类型多种多样，包括集群相关测试、资源清单测试、网络测试、存储测试、系统测试等。需要注意的是，存储测试不会检测那些正在被集群角色使用的在线磁盘或存储池。如果要测试这些磁盘/存储池，请先使用 `Stop-ClusterGroup` 命令停止相应的集群角色，然后再运行 `Test-Cluster` 命令。测试完成后，需要重新启动这些集群角色（即资源组）。

> [!注意] > 为了执行某些集群共享卷（CSV）的验证测试，`Test-Cluster` 命令会在每个集群节点上创建一个名为 `CliTest2` 的本地用户账户。这些账户在集群验证测试完成后会自动从您的系统中删除。

## 示例

#### 示例 1：验证本地集群

```powershell
Test-Cluster
```

这个示例会在本地集群上运行所有适用的集群验证测试。

### 示例 2：验证指定的节点

```powershell
Test-Cluster -Node "node1", "node2"
```

这个示例会在名为 `node1` 和 `node2` 的节点上运行所有集群验证测试。如果 `node1` 或 `node2` 已经是某个集群的成员，那么测试将包含该集群中的所有节点。

### 示例 3：在聚类验证中查看测试用例和分类

```powershell
Test-Cluster -List
```

这个示例列出了簇验证中所有测试的名称和类别。您可以使用 **Ignore** 或 **Include** 参数来指定要运行的特定测试。

### 示例 4：验证指定的节点是否适用于存储用途

```powershell
Test-Cluster -Node "node1", "node2" -Include "Storage"
```

这个示例会在名为“node1”和“node2”的节点上运行存储验证测试。如果“node1”或“node2”已经是某个集群的成员，那么这些测试将会涵盖该集群中的所有节点。

### 示例 5：验证指定节点的所有属性（除了库存信息）

```powershell
Test-Cluster -Node "node1", "node2" -Ignore Inventory
```

这个示例会在名为“node1”和“node2”的节点上运行所有验证测试（除了库存相关测试）。如果“node1”或“node2”已经是某个集群的成员，那么测试将会涵盖该集群中的所有节点。

### 示例 6：运行特定的测试

```powershell
Test-Cluster -Include "List Potential Cluster Disks"
```

这个示例会在本地集群上运行名为“List Potential Cluster Disks”的测试。

### 示例 7：运行多个测试

```powershell
Test-Cluster -Include "List System Drivers","List Unsigned Drivers"
```

这个示例在本地集群上运行名为“List System Drivers”和“List Unsigned Drivers”的测试。

## 参数

### -Cluster

指定要运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

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

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Disk

指定要运行此cmdlet的磁盘编号。如果指定的磁盘处于在线状态，并且被分配给某个集群角色或集群共享卷（Cluster Shared Volume），则必须同时指定**Force**参数，以在该存储测试期间将磁盘设置为离线状态。否则，在运行该cmdlet之前，必须先将指定的磁盘设置为离线状态。如果未指定**Disk**参数，存储测试将在集群中所有可用的磁盘上执行；或者在这些磁盘处于离线状态或出现故障的情况下执行。

此参数的可接受值为：

- **Int32, Int64, Uint32, or Uint64**. A number that represents a master boot record (MBR) signature of
  the disk.
- **System.String**. A string that represents a master boot record (MBR) signature of the disk,
  hexadecimal format is supported.
- **System.String**. A string that represents the GUID of a GPT disk.
- **ClusterResource**. A cluster resource object that represents a clustered disk.
- **CimInstance#MSFT_Disk**. An object returned from `Get-Disk`, from the Windows PowerShell storage
  module.

```yaml
Type: Object[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

该cmdlet会直接执行，而不会提示用户进行确认。默认情况下，该cmdlet会在执行前询问用户的确认意见。当与**Disk**或**Pool**参数结合使用时，在存储测试期间，相应的磁盘或存储池将被设置为离线状态。

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

### -Ignore

指定在验证测试运行期间应忽略哪些测试或哪一类测试。所有其他测试或测试类别仍将正常运行。

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

### -Include

指定在验证测试运行期间应包含哪些测试或测试类别。只有此处指定的测试或测试类别才会被执行。

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

### -InputObject

指定用于运行验证测试的集群。

```yaml
Type: PSObject
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -List

该命令会列出所有的测试及其所属的类别，但实际的测试过程（即在服务器或集群节点上执行测试）并不会被触发。

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

指定一个由逗号分隔的服务器名称列表，在这些服务器上运行集群验证测试。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Pool

指定要运行此 cmdlet 的集群存储池。当指定的存储池处于在线状态，并且该存储池中的某个虚拟磁盘被分配给了某个集群角色或集群共享卷（Cluster Shared Volume）时，必须同时指定 **Force** 参数，以在存储测试期间将该存储池设置为离线状态。否则，命令会因错误而退出。在运行存储测试之前，必须先将该存储池设置为离线状态。如果未指定 **Pool** 参数，则存储测试将在集群中所有可用的存储池上执行；或者在这些存储池处于离线或故障状态的情况下进行。

此参数的可接受值为：

- **System.String**: A string that represents the name of the clustered storage pool or pools.
- **ClusterResource**: A cluster resource object that represents a clustered storage pool.
- **CimInstance#MSFT_StoragePool**: An object returned from `Get-StoragePool`, from the Windows
  PowerShell storage module.

```yaml
Type: Object[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportName

指定要生成的测试报告的名称。

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

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell Cluster

## 输出

### System.IO.FileInfo

### MicrosoftFailoverClusters.PowerShellClusterTestInfo

## 备注

## 相关链接

[Get-Cluster](./Get-Cluster.md)

[新集群](./New-Cluster.md)

[Remove-Cluster](./Remove-Cluster.md)

[启动集群](./Start-Cluster.md)

[停止集群操作](./Stop-Cluster.md)
