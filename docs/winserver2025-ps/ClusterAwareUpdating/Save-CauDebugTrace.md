---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 07/01/2024
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/save-caudebugtrace?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Save-CauDebugTrace
---

# 保存调试跟踪信息

## 摘要
将中央自动化单元（CAU）的调试跟踪信息保存到本地ZIP文件中。

## 语法

```
Save-CauDebugTrace [[-ClusterName] <String>] [[-FilePath] <String>] [-Credential <PSCredential>]
 [-RunId <Guid>] [-Force] [-FeatureUpdateLogs {None | FailedSetup | All}] [<CommonParameters>]
```

## 描述

`Save-CauDebugTrace` cmdlet 将集群感知更新（Cluster-Aware Updating, CAU）的调试跟踪信息保存到本地的 ZIP 文件中。这些跟踪信息主要用于开发人员和支持工程师的使用。请使用 `FilePath` 参数指定文件名称。

要运行此cmdlet，必须在每个节点上启用Windows PowerShell远程功能。为此，请运行`Enable-PSRemoting` cmdlet。此外，还需确保在每个节点上启用了**Windows远程管理 - 兼容模式（HTTP-In）**防火墙例外设置。

## 示例

#### 示例 1：为指定的集群保存调试跟踪信息

```powershell
Save-CauDebugTrace -ClusterName "CONTOSO-FC1" -FilePath "C:\temp\testrun.zip"
```

该命令将名为**CONTOSO-FC1**的集群的调试跟踪信息保存到位于`C:\temp`文件夹中的`testrun.zip`文件中。

## 参数

### -ClusterName

指定用于收集CAU调试跟踪信息的集群名称。仅当此cmdlet不在故障转移集群节点上运行，或者该cmdlet用于引用与运行位置不同的故障转移集群时，才需要这个参数。

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

### -FeatureUpdateLogs

指定在功能更新的调试跟踪中应包含的详细信息级别。该参数的可接受值为：

- `None`: No feature update logs will be included in the debug trace.
- `FailedSetup`: Only logs related to failed feature updates will be included in the debug trace.
- `All`: All feature update logs will be included in the debug trace.

```yaml
Type: FeatureUpdateLogs
Parameter Sets: (All)
Aliases:
Accepted values: None, FailedSetup, All

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FilePath

指定用于保存跟踪信息的文件的名称，例如 `MyTrace.zip`。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Path

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令运行，而不会询问用户是否确认。

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

### -RunId

表示该cmdlet应仅包含与具有指定Run ID的更新运行相关的调试跟踪文件。

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### Microsoft-cluster Aware-UpdatingActivityIdMap

### System.IO.FileInfo

## 备注

## 相关链接

[Invoke-CauRun](invoke-caurun.md)
