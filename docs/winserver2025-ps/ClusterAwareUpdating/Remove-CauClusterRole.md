---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 09/27/2022
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/remove-cauclusterrole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-CauClusterRole
---

# 删除CauClusterRole

## 摘要
从指定的故障转移集群中移除CAU集群角色。

## 语法

```
Remove-CauClusterRole [[-ClusterName] <String>] [[-Credential] <PSCredential>] [-Force] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-CauClusterRole` cmdlet 用于从指定的故障转移集群中删除“集群感知更新”（Cluster-Aware Updating，简称 CAU）集群角色。要从某个集群中运行 CAU 功能，请确保该集群已配置了相应的 CAU 集群角色。

`Remove-CauClusterRole` cmdlet 会从 Active Directory 中删除与 CAU 集群角色相关的虚拟计算机对象（VCO），除非您之前使用 `Add-CauClusterRole` cmdlet 并通过 `VirtualComputerObjectName` 参数预先配置或指定了该 VCO。

## 示例

### 示例 1：删除在指定集群上配置的 CAU 集群角色的实例

```powershell
Remove-CauClusterRole -ClusterName "CONTOSO-FC1" -Force
```

此命令会删除在名为CONTOSO-FC1的集群上配置的CAU集群角色的实例。由于该命令指定了“Force”参数，因此该cmdlet会在不显示确认提示的情况下直接运行。

## 参数

### -ClusterName

指定要从其中删除 CAU 集成角色的集群的名称。仅当此 cmdlet 不在故障转移集群节点上运行，或者用于引用与执行该 cmdlet 的位置不同的故障转移集群时，才需要此参数。

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
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令执行，而无需请求用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: f

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Add-CauClusterRole](./Add-CauClusterRole.md)

[ Disable-CauClusterRole](./Disable-CauClusterRole.md)

[Enable-CauClusterRole](./Enable-CauClusterRole.md)

[Get-CauClusterRole](./Get-CauClusterRole.md)

[Set-CauClusterRole](./Set-CauClusterRole.md)

