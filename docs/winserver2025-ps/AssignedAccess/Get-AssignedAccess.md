---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: AssignedAccess-help.xml
Module Name: AssignedAccess
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/assignedaccess/get-assignedaccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AssignedAccess
---

# 获取分配的访问权限

## 摘要
获取当前分配的访问权限的相关配置信息。

## 语法

```
Get-AssignedAccess [<CommonParameters>]
```

## 描述
`Get-AssignedAccess` cmdlet 可获取当前关于分配访问权限的配置信息，包括用户名、用户 SID（Security Identifier）、应用程序友好名称以及应用程序 ID。

“Assigned Access” cmdlets 仅支持在 Windows 10 和 Windows 11 客户端操作系统上使用。

## 示例

### 示例 1：获取已分配访问权限的配置信息
```
PS C:\> Get-AssignedAccess

User Name: MYPC\UserName
User SID:  S-1-5-21-594534509-2542345234-234523453-1004
AUMID:     Microsoft.Media.PlayReadyClient_2.3.1678.0_x64__8wekyb3d8bbwe
App Name:  Microsoft.Media.PlayReadyClient
```

此命令用于获取当前分配的访问权限配置信息。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。
您无法将输入数据通过管道传递给此cmdlet。

## 输出

### 没有（需要处理的内容）。
此cmdlet不会生成任何输出。

## 备注

## 相关链接

[Clear-AssignedAccess](./Clear-AssignedAccess.md)

[Set-AssignedAccess](./Set-AssignedAccess.md)

