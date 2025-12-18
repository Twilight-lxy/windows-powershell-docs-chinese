---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusterparameter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterParameter
---

# Get-ClusterParameter

## 摘要
获取关于故障转移集群中某个对象（如集群资源）的详细信息。

## 语法

```
Get-ClusterParameter [[-Name] <StringCollection>] [-InputObject <PSObject>] [-Cluster <String>]
 [<CommonParameters>]
```

## 描述

`Get-ClusterParameter` cmdlet 可以获取故障转移集群中对象的详细信息，例如集群资源的相关数据。该 cmdlet 用于管理集群对象的私有属性。若需获取或设置集群对象的公共属性，请使用相应的 `Get-Cluster*` cmdlet 来获取目标集群对象，然后直接在该对象上设置所需的属性。

使用此 cmdlet 可以获取的详细信息类型取决于与其结合使用的其他 cmdlet。例如：

- If you use this cmdlet with the `Get-ClusterResource` cmdlet for a disk resource, then you can
  obtain the disk signature or GUID of a disk and information about whether maintenance is turned on
  for that disk.

- If you use this cmdlet with the `Get-ClusterResource` cmdlet for a Network Name resource, then
  you can obtain DNS-related information about the resource.

- If you use this cmdlet with the `Get-ClusterResource` cmdlet for an IP address resource, then
  you can obtain DHCP-related information about the IP Address resource.

- If you use this cmdlet with the `Get-ClusterResource` cmdlet for resources used by virtual
  machines, then you can obtain details about the settings for the virtual machines.

## 示例

### 示例 1

```powershell
Get-ClusterResource -Name cluster1FS | Get-ClusterParameter
```

这个示例用于获取本地集群中名为 `cluster1FS` 的集群资源的参数，包括详细信息。显示的参数会根据所查看的资源类型而有所不同。

### 示例 2

```powershell
Get-ClusterResource -Name cluster1FS | Get-ClusterParameter -Name HostRecordTTL
```

这个示例会显示本地集群中名为 `cluster1FS` 的集群资源的 `HostRecordTTL` 参数（如果该参数适用于 `cluster1FS` 的话）。

## 参数

### -Cluster

指定要运行此cmdlet的集群名称。如果该参数的输入为`.`或被省略，则cmdlet将在本地集群上运行。

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

### -InputObject

指定要获取更多信息的集群对象。

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

### -Name

指定要获取的集群参数的名称。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShell Cluster

### Microsoft_failoverClusters.PowShell-clusterGroup

### Microsoft_failoverClusters.PowerShell-clusterNetwork

### MicrosoftFailoverClusters.PowerShell-clusterNetworkInterface

### MicrosoftFailoverClusters.PowerShellClusterNode

### Microsoft FailoverClusters.PowerShellClusterResource

### MicrosoftFailoverClusters.PowerShell ClusterResourceType

### Microsoft FailoverClusters.PowerShell.ClusterSharedVolume

## 输出

### MicrosoftFailoverClusters.PowerShell ClusterParameter

## 备注

## 相关链接

[Set-ClusterParameter](./Set-ClusterParameter.md)
