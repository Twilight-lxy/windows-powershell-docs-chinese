---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clustergenericservicerole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterGenericServiceRole
---

# 添加集群通用服务角色（Add-ClusterGenericServiceRole）

## 摘要
为一项最初并未被设计为在故障转移集群中运行的服务配置高可用性。

## 语法

```
Add-ClusterGenericServiceRole -ServiceName <String> [-CheckpointKey <StringCollection>]
 [-Storage <StringCollection>] [-StaticAddress <StringCollection>]
 [-IgnoreNetwork <StringCollection>] [[-Name] <String>] [-Wait <Int32>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterGenericServiceRole` cmdlet 用于为那些原本并非为在故障转移集群中运行的服务配置高可用性。集群软件会启动该服务，然后定期查询操作系统中的 Service Controller，以确定该服务是否正在运行。如果服务确实正在运行，则会被视为处于在线状态，此时系统不会重新启动该服务或执行故障转移操作。

> [注意] > 如果服务器计算机上没有启用凭据安全服务提供者（CredSSP）的身份验证机制，那么无法远程运行此cmdlet。

## 示例

### 示例 1：配置一个使用默认值的服务

```powershell
Add-ClusterGenericServiceRole -ServiceName "Service1"
```

这个示例将 Service1 配置为一个通用的集群服务，默认使用名称和 IP 地址，并且没有为其分配磁盘。

#### 示例 2：配置一个服务，该服务使用默认值和指定的磁盘

```powershell
Add-ClusterGenericServiceRole -ServiceName "Service1" -Storage "Cluster Disk 6"
```

这个示例将 Service1 配置为一个使用“Cluster Disk 6”的通用集群服务，并为其名称和 IP 地址设置了默认值。

## 参数

### -CheckpointKey

指定一个用逗号分隔的注册表检查点键列表，这些键将添加到这个高可用性的通用应用程序中。所有的注册表路径都是相对于 HKEY_LOCAL_MACHINE 的。

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

### -IgnoreNetwork

指定在运行此cmdlet时要忽略的一个或多个网络。启用了DHCP的网络始终会被包含在内，但其他网络需要使用**StaticAddress**参数指定静态地址，或者应通过**IgnoreNetwork**参数明确忽略这些网络。

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

指定用于创建高可用性服务的集群。

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

指定要创建的高可用服务的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ServiceName

指定用于高可用性服务的服务名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StaticAddress

指定一个或多个在运行该 cmdlet 时使用的静态地址。启用 DHCP 的网络始终会被包含在内，但其他网络需要通过 **StaticAddress** 参数来指定静态地址；或者可以使用 **IgnoreNetwork** 参数明确忽略这些网络。

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

### -Storage

指定要添加到所创建的高可用服务中的集群磁盘资源。

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

### -Wait

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，那么cmdlet会一直等待直到完成；如果指定值为`0`，则命令会立即被执行，而cmdlet会在不等待的情况下返回结果。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell-cluster

## 输出

### MicrosoftFailoverClusters.PowerShell-clusterGroup

## 备注

## 相关链接

[Add-ClusterGenericApplicationRole](./Add-ClusterGenericApplicationRole.md)

[Add-ClusterGenericScriptRole](./Add-ClusterGenericScriptRole.md)

[Get-ClusterGroup](./Get-ClusterGroup.md)

[Move-ClusterGroup](./Move-ClusterGroup.md)

[Remove-ClusterGroup](./Remove-ClusterGroup.md)

[开始创建集群组](./Start-ClusterGroup.md)

[Stop-ClusterGroup](./Stop-ClusterGroup.md)
