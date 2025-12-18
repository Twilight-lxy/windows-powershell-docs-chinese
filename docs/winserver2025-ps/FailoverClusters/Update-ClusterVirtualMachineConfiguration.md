---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/23/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/update-clustervirtualmachineconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-ClusterVirtualMachineConfiguration
---

# 更新集群虚拟机配置

## 摘要
刷新故障转移集群中集群虚拟机的配置。

## 语法

```
Update-ClusterVirtualMachineConfiguration [[-Name] <String>] [-VMId <Guid>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Update-ClusterVirtualMachineConfiguration` 这个 cmdlet 用于更新故障转移集群中集群化虚拟机的配置。当需要添加或删除某个硬件设备（例如网络适配器），或者需要更改该集群化虚拟机的硬件配置设置（例如虚拟内存设置）时，可以使用此 cmdlet。

## 示例

### 示例 1：刷新本地集群中的集群化虚拟机

```powershell
Update-ClusterVirtualMachineConfiguration -Name "Virtual Machine Configuration VM1"
```

这个示例会刷新本地集群中名为“Virtual Machine Configuration VM1”的集群化虚拟机。

### 示例 2：刷新集群中的虚拟机

```powershell
$parameters = @{
    Name = 'Virtual Machine Configuration VM2'
    Cluster = 'cluster1'
}
Update-ClusterVirtualMachineConfiguration @parameters
```

这个示例会刷新名为 `Virtual Machine Configuration VM2` 的集群虚拟机，该虚拟机位于名为 `cluster1` 的集群中。示例使用了 “Splatting” 技术，将参数值从 `$Parameters` 变量传递给相应的命令。有关 [Splatting](/powershell/module/microsoft.powershell.core/about/about_splatting) 的更多信息，请参阅相关文档。

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

指定要更新的集群化虚拟机资源。

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

指定要更新的集群化虚拟机资源的名称。

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

### -VMId

指定虚拟机的标识符（ID）。

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters.PowerShellClusterResource

## 输出

### Microsoft FailoverClusters.PowerShellClusterResource

## 备注

## 相关链接

[Add-ClusterVirtualMachineRole](./Add-ClusterVirtualMachineRole.md)

[Move-ClusterVirtualMachineRole](./Move-ClusterVirtualMachineRole.md)
