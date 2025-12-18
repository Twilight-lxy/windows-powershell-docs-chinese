---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsNamespaceAccess.cdxml-help.xml
Module Name: DFSN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsn/remove-dfsnaccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DfsnAccess
---

# 移除对 DFSN 的访问权限

## 摘要
从DFS命名空间中的某个文件夹的ACL（访问控制列表）中移除用户和组。

## 语法

```
Remove-DfsnAccess [-Path] <String> [-AccountName] <String[]> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-DfsnAccess` cmdlet 用于从分布式文件系统（DFS）命名空间文件夹的访问控制列表（ACL）中删除用户和组。即使将用户从 ACL 中移除，ACL 中现有的权限仍可能允许该用户访问该文件夹。

有关DFS命名空间的更多信息，请参阅TechNet上的[DFS命名空间概述](https://technet.microsoft.com/library/cc730736)。

## 示例

### 示例 1：从文件夹的访问控制列表（ACL）中删除用户

```powershell
Remove-DfsnAccess -Path '\\Contoso\Software\Projects' -AccountName 'TSQA\PattiFuller'
```

此命令将用户 TSQA\PattiFuller 从 `\\Contoso\Software\Projects` 的访问控制列表中删除。

## 参数

### -AccountName

指定一个包含用户账户和组账户的数组。此cmdlet会从DFS命名空间文件夹的ACL中删除所指定的账户。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: Account, User

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob

将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `-*Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

指定一个DFS命名空间文件夹的路径。此cmdlet会从指定的文件夹的ACL中删除用户账户或组账户。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DfsPath, FolderPath, NamespacePath

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit

指定可以同时运行的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.String[]

## 输出

### System.Object

## 备注

## 相关链接

[Get-DfsnAccess](./Get-DfsnAccess.md)

[Grant-DfsnAccess](./Grant-DfsnAccess.md)

[Revoke-DfsnAccess](./Revoke-DfsnAccess.md)
