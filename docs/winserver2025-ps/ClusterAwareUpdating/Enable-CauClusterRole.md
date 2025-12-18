---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 09/27/2022
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/enable-cauclusterrole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-CauClusterRole
---

# 启用 CauClusterRole

## 摘要
重新启用指定集群上的自动更新功能。

## 语法

```
Enable-CauClusterRole [[-ClusterName] <String>] [-Credential <PSCredential>] [-Force] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Enable-CauClusterRole` cmdlet 会重新启用指定集群的自我更新功能。该集群的自我更新功能可以通过 `Disable-CauClusterRole` cmdlet 被禁用。

## 示例

### 示例 1：在指定的集群上启用 CAU 集群角色

```powershell
Enable-CauClusterRole -ClusterName "CONTOSO-FC1" -Force
```

此命令使 CONTOSO-FC1 集群上的 CAU 聚合角色开始执行更新操作。该 cmdlet 将 CAU 聚合角色的状态更改为 “Running”（正在运行）。由于该命令指定了 **Force** 参数，因此该 cmdlet 会直接运行而不会显示确认提示。

## 参数

### -ClusterName

指定要启用自更新功能的集群的名称。仅当此cmdlet不是在故障转移集群节点上运行，或者该cmdlet用于引用与执行该cmdlet的位置不同的故障转移集群时，才需要此参数。

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

### -Credential

指定目标集群的管理员凭据。

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

强制命令运行，而无需请求用户确认。

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

展示了如果该cmdlet运行会发生什么情况。不过实际上这个cmdlet并没有被执行。

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

### 无

## 输出

### 无

## 备注

## 相关链接

[Add-CauClusterRole](./Add-CauClusterRole.md)

[ Disable-CauClusterRole ](./Disable-CauClusterRole.md)

[Get-CauClusterRole](./Get-CauClusterRole.md)

[Remove-CauClusterRole](./Remove-CauClusterRole.md)

[Set-CauClusterRole](./Set-CauClusterRole.md)

