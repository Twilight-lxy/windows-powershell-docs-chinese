---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-clusteraccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ClusterAccess
---

# 移除集群访问权限

## 摘要
将用户从集群的访问列表中移除。

## 语法

```
Remove-ClusterAccess [[-User] <StringCollection>] [-InputObject <PSObject>] [-Cluster <String>]
 [<CommonParameters>]
```

## 描述

`Remove-ClusterAccess` cmdlet 用于将用户从集群的访问列表中移除。即使执行了此 cmdlet，如果该用户账户属于另一个也在集群访问列表中的用户组，该用户可能仍然能够访问集群。

## 示例

### 示例 1

```powershell
Remove-ClusterAccess -User contoso\johnj99
```

这个示例会将 `contoso` 域中的用户 `johnj99` 从本地集群的访问列表中删除。不过，如果该用户属于其他被授予访问权限的用户组，那么他仍然可以访问该集群。

## 参数

### -Cluster

指定用于运行此 cmdlet 的集群名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 会在本地集群上运行。

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

指定要从哪个集群中移除给定用户的访问权限。

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

### -User

指定要取消集群访问权限的用户。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Block-ClusterAccess](./Block-ClusterAccess.md)

[获取集群访问权限](./Get-ClusterAccess.md)

[Grant-ClusterAccess](./Grant-ClusterAccess.md)
