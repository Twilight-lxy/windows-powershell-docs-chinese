---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/set-clusterparameter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ClusterParameter
---

# 设置集群参数（Set-ClusterParameter）

## 摘要
用于控制故障转移集群中某个对象（如资源、组或网络）的特定属性。

## 语法

### NoMultiple（默认值）

```
Set-ClusterParameter [-InputObject <PSObject>] [-Create] [-Delete] [-Cluster <String>]
 [<CommonParameters>]
```

### 单个参数

```
Set-ClusterParameter [-InputObject <PSObject>] [[-Name] <String>] [[-Value] <PSObject>] [-Create]
 [-Delete] [-Cluster <String>] [<CommonParameters>]
```

### 多个参数

```
Set-ClusterParameter [-InputObject <PSObject>] [[-Multiple] <Hashtable>] [-Create] [-Delete]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Set-ClusterParameter` cmdlet 用于控制故障转移集群中对象的特定属性，例如资源、组或网络。

- For a disk resource, you can set the disk signature or GUID of a disk, and turn maintenance on
  or off for that disk.

- For a Network Name resource, you can set DNS-related information about the resource.

- For an IP address resource, you can set DHCP-related information about the IP Address resource.

- For resources used by virtual machines, you can set details about the settings for the virtual
  machines.

## 示例

### 示例 1

```powershell
Get-ClusterResource -Name "Cluster Disk 3" | Set-ClusterOwnerNode -Owners node1,node2
```

这个示例将名为“Cluster Disk 3”的集群在本地集群上的可能所有者设置为节点“node1”和“node2”。

### 示例 2

```powershell
Set-ClusterOwnerNode -Group cluster12FS -Owners node3,node2
```

这个示例将名为 `cluster12FS` 的集群服务的首选所有者设置为本地集群中的 `node3` 节点，其次再设置为 `node2` 节点。

## 参数

### -Cluster

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

### -Create

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

### -Delete

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

### -InputObject

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

### -Multiple

```yaml
Type: Hashtable
Parameter Sets: Multiple Parameter
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

```yaml
Type: String
Parameter Sets: Single Parameter
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Value

```yaml
Type: PSObject
Parameter Sets: Single Parameter
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShellCluster

### MicrosoftFailoverClusters.PowerShell-clusterGroup

### MicrosoftFailoverClusters.PowerShell_clusterNetwork

### Microsoft FailoverClusters PowerShell ClusterNetworkInterface

### Microsoft FailoverClusters PowerShell ClusterNode

### MicrosoftFailoverClusters.PowerShellClusterParameter

### MicrosoftFailoverClusters.PowShell ClusterResource

### MicrosoftFailoverClusters.PowerShell ClusterResourceType

### MicrosoftFailoverClusters.PowerShell-clusterSharedVolume

## 输出

## 备注

## 相关链接

[Get-ClusterParameter](./Get-ClusterParameter.md)
