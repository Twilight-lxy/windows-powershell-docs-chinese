---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/set-clusterquorum?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ClusterQuorum
---

# 设置集群法定人数（Set-ClusterQuorum）

## 摘要
配置故障转移集群的法定人数（quorum）相关选项。

## 语法

```
Set-ClusterQuorum [-DiskOnly <String>] [-NoWitness] [-DiskWitness <String>]
 [-FileShareWitness <String>] [-CloudWitness] [-AccountName <String>] [-Endpoint <String>]
 [-AccessKey <String>] [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Set-ClusterQuorum` cmdlet 用于配置故障转移集群的法定人数（quorum）相关选项。在故障转移集群中，法定人数的设置决定了该集群能够承受的故障数量；如果再发生额外的故障，集群就必须停止运行。这里的“故障”指的是节点故障，或者在某些情况下，还包括磁盘见证（其中存储有集群配置的副本）或文件共享见证的故障。

## 示例

### 示例 1

```powershell
Set-ClusterQuorum -NodeMajority
```

这个示例将本地集群的投票机制（quorum configuration）更改为“节点多数制”（Node Majority）。

### 示例 2

```powershell
Set-ClusterQuorum -DiskWitness "Cluster Disk 7"
```

这个示例将本地集群的法定人数（quorum）配置更改为“节点多数”（Node Majority）和“磁盘多数”（Disk Majority），并使用名为“Cluster Disk 7”的磁盘资源作为磁盘见证者（disk witness）。

### 示例 3

```powershell
Set-ClusterQuorum -NodeAndFileShareMajority \\fileserver\fsw
```

这个示例将本地集群的法定人数（quorum）配置更改为“节点多数”（Node Majority）和“文件共享多数”（File Share Majority），并使用位于 `\\fileserver\fsw` 的磁盘资源作为文件共享见证节点。

### 示例 4

```powershell
$parameters = @{
    CloudWitness = $true
    AccountName  = '<AzureStorageAccountName>'
    AccessKey    = '<AzureStorageAccountAccessKey>'
}
Set-ClusterQuorum @parameters
```

这个示例将法定人数（quorum）配置更改为使用一个Azure存储账户作为云见证（Cloud Witness）。

这个示例使用了“拆分”（splatting）技术，将 `$Parameters` 变量中的参数值传递给命令。有关 [拆分](/powershell/module/microsoft.powershell.core/about/about_splatting) 的更多信息，请参阅相关文档。

## 参数

### -AccessKey

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

### -AccountName

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

### -CloudWitness

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

### -DiskOnly

这会导致集群的法定人数（quorum）仅设置为基于磁盘存储的方式。这种设置并不推荐，因为它会为整个集群带来单点故障的风险。

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

### -DiskWitness

指定集群法定人数（quorum）用作磁盘见证者（disk witness）的磁盘资源名称。设置此参数后，集群法定人数的类型将变为“节点和磁盘多数制”（Node and Disk Majority）。

```yaml
Type: String
Parameter Sets: (All)
Aliases: NodeAndDiskMajority

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Endpoint

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

### -FileShareWitness

指定集群仲裁机制（quorum）用作“文件见证”（file witness）的文件共享路径。设置此参数后，集群仲裁机制的模式将变为“节点和文件共享多数投票”（Node and File Share Majority）类型。

```yaml
Type: String
Parameter Sets: (All)
Aliases: NodeAndFileShareMajority

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定要更改仲裁团类型的集群。

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

### -NoWitness

表示该cmdlet将集群法定人数（quorum）设置为“节点多数”（Node Majority）类型。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: NodeMajority

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShell Cluster

## 输出

### MicrosoftFailoverClusters.PowerShellClusterQuorumSettings

## 备注

## 相关链接

[Get-ClusterQuorum](./Get-ClusterQuorum.md)
