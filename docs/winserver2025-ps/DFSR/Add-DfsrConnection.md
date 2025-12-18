---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/add-dfsrconnection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DfsrConnection
---

# Add-DfsrConnection

## 摘要
在复制组的成员之间建立连接。

## 语法

```
Add-DfsrConnection [-GroupName] <String[]> [-SourceComputerName] <String> [-DestinationComputerName] <String>
 [-DisableConnection] [-DisableRDC] [-DisableCrossFileRDC] [[-Description] <String>]
 [[-MinimumRDCFileSizeInKB] <Int64>] [-CreateOneWay] [[-DomainName] <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-DfsrConnection` cmdlet 可用于在复制组的成员之间建立连接。

分布式文件系统（DFS）复制连接是复制组中各成员之间的逻辑关联。DFS复制服务使用远程过程调用（RPC）协议在服务器之间进行通信。在DFS复制服务能够启动复制之前，必须先在一对计算机之间建立连接。即使您使用的是只读复制模式，也应当始终在两台服务器之间建立双向连接。唯一的例外情况是当您在三台或更多服务器之间创建环形拓扑结构时：在这种情况下，所有成员都会相互复制数据，并且所有服务器都仅托管可写复制的文件夹。

这个cmdlet不支持修改连接带宽或调度安排，因为这些通常不需要进行更改。

## 示例

### 示例 1：在复制组的成员之间创建双向连接
```
PS C:\> Add-DfsrConnection -GroupName "RG24" -SourceComputerName "SRV01" -DestinationComputerName "SRV02"

GroupName               : RG24
SourceComputerName      : SRV01
DestinationComputerName : SRV02
DomainName              : corp.contoso.com
Identifier              : c33eaaf1-9e50-4510-8484-68271bf93b25c33eaaf1-9e50-4510-8484-68271bf93b25
Enabled                 : True
RdcEnabled              : True
CrossFileRdcEnabled     : True
Description             :
MinimumRDCFileSizeInKB  : 64
State                   : Normal

GroupName               : RG24
SourceComputerName      : SRV02
DestinationComputerName : SRV01
DomainName              : corp.contoso.com
Identifier              : 97c3603a-7828-4403-adac-49575c9e5921
Enabled                 : True
RdcEnabled              : True
CrossFileRdcEnabled     : True
Description             :
MinimumRDCFileSizeInKB  : 64
State                   :

NormalGroupName         : RG24
SourceComputerName      : SRV02
DestinationComputerName : SRV01
DomainName              : corp.contoso.com
Identifier              : 97c3603a-7828-4403-adac-49575c9e5921
Enabled                 : True
RdcEnabled              : True
CrossFileRdcEnabled     : True
Description             :
MinimumRDCFileSizeInKB  : 64
State                   : Normal
```

该命令在名为RG24的复制组中，创建了名为SRV01的计算机与名为SRV02的计算机之间的双向复制连接。

### 示例 2：在复制组中的成员之间创建单向连接
```
PS C:\> Add-DfsrConnection -GroupName "RG24" -SourceComputerName SRV02 -DestinationComputerName "SRV01" -CreateOneWay

GroupName               : rg24
SendingComputerName     : SRV02
ReceivingComputerName   : SRV01
DomainName              : corp.contoso.com
Identifier              : c33eaaf1-9e50-4510-8484-68271bf93b25
Enabled                 : True
RdcEnabled              : true
CrossFileRdcEnabled     : True
Description             :
MinimumRDCFileSizeInKB  : 64
State                   : Normal
```

此命令会在名为RG24的复制组中，建立从计算机SRV02到计算机SRV01的单向复制连接。要创建单向复制连接，必须在复制组的各成员之间分别运行该cmdlet（每个方向执行一次）。DFS复制仅支持在三个或更多服务器组成的环形拓扑配置中使用单向复制连接。

### 示例 3：创建数据分布复制拓扑结构
```
The first command uses the **New-DfsReplicationGroup** cmdlet to create a replication group object named Branch Office 1, and passes the object to the **New-DfsReplicatedFolder** cmdlet by using the pipe operator. The **New-DfsReplicatedFolder** cmdlet creates a replication folder object named Data Distribution 1, and passes the object to the **Add-DfsrMember** cmdlet by using the pipe operator. The **Add-DfsrMember** cmdlet adds the computers named SRV01, SRV02, and SRV03 to the replication group named Branch Office 1.
PS C:\> New-DfsReplicationGroup -GroupName "Branch Office 1" | New-DfsReplicatedFolder -FolderName "Data Distribution 1" | Add-DfsrMember -ComputerName "SRV01","SRV02","SRV03" | Format-Table dnsname,groupname -auto -wrap
DnsName                 GroupName
-------               ---------
SRV01.corp.contoso.com Branch Office 1
SRV02.corp.contoso.com Branch Office 1
SRV03.corp.contoso.com Branch Office 1

The second command creates a bidirectional replication connection between the computer named SRV01 and the computer named SRV02 in the replication group named Branch Office 1.
PS C:\> Add-DfsrConnection -GroupName "Branch Office 1" -SourceComputerName SRV01 -DestinationComputerName SRV02 | Format-Table *name -wrap -auto
GroupName       SourceComputerName DestinationComputerName
---------       ------------------ -----------------------
Branch Office 1 SRV01               SRV02
Branch Office 1 SRV02               SRV01

The third command creates a bidirectional replication connection between the computer named SRV01 and the computer named SRV03 in the replication group named Branch Office 1.
PS C:\> Add-DfsrConnection -GroupName "Branch Office 1" -SourceComputerName SRV01 -DestinationComputerName SRV03 | Format-Table *name -wrap -auto
GroupName       SourceComputerName DestinationComputerName
---------       ------------------ -----------------------
Branch Office 1 SRV01               SRV03
Branch Office 1 SRV03               SRV01

The fourth command uses the **Set-DfsrMembership** cmdlet to configure membership settings for the primary member of the replication group named Branch Office 1. The command specifies that the computer named SRV01 is the primary member of the group. The command sets an appropriate quota size of the staging folder instead of the lower default.
PS C:\> Set-DfsrMembership -GroupName "Branch Office 1" -FolderName "Data Distribution 1" -ContentPath c:\rf1 -ComputerName SRV01 -PrimaryMember $True -StagingPathQuotaInMB 16384 -Force | Format-Table *name,*path,primary* -auto -wrap
DomainName       GroupName       FolderName          ComputerName ContentPath StagingPath                PrimaryMember
----------       ---------       ----------          ------------ ----------- -----------                -------------
corp.contoso.com Branch Office 1 Data Distribution 1 SRV01         c:\rf1      c:\rf1\DfsrPrivate\Staging          True

The last command uses the **Set-DfsrMembership** cmdlet to configure membership settings for the members of the replication group named Branch Office 1. The command specifies that the computers named SRV02 and SRV03 are members of the group. The command sets an appropriate quota size of the staging folder instead of the lower default.
PS C:\> Set-DfsrMembership -GroupName "Branch Office 1" -FolderName "Data Distribution 1" -ContentPath c:\rf1 -ComputerName SRV02,SRV03 -StagingPathQuotaInMB 16384 -Force | Format-Table *name,*path,primary* -auto -wrap
DomainName       GroupName       FolderName          ComputerName ContentPath StagingPath                PrimaryMember
----------       ---------       ----------          ------------ ----------- -----------                -------------
corp.contoso.com Branch Office 1 Data Distribution 1 SRV02         c:\rf1      c:\rf1\DfsrPrivate\Staging         False
corp.contoso.com Branch Office 1 Data Distribution 1 SRV03         c:\rf1      c:\rf1\DfsrPrivate\Staging         False
```

这个示例创建了一个中心辐射式（hub-and-spoke）的数据分布复制拓扑结构。

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

### -CreateOneWay
指定DFSR服务不会在两台计算机之间创建反向的连接。

通常情况下，你不需要指定这个参数。DFS复制需要一个完全连接的复制拓扑结构，这意味着所有服务器都必须与其直接的对等节点之间存在双向连接（无论是直接的入站/出站连接，还是通过间接的复制机制）。即使你使用 **Set-DfsrMembership** cmdlet 并将 *ReadOnly* 参数设置为 $True 以指定只读复制模式，这一要求也同样适用。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 8
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Description
为该连接指定一个描述。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DestinationComputerName
指定接收计算机的名称。接收计算机也被称为入站计算机或下游计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ReceivingMember, RMem

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DisableConnection
指定DFSR服务会断开连接。

通常情况下，你不需要手动禁用连接。如果你想暂时停止复制过程，可以设置这个参数。此外，你还可以使用 **Suspend-DfsReplicationGroup** cmdlet 来中断计算机之间的复制操作。在 DFS 复制服务能够重新启动复制之前，你必须先恢复计算机之间的连接。

重要提示：请使用该参数来指定相关设置，而不是通过 `Set-DfsrMembership` cmdlet 来禁用某台计算机在复制组中的成员身份。禁用或重新启用某台计算机的成员资格会导致非授权的入站复制操作发生。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableCrossFileRDC
表示DFSR服务在此连接上禁用了跨文件相似性的远程差分压缩（RDC）算法。

跨文件RDC（Cross-File RDC）会使用卷上已存在的五个先前复制过的文件来作为新复制文件的“种子”。在带宽较低的网络连接环境下，如果复制的文件之间具有很高的相似性，那么采用跨文件RDC技术可以显著节省带宽和传输时间。然而，在带宽较高的网络环境下，跨文件RDC可能会导致过多的本地处理开销，从而影响系统性能。对于包含大量高度相似文件的庞大数据集（例如卷上拥有数百万个文件的情况），跨文件RDC还可能对CPU和磁盘利用率产生负面影响。因此，在通过局域网（LAN）或高性能广域网（WAN）进行数据复制时，建议禁用跨文件RDC功能。此设置仅支持Windows Server 2012 R2及更高版本的系统。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableRDC
这表示DFS复制服务在禁用远程差分压缩（Remote Differential Compression，简称RDC）的情况下创建连接。

当使用带宽较低、延迟较高的连接时，通常不需要指定此参数。但如果连接是通过局域网（LAN）或性能非常高的广域网（WAN）建立的，则建议指定该参数。默认情况下，DFS复制连接会启用RDC功能。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果未指定此参数，该cmdlet 将使用当前用户的域。

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
指定一个复制组名称的数组。你可以使用逗号分隔的列表以及通配符（*）。

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

### -MinimumRDCFileSizeInKB
指定用于远程桌面连接（RDC）应用的文件大小阈值，单位为千字节（kilobytes）。

当使用带宽较低、延迟较高的连接时，通常不需要指定这个参数。只有在连接是通过局域网（LAN）或性能非常高的广域网（WAN）建立的情况下，才需要考虑指定该参数。默认情况下，RDC会将大小等于或大于64KB的文件分割成多个数据块进行传输。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: 7
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SourceComputerName
指定发送计算机的名称。发送计算机也被称为出站计算机或上游计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: SendingMember, SMem

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生的后果。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrConnection

## 备注

## 相关链接

[Get-DfsrConnection](./Get-DfsrConnection.md)

[Set-DfsrConnection](./Set-DfsrConnection.md)

[Remove-DfsrConnection](./Remove-DfsrConnection.md)

