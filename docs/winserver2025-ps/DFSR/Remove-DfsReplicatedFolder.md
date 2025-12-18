---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/remove-dfsreplicatedfolder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DfsReplicatedFolder
---

# 删除DFS复制文件夹

## 摘要
从复制组中删除一个已复制的文件夹。

## 语法

```
Remove-DfsReplicatedFolder [-GroupName] <String[]> [-FolderName] <String[]> [-Force] [[-DomainName] <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DfsReplicatedFolder` cmdlet 用于从复制组中删除已复制的文件夹。这些复制的文件夹只是数据复制的逻辑结构，其中不包含与特定计算机相关的设置信息。

当你删除一个已复制的文件夹时，分布式文件系统（DFS）的复制服务将无法继续复制该文件夹。此操作不会删除任何已复制的文件数据。仅当你需要停止使用某个已复制的文件夹时，请使用此 cmdlet。

## 示例

#### 示例 1：删除一个被复制的文件夹
```
PS C:\> Remove-DfsReplicatedFolder -GroupName "RG11" -FolderName "RF22"

Performing this operation will remove the replicated folder "RF22" and its memberships.
Are you sure you want to continue to remove this replicated folder and its memberships?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): y
```

此命令会将复制的文件夹RF22及其关联的成员从名为RG11的复制组中删除。

### 示例 2：删除与某个复制组关联的所有重复文件夹
```
PS C:\> Remove-DfsReplicatedFolder -GroupName "RG11" -FolderName * -Force
```

此命令会从名为 RG11 的复制组中删除所有已复制的文件夹及其关联的成员资格。*Force* 参数表示该cmdlet不会提示您确认是否要删除每个复制的文件夹。

## 参数

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名或完全限定域名（FQDN）。如果未指定此参数，cmdlet 将使用当前用户的域。

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

### -FolderName
指定一个包含已复制文件夹名称的数组。您可以使用逗号分隔的列表以及通配符（*）。如果您不指定此参数，该cmdlet将获取所有已复制的文件夹。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RF, RfName

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### -Force
强制命令运行，而无需请求用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GroupName
指定一个复制组名称的数组。您可以使用逗号分隔的列表以及通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RG, RgName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

### -WhatIf
展示了如果该 cmdlet 被运行时会发生什么情况。但实际上，这个 cmdlet 并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### 字符串

## 输出

### 无

## 备注

## 相关链接

[Get-DfsReplicatedFolder](./Get-DfsReplicatedFolder.md)

[Set-DfsReplicatedFolder](./Set-DfsReplicatedFolder.md)

[New-DfsReplicatedFolder](./New-DfsReplicatedFolder.md)

