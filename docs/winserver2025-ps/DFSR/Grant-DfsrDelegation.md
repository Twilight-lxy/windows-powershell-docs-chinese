---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/grant-dfsrdelegation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Grant-DfsrDelegation
---

# 授予 DFSR 委托权限

## 摘要
为安全主体授予复制组的权限。

## 语法

```
Grant-DfsrDelegation [-GroupName] <String[]> [-AccountName] <String[]> [-Force] [[-DomainName] <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Grant-DfsrDelegation** cmdlet 允许用户或组创建复制文件夹、连接、成员以及复制组中的成员关系。该功能使得在运行分布式文件系统（DFS）复制服务的服务器上担任本地管理员的用户，能够在不具备域管理员权限的情况下管理 Active Directory 域服务（AD DS）相关部分的复制拓扑结构。

## 示例

### 示例 1：授予委托权限
```
PS C:\> Grant-DfsrDelegation -GroupName "RG01" -AccountName "DFSR Admins"
GroupName   : RG01
AccountName : TSQA\DFSR Admins
IsInherited : False
```

此命令为名为“DFSR Admins”的安全组授予对名为“RG01”的复制组的委托权限。

## 参数

### -AccountName
指定一个安全主体名称的数组。此cmdlet会为该参数所指定的用户和组分配权限。

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
在运行该 cmdlet 之前，会提示您进行确认。

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
指定包含复制组的 AD DS 域的 NetBIOS 名称或完全限定域名（FQDN）。如果未指定此参数，cmdlet 将使用当前用户的域。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### 字符串[]

### 字符串

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrDelegation

## 备注

## 相关链接

[Get-DfsrDelegation](./Get-DfsrDelegation.md)

[Revoke-DfsrDelegation](./Revoke-DfsrDelegation.md)

