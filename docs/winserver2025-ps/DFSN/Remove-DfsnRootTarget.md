---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsNamespaceRootTarget.cdxml-help.xml
Module Name: DFSN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsn/remove-dfsnroottarget?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DfsnRootTarget
---

# 移除 DfsnRoot 目标

## 摘要
删除DFS命名空间根的目标（即与该根相关的所有目标）。

## 语法

```
Remove-DfsnRootTarget [-Path <String>] [-TargetPath] <String> [-Cleanup]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Remove-DfsnRootTarget` cmdlet 用于删除分布式文件系统（DFS）命名空间根的目标对象。该 cmdlet 会删除目标对象本身，但不会删除目标对象中的内容。

一个 DFS 命名空间根可以有多个根目标。如果您删除了与某个 DFS 命名空间根关联的最后一个根目标，此 cmdlet 也会同时删除该命名空间。在删除命名空间后，用户将无法再使用该命名空间的路径。

有关DFS命名空间的更多信息，请参阅TechNet上的[DFS命名空间概述](https://technet.microsoft.com/library/cc730736)。

## 示例

#### 示例 1：移除根目标（root target）

```powershell
Remove-DfsnRootTarget -TargetPath '\\Contoso-FS\AccountingSoftware' -Path '\\Contoso\AccountingSoftware'
```

此命令会从名为 `\\Contoso\AccountingSoftware` 的 DFS 命名空间中，删除 DFS 根目标路径 `\\Contoso-FS\AccountingSoftware`。

## 参数

### -AsJob

将该 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中操作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession

在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: Microsoft.Management.Infrastructure.CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Cleanup

表示该cmdlet尝试强制清理Active Directory域服务（AD DS）中的根目标对象。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm

在运行该cmdlet之前，系统会提示您确认操作。默认值为**True**（即需要确认）。如果您不想确认该操作，则必须使用带有**False**值的开关，如下例所示：`-Confirm:$false`

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: True
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

指定DFS命名空间根目录的路径。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DfsPath, NamespaceRoot

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetPath

指定根目标的路径。此cmdlet会删除具有所指定路径的根目标。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Target, DfsTarget, RootTargetPath

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时执行的cmdlet操作的最大数量。如果省略此参数或输入值为`0`，那么Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前执行的cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果该cmdlet运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Get-DfsnRootTarget](./Get-DfsnRootTarget.md)

[New-DfsnRootTarget](./New-DfsnRootTarget.md)

[Set-DfsnRootTarget](./Set-DfsnRootTarget.md)
