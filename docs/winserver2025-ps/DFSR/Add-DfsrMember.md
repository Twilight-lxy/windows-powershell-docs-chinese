---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/add-dfsrmember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DfsrMember
---

# Add-DfsrMember

## 摘要
将计算机添加到复制组中。

## 语法

```
Add-DfsrMember [-GroupName] <String[]> [-ComputerName] <String[]> [[-Description] <String>]
 [[-DomainName] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DfsrMember` cmdlet 可以将计算机添加到复制组中，使其成为该组的成员。复制组的成员会托管被复制的文件夹。你可以为这些成员计算机指定描述信息。使用 `Remove-DfsrMember` cmdlet 可以从复制组中移除成员计算机。

## 示例

### 示例 1：向复制组中添加成员
```
PS C:\> Add-DfsrMember -GroupName "RG01" -ComputerName "SRV07"
GroupName                    : RG01
ComputerName                 : SRV07
DomainName                   : corp.contoso.com
Identifier                   : 838bba5e-b487-4d1e-8c1c-d2303af49e2a
Description                  :
DnsName                      : SRV07.corp.contoso.com
Site                         : Default-First-Site-Name
NumberOfConnections          : 0
NumberOfInboundConnections   : 0
NumberOfOutboundConnections  : 0
NumberOfInterSiteConnections : 0
NumberOfIntraSiteConnections : 0
IsClusterNode                : False
State                        : Normal
```

此命令将名为 SRV07 的计算机添加到名为 RG01 的复制组中。控制台会显示新的 **DfsrMember** 对象。

### 示例 2：向新组中添加多个成员
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

The fourth command makes the computer named SRV01 the primary member of the group by using the **Set-DfsrMembership** cmdlet. The command also specifies Data Distribution 01 as the name of the replicated folder in the location C:\RF01. The command specifies the staging folder quota as 16384 MB. The command includes the *Force* parameter, and, therefore, does not prompt the user for confirmation.
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

这个示例创建了一个名为“River Branch Office”的复制组。该组由三台计算机组成：一台主成员（名称为SRV01），以及另外两台名为SRV02和SRV03的计算机。示例中指定了用于复制的文件夹，并建立了这些成员之间的连接；同时，还规定了用于临时存储数据的文件夹的最大容量。

每个命令都会返回相应的对象或多个对象。在这个例子中，我们使用了 **Format-Table** cmdlet 来格式化控制台中的输出内容。如需更多信息，请输入 `Get-Help Format-Table`。

## 参数

### -ComputerName
指定一个包含计算机名称的数组。该cmdlet会将这些计算机添加到由*GroupName*参数指定的复制组中。您可以使用逗号分隔的列表以及通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: MemberList, MemList

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -Description
为成员计算机指定一个描述信息。

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

### -GroupName
指定一个复制组名称数组。您可以使用逗号分隔的列表以及通配符（*）。

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

### -WhatIf
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrMember

## 备注

## 相关链接

[Get-DfsrMember](./Get-DfsrMember.md)

[Remove-DfsrMember](./Remove-DfsrMember.md)

[Set-DfsrMember](./Set-DfsrMember.md)

[New-DfsReplicationGroup](./New-DfsReplicationGroup.md)

[New-DfsReplicatedFolder](./New-DfsReplicatedFolder.md)

[Set-DfsrMembership](./Set-DfsrMembership.md)

