---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clusterscaleoutfileserverrole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterScaleOutFileServerRole
---

# 添加 ClusterScaleOutFileServerRole 角色

## 摘要
创建一个集群化的文件服务器，用于扩展应用程序数据存储容量。

## 语法

```
Add-ClusterScaleOutFileServerRole [[-Name] <String>] [-Wait <Int32>] [-Infrastructure]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterScaleOutFileServerRole` cmdlet 用于创建一个集群化的文件服务器，以支持应用程序数据的扩展需求。这种类型的文件服务器可以为那些需要长时间保持文件打开状态的应用程序或虚拟机提供存储空间。客户端连接会被分布到各个节点上，从而提高数据传输效率。该文件服务器支持 Server Message Block (SMB) 协议，但不支持 Network File System (NFS) 协议，也不支持某些角色服务（如 File Server Resource Manager (FSRM) 或 Distributed File System (DFS) 复制功能）。

> [注意] > 如果服务器计算机上没有启用凭据安全服务提供程序（CredSSP）进行身份验证，该cmdlet无法远程运行。

## 示例

### 示例 1

```powershell
Add-ClusterScaleOutFileServerRole
```
这个示例创建了一个高可用性的可扩展文件服务器角色。

### 示例 2

```powershell
Add-ClusterScaleOutFileServerRole -Wait 0
```

这个示例创建了一个高可用性的可扩展文件服务器角色。该命令行工具（cmdlet）会在不等待所有资源都上线的情况下完成执行。

### 示例 3

```powershell
Add-ClusterScaleOutFileServerRole -Cluster MyCluster -Infrastructure -Name InfraSOFSName
```

这个示例创建了一个用于基础设施文件服务器扩展的文件服务器角色。它会自动为 CSV 驱动器创建一个命名空间共享（例如 `\\InfraSOFSName\Volume1`）。在超融合配置中，这样的基础设施文件服务器可以确保 SMB 客户端（Hyper-V 主机）与基础设施文件服务器之间的通信具有高可用性（即持续稳定的连接）。在一个故障转移集群上，最多只能有一个基础设施文件服务器扩展角色。

## 参数

### -Cluster

指定用于运行此 cmdlet 的集群的名称。如果该参数的输入为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

### -Infrastructure

指定是否创建用于扩展文件服务器角色的基础设施文件服务器。

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

指定用于创建高可用性扩展文件服务器的集群。

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

指定正在创建的高可用性横向扩展文件服务器的名称。

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

### -Wait

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，那么cmdlet会一直等待直到操作完成。如果指定的值为`0`，则表示命令将立即被执行，cmdlet会在不等待的情况下立即返回结果。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters.PowerShellCluster

## 输出

### MicrosoftFailoverClusters.PowerShell.ClusterGroup

## 备注

## 相关链接

[Add-ClusterFileServerRole](./Add-ClusterFileServerRole.md)

[Get-ClusterGroup](./Get-ClusterGroup.md)

[Move-ClusterGroup](./Move-ClusterGroup.md)

[Remove-ClusterGroup](./Remove-ClusterGroup.md)

[启动集群组](./Start-ClusterGroup.md)

[Stop-ClusterGroup](./Stop-ClusterGroup.md)
