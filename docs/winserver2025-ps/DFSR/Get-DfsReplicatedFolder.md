---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsreplicatedfolder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsReplicatedFolder
---

# Get-DfsReplicatedFolder

## 摘要
从一个复制组中获取一个已复制的文件夹。

## 语法

```
Get-DfsReplicatedFolder [[-GroupName] <String[]>] [[-FolderName] <String[]>] [[-DomainName] <String>]
 [<CommonParameters>]
```

## 描述
`Get-DfsReplicatedFolder` cmdlet 可用于获取现有的复制文件夹。该 cmdlet 会返回复制文件夹的全局设置信息，例如过滤规则以及与分布式文件系统（DFS）命名空间的关联关系。复制文件夹是一种逻辑上的复制结构，其中不包含与特定计算机相关的设置信息。

## 示例

### 示例 1：获取一个已复制的文件夹
```
PS C:\> Get-DfsReplicatedFolder -GroupName "RG24" -FolderName "RF01"


GroupName              : RG24
DomainName             : corp.contoso.com
FolderName             : RF01
Identifier             : c335e8f6-bc3e-4671-8f7b-9cdc51a6b222
Description            :
FileNameToExclude      : {~*, *.bak, *.tmp}
DirectoryNameToExclude : {}
DfsnPath               :
IsDfsnPathPublished    : False
State                  : Normal
```

该命令从名为RG24的复制组中获取名为RF01的已复制文件夹。

## 参数

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果未指定此参数，该 cmdlet 将使用当前用户的域。

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
指定一个包含已复制文件夹名称的数组。您可以使用逗号分隔的列表以及通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RF, RfName

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

### -GroupName
指定一个复制组名称的数组。你可以使用逗号分隔的列表以及通配符（*）。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 输出

### Microsoft.DFSRManagement.ReplicatedFolder

## 备注

## 相关链接

[Set-DfsReplicatedFolder](./Set-DfsReplicatedFolder.md)

[Set-DfsReplicatedFolder](./Set-DfsReplicatedFolder.md)

[Remove-DfsReplicatedFolder](./Remove-DfsReplicatedFolder.md)

