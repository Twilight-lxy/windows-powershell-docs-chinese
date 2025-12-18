---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/set-dfsreplicatedfolder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DfsReplicatedFolder
---

# Set-DfsReplicatedFolder

## 摘要
更改已复制文件夹的设置。

## 语法

```
Set-DfsReplicatedFolder [-GroupName] <String[]> [[-FolderName] <String[]>] [[-Description] <String>]
 [[-FileNameToExclude] <String[]>] [[-DirectoryNameToExclude] <String[]>] [[-DfsnPath] <String>]
 [[-DomainName] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DfsReplicatedFolder` cmdlet 用于更改复制组中复制文件夹的设置。您可以使用此 cmdlet 来修改复制文件夹的全局设置，例如过滤器以及分布式文件系统（DFS）命名空间关联等。复制文件夹是一种逻辑上的复制结构，其中不包含与特定计算机相关的设置。

## 示例

### 示例 1：为复制的文件夹添加描述
```
PS C:\> Set-DfsReplicatedFolder -GroupName "RG11" -FolderName "RF101" -Description "Branch Store #101, Data Collection for Backups"
GroupName              : RG11
FolderName             : RF101
DomainName             : corp.contoso.com
Identifier             : c335e8f6-bc3e-4671-8f7b-9cdc51a6b222
Description            : Branch Store #101 Data Collection for Backups
FileNameToExclude      : {~*, *.bak, *.tmp}
DirectoryNameToExclude : {}
DfsnPath               :
IsDfsnPathPublished    : False
State                  : Normal
```

此命令为名为“RG11”的复制组中、名为“RF101”的复制文件夹设置了一个新的描述。

### 示例 2：排除所有已复制文件夹中的文件
```
PS C:\> Set-DfsReplicatedFolder -GroupName "RG11" -FolderName * -FileNameToExclude "~*, *.bak, *.tmp, *.ned"
GroupName              : RG11
FolderName             : RF11
DomainName             : corp.contoso.com
Identifier             : c335e8f6-bc3e-4671-8f7b-9cdc51a6b222
Description            :
FileNameToExclude      : {~*, *.bak, *.tmp, *.ned}
DirectoryNameToExclude : {}
DfsnPath               :
IsDfsnPathPublished    : False
State                  : Normal

GroupName              : RG11
FolderName             : rf12
DomainName             : corp.contoso.com
Identifier             : 50e057af-08a4-4dbb-af1c-3765620afd9e
Description            :
FileNameToExclude      : {~*, *.bak, *.tmp, *.ned}
DirectoryNameToExclude : {}
DfsnPath               :
State                  : Normal

IsDfsnPathPublished    : False

GroupName              : RG11
FolderName             : rf101
DomainName             : corp.contoso.com
Identifier             : c335e8f6-bc3e-4671-8f7b-9cdc51a6b222
Description            : Branch Store #101 Data Collection for Backups
FileNameToExclude      : {~*, *.bak, *.tmp, *.ned}
DirectoryNameToExclude : {}
DfsnPath               :
IsDfsnPathPublished    : False
State                  : Normal
```

此命令用于设置要从RG11复制组中所有被复制的文件夹的复制过程中排除的文件列表。该命令指定DFS复制服务应排除以波浪号（~）开头的文件名，以及扩展名为.bak、.tmp和.ned的文件。

## 参数

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

### -Description
为复制的文件夹指定一个描述。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DfsnPath
指定已复制文件夹的 DFS 命名空间文件夹路径。

此参数用于将复制组连接到被复制的文件夹。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DirectoryNameToExclude
指定一个子文件夹名称数组，DSFR服务将排除这些文件夹，并且不会将这些文件夹复制到目标复制的文件夹中。您只需提供文件夹名称，无需提供完整的路径。可以使用通配符。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: DirectoryFilter

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果您不指定此参数，该 cmdlet 将使用当前用户的域。

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

### -FileNameToExclude
指定一个文件名称和扩展名的数组，这些文件将被 DSFR 服务排除且不会被复制。您只需提供文件名称，无需提供完整路径。可以使用通配符。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: FileFilter

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FolderName
指定一个包含已复制文件夹名称的数组。你可以使用逗号分隔的列表以及通配符（*）。如果未指定此参数，该cmdlet将获取所有已复制的文件夹。

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

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### Microsoft.DistributedFileSystemReplication.DfsReplicatedFolder

## 输出

### Microsoft.DistributedFileSystemReplication.DfsReplicatedFolder

## 备注

## 相关链接

[Get-DfsReplicatedFolder](./Get-DfsReplicatedFolder.md)

[New-DfsReplicatedFolder](./New-DfsReplicatedFolder.md)

[Remove-DfsReplicatedFolder](./Remove-DfsReplicatedFolder.md)
