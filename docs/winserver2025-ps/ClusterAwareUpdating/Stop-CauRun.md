---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 09/27/2022
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/stop-caurun?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-CauRun
---

# 停止 CauRun

## 摘要
停止集群上正在进行的更新操作。

## 语法

```
Stop-CauRun [[-ClusterName] <String>] [-Credential <PSCredential>] [-Wait] [-Force]
 [<CommonParameters>]
```

## 描述

`Stop-CauRun` cmdlet 用于停止在故障转移集群上正在进行的更新操作。

## 示例

#### 示例 1：停止在指定集群上进行的更新操作

```
Stop-CauRun -ClusterName "CONTOSO-FC1" -Wait -Force
```

此命令会停止由配置在名为 CONTOSO-FC1 的集群上的 CAU Update Coordinator 执行的更新操作。该 cmdlet 会一直等待，直到被取消的更新操作完成为止。由于该命令指定了 **Force** 参数，因此它在执行时不会显示任何确认提示。

## 参数

### -ClusterName

指定要停止正在进行的更新操作的集群名称。仅当此cmdlet不在故障转移集群节点上运行，或者用于引用与执行该cmdlet的集群不同的故障转移集群时，才需要此参数。

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
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令运行，而无需询问用户的确认。

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

### -Wait

表示该cmdlet会一直等待，直到被取消的更新操作完成为止。否则，一旦当前集群感知更新（Cluster-Aware Updating, CAU）更新协调器接收到停止请求，它就会立即返回结果。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System Boolean

## 备注

## 相关链接

[Get-CauRun](./Get-CauRun.md)

[Invoke-CauRun](./Invoke-CauRun.md)

