---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsscopedescription?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsScopeDescription
---

# 获取 AdfsScope 描述信息

## 摘要
获取 AD FS 中某个范围的描述信息。

## 语法

```
Get-AdfsScopeDescription [[-Name] <String[]>] [<CommonParameters>]
```

## 描述
**Get-AdfsScopeDescription** 这个 cmdlet 可以获取表示在 Active Directory Federation Services (AD FS) 中授予资源和应用程序的访问权限范围的描述信息。

## 示例

## 参数

### -Name
指定一个用于获取作用域描述名称的数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

字符串对象是通过*Name*参数接收的。

## 输出

### Microsoft_identityServer.Management Resources.OAuthScopeDescription

返回一个或多个 OAuthScopeDescription 对象，这些对象表示联邦服务的范围描述信息。

## 备注

## 相关链接

[Add-AdfsScopeDescription](./Add-AdfsScopeDescription.md)

[Remove-AdfsScopeDescription](./Remove-AdfsScopeDescription.md)

[Set-AdfsScopeDescription](./Set-AdfsScopeDescription.md)

