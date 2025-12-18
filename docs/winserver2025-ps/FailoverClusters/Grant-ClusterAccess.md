---
description: 利用这篇文章来帮助您使用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 05/17/2023
online version: https://learn.microsoft.com/powershell/module/failoverclusters/grant-clusteraccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Grant-ClusterAccess
---

# 授予集群访问权限

## 摘要
授予对故障转移集群的访问权限，可以是完全访问权限，也可以是只读访问权限。

## 语法

```
Grant-ClusterAccess [-User] <StringCollection> [-Full] [-ReadOnly] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Grant-ClusterAccess` cmdlet 可以授予对故障转移集群的访问权限，包括完全访问权或仅读访问权。若要为某人提供仅读访问权限，请使用 **ReadOnly** 参数。授予集群完全访问权限等同于同时授予该集群中每个节点的完全访问权限。

## 示例

### 示例 1

```powershell
Grant-ClusterAccess -User contoso\johnj99 -Full
```

这个示例为位于 `contoso` 域中的用户 `johnj99` 授予了对本地集群的完全访问权限。

### 示例 2

```powershell
Grant-ClusterAccess -User contoso\johnj99 -ReadOnly
```

这个示例为属于“contoso”域的“johnj99”用户授予了对本地集群的只读访问权限。

## 参数

### -Cluster

指定用于运行此cmdlet的集群名称。如果该参数的输入为`.`或被省略，则cmdlet将在本地集群上运行。

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

### -Full

指定用户具有对整个集群的完全访问权限。如果没有指定访问级别，则用户仅具有只读权限。

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

指定要授予给该用户访问权限的集群。

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

### -ReadOnly

指定用户具有只读集群访问权限。如果没有指定访问级别，则用户将获得只读集群访问权限。

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

### -User

指定要授予集群访问权限的用户。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell_cluster

## 输出

### 无

## 备注

## 相关链接

[Block-ClusterAccess](./Block-ClusterAccess.md)

[Get-ClusterAccess](./Get-ClusterAccess.md)

[Remove-ClusterAccess](./Remove-ClusterAccess.md)
