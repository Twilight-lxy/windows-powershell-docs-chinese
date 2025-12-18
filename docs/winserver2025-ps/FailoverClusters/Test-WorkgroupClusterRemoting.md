---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.Adless.PowerShell.psm1-help.xml
Module Name: FailoverClusters
ms.date: 09/11/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusters/test-workgroupclusterremoting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-WorkgroupClusterRemoting
---

# 测试工作组集群远程连接功能

## 摘要
检查所有节点上是否都配置了远程连接功能（即是否可以远程操控这些节点）。

## 语法

```
Test-WorkgroupClusterRemoting [[-Node] <String[]>] [[-Credentials] <PSCredential[]>]
 [<CommonParameters>]
```

## 描述

`Test-WorkgroupClusterRemoting` 函数用于检测所有节点上是否配置了远程访问功能，并验证是否安装了 CredSSP（一种安全身份验证协议）。

## 示例

### 示例 1

```powershell
Test-WorkgroupClusterRemoting -Node "Node1", "Node2" -Credentials $cred1, $cred2
```

这个示例使用 `$cred1` 和 `$cred2` 中的凭据来检测 `Node1` 和 `Node2` 是否配置了远程连接功能。

## 参数

### -Node

一组用于测试远程连接的节点。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
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
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接

[添加工作组集群节点](add-workgroupclusternode.md)

[New-WorkgroupCluster](new-workgroupcluster.md)

[Remove-WorkgroupCluster](remove-workgroupcluster.md)

[Remove-WorkgroupClusterNode](remove-workgroupclusternode.md)

[Set-WorkgroupClusterRemotingConfiguration](set-workgroupclusterremotingconfiguration.md)

[测试-工作组集群](test-workgroupcluster.md)
