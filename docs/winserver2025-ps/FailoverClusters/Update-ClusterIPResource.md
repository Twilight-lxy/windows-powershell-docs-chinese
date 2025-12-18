---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/23/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/update-clusteripresource?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-ClusterIPResource
---

# 更新 ClusterIP 资源

## 摘要
在故障转移集群中，续订或释放某个IP地址资源的DHCP租约。

## 语法

```
Update-ClusterIPResource [[-Name] <String>] [-Renew] [-Release] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Update-ClusterIPResource` cmdlet 用于更新或释放故障转移集群中 IP 地址资源的 DHCP 租约。此 cmdlet 仅适用于使用 DHCP 协议的 IP 地址资源。

## 示例

#### 示例 1：更新 DHCP 租约

```powershell
Update-ClusterIPResource -Name "Cluster IP Address"
```

这个示例用于更新名为“Cluster IP Address”的资源的DHCP租约（如果该资源是通过DHCP分配的）。

### 示例 2：更新所有集群化 IP 资源的 DHCP 租约

```powershell
$clusterIP = Get-ClusterResource | Where-Object {$_.ResourceType.Name -eq "IP Address"}
$clusterIP | Update-ClusterIPResource
```

这个示例会更新所有通过 DHCP 分配的集群化 IP 资源的 DHCP 租约信息。

#### 示例 3：将某个资源设置为离线状态，并释放其租约

```powershell
$clusterResource = Get-ClusterResource -Name "IP Address 10.24.11.0"
$clusterResource | Stop-ClusterResource | Update-ClusterIPResource -Release
```

这个示例会将名为“IP地址172.24.11.0”的资源设置为离线状态，并释放与该资源相关的DHCP租约。

## 参数

### -Cluster

指定要运行此 cmdlet 的集群的名称。如果该参数的输入为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

指定要更新的集群IP地址资源。

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

指定要更新的集群IP地址资源的名称。

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

### -Release

该操作会导致cmdlet释放与该IP地址资源相关的DHCP租约。

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

### -Renew

该命令使cmdlet更新IP地址资源的DHCP租约。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShellClusterResource

## 输出

### MicrosoftFailoverClusters.PowerShellClusterResource

## 备注

## 相关链接

[Get-ClusterResource](./Get-ClusterResource.md)

[更新集群网络名称资源](./Update-ClusterNetworkNameResource.md)

[Where-Object](https://go.microsoft.com/fwlink/?LinkID=113423)
