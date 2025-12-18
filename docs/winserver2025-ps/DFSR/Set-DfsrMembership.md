---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/set-dfsrmembership?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DfsrMembership
---

# Set-DfsrMembership

## 摘要
配置复制组成员的成员身份设置。

## 语法

```
Set-DfsrMembership [-GroupName] <String[]> [-FolderName] <String[]> [-ComputerName] <String[]>
 [[-ContentPath] <String>] [[-PrimaryMember] <Boolean>] [[-StagingPath] <String>]
 [[-StagingPathQuotaInMB] <UInt32>] [[-ConflictAndDeletedQuotaInMB] <UInt32>] [[-ReadOnly] <Boolean>]
 [[-RemoveDeletedFiles] <Boolean>] [[-DisableMembership] <Boolean>]
 [[-MinimumFileStagingSize] <FileStagingSize>] [[-DfsnPath] <String>] [-Force] [[-DomainName] <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DfsrMembership` cmdlet 用于配置分布式文件系统（DFS）复制组成员的成员身份设置。复制组的成员会托管被复制的文件夹。可以使用 `Add-DfsrMember` cmdlet 将新成员添加到该组中；添加成员后会自动创建一个包含默认值的成员身份记录。在添加成员之后，可以使用当前的 `Set-DfsrMembership` cmdlet 来修改这些成员身份设置。

使用此cmdlet来指定复制文件夹的名称和位置，以及该复制文件夹是否为只读属性。您还可以将某台成员计算机指定为其组的主要成员。

您还可以指定成员计算机为其“ConflictsAndDeleted”文件夹分配多少磁盘空间，以及是否将已删除的复制文件复制到该文件夹中。此外，您可以指定一个临时文件夹及其最大容量，并设置DSF Replication在出站复制过程中应处理的最低文件大小。

你可以使用这个cmdlet来禁用成员计算机的复制功能。不过，如果要暂停复制过程，可以通过在成员计算机上使用**Remove-DfsrConnection** cmdlet来断开连接，或者使用**Suspend-DfsReplicationGroup** cmdlet来实现。

## 示例

### 示例 1：更改会员设置
```
PS C:\> Set-DfsrMembership -GroupName "RG22" -FolderName "RepFolder" -ComputerName "SRV07" -StagingPathQuotaInMB 32768 -ConflictAndDeletedQuotaInMB 4096
GroupName                   : RG22
ComputerName                : SRV07
FolderName                  : RF01
GroupDomainName             : corp.contoso.com
ComputerDomainName          : corp.contoso.com
Identifier                  : 9931c757-b252-4f04-8347-53575610c423
DistinguishedName           : CN=72c0c2bc-8a4e-4984-a23c-2efadc238724,CN=957751c2-15f0-429b-8688-44c22044226d,CN=DFSR-L
                              ocalSettings,CN=SRV07,OU=Domain Controllers,DC=corp,DC=contoso,DC=com
ContentPath                 : c:\rf01
PrimaryMember               : False
StagingPath                 : c:\rf01\DfsrPrivate\Staging
StagingPathQuotaInMB        : 32768
MinimumStagingFileSize      : Size256KB
ConflictAndDeletedPath      : c:\rf01\DfsrPrivate\ConflictAndDeleted
ConflictAndDeletedQuotaInMB : 4096
ReadOnly                    : False
RemoveDeletedFiles          : False
Enabled                     : True
DfsnPath                    :
State                       : Normal
```

这个命令用于修改名为SRV07的计算机上某个复制文件夹的设置，该计算机属于名为RG22的组。该命令将“staging”文件夹的配额设置为32768MB，将“ConflictAndDeleted”文件夹的配额设置为4096MB。控制台会显示相应的成员对象信息，其中包含这些新设置的值。

#### 示例 2：创建一个复制组
```
The first command creates a replication group, specifies a replicated folder, and adds three computers to the group as members. The command creates a replication group named River Branch Office by using the **New-DfsReplicationGroup** cmdlet. The command passes the new group to the **New-DfsReplicatedFolder** cmdlet by using the pipeline operator. That cmdlet creates a replicated folder named Data Distribution 01. The command adds three computers, named SRV01, SRV02, and SRV03, to the new replication group.
PS C:\> New-DfsReplicationGroup -GroupName "River Branch Office" | New-DfsReplicatedFolder -FolderName "Data Distribution 01" | Add-DfsrMember -ComputerName "SRV01","SRV02","SRV03" | Format-Table dnsname,groupname -auto -wrap
DnsName                GroupName
-------                ---------
SRV01.corp.contoso.com River Branch Office
SRV02.corp.contoso.com River Branch Office
SRV03.corp.contoso.com River Branch Office

The second command adds a connection between the source computer named SRV01 and the destination computer named SRV02 by using the **Add-DfsrConnection** cmdlet.
PS C:\> Add-DfsrConnection -GroupName "River Branch Office" -SourceComputerName "SRV01" -DestinationComputerName "SRV02" | Format-Table *name -wrap -auto
GroupName           SourceComputerName  DestinationComputerName
---------           ------------------  -----------------------
River Branch Office SRV01               SRV02
River Branch Office SRV02               SRV01

The third command adds a connection between the source computer named SRV01 and the destination computer named SRV03.
PS C:\> Add-DfsrConnection -GroupName "River Branch Office" -SourceComputerName "SRV01" -DestinationComputerName "SRV03" | Format-Table *name -wrap -auto
GroupName           SourceComputerName  DestinationComputerName
---------           ------------------  -----------------------
River Branch Office SRV01               SRV03
River Branch Office SRV03               SRV01

The fourth command makes the computer named SRV01 the primary member of the group. The command also specifies Data Distribution 01 as the name of the replicated folder in the location C:\RF01. The command specifies the staging folder quota as 16384 MB. The command includes the *Force* parameter, and, therefore, does not prompt the user for confirmation.
PS C:\> Set-DfsrMembership -GroupName "River Branch Office" -FolderName "Data Distribution 01" -ContentPath "C:\RF01" -ComputerName "SRV01" -PrimaryMember $True -StagingPathQuotaInMB 16384 -Force | Format-Table *name,*path,primary* -auto -wrap
DomainName       GroupName           FolderName           ComputerName  ContentPath StagingPath                PrimaryMember
----------       ---------           ----------           ------------  ----------- -----------                -------------
corp.contoso.com River Branch Office Data Distribution 01 SRV01         C:\RF01     C:\RF01\DfsrPrivate\Staging         True

The fifth command modifies values for the computers named SRV02 and SRV03. The command specifies Data Distribution 01 as the name of the replicated folder in the location C:\RF01. The command specifies the staging folder quota as 16384 MB. The command includes the *Force* parameter, and, therefore, does not prompt the user for confirmation.Unlike the previous command, this command does not specify a value of the *PrimaryMember* parameter. The computers named SRV02 and SRV03 have the default value of $False for the setting.
PS C:\> Set-DfsrMembership -GroupName "River Branch Office" -FolderName "Data Distribution 1" -ContentPath "C:\RF01" -ComputerName "SRV02","SRV03" -StagingPathQuotaInMB 16384 -Force | Format-Table *name,*path,primary* -auto -wrap
DomainName       GroupName           FolderName           ComputerName  ContentPath StagingPath                PrimaryMember
----------       ---------           ----------           ------------  ----------- -----------                -------------
corp.contoso.com River Branch Office Data Distribution 01 SRV02         C:\RF01     C:\RF01\DfsrPrivate\Staging        False
corp.contoso.com River Branch Office Data Distribution 01 SRV03         C:\RF01     C:\RF01\DfsrPrivate\Staging        False
```

这个示例创建了一个名为“River Branch Office”的复制组。该组由三台计算机组成：一台主成员（名为SRV01），以及另外两台名为SRV02和SRV03的计算机。示例指定了用于复制的文件夹，并建立了这些成员之间的连接；同时，还指定了该临时文件夹（staging folder）的最大容量。

每个命令都会返回相应的对象或多个对象。在这个例子中，我们使用了 `Format-Table` cmdlet 来格式化控制台中的输出内容。有关更多信息，请输入 `Get-Help Format-Table`。

## 参数

### -ComputerName
指定一组成员计算机的名称。该cmdlet会修改这些成员计算机的成员资格设置。您可以使用逗号分隔的列表以及通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: MemberList, MemList

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

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

### -ConflictAndDeletedQuotaInMB
指定 `ConflictsAndDeleted` 文件夹的最大大小（以兆字节为单位）。默认值为 4096 MB。

当这个文件夹的大小达到配额值的指定百分比时，DFS复制（DFS Replication）会删除该文件夹中最旧的文件。默认的百分比为90%。DFS复制会持续删除文件，直到文件夹的大小再次达到配额值的指定百分比；此时的默认百分比为60%。你可以使用**Set-DfsrServiceConfiguration** cmdlet来修改这些百分比值。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 7
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ContentPath
指定一个本地文件夹，用于存放与使用 *FolderName* 参数指定的复制的文件夹相关联的复制文件。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DfsnPath
指定成员所属的DFS命名空间文件夹路径。您可以使用此值来跟踪该DFS命名空间文件夹的位置。该值不会影响数据复制过程。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 12
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableMembership
用于指示是否禁用复制组中某个复制文件夹的成员资格。

如果您禁用成员资格，DFS复制将停止在这台计算机上复制内容，但不会删除已复制的文件夹或其私有复制数据。如果您重新启用成员资格，将会丢失所有私有数据以及可能已被复制的数据。您可以使用 **Restore-DfsrPreservedFiles** cmdlet 来尝试恢复这些被复制的数据。默认情况下，成员资格是处于启用状态的。

如果您想暂时暂停复制操作，可以使用 **Set-DfsrConnection** cmdlet 来断开成员节点的连接，或者使用 **Suspend-DfsReplicationGroup** cmdlet 来暂停整个复制组的操作。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 10
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

### -FolderName
指定一个包含已复制文件夹名称的数组。如果您不指定此参数，该cmdlet将适用于所有参与复制的文件夹。您可以使用逗号分隔的列表以及通配符（*）。

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

### -Force
强制命令执行，而不要求用户确认。

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
指定一个复制组名称的数组。如果您不指定此参数，该 cmdlet 将应用于所有参与的复制组。您可以使用逗号分隔的列表以及通配符（*）。

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

### -MinimumFileStagingSize
指定 DFS 复制在出站复制过程中进行文件分阶段传输的最小文件大小。默认情况下，该值为 256 KB。如果您同时禁用了远程差异压缩（RDC），那么小于此大小的文件将直接进行复制，而不会经过分阶段传输的过程。在带宽较高、延迟较低的网络环境中（如局域网和高速广域网），这种方式通常可以实现更快的复制速度，但会导致更高的网络带宽利用率。您可以使用 **Set-DfsrConnection** cmdlet 来禁用或启用 RDC 功能。

Windows Server® 2012 及更早版本的 Windows 操作系统不支持文件大小设置。那些支持 DFS 复制的旧版本 Windows 操作系统会使用固定的最小暂存区大小（256 KB）。

此参数的可接受值为：

- Size256KB (0)
- Size512KB (1)
- Size1MB (2)
- Size2MB (3)
- Size4MB (4)
- Size8MB (5)
- Size16MB (6)
- Size32MB (7)
- Size64MB (8)
- Size128MB (9)
- Size256MB (10)
- Size512MB (11)
- Size1GB (12)
- Size2GB (13)
- Size4GB (14)
- Size8GB (15)
- Size16GB (16)
- Size32GB (17)
- Size64GB (18)
- Size128GB (19)
- Size256GB (20)
- Size512GB (21)
- Size1TB (22)
- Size2TB (23)
- Size4TB (24)
- Size8TB (25)
- Size16TB (26)
- Size32TB (27)
- Size64TB (28)
- Size128TB (29)
- Size256TB (30)
- Size512TB (31)

```yaml
Type: FileStagingSize
Parameter Sets: (All)
Aliases:
Accepted values: Size256KB, Size512KB, Size1MB, Size2MB, Size4MB, Size8MB, Size16MB, Size32MB, Size64MB, Size128MB, Size256MB, Size512MB, Size1GB, Size2GB, Size4GB, Size8GB, Size16GB, Size32GB, Size64GB, Size128GB, Size256GB, Size512GB, Size1TB, Size2TB, Size4TB, Size8TB, Size16TB, Size32TB, Size64TB, Size128TB, Size256TB, Size512TB

Required: False
Position: 11
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PrimaryMember
该字段用于指示这台成员计算机是否是一个组的主要成员。在每个复制组中，只能指定一个成员作为主要成员。默认情况下，所有成员都不是主要成员。

如果您为这个参数指定了 `$True` 的值，请不要同时为 `*ReadOnly*` 参数也指定 `$True` 的值。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReadOnly
用于指示复制的文件夹是否为只读模式。默认情况下，该文件夹的支持权限（读/写）是可同时设置的。

如果您将一个可读/写的文件夹更改为只读模式，或者将一个只读文件夹更改为可读/写模式，DFS复制（DFS Replication）会将所有未复制的本地更改移动到“ConflictAndDeleted”文件夹中。您可以使用 **Restore-DfsrPreservedFiles** cmdlet 来恢复这些更改。

如果您为该参数指定了 `$True` 的值，请不要同时为 `*PrimaryMember` 参数也指定 `$True` 的值。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 8
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemoveDeletedFiles
该参数用于指示成员计算机在接收到复制请求后是否立即删除文件和文件夹。如果该参数的值为 `$False`，则成员计算机会在将删除操作复制到本地时，将这些文件和文件夹移至 `ConflictAndDeleted` 文件夹中；而源服务器始终会直接删除文件（不会保留任何副本）。您可以使用 `Restore-DfsrPreservedFiles` cmdlet 在这些文件仍存在于 `ConflictAndDeleted` 文件夹中时将其恢复。如果该参数的值为 `$True`，则在成员计算机执行删除操作时，它会立即删除本地文件副本。如果不指定此参数，默认情况下 DFS 复制功能会保留被删除的文件。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 9
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StagingPath
指定一个用于存放临时内容的本地文件夹。如果您不指定此参数，DFS复制会创建一个名为 “\<replicated folder\>\DfsrPrivate\Staging” 的文件夹。

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

### -StagingPathQuotaInMB
用于指定临时文件夹的最大大小（以兆字节为单位）。该参数的默认值为 4096 MB。当文件夹的大小达到配额值的指定百分比（默认为 90%）时，DFS 复制会删除文件夹中最旧的文件；此后会继续删除文件，直到文件夹的大小再次达到配额值的另一个指定百分比（默认为 60%）。可以使用 **Set-DfsrServiceConfiguration** cmdlet 来修改这些百分比值。

如果您选择更大的配额，成员计算机将阶段数据保留更长的时间，从而提供更好的复制性能。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生的结果。不过实际上这个cmdlet并没有被运行。

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

### Microsoft.DistributedFileSystemReplication.DfsReplicatedFolder

### 字符串

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrMembership

## 备注

## 相关链接

[Get-DfsrMembership](./Get-DfsrMembership.md)

[Add-DfsrMember](./Add-DfsrMember.md)

[Set-DfsrServiceConfiguration](./Set-DfsrServiceConfiguration.md)

[Restore-DfsrPreservedFiles](./Restore-DfsrPreservedFiles.md)

[停用DFS复制组](./Suspend-DfsReplicationGroup.md)

[Add-DfsrConnection](./Add-DfsrConnection.md)

[Remove-DfsrConnection](./Remove-DfsrConnection.md)

[Set-DfsrConnection](./Set-DfsrConnection.md)

[New-DfsReplicationGroup](./New-DfsReplicationGroup.md)

[New-DfsReplicatedFolder](./New-DfsReplicatedFolder.md)
