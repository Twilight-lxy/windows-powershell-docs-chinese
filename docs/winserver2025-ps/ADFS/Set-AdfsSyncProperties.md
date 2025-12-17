---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfssyncproperties?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsSyncProperties
---

# 设置 AdfsSyncProperties 属性

## 摘要
修改 AD FS 配置数据库的同步频率，以及确定服务器群中哪台服务器作为主服务器。

## 语法

```
Set-AdfsSyncProperties [-PrimaryComputerName <String>] [-PrimaryComputerPort <Int32>] [-PollDuration <Int32>]
 [-Role <String>] [<CommonParameters>]
```

## 描述
`Set-ADFSSyncProperties` 这个 cmdlet 用于修改 Active Directory Federation Services (AD FS) 配置数据库的同步频率。此外，该 cmdlet 还可以指定联邦服务器组中的哪台服务器是主服务器。

## 示例

### 示例 1：修改某个农场的投票时长
```
PS C:\> Set-AdfsSyncProperties -PollDuration 3600 -PrimaryComputerName "FederationServerPrimary"
```

该命令将数据库同步间隔修改为3600秒。这一更改会应用于主联邦服务器。

### 示例 2：将一台服务器从辅助角色切换到主要角色
```
PS C:\> Set-AdfsSyncProperties -Role "PrimaryComputer"
```

此命令会将WID（Windows Identity Foundation）集群中的一台AD FS（Active Directory Federation Services）服务器从辅助服务器切换为主服务器。

### 示例 3：将主服务器更改为从服务器
```
PS C:\> Set-AdfsSyncProperties -Role "SecondaryComputer" -PrimaryComputerName "<FQDN of primary server>"
```

此命令会将 WID（Windows Integrated Domain）环境中的某个主 AD FS（Active Directory Federation Services）服务器更改为从属服务器。注意：从属服务器必须能够通过 HTTP 协议在端口 80 上访问该主服务器。

## 参数

### -PollDuration
指定 AD FS 配置数据库与主联合服务器同步的频率（以秒为单位）。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PrimaryComputerName
指定联邦服务器群中的主要联邦服务器的名称。请修改该主要联邦服务器上的 Federation Service 的相关设置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PrimaryComputerPort
指定主要的计算机端口。联邦服务器群中的主要计算机将使用您指定的TCP端口。请修改主联邦服务器上的Federation Service相关设置。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Role
指定该联邦服务器的角色。此参数的可接受值为：primary（主服务器）和secondary（从服务器）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[Get-AdfsSyncProperties](./Get-AdfsSyncProperties.md)

