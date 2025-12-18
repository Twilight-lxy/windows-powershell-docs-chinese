---
description: 使用此主题来帮助您使用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-cluster?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-Cluster
---

# 移除集群

## 摘要
删除一个现有的故障转移集群。

## 语法

```
Remove-Cluster [[-Cluster] <String>] [-CleanupAD] [-Force] [-InputObject <PSObject>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-Cluster` cmdlet 用于销毁现有的故障转移集群。受影响的服务器将不再作为一个集群一起运行。

此 cmdlet 会删除所有集群节点上的所有集群配置数据库副本。

注意：如果没有服务器计算机上的凭据安全服务提供程序（CredSSP）进行身份验证，此cmdlet无法远程运行。

## 示例

### 示例 1

```powershell
Remove-Cluster
```

这个示例会先提示用户进行确认，随后销毁本地的故障转移集群，并从集群节点中删除相应的集群配置信息。

### 示例 2

```powershell
Remove-Cluster -Force
```

这个示例会销毁本地的故障转移集群，并从集群节点中删除集群配置信息。该cmdlet不会提示用户进行确认操作。

### 示例 3

```powershell
Get-Cluster -Name Cluster1 | Remove-Cluster -Force -CleanupAD
```

这个示例会销毁名为 `Cluster1` 的集群，从集群节点中删除集群配置信息，并在 Active Directory 中删除相关集群对象。该命令行工具（cmdlet）不会提示用户进行确认操作。

## 参数

### -CleanupAD

该规定指出：当集群被销毁时，与集群关联的Active Directory中的对象也将被删除。

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

### -Cluster

指定用于运行此 cmdlet 的集群名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

在运行 cmdlet 之前，会提示您进行确认。

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

该cmdlet会直接执行操作，而不会提示用户确认是否继续。默认情况下，该cmdlet会在执行前询问用户的确认意见。

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

指定要销毁的集群。

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

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

### Microsoft FailoverClusters.PowerShell Cluster

## 输出

### 无

## 备注

## 相关链接

[Get-Cluster](./Get-Cluster.md)

[新建集群](./New-Cluster.md)

[启动集群](./Start-Cluster.md)

[停止集群](./Stop-Cluster.md)

[测试集群](./Test-Cluster.md)
