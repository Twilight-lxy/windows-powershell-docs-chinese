---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.Adless.PowerShell.psm1-help.xml
Module Name: FailoverClusters
ms.date: 09/11/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusters/new-workgroupcluster?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-WorkgroupCluster
---

# 新工作组集群

## 摘要
创建一个新的工作组集群。

## 语法

```
New-WorkgroupCluster [[-Node] <String[]>] [[-Credentials] <PSCredential[]>] [[-Name] <String>]
 [[-StaticAddress] <String[]>] [[-IgnoreNetwork] <String[]>]
 [[-ManagementPointNetworkType] <AdminAccessPointResType>]
 [[-AdministrativeAccessPoint] <AdminAccessPoint>] [-NoStorage] [-S2D] [-Force] [-Confirm] [-WhatIf]
 [<CommonParameters>]
```

## 描述

`New-WorkgroupCluster` cmdlet 用于创建一个新的工作组集群。

## 示例

### 示例 1

```powershell
New-WorkgroupCluster -Node "Node1", "Node2" -Credentials $cred1, $cred2 -Name "Cluster1"
```

这个示例使用 `$cred1` 和 `$cred2` 中的凭据创建了一个名为 `Cluster1` 的新的工作组集群，该集群包含 `Node1` 和 `Node2`。

注意：对于 AdministrativeAccessPoint，仅支持 “None” 和 “DNS” 两种设置。

## 参数

### -Node

一组要包含在集群中的节点。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: @()
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credentials

用于节点的一组凭据。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

工作组集群的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StaticAddress

指定一个或多个在运行该 cmdlet 时使用的静态地址。启用 DHCP 的网络始终会被包含在内，但其他网络需要通过 **StaticAddress** 参数来指定静态地址；或者可以使用 **IgnoreNetwork** 参数明确忽略这些网络。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IgnoreNetwork

指定在运行此 cmdlet 时要忽略的一个或多个网络。启用 DHCP 的网络总是会被包含在内，但其他网络需要使用 **StaticAddress** 参数来指定静态地址，或者应该通过 **IgnoreNetwork** 参数明确地将其忽略。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagementPointNetworkType

指定用于确定 IP 地址设置的网络配置。可接受的值有：

- `Automatic`: Automatically detects the appropriate setting.
  - If SQL Server is running in Azure, it uses `Distributed`.
  - If SQL Server is running on-premises, it uses `Singleton`.
- `Singleton`: The traditional method of DHCP or static IP address.
- `Distributed`: Uses a Distributed Network Name by using Node IP addresses.

对于本地部署的 SQL Server，如果该值被设置为 `Automatic`，则默认情况下会使用 `Singleton` 模式。

```yaml
Type: AdminAccessPointResType
Parameter Sets: (All)
Aliases:
Accepted values: Automatic, Singleton, Distributed

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AdministrativeAccessPoint

指定cmdlet为集群创建的管理访问点的类型。可接受的值有：

- `DNS`: The cmdlet creates an administrative access point for the cluster. The administrative
  access point is registered in DNS but isn't enabled in Active Directory Domain Services.
- `None`

The cmdlet doesn't create an administrative access point for the cluster. Some clustered roles and
functionality might not be available for a cluster that doesn't have an administrative access
point. Also, you cannot use Failover Cluster Manager to manage a cluster that doesn't have an
administrative access point.

```yaml
Type: AdminAccessPoint
Parameter Sets: (All)
Aliases:
Accepted values: None, Dns

Required: False
Position: 7
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoStorage

指定工作组集群节点将忽略共享存储资源。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -S2D

指定在创建工作组集群时是否启用“Storage Spaces Direct”功能。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令运行，而无需询问用户的确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm

在运行 cmdlet 之前会提示您确认是否要执行该操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果该cmdlet被运行会发生的情景。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接

[添加工作组集群节点](add-workgroupclusternode.md)

[Remove-WorkgroupCluster](remove-workgroupcluster.md)

[Remove-WorkgroupClusterNode](remove-workgroupclusternode.md)

[Set-WorkgroupClusterRemotingConfiguration](set-workgroupclusterremotingconfiguration.md)

[Test-WorkgroupCluster](test-workgroupcluster.md)

[Test-WorkgroupClusterRemoting](test-workgroupclusterremoting.md)
