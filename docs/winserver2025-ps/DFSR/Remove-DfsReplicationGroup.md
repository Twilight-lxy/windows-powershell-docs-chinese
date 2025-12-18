---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/remove-dfsreplicationgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DfsReplicationGroup
---

# 删除DFS复制组

## 摘要
删除一个复制组。

## 语法

```
Remove-DfsReplicationGroup [-GroupName] <String[]> [-RemoveReplicatedFolders] [-Force] [[-DomainName] <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Remove-DfsReplicationGroup** cmdlet 用于删除一个复制组。

当你删除一个复制组时，该复制组会从 Active Directory 中被移除，同时与该复制组相关的分布式文件系统（DFS）复制拓扑结构中的所有内容也会被删除，包括成员、成员关系以及连接等信息。此时，所有成员上的复制操作都会停止。此操作不会删除任何已复制的文件数据或私有数据。请仅在需要停用某个复制组时使用此命令。

## 示例

### 示例 1：删除一个复制组
```
PS C:\> Remove-DfsReplicationGroup -GroupName "RG01"
Performing this operation will remove the replication group "RG01" and the subscriptions members have to this
replication group. Are you sure you want to continue to remove this replication group? [Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): y
```

此命令将从当前域中删除名为 RG01 的复制组。

### 示例 2：使用通配符删除复制组
```
PS C:\> Remove-DfsReplicationGroup -GroupName "RG*" -RemoveReplicatedFolders -Domain "corp.contoso.com"
Performing this operation will remove the replication group "RG01" and the subscriptions members have to this
replication group. Are you sure you want to continue to remove this replication group? [Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):

Performing this operation will remove the replication group "RG02" and the subscriptions members have to this
replication group. Are you sure you want to continue to remove this replication group? [Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):

Performing this operation will remove the replication group "RG03" and the subscriptions members have to this
replication group. Are you sure you want to continue to remove this replication group? [Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):
```

此命令会删除域 corp.contoso.com 中所有包含 “RG*” 模式的复制组，即使这些组中包含已复制的文件夹。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行。

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

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果您不指定此参数，该 cmdlet 将使用当前域。

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

### -Force
强制命令运行而无需用户确认。使用此参数可批量删除复制组。

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

### -GroupName
指定一个复制组名称数组。您可以使用逗号分隔的列表以及通配符（*）。

如果复制组中包含任何已复制的文件夹，您必须指定 **RemoveReplicatedFolders** 参数。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RG, RgName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -RemoveReplicatedFolders
这表示在删除复制组之前，该cmdlet会先移除属于该复制组的所有已复制的文件夹。

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

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上该cmdlet并没有被运行。

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

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 输出

### 无

## 备注

## 相关链接

[Get-DfsReplicationGroup](./Get-DfsReplicationGroup.md)

[New-DfsReplicationGroup](./New-DfsReplicationGroup.md)

[Set-DfsReplicationGroup](./Set-DfsReplicationGroup.md)

