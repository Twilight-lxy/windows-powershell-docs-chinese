---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clusterdisk?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterDisk
---

# 添加集群磁盘

## 摘要
为故障转移集群创建一个可用的新磁盘。

## 语法

```
Add-ClusterDisk [-InputObject] <PSObject[]> [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterDisk` cmdlet 可用于创建一个新的磁盘，以便在故障转移集群中使用。该磁盘（LUN）必须能够被故障转移集群中的所有节点访问，同时不应被其他任何服务器访问。

在添加磁盘时，请确保存储配置允许操作系统根据需要识别并挂载该磁盘。该磁盘必须是基本磁盘（而非动态磁盘），并且不应暴露给集群外的服务器。《Get-ClusterAvailableDisk》命令可用于获取可添加到集群中的磁盘的相关信息。

## 示例

### 示例 1：将可用磁盘添加到“可用存储”组中

```powershell
Get-ClusterAvailableDisk | Add-ClusterDisk
```

这个示例会识别出那些可以添加到集群中的磁盘，然后将它们加入到“可用存储”（Available Storage）集群组中。

### 示例 2：将某个可用的磁盘添加到可用存储资源中

```powershell
Get-ClusterAvailableDisk | Where-Object -FilterScript { $_.ScsiAddress -Eq 50331651 } | Add-ClusterDisk
```

这个示例会检查那些可以添加到集群中的磁盘，找到具有特定SCSI地址的磁盘，并将其添加到“可用存储”（Available Storage）集群组中。

### 示例 3：对物理磁盘进行聚类

```powershell
Get-Disk -Number 11 | Add-ClusterDisk
```

这个示例用于将一个物理磁盘加入集群。该cmdlet会将这个物理磁盘添加到集群的“可用存储”（_Available Storage_）中。

## 参数

### -Cluster

指定要运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

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

指定要添加到集群中的共享磁盘列表。该磁盘列表是通过 `Get-ClusterAvailableDisk` cmdlet 生成的。

```yaml
Type: PSObject[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FAILoverClusters.PowerShell.ClusterDiskInfo

### Microsoft.ManagementInfrastructure.CimInstance

这个对象是由 `Get-Disk` 和 `Get-VirtualDisk` 这两个 cmdlet 生成的。

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/Microsoft/Windows/Storage/MSFT_Disk

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/Microsoft/Windows/Storage/MSFT_VirtualDisk

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### MicrosoftFailoverClusters.PowerShell ClusterResource

## 备注

## 相关链接

[Get-ClusterAvailableDisk](./Get-ClusterAvailableDisk.md)

[测试集群](./Test-Cluster.md)

[Get-Disk](../storage/Get-Disk.md)

[Get-VirtualDisk](../storage/Get-VirtualDisk.md)
