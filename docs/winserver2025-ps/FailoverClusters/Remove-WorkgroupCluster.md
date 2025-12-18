---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.Adless.PowerShell.psm1-help.xml
Module Name: FailoverClusters
ms.date: 09/11/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-workgroupcluster?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-WorkgroupCluster
---

# 移除工作组集群

## 摘要
删除一个工作组群集。

## 语法

```
Remove-WorkgroupCluster [[-Node] <String[]>] [[-Credentials] <PSCredential[]>] [-Force] [-Confirm]
 [-WhatIf] [<CommonParameters>]
```

## 描述

`Remove-WorkgroupCluster` cmdlet 用于删除一个工作组集群。

## 示例

### 示例 1

```powershell
Remove-WorkgroupCluster -Node "Node1", "Node2" -Credentials $cred1, $cred2
```

这个示例将集群从`Node1`和`Node2`中都移除。

如果与某个节点的通信中断，或者该节点的成员身份信息不完整，那么该集群可能不会被自动删除，此时可能需要手动进行清理操作。

## 参数

### -Node

一组节点构成了当前的集群。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: @()
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credentials

一组用于节点的身份凭证（credentials）。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
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
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接

[添加工作组集群节点](add-workgroupclusternode.md)

[新工作组集群](new-workgroupcluster.md)

[Remove-WorkgroupClusterNode](remove-workgroupclusternode.md)

[Set-WorkgroupClusterRemotingConfiguration](set-workgroupclusterremotingconfiguration.md)

[Test-WorkgroupCluster](test-workgroupcluster.md)

[Test-WorkgroupClusterRemoting](test-workgroupclusterremoting.md)
