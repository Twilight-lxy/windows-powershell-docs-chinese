---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/write-dfsrhealthreport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Write-DfsrHealthReport
---

# 编写DFSR健康报告

## 摘要
生成一份深度优先（DFS）复制健康状态报告。

## 语法

```
Write-DfsrHealthReport [-GroupName] <String[]> [[-ReferenceComputerName] <String>]
 [[-MemberComputerName] <String[]>] [[-Path] <String>] [-CountFiles] [[-DomainName] <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Write-DfsrHealthReport` cmdlet 为两个或多个服务器生成分布式文件系统（DFS）复制状态的健康报告或诊断报告。该健康报告包含有关复制状态、效率以及任何潜在复制问题的管理信息。

该cmdlet会将报告生成为HTML文件，并附带一个XML文件。

## 示例

### 示例 1：生成一份包含文件数量的健康报告
```
PS C:\> Write-DfsrHealthReport -GroupName "RG01" -ReferenceComputerName "SRV01" -MemberComputerName "SRV02" -Path "C:\reports" -CountFiles
```

该命令为复制组RG01和参考计算机SRV01生成一份报告。

### 示例 2：生成一份健康报告
```
PS C:\> Write-DfsrHealthReport -GroupName "RG01" -ReferenceComputerName "SRV01" -Verbose
VERBOSE: Performing operation "Write-DfsrHealthReport" on Target "RG01".
VERBOSE: Successfully saved the health report for the replication group named "RG01". The XML file is located here: "C:\Health-RG01-04Apr2013-2022.xml". The HTML file is located here: "C:\Health-RG01-04Apr2013-2022.html".
```

该命令为RG01复制组生成一份健康报告，其中基准服务器为SRV01，复制组中的其他所有服务器也包含在内。报告会被写入C:\文件夹中。

## 参数

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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

### -CountFiles
该cmdlet用于统计复制内容文件夹中存在的文件数量。默认情况下，为了在生成报告时节省时间，该cmdlet不会计算文件的数量。

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

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果未指定此参数，该 cmdlet 将使用用户的当前域。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 100
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GroupName
用于指定复制组名称的数组。如果不指定此参数，该 cmdlet 会查询所有参与的复制组。您可以使用逗号分隔的列表以及通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RG, RgName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### -MemberComputerName
指定一个DFS复制成员数组，以便与由*ReferenceComputerName*参数指定的服务器进行比较分析。如果您没有指定此参数，该cmdlet将包含复制组中的所有成员。您可以指定多个计算机名称（用逗号分隔），也可以使用通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: MemberList, MemList

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path
指定报告文件的文件夹路径。如果未指定此参数，cmdlet 将使用当前的工作目录。

该cmdlet以“Health-\<复制组名称\>-\<日期\>-\<时间\>”的格式为每个报告命名，并生成带有HTML和XML扩展名的文件。

```yaml
Type: String
Parameter Sets: (All)
Aliases: FilePath

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReferenceComputerName
指定复制组中参考计算机的名称。来自该服务器的复制延迟数据（replication backlog）会与 *MemberComputerName* 参数中指定的所有其他成员进行比较。如果您不指定此参数，该cmdlet将使用本地计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ReferenceMember, RefMem

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

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

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 输出

### 无

## 备注

## 相关链接

