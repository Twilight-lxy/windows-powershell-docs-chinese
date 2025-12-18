---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-clustergroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ClusterGroup
---

# 移除 ClusterGroup

## 摘要
从一个故障转移集群中移除一个集群角色（也称为资源组）。

## 语法

```
Remove-ClusterGroup [-VMId <Guid>] [[-Name] <StringCollection>] [-Force] [-RemoveResources]
 [-InputObject <PSObject>] [-Cluster <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-ClusterGroup` cmdlet 用于从故障转移集群中删除一个集群角色（也称为资源组）。

使用此cmdlet来删除一个组。如果该组中仍包含资源，请先移除这些资源，或者指定**RemoveResources**参数。

## 示例

### 示例 1

```powershell
Remove-ClusterGroup -Name MyFileServer
```

这个示例会先提示用户进行确认，然后删除名为`MyFileServer`的集群角色。不过，在执行删除操作之前，系统会先从该集群角色中移除相关资源。

### 示例 2

```powershell
Remove-ClusterGroup -Name MyFileServer -Force
```

这个示例会删除名为`MyFileServer`的集群角色，但前提是首先需要从该集群角色中移除相关资源。此cmdlet不会提示用户进行确认操作。

### 示例 3

```powershell
Remove-ClusterGroup -Name MyFileServer -Force -RemoveResources
```

这个示例会删除名为 `MyFileServer` 的集群角色，而不会提示用户进行确认。`MyFileServer` 中的所有集群资源都将被删除。

## 参数

### -Cluster

指定用于运行此 cmdlet 的集群名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

直接执行该cmdlet，而不会提示用户确认。默认情况下，该cmdlet在执行程序之前会请求用户的确认。

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

指定要移除的集群角色。

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

指定要删除的集群角色的名称。

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

### -RemoveResources

该操作会导致 cmdlet 在删除集群角色之前，先删除该集群角色中的所有资源。

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

### -VMId

指定虚拟机标识符（ID）。

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

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell ClusterGroup

## 输出

### 无

## 备注

## 相关链接

[添加集群组](./Add-ClusterGroup.md)

[Get-ClusterGroup](./Get-ClusterGroup.md)

[Move-ClusterGroup](./Move-ClusterGroup.md)

[开始创建集群组](./Start-ClusterGroup.md)

[停止集群组](./Stop-ClusterGroup.md)
