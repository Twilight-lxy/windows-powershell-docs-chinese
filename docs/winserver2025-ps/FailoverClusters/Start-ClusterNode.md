---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/start-clusternode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-ClusterNode
---

# 启动集群节点

## 摘要
在故障转移集群中的一个节点上启动Cluster服务。

## 语法

```
Start-ClusterNode [[-Name] <StringCollection>] [-ForceQuorum] [-ClearQuarantine]
 [-IgnorePersistentState] [-PreventQuorum] [-Wait <Int32>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Start-ClusterNode` cmdlet 用于在故障转移集群中的一个节点上启动 Cluster 服务。如果这是第一个被启动的节点，它会等待其他节点加入。当达到法定人数（quorum）时，集群才会开始运行。

这个带有 **FixQuorum** 参数的 cmdlet 可以用于强制达到集群所需的法定人数（即 quorum），也就是说，即使尚未达到法定人数要求，也可以强制启动某个集群节点。当在某个节点上强制达成法定人数时，该节点上的集群配置副本将被视为权威配置，并会被复制到所有其他节点。因此，强制达成法定人数应被视为最后的手段，因为某些集群配置更改可能会丢失。在多站点集群环境中，如果拥有大多数节点的主要站点不可用，而需要启动只有少数节点的次要站点时，这种强制达成法定人数的功能就尤为有用。同样地，当没有任何可用的集群节点包含当前的集群配置副本时，该功能也可以用来启动那些采用“节点和文件共享多数投票机制”（Node and File Share Majority quorum）来决定集群状态的集群。

注意：如果服务器计算机上没有启用凭据安全服务提供程序（CredSSP）进行身份验证，那么无法远程运行此cmdlet。

## 示例

### 示例 1

```powershell
Start-ClusterNode -Name node3
```

这个示例在本地集群中名为`node3`的节点上启动了Cluster服务。

### 示例 2

```powershell
Start-ClusterNode -Name node1 -Cluster cluster2
```

这个示例在名为 `cluster2` 的集群中的节点 `node1` 上启动了 Cluster 服务。

### 示例 3

```powershell
Start-ClusterNode -FixQuorum
```

这个示例会强制本地节点和本地集群启动，即使尚未达到法定人数（quorum）的要求。如果尚未达到法定人数，那么本地节点上保存的集群配置副本将被视为权威版本，并会被复制到所有其他节点。请注意，此命令应仅作为最后的手段使用，因为某些集群配置更改可能会丢失（例如与集群服务相关的恢复选项）。

## 参数

### -ClearQuarantine

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cq

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Cluster

指定用于运行此 cmdlet 的集群名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 会在本地集群上运行。

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

### -ForceQuorum

表示该cmdlet会强制启动集群节点，无论是否已达到法定人数（quorum）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: fq, FixQuorum

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IgnorePersistentState

启动集群节点，但不会在该节点上启用任何资源（即不会让相关服务或应用程序开始运行）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: ips

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定要启动的集群节点。

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

指定要启动的集群节点的名称。

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

### -PreventQuorum

启动该节点，但阻止其达到法定人数（quorum）并形成集群，以避免出现两个相互竞争的集群实例同时运行的情况。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: pq

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Wait

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，那么cmdlet会一直等待直到完成。如果指定了`-Wait 0`，则命令会被立即执行，而cmdlet会在不等待的情况下立即返回结果。

```yaml
Type: Int32
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

### MicrosoftFailoverClusters.PowerShellClusterNode

## 输出

### MicrosoftFailoverClusters.PowerShellClusterNode

## 备注

## 相关链接

[添加集群节点](./Add-ClusterNode.md)

[Get-ClusterNode](./Get-ClusterNode.md)

[Remove-ClusterNode](./Remove-ClusterNode.md)

[Resume-ClusterNode](./Resume-ClusterNode.md)

[Stop-ClusterNode](./Stop-ClusterNode.md)

[暂停集群节点](./Suspend-ClusterNode.md)
