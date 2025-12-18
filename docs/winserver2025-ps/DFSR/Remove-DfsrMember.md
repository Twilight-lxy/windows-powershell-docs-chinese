---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/remove-dfsrmember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DfsrMember
---

# 移除DFSR成员

## 摘要
从复制组中移除计算机。

## 语法

```
Remove-DfsrMember [-GroupName] <String[]> [-ComputerName] <String[]> [-Force] [[-DomainName] <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DfsrMember` cmdlet 用于将成员计算机从复制组中移除。复制组的成员会托管被复制的文件夹。如果您将某个成员从其复制组中移除，分布式文件系统（DFS）的复制功能将在该成员上停止复制操作。此 cmdlet 不会删除被复制文件夹的内容或其私有数据。要向复制组中添加成员计算机，请使用 `Add-DfsrMember` cmdlet。

## 示例

#### 示例 1：从群组中移除一名成员
```
PS C:\> Remove-DfsrMember -GroupName "River Branch Office" -ComputerName "SRV02"
This operation will remove the computer and all of its memberships and connections.
Computer: SRV02 Replication group:"River Branch Office"
Are you sure you want to continue to remove this computer from its replication group and all of its memberships and
connections?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):
```

此命令会将名为 SRV02 的成员计算机从 River 分支办公室的复制组中移除。由于该示例中没有使用 *Force* 参数，因此系统会提示您进行确认操作。

### 示例 2：从组中删除所有成员
```
PS C:\> Remove-DfsrMember -GroupName "RG07" -ComputerName * -Force
```

此命令会将所有成员计算机从名为RG07的复制组中移除。由于该命令包含了“Force”参数，因此会在不提示确认的情况下直接执行移除操作。

## 参数

### -ComputerName
指定一个成员计算机的名称数组。此cmdlet会将这些成员从复制组中删除。你可以使用逗号分隔的列表以及通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: MemberList, MemList

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
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

### -Force
强制命令运行，而不需要用户确认。

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
展示了如果该cmdlet运行会发生什么情况。但实际上该cmdlet并未被执行。

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

### 无

## 备注

## 相关链接

[Add-DfsrMember](./Add-DfsrMember.md)

[Get-DfsrMember](./Get-DfsrMember.md)

[Set-DfsrMember](./Set-DfsrMember.md)

