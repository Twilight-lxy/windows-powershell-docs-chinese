---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/update-dfsrconfigurationfromad?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-DfsrConfigurationFromAD
---

# 从 Active Directory 更新 DFSR 配置

## 摘要
启动DFS复制服务的更新过程。

## 语法

```
Update-DfsrConfigurationFromAD [[-ComputerName] <String[]>] [<CommonParameters>]
```

## 描述
`Update-DfsrConfigurationFromAD` cmdlet 用于启动分布式文件系统（DFS）复制服务的更新。该 cmdlet 强制 DFS 复制服务立即对 Active Directory 域服务（AD DS）执行一次完整的轻量级目录访问协议（LDAP）查询，以检测配置变更，并将任何变更应用到该服务中。

默认情况下，DFS复制服务会每隔五分钟查询一次域控制器，通过简单的检查来检测AD DS中的成员配置是否发生了变化。这种定期检查可以加快服务对某些类型配置变化的响应速度。如果DFS复制服务发现新的成员信息，它会随后进行一次全面的轮询。默认情况下，DFS复制服务每小时会执行一次全面轮询。

## 示例

### 示例 1：更新DFS复制服务
```
PS C:\> Update-DfsrConfigurationFromAD -ComputerName "SRV01","SRV02" -Verbose


VERBOSE: Performing operation "Update-DfsrConfigurationFromAD" on Target "SRV01".
VERBOSE: Successfully updated the DFSR Active Directory Domain Service configuration on the computer named SRV01.
VERBOSE: Performing operation "Update-DfsrConfigurationFromAD" on Target "SRV02".
VERBOSE: Successfully updated the DFSR Active Directory Domain Service configuration on the computer named SRV02.
```

此命令强制远程DFS复制服务器SRV01和SRV02立即查询AD DS，并将任何更改应用到DFS复制服务中。

## 参数

### -ComputerName
指定一组成员计算机的名称。可以使用逗号分隔的列表以及通配符（*）。此cmdlet会强制这些计算机上的DFS复制服务立即向Active Directory发送查询请求。

如果您不指定此参数，cmdlet 将使用本地计算机。要返回响应，请使用 *Verbose* 参数。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: MemberList, MemList

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串

## 输出

### 无

## 备注

## 相关链接

[Get-DfsrMember](./Get-DfsrMember.md)

