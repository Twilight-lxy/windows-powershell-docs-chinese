---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/remove-dfsrconnection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DfsrConnection
---

# 删除 DFSR 连接

## 摘要
删除复制组成员之间的连接。

## 语法

```
Remove-DfsrConnection [-GroupName] <String[]> [-SourceComputerName] <String>
 [-DestinationComputerName] <String> [-Force] [[-DomainName] <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
**Remove-DfsrConnection** cmdlet 用于删除复制组成员之间的连接。一旦删除了某对服务器之间的连接，分布式文件系统（DFS）复制服务就无法在这些服务器之间进行数据复制了。因此，您应该始终同时删除两台服务器之间的双向连接。请在该命令行工具上分别针对接收数据的计算机和发送数据的计算机运行此 cmdlet。

DFS复制连接是复制组中各个成员之间的逻辑合作关系。DFS复制服务使用远程过程调用（RPC）协议在服务器之间进行通信。

## 示例

### 示例 1：删除复制组中成员之间的连接
```
PS C:\> Remove-DfsrConnection -GroupName "RG24" -SourceComputerName "SRV01" -DestinationComputerName "SRV02"
This operation will remove the connection from the replication group. First computer: SRV01 Second computer: SRV02 Replication group: "RG24"
Are you sure you want to continue to remove this connection?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): y
```

此命令会断开名为SRV01的计算机与名为RG24的复制组中名为SRV02的计算机之间的连接。

### 示例 2：在未经确认的情况下，删除复制组中成员之间的连接
```
PS C:\> Remove-DfsrConnection -GroupName "RG24" -SourceComputerName "SRV02" -DestinationComputerName "SRV01" -Force
```

此命令会删除名为 SRV01 的计算机与名为 SRV02 的计算机之间的连接，而不会提示您确认是否要执行该操作。

## 参数

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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
Accept wildcard characters: True
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

### -Force
强制命令运行，而无需请求用户确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

### 字符串

## 输出

### 无

## 备注

## 相关链接

[Get-DfsrConnection](./Get-DfsrConnection.md)

[Add-DfsrConnection](./Add-DfsrConnection.md)

[Set-DfsrConnection](./Set-DfsrConnection.md)

