---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsrconnection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsrConnection
---

# Get-DfsrConnection

## 摘要
建立DFS复制伙伴之间的连接。

## 语法

```
Get-DfsrConnection [[-GroupName] <String[]>] [[-SourceComputerName] <String>]
 [[-DestinationComputerName] <String>] [[-DomainName] <String>] [<CommonParameters>]
```

## 描述
`Get-DfsrConnection` cmdlet 可用于获取两个分布式文件系统（DFS）复制伙伴之间的现有连接。

DFS复制连接是复制组中各成员之间的逻辑关联。DFS复制服务使用远程过程调用（RPC）协议在服务器之间进行通信。

## 示例

### 示例 1：在计算机之间建立单向连接
```
PS C:\> Get-DfsrConnection -GroupName "RG24" -SourceComputerName "SRV01" -DestinationComputerName "SRV02"


GroupName               : RG24
SourceComputerName      : SRV01
DestinationComputerName : SRV02
DomainName              : corp.contoso.com
Identifier              : c33eaaf1-9e50-4510-8484-68271bf93b25
Enabled                 : True
RdcEnabled              : True
CrossFileRdcEnabled     : True
Description             :
MinimumRDCFileSizeInKB  : 64
State                   : Normal
```

此命令用于建立从名为 SRV01 的计算机到名为 SRV02 的计算机之间的单向连接，该连接属于 RG24 复制组。

## 参数

### -DestinationComputerName
指定接收计算机的名称。接收计算机也被称为入站计算机或下游计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ReceivingMember, RMem

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果未指定此参数，cmdlet 将使用当前用户的域。

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
指定一个复制组名称的数组。您可以使用逗号分隔的列表以及通配符（*）。

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

### -SourceComputerName
指定发送计算机的名称。发送计算机也被称为出站计算机或上游计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: SendingMember, SMem

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrConnection

## 备注

## 相关链接

[Add-DfsrConnection](./Add-DfsrConnection.md)

[Set-DfsrConnection](./Set-DfsrConnection.md)

[Remove-DfsrConnection](./Remove-DfsrConnection.md)

