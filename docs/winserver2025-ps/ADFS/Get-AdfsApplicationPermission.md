---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsapplicationpermission?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsApplicationPermission
---

# Get-AdfsApplicationPermission

## 摘要
获取应用程序的使用权限。

## 语法

### 标识符（默认值）
```
Get-AdfsApplicationPermission [[-Identifiers] <String[]>] [<CommonParameters>]
```

### ClientRoleIdentifier
```
Get-AdfsApplicationPermission [[-ClientRoleIdentifiers] <String[]>] [<CommonParameters>]
```

### ServerRoleIdentifier
```
Get-AdfsApplicationPermission [[-ServerRoleIdentifiers] <String[]>] [<CommonParameters>]
```

## 描述
`Get-AdfsApplicationPermission` cmdlet 用于获取 Active Directory Federation Services (AD FS) 中应用程序的权限。

## 示例

## 参数

### -ClientRoleIdentifiers
指定一个客户端角色标识符数组。

```yaml
Type: String[]
Parameter Sets: ClientRoleIdentifier
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Identifiers
指定一个标识符数组。

```yaml
Type: String[]
Parameter Sets: Identifier
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServerRoleIdentifiers
指定一个服务器角色标识符数组。

```yaml
Type: String[]
Parameter Sets: ServerRoleIdentifier
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

`String` 对象通过 `ClientRoleIdentifiers`、`Identifiers` 和 `ServerRoleIdentifiers` 参数被接收。

## 输出

### Microsoft.IdentityServer.Management Resources.OAuthPermission

返回一个或多个 OAuthPermission 对象，这些对象表示应用程序在联邦服务（Federation Service）中的权限。

## 备注

## 相关链接

[Grant-AdfsApplicationPermission](./Grant-AdfsApplicationPermission.md)

[Revoke-AdfsApplicationPermission](./Revoke-AdfsApplicationPermission.md)

[Set-AdfsApplicationPermission](./Set-AdfsApplicationPermission.md)
