---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfssyncproperties?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsSyncProperties
---

# Get-AdfsSyncProperties

## 摘要
从 AD FS 的配置数据库中获取同步相关属性。

## 语法

```
Get-AdfsSyncProperties [<CommonParameters>]
```

## 描述
`Get-ADFSSyncProperties` cmdlet 可以获取 Active Directory Federation Services (AD FS) 配置数据库的同步属性。

## 示例

### 示例 1：获取同步属性
```
PS C:\> Get-ADFSSyncProperties
```

这个命令用于获取配置数据库的同步属性。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[Set-AdfsSyncProperties](./Set-AdfsSyncProperties.md)

