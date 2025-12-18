---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsNamespace.cdxml-help.xml
Module Name: DFSN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsn/get-dfsnroot?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsnRoot
---

# Get-DfsnRoot

## 摘要
获取DFS命名空间的设置信息。

## 语法

### 按域名分类（默认设置）

```
Get-DfsnRoot [[-Domain] <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByRoot

```
Get-DfsnRoot [[-Path] <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### 按服务器（ByServer）

```
Get-DfsnRoot [[-ComputerName] <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

## 描述

`Get-DfsnRoot` cmdlet 可以获取分布式文件系统（DFS）命名空间的配置设置。您可以使用独立的命名空间路径或基于域的命名空间路径来指定 DFS 命名空间，也可以通过服务器或域来进行指定。如果不传递任何参数使用该 cmdlet，它可以显示所有 DFS 命名空间的相关信息。您可以使用 `Set-DfsnRoot` cmdlet 来修改 DFS 的配置设置。

有关DFS命名空间的更多信息，请参阅TechNet上的[DFS命名空间概述](https://technet.microsoft.com/library/cc730736)。

## 示例

### 示例 1：获取 DFS 命名空间配置设置

```powershell
Get-DfsnRoot -Path '\\Contoso\AccountingResources' | Format-List
```

```Output
Path          : \\Contoso\AccountingResources
Description   :
Type          : Standalone
State         : Online
Flags         : Site Costing
TimeToLiveSec : 300
```

此命令用于获取路径为 `\\Contoso\AccountingResources` 的命名空间的配置设置。该命令使用 **Format-List** cmdlet 来格式化输出结果。有关此 cmdlet 的更多信息，请输入 `Get-Help Format-List`。

### 示例 2：获取某个域的所有深度优先搜索（DFS）命名空间

```powershell
Get-DfsnRoot -Domain 'Contoso.com'
```

这个命令可以获取所有托管在 Contoso.com 域名下的 DFS（分布式文件系统）命名空间。

## 参数

### -AsJob

以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的任务。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业的结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该cmdlet。输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -ComputerName

指定服务器的名称。此cmdlet会获取该服务器托管的所有DFS命名空间的配置设置。

```yaml
Type: System.String
Parameter Sets: ByServer
Aliases: Server

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Domain

指定一个域名。此cmdlet会获取所指定域名中DFS命名空间的配置设置。

```yaml
Type: System.String
Parameter Sets: ByDomain
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path

指定一个DFS命名空间的根文件夹路径。此cmdlet会获取具有该根路径的DFS命名空间的配置设置。

```yaml
Type: System.String
Parameter Sets: ByRoot
Aliases: RootPath, root, namespace, NamespaceRoot

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该命令的最佳限制值。此限制仅适用于当前执行的命令，而不影响整个会话或计算机本身。

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

### CommonParameters

此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft.ManagementInfrastructure.CimInstance[]

## 备注

## 相关链接

[New-DfsnRoot](./New-DfsnRoot.md)

[Remove-DfsnRoot](./Remove-DfsnRoot.md)

[Set-DfsnRoot](./Set-DfsnRoot.md)
