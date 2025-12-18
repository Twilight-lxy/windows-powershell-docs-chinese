---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.Adless.PowerShell.psm1-help.xml
Module Name: FailoverClusters
ms.date: 09/11/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusters/test-workgroupcluster?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-WorkgroupCluster
---

# 测试工作群组集群

## 摘要
用于测试工作组集群的配置。

## 语法

```
Test-WorkgroupCluster [[-Node] <String[]>] [[-Credentials] <PSCredential[]>] [[-Disk] <Object[]>]
 [[-Pool] <Object[]>] [[-ReportName] <String>] [[-Include] <String[]>] [[-Ignore] <String[]>]
 [-Force] [[-Cluster] <String>] [-Confirm] [-WhatIf] [-Destination] <String> [<CommonParameters>]
```

## 描述

`Test-WorkgroupCluster` 函数用于测试工作组集群的配置。其他参数将会被转发给 `Test-Cluster` 函数。有关 [Test-Cluster](/powershell/module/failoverclusters/test-cluster) cmdlet 的详细信息，请参考其官方文档。

## 示例

### 示例 1

```powershell
Test-WorkgroupCluster -Node "Node1", "Node2" -Credentials $cred1, $cred2
```

这个示例使用 `$cred1` 和 `$cred2` 中的凭据以及其他参数来测试包含 `Node1` 和 `Node2` 的工作组集群的配置。

## 参数

### -Node

工作组集群中的一组节点。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: @()
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credentials

一组用于节点的身份凭证（credentials）。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Disk

指定要运行该 cmdlet 的磁盘编号。如果指定的磁盘处于在线状态，并且被分配给了某个集群角色或集群共享卷（Cluster Shared Volume），则还必须指定 **Force** 参数，以使该磁盘在存储测试期间处于离线状态。否则，在运行该 cmdlet 之前，必须先将指定的磁盘设置为离线状态。

如果未指定 **Disk** 参数，则存储测试将在集群中所有可用的磁盘上进行；这些磁盘可能是处于离线状态，也可能是出现故障的状态。

可接受的值包括：

- **Int32, Int64, Uint32, or Uint64**: A number that represents a master boot record (MBR)
  signature of the disk.
- **System.String**: A string that represents a master boot record (MBR) signature of the disk,
  hexadecimal format is supported, or a string that represents the GUID of a GPT disk.
- **ClusterResource**: A cluster resource object that represents a clustered disk.
- **CimInstance#MSFT_Disk**: An object returned from `Get-Disk`, from the Windows PowerShell storage
  module.

```yaml
Type: Object[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Pool

指定要运行该 cmdlet 的集群存储池。当指定的存储池处于在线状态，并且该存储池中的某个虚拟磁盘已被分配给某个集群角色或集群共享卷（Cluster Shared Volume）时，您还必须指定 **Force** 参数，以便在存储测试期间将该存储池设置为离线状态。否则，命令将因错误而终止执行。

在运行存储测试之前，必须将指定的存储池设置为离线状态。如果未指定 `Pool` 参数，存储测试将在集群中所有可用的存储池上执行；或者这些存储池处于离线状态或故障状态。

可接受的值包括：

- **System.String**: A string that represents the name of the clustered storage pool or pools.
- **ClusterResource**: A cluster resource object that represents a clustered storage pool.
- **CimInstance#MSFT_StoragePool**: An object returned from `Get-StoragePool`, from the Windows
  PowerShell storage module.

```yaml
Type: Object[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
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
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Include

指定在验证测试运行期间应包含哪些测试或哪一类测试。只有所指定的测试或测试类别才会被执行。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 7
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Ignore

指定在验证测试运行期间应忽略哪些测试或哪些类型的测试。其他所有测试或测试类型都将正常执行。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 8
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
Position: 9
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Cluster

指定用于运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 10
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 11
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 12
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Destination

指定用于复制一个或多个集群日志的目标位置。若要复制到当前文件夹，请使用`.`作为此参数的输入值。默认位置是 `C:\Windows\Cluster\Reports`。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 13
Default value: (Get-Location).Path
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接

[添加工作组集群节点](add-workgroupclusternode.md)

[New-WorkgroupCluster](new-workgroupcluster.md)

[Remove-WorkgroupCluster](remove-workgroupcluster.md)

[Remove-WorkgroupClusterNode](remove-workgroupclusternode.md)

[Set-WorkgroupClusterRemotingConfiguration](set-workgroupclusterremotingconfiguration.md)

[Test-WorkgroupClusterRemoting](test-workgroupclusterremoting.md)
