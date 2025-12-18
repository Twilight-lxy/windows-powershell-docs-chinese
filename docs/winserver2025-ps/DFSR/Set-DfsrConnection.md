---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/set-dfsrconnection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DfsrConnection
---

# Set-DfsrConnection

## 摘要
用于更改复制组中成员之间连接的相关设置。

## 语法

```
Set-DfsrConnection [[-GroupName] <String[]>] [-SourceComputerName] <String> [-DestinationComputerName] <String>
 [[-DisableConnection] <Boolean>] [[-DisableRDC] <Boolean>] [[-DisableCrossFileRDC] <Boolean>]
 [[-Description] <String>] [[-MinimumRDCFileSizeInKB] <Int64>] [[-DomainName] <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-DfsrConnection` cmdlet 用于更改复制组中两个成员之间的连接关系。

分布式文件系统（DFS）的复制连接是复制组中各成员之间的逻辑关联。DFS复制服务使用远程过程调用（RPC）协议在服务器之间进行通信。该服务不支持修改连接带宽或调度计划，因为这些通常不需要调整。

## 示例

### 示例 1：更改复制组中成员之间的连接关系
```
PS C:\> Set-DfsrConnection -GroupName "RG24" -SourceComputerName "SRV01" -DestinationComputerName "SRV02" -DisableRDC $True -DisableCrossFileRDC $True


GroupName               : rg 1
SourceComputerName      : SRV01
DestinationComputerName : SRV02
DomainName              : corp.contoso.com
Identifier              : 8b51a050-f32d-42dc-b008-80f56754f373
Enabled                 : True
RdcEnabled              : False
CrossFileRdcEnabled     : False
Description             :
MinimumRDCFileSizeInKB  : 64
State                   : Normal
```

此命令用于更改RG24复制组中名为SRV01和SRV02的计算机之间的连接设置。该命令指定，从SRV01到SRV02的连接不再使用远程差分压缩（Remote Differential Compression）或跨文件RDC（Cross-File RDC）技术。管理员认为，连接这些服务器的网络属于高带宽局域网（LAN），其复制速度应该比低带宽广域网（WAN）连接更快。

## 参数

### -Confirm
在运行cmdlet之前会提示您确认是否要继续执行该操作。

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
为该连接指定一个描述信息。

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
指定接收计算机的名称。接收计算机也被称为“入站计算机”或“下游计算机”。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ReceivingMember, RMem

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

### -DisableConnection
指定DFS复制服务会断开连接。

通常情况下，您不需要禁用连接。指定此参数可以暂时暂停复制过程。您也可以使用 **Suspend-DfsReplicationGroup** cmdlet 来停止计算机之间的复制操作。在 DFS 复制服务能够重新启动复制之前，必须先恢复计算机之间的连接。

重要提示：请使用此参数来指定计算机在复制组中的成员身份，而不是通过 `Set-DfsrMembership` cmdlet 来禁用计算机的成员资格。禁用或重新启用计算机的成员资格会导致非权威性的入站复制操作（即复制数据时可能会出现不一致或错误的情况）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableCrossFileRDC
表示DFS复制服务在此连接上禁用了跨文件相似性的远程差分压缩（RDC）算法。

跨文件RDC（Cross-File Remote Desktop Connection）会使用卷上已存在的前五个复制过的文件来创建一个新的待复制的文件。在带宽较低的网络连接环境下，如果复制的文件内容非常相似，那么这种技术可以显著节省网络带宽和传输时间。然而，在带宽较高的网络环境中，跨文件RDC可能会增加过多的本地处理开销，从而影响系统性能。对于规模庞大的数据集（例如卷上包含数百万个高度相似的文件），跨文件RDC还可能对CPU和磁盘利用率产生负面影响。在通过局域网（LAN）或高性能广域网（WAN）进行文件复制时，建议禁用该功能。此设置仅适用于Windows Server 2012 R2及更高版本的操作系统。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableRDC
表示DFS复制服务在禁用远程差异压缩（Remote Differential Compression，简称RDC）的情况下创建连接。

当你使用带宽较低、延迟较高的连接时，通常不需要指定这个参数。但如果连接是通过局域网（LAN）或性能非常高的广域网（WAN）建立的，那么建议指定该参数。默认情况下，DFS复制连接会启用RDC（Remote Desktop Connection）功能。

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

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果您不指定此参数，该 cmdlet 将使用当前用户的所在域。

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

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### -MinimumRDCFileSizeInKB
指定用于 RDC（Remote Desktop Connection）应用的文件大小阈值，单位为千字节（Kilobytes）。

在使用带宽较低/延迟较高的连接时，通常不需要指定这个参数。只有在连接是通过局域网（LAN）或性能非常高的广域网（WAN）建立的情况下，才建议指定该参数。默认情况下，RDC会将对大小等于或大于64KB的文件进行分块传输。

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
Accept wildcard characters: True
```

### -WhatIf
展示了如果该 cmdlet 被运行会发生什么情况。但实际上，这个 cmdlet 并没有被运行。

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

### 字符串（String）

### 字符串（String）

## 备注

## 相关链接

[Get-DfsrConnection](./Get-DfsrConnection.md)

[Add-DfsrConnection](./Add-DfsrConnection.md)

[Remove-DfsrConnection](./Remove-DfsrConnection.md)
