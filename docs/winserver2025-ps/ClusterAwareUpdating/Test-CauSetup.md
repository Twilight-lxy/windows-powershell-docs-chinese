---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 09/27/2022
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/test-causetup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-CauSetup
---

# Test-CauSetup

## 摘要
用于测试集群是否已正确配置，以便使用CAU（Cluster Application Update）机制来应用软件更新。

## 语法

```
Test-CauSetup [[-ClusterName] <String>] [[-Credential] <PSCredential>] [<CommonParameters>]
```

## 描述

`Test-CauSetup` 这个 cmdlet 用于检测故障转移集群是否已正确配置为使用 Cluster-Aware Updating (CAU) 来应用软件更新。该 cmdlet 通过调用随 CAU 安装的 ClusterAwareUpdating BPA 模型，对故障转移集群和网络环境进行最佳实践分析（Best Practices Analyzer, BPA）扫描。要查看由 `Test-CauSetup` 执行的 BPA 扫描结果（包括可能存在的问题及解决方法），请运行 `Get-BpaResult` cmdlet。

你必须使用本地管理员凭据来运行 `Test-CauSetup` cmdlet。

## 示例

### 示例 1：测试指定的故障转移集群是否已设置为支持 CAU（Continuous Availability Update）

```powershell
Test-CauSetup -ClusterName "CONTOSO-FC1"
```

这个示例用于测试名为 CONTOSO-FC1 的故障转移集群是否已正确配置以支持 CAU（Content Access Unified）。

## 参数

### -ClusterName

指定用于测试是否设置正确的集群名称。只有当此 cmdlet 不在故障转移集群节点上运行，或者用于引用与执行该 cmdlet 的位置不同的故障转移集群时，才需要这个参数。

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

### -Credential

指定目标集群的管理凭据。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft_clusterAwareUpdating.CauBpaProgress

## 备注

## 相关链接

