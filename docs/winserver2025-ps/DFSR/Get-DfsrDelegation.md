---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsrdelegation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsrDelegation
---

# Get-DfsrDelegation

## 摘要
获取具有复制组权限的主体（principals）。

## 语法

```
Get-DfsrDelegation [[-GroupName] <String[]>] [[-DomainName] <String>] [<CommonParameters>]
```

## 描述
`Get-DfsrDelegation` cmdlet 可以获取具有创建复制文件夹、连接以及为复制组添加成员等权限的用户和组。有关分布式文件系统（DFS）复制服务中委派机制的更多信息，请参阅 `Grant-DfsrDelegation` cmdlet 的相关文档。

## 示例

#### 示例 1：获取复制组的 principals（管理信息）
```
PS C:\> Get-DfsrDelegation -GroupName "RG01"

GroupName   : RG01
AccountName : NT AUTHORITY\SYSTEM
IsInherited : False

GroupName   : RG01
AccountName : TSQA\Domain Admins
IsInherited : False

GroupName   : RG01
AccountName : TSQA\DFSR Admins
IsInherited : False

GroupName   : RG01
AccountName : TSQA\Enterprise Admins
IsInherited : True
```

此命令用于获取被授权访问名为RG01的复制组的用户和组。

## 参数

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果未指定此参数，cmdlet 将使用当前用户的所在域。

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
指定一个复制组名称数组。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### 字符串[]

### 字符串

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrDelegation

## 备注

## 相关链接

[Grant-DfsrDelegation](./Grant-DfsrDelegation.md)

[Revoke-DfsrDelegation](./Revoke-DfsrDelegation.md)

