---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsNamespaceFolder.cdxml-help.xml
Module Name: DFSN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsn/move-dfsnfolder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Move-DfsnFolder
---

# 移动 DFSN 文件夹

## 摘要
移动或重命名DFS命名空间文件夹。

## 语法

```
Move-DfsnFolder [-Path] <String> [-NewPath] <String> [-Force] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Move-DfsnFolder` cmdlet 用于移动或重命名分布式文件系统（DFS）的命名空间文件夹。

有关DFS命名空间的更多信息，请参阅TechNet上的[DFS命名空间概述](https://technet.microsoft.com/library/cc730736)。

## 示例

#### 示例 1：移动一个文件夹

```powershell
Move-DfsnFolder -Path '\\Contoso\Western\Development\DesignDocuments' -NewPath '\\Contoso\Western\HumanResources\DesignDocuments'
```

这个命令会将“DesignDocuments”文件夹移动到“\\Contoso\Western\HumanResources”位置。执行此命令后，“\\Contoso\Western\Development\DesignDocuments”文件夹将不再存在。

### 示例 2：重命名文件夹

```powershell
Move-DfsnFolder -Path '\\Contoso\AccountingSoftware\Software' -NewPath '\\Contoso\AccountingSoftware\LegacySoftware'
```

这个命令会将位于 `\\Contoso\AccountingSoftware` 文件夹中的 `Software` 文件夹重命名为 `\\Contoso\AccountingSoftware\LegacySoftware`。

## 参数

### -AsJob

以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的任务。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

在运行该 cmdlet 之前，会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

会直接移动或重命名DFS命名空间文件夹，而不会提示您进行确认。默认情况下，该cmdlet在执行操作之前会先询问您的确认。

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

### -NewPath

指定 DFS 命名空间文件夹的路径。此 cmdlet 会将该文件夹移动或重命名为指定的路径。请勿指定现有的 DFS 命名空间文件夹。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: NewDfsPath, NewNamespacePath

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path

指定DFS命名空间文件夹的路径。此cmdlet会移动或重命名具有指定路径的文件夹。

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

指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值（即并发操作的最大数量）。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

[Get-DfsnFolder](./Get-DfsnFolder.md)

[New-DfsnFolder](./New-DfsnFolder.md)

[Remove-DfsnFolder](./Remove-DfsnFolder.md)

[Set-DfsnFolder](./Set-DfsnFolder.md)
