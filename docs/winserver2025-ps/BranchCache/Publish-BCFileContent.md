---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BranchCacheOrchestrator.cdxml-help.xml
Module Name: BranchCache
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/branchcache/publish-bcfilecontent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Publish-BCFileContent
---

# 发布 BC 文件内容

## 摘要
为共享文件夹中的文件生成哈希值。

## 语法

```
Publish-BCFileContent [-Path] <String[]> [-UseVersion <UInt32>] [-StageData] [-StagingPath <String>]
 [-ReferenceFile <String>] [-Force] [-Recurse] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Publish-BCFileContent** cmdlet 会为文件服务器上共享文件夹中的文件生成哈希值（也称为内容信息），这些文件已启用 BranchCache 功能，并且安装了 BranchCache for Network Files 角色服务。

此cmdlet还用于准备数据，以便创建数据预加载包。可以使用带有*StageData*参数的此cmdlet对一个或多个文件集合进行处理。然后运行**Export-BCCachePackage** cmdlet来生成包含所有已处理数据的数据包。您可以将该数据包导入到远程托管的缓存计算机上。

## 示例

### 示例 1：对文件夹的内容进行哈希处理以便导出
```
PS C:\> Publish-BCFileContent -Path "D:\share" -StageData
```

此命令会对 D:\share 目录中的内容进行哈希处理，并将生成的数据添加到一个缓存包中。该缓存包之后可以导出并发送到远程的托管缓存服务器上。

## 参数

### -AsJob
以后台作业的形式运行该 cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，也可以输入会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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
强制命令运行，而无需请求用户确认。

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

### -Path
指定包含该 cmdlet 需要哈希处理的文件的文件路径或文件夹路径。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Recurse
表示将为子文件夹中的内容生成哈希值。如果您不指定此参数，该cmdlet将仅为顶层文件夹中的内容生成哈希值。

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

### -ReferenceFile
指定一个来自之前运行的参考文件。该参考文件包含一组标识符，用于描述数据包中的数据。如果指定了参考文件，此 cmdlet 会将该文件中描述的所有数据从输出结果中排除。你可以使用参考文件来创建仅包含自上次生成数据包以来发生更改的数据包。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StageData
表示此cmdlet会将数据保存到一个临时区域，以便将来使用**Export-BCCachePackage** cmdlet进行导出。如果您不指定此参数，则系统会为数据生成哈希值，但数据本身不会被准备用于导出。

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

### -StagingPath
指定一个临时文件夹，用于保存此cmdlet阶段处理的数据。如果没有指定位置，该cmdlet将使用本地硬盘上的默认位置。如果正在创建一个较大的数据包，并且需要将该数据包存储在单独的硬盘上，请使用此参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时进行的操作的最大数量，以便运行相应的 Cmdlet。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM Cmdlet 的数量来计算该 Cmdlet 的最佳限制值。这个限制仅适用于当前的 Cmdlet，而不适用于整个会话或计算机本身。

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

### -UseVersion
指定要使用的 BranchCache 哈希方案版本。如果指定的版本是 1，则内容信息将按照 Windows 7 客户端所使用的方案生成；如果指定的版本是 2，则内容信息将按照运行较新操作系统（晚于 Windows® 7）的客户端计算机所使用的更高效的哈希方案生成。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Export-BCCachePackage](./Export-BCCachePackage.md)

