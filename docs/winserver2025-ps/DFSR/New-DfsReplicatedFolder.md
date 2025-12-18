---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/new-dfsreplicatedfolder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-DfsReplicatedFolder
---

# 新DFS复制文件夹

## 摘要
在复制组中创建一个已复制的文件夹。

## 语法

```
New-DfsReplicatedFolder [-GroupName] <String[]> [-FolderName] <String[]> [[-Description] <String>]
 [[-FileNameToExclude] <String[]>] [[-DirectoryNameToExclude] <String[]>] [[-DfsnPath] <String>]
 [-CreateDisabledMemberships] [[-DomainName] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-DfsReplicatedFolder` cmdlet 可以在复制组中创建一个新的复制文件夹。复制文件夹是一种逻辑上的复制结构，其中不包含与特定计算机相关的设置。

## 示例

### 示例 1：创建一个可复制的文件夹
```
PS C:\> New-DfsReplicatedFolder -GroupName "RG22" -FolderName "RF26"


GroupName              : RG22
FolderName             : RF26
DomainName             : corp.contoso.com
Identifier             : 434ca205-388d-4f24-a5b0-7ff875d433e0
Description            :
FileNameToExclude      : {~*, *.bak, *.tmp}
DirectoryNameToExclude : {}
DfsnPath               :
IsDfsnPathPublished    : False
State                  : Normal
```

该命令在名为RG22的复制组中创建一个名为RF26的复制文件夹。此命令不会更改复制文件夹的默认设置。

### 示例 2：创建一个复制的文件夹，并添加一个DFS命名空间链接路径
```
PS C:\> New-DfsReplicatedFolder -GroupName "RG22" -FolderName "RF26" -DfsnPath "\\corp.contoso.com\public\link1"


WARNING: The DfsnPath parameter is not validated. An incorrect path will not produce an error.


GroupName              : RG22
FolderName             : RF267
DomainName             : corp.contoso.com
Identifier             : 111c28cb-348a-47e3-8e4d-4bf394f640bb
Description            :
FileNameToExclude      : {~*, *.bak, *.tmp}
DirectoryNameToExclude : {}
DfsnPath               : \\corp.contoso.com\public\link1
IsDfsnPathPublished    : True
State                  : Normal
```

此命令在名为 RG22 的复制组中创建一个名为 RF26 的复制文件夹。参数 **DfsnPath** 用于设置 DFS 命名空间链接路径的相关管理属性。该 cmdlet 提醒管理员：DFSN 路径仅具有显示性作用，DFS 复制功能并不会以任何方式验证或使用该路径。

### 示例 3：创建一个复制文件夹，但该文件夹会排除某些特定的文件名
```
PS C:\> New-DfsReplicatedFolder -GroupName "RG11" -FolderName "RF08" -FileNameToExclude "~*, *.bak, *.tmp, *.ned"


GroupName              : RG11
FolderName             : RF08
DomainName             : corp.contoso.com
Identifier             : 085a1de3-b4e5-46a4-a8f4-8f36a20bafdf
Description            :
FileNameToExclude      : {~*, *.bak, *.tmp, *.ned}
DirectoryNameToExclude : {}
DfsnPath               :
IsDfsnPathPublished    : False
State                  : Normal
```

该命令在名为 RG11 的复制组中创建一个名为 RF08 的复制文件夹。命令指出，DFS 复制服务应排除以波浪号（~）开头的文件名以及具有 .bak、.tmp 和 .ned 扩展名的文件，这些文件不会被纳入复制过程。

### 示例 4：创建数据分布复制拓扑结构
```
The first command uses the **New-DfsReplicationGroup** cmdlet to create a replication group object named Branch Office 1, and passes the object to the **New-DfsReplicatedFolder** cmdlet by using the pipe operator. The **New-DfsReplicatedFolder** cmdlet creates a replication folder object named Data Distribution 1, and passes the object to the **Add-DfsrMember** cmdlet by using the pipe operator. The **Add-DfsrMember** cmdlet adds the computers named SRV01, SRV02, and SRV03 to the replication group named Branch Office 1.
PS C:\> New-DfsReplicationGroup -GroupName "Branch Office 1" | New-DfsReplicatedFolder -FolderName "Data Distribution 1" | Add-DfsrMember -ComputerName "SRV01","SRV02","SRV03" | Format-Table dnsname,groupname -auto -wrap

DnsName               GroupName
-------               ---------
SRV01.corp.contoso.com Branch Office 1
SRV02.corp.contoso.com Branch Office 1
SRV03.corp.contoso.com Branch Office 1


The second command creates a bidirectional replication connection between the computer named SRV01 and the computer named SRV02 in the replication group named Branch Office 1.
PS C:\> Add-DfsrConnection -GroupName "Branch Office 1" -SourceComputerName "SRV01" -DestinationComputerName "SRV02" | Format-Table *name -wrap -auto



GroupName       SourceComputerName DestinationComputerName
---------       ------------------ -----------------------
Branch Office 1 SRV01               SRV02
Branch Office 1 SRV02               SRV01


The third command creates a bidirectional replication connection between the computer named SRV01 and the computer named SRV03 in the replication group named Branch Office 1.
PS C:\> Add-DfsrConnection -GroupName "Branch Office 1" -SourceComputerName "SRV01" -DestinationComputerName "SRV03" | Format-Table *name -wrap -auto
GroupName       SourceComputerName DestinationComputerName
---------       ------------------ -----------------------
Branch Office 1 SRV01               SRV03
Branch Office 1 SRV03               SRV01


The fourth command uses the **Set-DfsrMembership** cmdlet to configure membership settings for the primary member of the replication group named Branch Office 1. The command specifies that the computer named SRV01 is the primary member of the group. The command sets an appropriate quota size of the staging folder instead of the lower default.
PS C:\> Set-DfsrMembership -GroupName "Branch Office 1" -FolderName "Data Distribution 1" -ContentPath "C:\rf1" -ComputerName "SRV01" -PrimaryMember $True -StagingPathQuotaInMB 16384 -Force | Format-Table *name,*path,primary* -auto -wrap


DomainName       GroupName       FolderName          ComputerName ContentPath StagingPath                PrimaryMember
----------       ---------       ----------          ------------ ----------- -----------                -------------
corp.contoso.com Branch Office 1 Data Distribution 1 SRV01         c:\rf1      c:\rf1\DfsrPrivate\Staging          True

The last command uses the **Set-DfsrMembership** cmdlet to configure membership settings for the members of the replication group named Branch Office 1. The command specifies that the computers named SRV02 and SRV03 are members of the group. The command sets an appropriate quota size of the staging folder instead of the lower default.
PS C:\> Set-DfsrMembership -GroupName "Branch Office 1" -FolderName "Data Distribution 1" -ContentPath "C:\rf1" -ComputerName "SRV02","SRV03" -StagingPathQuotaInMB 16384 -Force | Format-Table *name,*path,primary* -auto -wrap


DomainName       GroupName       FolderName          ComputerName ContentPath StagingPath                PrimaryMember
----------       ---------       ----------          ------------ ----------- -----------                -------------
corp.contoso.com Branch Office 1 Data Distribution 1 SRV02         c:\rf1      c:\rf1\DfsrPrivate\Staging         False
corp.contoso.com Branch Office 1 Data Distribution 1 SRV03         c:\rf1      c:\rf1\DfsrPrivate\Staging         False
```

这个示例创建了一个中心辐射式（hub-and-spoke）的数据分布复制拓扑结构。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您确认是否要执行操作。

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

### -CreateDisabledMemberships
这表示您添加到复制文件夹中的任何成员的会员资格都被禁用了。通常情况下，您不需要设置此参数，因为创建新的复制拓扑结构的下一步就是建立连接和配置成员资格，然后开始复制过程。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 6
Default value: None
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
指定复制文件夹的DFS命名空间（DFSN）文件夹路径。

DFSN文件夹路径对复制过程没有影响。此属性仅作为描述性信息提供给管理员使用，DFS复制服务不会验证该属性的值。

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
指定一个子文件夹名称数组，DSFR服务将排除这些子文件夹，并且不会在复制的文件夹中复制它们。您只需提供文件夹名称，无需提供完整路径。可以使用通配符。

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
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果您不指定此参数，cmdlet 将使用当前用户的域。

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
指定一个文件名称和扩展名的数组，这些文件将被分布式文件系统（DSF）复制服务排除，不会被复制到目标文件夹中。此参数只需提供文件夹名称，无需指定完整路径。可以使用通配符。

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
指定一个包含已复制文件夹名称的数组。您可以使用逗号分隔的列表以及通配符（*）。如果不指定此参数，该cmdlet将获取所有已复制的文件夹。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RF, RfName

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
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
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上并没有运行这个cmdlet。

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

### Microsoft.DistributedFileSystemReplication.DfsReplicatedFolder

## 备注

## 相关链接

[Get-DfsReplicatedFolder](./Get-DfsReplicatedFolder.md)

[Set-DfsReplicatedFolder](./Set-DfsReplicatedFolder.md)

[Remove-DfsReplicatedFolder](./Remove-DfsReplicatedFolder.md)

