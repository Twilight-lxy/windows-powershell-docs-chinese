---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterCollection.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clustergroupsetdependency?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterGroupSetDependency
---

# 添加 ClusterGroupSet 的依赖关系

## 摘要
向集群集添加一个依赖项。

## 语法

### 查询（cdxml）（默认设置）

```
Add-ClusterGroupSetDependency [[-Name] <String[]>] [-Provider] <String>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

### InputObject (cdxml)

```
Add-ClusterGroupSetDependency -InputObject <CimInstance[]> [-Provider] <String>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

## 描述

`Add-ClusterGroupSetDependency` cmdlet 用于向集群集添加一个依赖关系。

## 示例

#### 示例 1：向提供程序集添加依赖项

```powershell
Add-ClusterGroupSetDependency -Name "Set001" -Provider "Provider002"
```

这条命令将名为 `Provider002` 的集合作为提供者添加到名为 `Set001` 的集合中。这两个集合都不能为空。

## 参数

### -AsJob

以后台作业的形式运行该cmdlet。使用此参数来执行需要很长时间才能完成的任务。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。请输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定在管道命令中使用的输入对象。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name

指定要添加依赖关系的组集名称（以数组形式）。

```yaml
Type: String[]
Parameter Sets: Query (cdxml)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru

返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不生成任何输出。

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

### -Provider

指定要添加为提供者的集合的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时执行的cmdlet操作的最大数量。如果省略此参数或输入值`0`，则Windows PowerShell会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最优限制值。此限制仅适用于当前运行的cmdlet，而不影响整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
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

## 输出

## 备注

## 相关链接

[Get-ClusterGroupSetDependency](./Get-ClusterGroupSetDependency.md)

[Remove-ClusterGroupSetDependency](./Remove-ClusterGroupSetDependency.md)
