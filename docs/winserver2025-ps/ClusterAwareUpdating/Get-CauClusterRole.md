---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 09/27/2022
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/get-cauclusterrole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-CauClusterRole
---

# Get-CauClusterRole

## 摘要
获取指定集群上CAU（Clustered Authentication Unit）角色相关的配置属性。

## 语法

```
Get-CauClusterRole [[-ClusterName] <String>] [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述

`Get-CauClusterRole` cmdlet 用于获取指定集群中“集群感知更新”（Cluster-Aware Updating, CAU）集群角色的配置属性。

## 示例

#### 示例 1：获取指定集群上关于 CAU 集群角色的信息

```powershell
Get-CauClusterRole -ClusterName "CONTOSO-FC1"
```

此命令用于获取名为 CONTOSO-FC1 的集群上 CAU 集群角色的相关信息。

## 参数

### -ClusterName

指定此cmdlet获取CAU（Clustered Authentication Unit）集群角色信息所对应的集群名称。仅当该cmdlet不在故障转移集群节点上运行，或者用于引用与执行该cmdlet的集群不同的故障转移集群时，才需要这个参数。

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

### -Credential

指定目标集群的管理凭据。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft_CLUSTERAwareUpdating.CauParameter

## 备注

## 相关链接

[Add-CauClusterRole](./Add-CauClusterRole.md)

[Disable-CauClusterRole](./Disable-CauClusterRole.md)

[Enable-CauClusterRole](./Enable-CauClusterRole.md)

[Remove-CauClusterRole](./Remove-CauClusterRole.md)

[Set-CauClusterRole](./Set-CauClusterRole.md)

