---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.Adless.PowerShell.psm1-help.xml
Module Name: FailoverClusters
ms.date: 09/11/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-workgroupclusternode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-WorkgroupClusterNode
---

# 添加工作组集群节点

## 摘要
向工作组集群中添加一个节点。

## 语法

```
Add-WorkgroupClusterNode [-Node] <String[]> [-Credentials] <PSCredential[]> [-Name] <String>
 [-Credential] <PSCredential> [-NoStorage] [-Confirm] [-WhatIf] [<CommonParameters>]
```

## 描述

`Add-WorkgroupClusterNode` cmdlet 用于将一个节点添加到工作组集群中。

## 示例

### 示例 1

```powershell
$params = @{
    Node = @("Node1", "Node2")
    Credentials = @($cred1, $cred2)
    Name = "Node3"
    Credential = $cred3
}
Add-WorkgroupClusterNode @params
```

这个示例将 `Node3` 添加到由 `Node1` 和 `Node2` 组成的集群中。

## 参数

### -Node

一个需要添加到集群中的节点数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credentials

一组用于节点的身份凭证（credentials）。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

要添加的节点的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential

要添加的节点所需的凭据。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: True
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoStorage

指定工作组集群节点将忽略共享存储。

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

展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接

[新工作群组集群](new-workgroupcluster.md)

[Remove-WorkgroupCluster](remove-workgroupcluster.md)

[Remove-WorkgroupClusterNode](remove-workgroupclusternode.md)

[Set-WorkgroupClusterRemotingConfiguration](set-workgroupclusterremotingconfiguration.md)

[测试-工作组集群](test-workgroupcluster.md)

[Test-WorkgroupClusterRemoting](test-workgroupclusterremoting.md)
