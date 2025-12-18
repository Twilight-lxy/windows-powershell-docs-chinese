---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/revoke-dfsrdelegation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Revoke-DfsrDelegation
---

# 撤销 DFSR 委派（Revoke-DfsrDelegation）

## 摘要
撤销复制组中安全主体（security principals）的权限。

## 语法

```
Revoke-DfsrDelegation [-GroupName] <String[]> [-AccountName] <String[]> [-Force] [[-DomainName] <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Revoke-DfsrDelegation` cmdlet 用于撤销用户或组在某个复制组中的委托权限。有关分布式文件系统（DFS）复制服务中委托机制的更多信息，请参阅 `Grant-DfsrDelegation` cmdlet 的文档。

## 示例

### 示例 1：撤销委托的权限
```
PS C:\> Revoke-DfsrDelegation -GroupName "RG01" -AccountName "DFSR Admins"
This operation will revoke delegation of permissions on the replication group named "RG01" for the account named DFSR
Admins.
Are you sure you want to revoke delegation of permissions on this replication group?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):
```

此命令将撤销名为“DFSR Admins”的安全组针对名为“RG01”的复制组的委托权限。

### 示例 2：在无需确认的情况下撤销委托的权限
```
PS C:\> Revoke-DfsrDelegation -GroupName "RG02 -AccountName "DFSR Admins" -Verbose -Force
VERBOSE: Performing the operation "Revoke-DfsrDelegation" on target "RG02".
VERBOSE: Successfully revoked delegation of permissions on the replication group named "RG02" for the account named
DFSR Admins
```

此命令会撤销名为“DFSR Admins”的安全组对名为“RG02”的复制组所拥有的授权权限。该命令指定了“Force”参数，因此不会提示用户确认是否执行删除操作；同时，它还指定了“Verbose”参数，从而会显示操作的详细信息。

## 参数

### -AccountName
指定一个安全主体名称数组。此cmdlet会撤销该参数所指定的用户和组的权限。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

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

### -Force
强制命令执行，而无需请求用户确认。

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
指定一个复制组名称的数组。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### 字符串（String）[]

### 字符串（String）

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrDelegation

## 备注

## 相关链接

[Get-DfsrDelegation](./Get-DfsrDelegation.md)

[Grant-DfsrDelegation](./Grant-DfsrDelegation.md)
