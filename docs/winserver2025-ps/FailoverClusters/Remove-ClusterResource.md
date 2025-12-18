---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-clusterresource?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ClusterResource
---

# 移除集群资源

## 摘要
从故障转移集群中移除一个已聚类的资源。

## 语法

```
Remove-ClusterResource [[-Name] <StringCollection>] [-Force] [-InputObject <PSObject>]
 [-Cluster <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-ClusterResource` cmdlet 用于将集群资源从故障转移集群中删除。在删除某个资源之前，请务必检查是否有其他资源依赖于该资源。

## 示例

### 示例 1

```powershell
Remove-ClusterResource -Name "Cluster Disk 4"
```

这个示例会提示用户进行确认，然后从本地集群中删除名为“Cluster Disk 4”的集群。

### 示例 2

```powershell
Remove-ClusterResource -Name "Cluster Disk 5" -Force
```

这个示例会从本地集群中删除名为“Cluster Disk 5”的集群，而不会提示用户进行确认。

## 参数

### -Cluster

指定要运行此 cmdlet 的集群的名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

直接运行该cmdlet，而不会提示用户进行确认。默认情况下，该cmdlet在执行前会先询问用户的确认意见。

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

指定要删除的集群资源。

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

指定要删除的集群资源的名称。

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

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShellClusterResource

## 输出

### 无

## 备注

## 相关链接

[Add-ClusterResource](./Add-ClusterResource.md)

[Get-ClusterResource](./Get-ClusterResource.md)

[Move-ClusterResource](./Move-ClusterResource.md)

[ Resume-ClusterResource](./Resume-ClusterResource.md)

[开始创建集群资源](./Start-ClusterResource.md)

[Stop-ClusterResource](./Stop-ClusterResource.md)

[暂停集群资源](./Suspend-ClusterResource.md)
