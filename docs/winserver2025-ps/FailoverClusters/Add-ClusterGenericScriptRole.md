---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clustergenericscriptrole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterGenericScriptRole
---

# 添加通用集群脚本角色（Add-ClusterGenericScriptRole）

## 摘要
配置一个由脚本控制的应用程序，该脚本在 Windows 脚本宿主（Windows Script Host）中运行，并且属于一个故障转移集群（failover cluster）的一部分。

## 语法

```
Add-ClusterGenericScriptRole -ScriptFilePath <String> [-Storage <StringCollection>]
 [-StaticAddress <StringCollection>] [-IgnoreNetwork <StringCollection>] [[-Name] <String>]
 [-Wait <Int32>] [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterGenericScriptRole` cmdlet 用于配置一个由脚本控制的应用程序，该脚本在 Windows 脚本宿主（Windows Script Host）中运行，并且该应用程序属于一个故障转移集群（failover cluster）的一部分。

该脚本向集群软件提供了关于应用程序当前状态的信息。根据需要，集群软件会重新启动应用程序或进行故障转移操作。通过该脚本，应用程序可以被成功重启或顺利完成故障转移。

> [注意] > 如果服务器计算机上没有启用凭据安全服务提供程序（CredSSP）的身份验证功能，此 cmdlet 无法远程运行。

## 示例

#### 示例 1：配置一个脚本以便在故障转移集群上运行

```powershell
Add-ClusterGenericScriptRole -ScriptFilePath "script1.vbs"
```

这个示例配置了名为 `script1.vbs` 的脚本，使其在故障转移集群中运行。该脚本的名称和 IP 地址使用默认值设置，并且没有分配任何磁盘。

### 示例 2：在故障转移集群上配置一个脚本，并为其指定一个集群脚本名称

```powershell
Add-ClusterGenericScriptRole -ScriptFilePath "script1.vbs" -Storage "Cluster Disk 4" -Name "script1"
```

这个示例配置了一个名为 `script1.vbs` 的脚本，使其能够在故障转移集群中运行，并使用 “Cluster Disk 4” 作为存储资源。该命令行工具（cmdlet）为这个集群化的脚本指定了名称 “script1”。

### 示例 3：配置一个脚本，在故障转移集群上运行时无需等待资源准备好

```powershell
Add-ClusterGenericScriptRole -ScriptFilePath "script1.vbs" -Wait 0
```

这个示例配置了一个名为 `script1.vbs` 的脚本，使其在故障转移集群中运行。该脚本使用默认的名称和 IP 地址进行配置，并且没有为脚本分配任何磁盘资源。此外，此 cmdlet 在所有资源都上线之前就会完成执行过程（即不会等待所有资源都准备好才继续执行）。

## 参数

### -Cluster

指定用于运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

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

指定在运行该cmdlet时需要忽略的一个或多个网络。启用DHCP的网络总是会被包含在内，但其他网络则需要使用**StaticAddress**参数来指定静态地址，或者可以使用**IgnoreNetwork**参数明确表示忽略这些网络。

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

指定用于创建高可用性脚本的集群。

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

指定要创建的高可用性脚本的名称。

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

### -ScriptFilePath

指定用于高可用性脚本的脚本文件的路径。

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

指定一个或多个在运行该 cmdlet 时使用的静态地址。启用 DHCP 的网络始终会被包含在内，但其他网络需要使用 **StaticAddress** 参数来指定静态地址；或者可以通过使用 **IgnoreNetwork** 参数明确忽略这些网络。

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

指定要添加到创建的高可用性脚本中的集群磁盘资源。

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

该参数用于指定等待 cmdlet 完成的时间（以秒为单位）。如果未指定 `Wait` 参数，那么 cmdlet 会一直等待直到完成；如果指定了值 `0`，则 cmdlet 会立即执行并立即返回，而不会进行任何等待。

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

### Microsoft_failoverClusters.PowerShell_cluster

## 输出

### Microsoft FailoverClusters.PowerShell ClusterGroup

## 备注

## 相关链接

[Add-ClusterGenericApplicationRole](./Add-ClusterGenericApplicationRole.md)

[Add-ClusterGenericServiceRole](./Add-ClusterGenericServiceRole.md)

[Get-ClusterGroup](./Get-ClusterGroup.md)

[Move-ClusterGroup](./Move-ClusterGroup.md)

[Remove-ClusterGroup](./Remove-ClusterGroup.md)

[开始集群组操作](./Start-ClusterGroup.md)

[停止集群组](./Stop-ClusterGroup.md)
