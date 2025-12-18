---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 09/27/2022
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/get-caurun?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-CauRun
---

# Get-CauRun

## 摘要
获取关于当前正在进行中的更新运行的状态信息。

## 语法

### DefaultParamSet（默认值）

```
Get-CauRun [[-ClusterName] <String>] [-Credential <PSCredential>] [<CommonParameters>]
```

### WaitForStart

```
Get-CauRun [[-ClusterName] <String>] [-Credential <PSCredential>] [-WaitForStart]
 [<CommonParameters>]
```

### WaitForCompletion

```
Get-CauRun [[-ClusterName] <String>] [-Credential <PSCredential>] [-WaitForCompletion]
 [<CommonParameters>]
```

### ShowClusterNodeState

```
Get-CauRun [[-ClusterName] <String>] [-Credential <PSCredential>] [-ShowClusterNodeState]
 [<CommonParameters>]
```

## 描述

`Get-CauRun` cmdlet 可以获取当前正在进行中的更新运行的状态信息。您可以使用此 cmdlet 来监控这些更新运行过程。

## 示例

### 示例 1：从指定的集群中获取有关正在进行中的更新运行的状态信息

```powershell
Get-CauRun -ClusterName "CONTOSO-FC1"
```

```output
RunId                   : 834dd11e-584b-41f2-8d22-4c9c0471dbad
RunStartTime            : 10/13/2011 1:35:39 PM
CurrentOrchestrator     : NODE1
NodeStatusNotifications : {
Node      : NODE1
Status    : Waiting
Timestamp : 10/13/2011 1:35:49 PM
}
NodeResults             : {
Node                     : NODE2
Status                   : Succeeded
ErrorRecordData          :
NumberOfSucceededUpdates : 0
NumberOfFailedUpdates    : 0
InstallResults           : Microsoft.ClusterAwareUpdating.UpdateInstallResult[]
}
```

该命令用于获取关于在名为CONTOSO-FC1的集群上当前正在进行的更新操作的状态信息。

## 参数

### -ClusterName

指定该 cmdlet 获取更新运行状态的集群名称。仅当此 cmdlet 不在故障转移集群节点上运行，或者用于引用与执行该 cmdlet 的位置不同的故障转移集群时，才需要这个参数。

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

### -ShowClusterNodeState

表示该 cmdlet 用于获取在每个集群节点上创建的 Windows 管理规范（WMI）对象的状态。这可以帮助调试遗留对象的问题（即那些未被正确删除或配置的对象）。

```yaml
Type: SwitchParameter
Parameter Sets: ShowClusterNodeState
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WaitForCompletion

表示该cmdlet会等待更新任务的完成。如果指定了此参数，cmdlet还会将更新的CAU任务对象写入输出流中，以便当前CAU更新协调器记录进度信息。

```yaml
Type: SwitchParameter
Parameter Sets: WaitForCompletion
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WaitForStart

表示此 cmdlet 会等待在指定集群上正在进行的更新操作完成；否则，该 cmdlet 会等待更新操作的开始。

```yaml
Type: SwitchParameter
Parameter Sets: WaitForStart
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft-cluster Aware-Updating.CauRun

### Microsoft-cluster Aware-Updating.RunState

## 备注

## 相关链接

[Invoke-CauRun](./Invoke-CauRun.md)

[Stop-CauRun](./Stop-CauRun.md)

