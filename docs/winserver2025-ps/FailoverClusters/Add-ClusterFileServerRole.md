---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clusterfileserverrole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterFileServerRole
---

# 添加 ClusterFileServerRole 角色

## 摘要
创建一个集群文件服务器资源组。

## 语法

```
Add-ClusterFileServerRole -Storage <StringCollection> [-StaticAddress <StringCollection>]
 [-IgnoreNetwork <StringCollection>] [[-Name] <String>] [-Wait <Int32>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterFileServerRole` cmdlet 创建一个集群文件服务器资源组，该资源组包含一个或多个磁盘，在这些磁盘上可以为用户创建共享文件夹。

在添加集群文件服务器时，请指定该文件服务器的名称、任何未被DHCP设置自动提供的IP地址信息，以及该集群文件服务器应使用的存储卷。

> [注意] > 如果服务器计算机上没有启用凭据安全服务提供程序（CredSSP）的身份验证功能，就无法远程运行此cmdlet。

## 示例

### 示例 1：创建一个集群文件服务器

```powershell
Add-ClusterFileServerRole -Storage "Cluster Disk 8"
```

这个示例使用“Cluster Disk 8”创建了一个集群文件服务器，并为其分配了一个默认名称。

### 示例 2：创建并命名一个集群文件服务器

```powershell
Add-ClusterFileServerRole -Storage "Cluster Disk 6" -Name cluster1FS12
```

这个示例使用“Cluster Disk 6”创建了一个集群文件服务器，并将其命名为“cluster1FS12”。

### 示例 3：创建一个集群文件服务器，无需等待资源分配

```powershell
Add-ClusterFileServerRole -Storage "Cluster Disk 8" -Wait 0
```

这个示例使用“Cluster Disk 8”创建了一个集群文件服务器，并为其分配了一个默认名称。该cmdlet在不需要等待所有资源都上线的情况下即可完成操作。

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

指定在运行该cmdlet时要忽略的一个或多个网络。启用DHCP的网络总是会被包含在内，但其他网络需要使用**StaticAddress**参数来指定静态地址，或者应该通过**IgnoreNetwork**参数明确地忽略它们。

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

指定用于创建高可用性文件服务器的集群。

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

指定要创建的高可用文件服务器的名称。

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

### -StaticAddress

指定一个或多个在运行该 cmdlet 时使用的静态地址。启用 DHCP 的网络总是会被包含在内，但其他网络需要通过 `StaticAddress` 参数来指定静态地址；或者可以使用 `IgnoreNetwork` 参数明确忽略这些网络。

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

指定要添加到新建的高可用文件服务器中的集群磁盘资源。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Wait

指定用于等待该cmdlet完成的时间（以秒为单位）。如果未指定**Wait**参数，则cmdlet会一直等待直到操作完成。如果指定的值为`0`，则命令会立即被执行，并且cmdlet会在不进行任何等待的情况下立即返回结果。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell Cluster

## 输出

### MicrosoftFailoverClusters.PowerShell ClusterGroup

## 备注

## 相关链接

[Add-ClusterScaleOutFileServerRole](./Add-ClusterScaleOutFileServerRole.md)

[Get-ClusterGroup](./Get-ClusterGroup.md)

[Move-ClusterGroup](./Move-ClusterGroup.md)

[Remove-ClusterGroup](./Remove-ClusterGroup.md)

[开始创建集群组](./Start-ClusterGroup.md)

[Stop-ClusterGroup](./Stop-ClusterGroup.md)
