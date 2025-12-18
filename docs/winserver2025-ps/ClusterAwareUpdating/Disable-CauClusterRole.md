---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 09/27/2022
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/disable-cauclusterrole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-CauClusterRole
---

# 禁用 CauClusterRole

## 摘要
暂停指定集群上的自动更新功能。

## 语法

```
Disable-CauClusterRole [[-ClusterName] <String>] [-Credential <PSCredential>] [-Force] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Disable-CauClusterRole` cmdlet 会暂停指定集群的自动更新功能。该功能的重新启用可以通过 `Enable-CauClusterRole` cmdlet 来实现。

## 示例

### 示例 1：在指定的集群上禁用一个 CAU 集群角色

```powershell
Disable-CauClusterRole -ClusterName CONTOSO-FC1 -Force
```

此命令可防止位于 CONTOSO-FC1 集群上的 CAU 集群角色执行更新操作。该cmdlet会将 CAU 集群角色的状态更改为“离线”（Offline）。由于该命令指定了 **Force** 参数，因此在执行过程中不会显示确认提示。

## 参数

### -ClusterName

指定要禁用自更新功能的集群名称。仅当此 cmdlet 不在故障转移集群节点上运行，或者用于引用与执行该 cmdlet 的位置不同的故障转移集群时，才需要此参数。

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

### -Confirm

在运行该 cmdlet 之前，会提示您进行确认。

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

### -Force

强制命令运行，而不需要用户确认。

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

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被运行。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Enable-CauClusterRole](./Enable-CauClusterRole.md)

[Get-CauClusterRole](./Get-CauClusterRole.md)

[Remove-CauClusterRole](./Remove-CauClusterRole.md)

[Set-CauClusterRole](./Set-CauClusterRole.md)

