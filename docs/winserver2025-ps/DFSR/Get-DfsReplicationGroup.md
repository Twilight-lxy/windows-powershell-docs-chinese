---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsreplicationgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsReplicationGroup
---

# Get-DfsReplicationGroup

## 摘要
检索一个复制组。

## 语法

```
Get-DfsReplicationGroup [[-GroupName] <String[]>] [-IncludeSysvol] [[-DomainName] <String>]
 [<CommonParameters>]
```

## 描述
`Get-DfsReplicationGroup` cmdlet 用于检索现有的复制组。

复制组是一组服务器或成员，它们共同参与一个或多个文件夹的复制过程。被复制的文件夹会在复制组的各个成员之间保持同步状态。分布式文件系统（DFS）中的“Replication Get-*”命令集对于管道操作或资源清单管理非常有用。

## 示例

### 示例 1：检索复制组
```
PS C:\> Get-DfsReplicationGroup -GroupName RG02
GroupName              : RG02
DomainName             : corp.contoso.com
Identifier             : 81251362-e30f-4c1e-b6b0-23906c1ebdd7
Description            :
State                  : Normal
```

该命令用于检索 RG02 复制组的信息，以便进行库存管理或在其他流程中使用。

### 示例 2：检索复制组（replication groups）和 SYSVOL 共享卷
```
PS C:\> Get-DfsReplicationGroup -GroupName * -IncludeSysvol
GroupName              : Domain System Volume
DomainName             : corp.contoso.com
Identifier             : a8ff93e7-aab3-4330-ab66-dcab60dd9d1b
Description            :
State                  : Normal

GroupName              : RG02
DomainName             : corp.contoso.com
Identifier             : 81251362-e30f-4c1e-b6b0-23906c1ebdd7
Description            :
State                  : Normal

GroupName              : RG3
DomainName             : corp.contoso.com
Identifier             : 075a5be7-ef53-455d-9c27-0a2ffe6f688a
Description            :
State                  : Normal
```

此命令用于检索所有用于库存管理的复制组，其中包括由域控制器创建的特殊“Domain System Volume”资源组。默认情况下，该资源组不会被返回，因为其管理是由Active Directory控制的。

## 参数

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果您不指定此参数，该 cmdlet 将使用用户的当前域。

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
指定一个复制组名称的数组。如果您不指定此参数，该 cmdlet 会查询所有参与的复制组。您可以使用逗号分隔的列表以及通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RG, RgName

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### -IncludeSysvol
该参数表示 cmdlet 用于检索域控制器创建的特殊“域名系统卷复制组”（Domain System Volume replication group）。这个复制组包含了被复制的 SYSVOL 共享文件夹。由于内部限制，DFS 复制（DFS Replication）不允许直接修改 SYSVOL 文件夹；因此提供此参数仅是为了方便管理员了解某个域是否包含使用 DFSR （Domain Name System Resource Manager）进行管理的 SYSVOL 文件夹。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串

## 输出

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup
此 cmdlet 返回一个对象，其中包含 DFS 复制组的属性信息。

## 备注

## 相关链接

[New-DfsReplicationGroup](./New-DfsReplicationGroup.md)

[Remove-DfsReplicationGroup](./Remove-DfsReplicationGroup.md)

[Set-DfsReplicationGroup](./Set-DfsReplicationGroup.md)

[暂停DFS复制组](./Suspend-DfsReplicationGroup.md)

[Sync-DfsReplicationGroup](./Sync-DfsReplicationGroup.md)

