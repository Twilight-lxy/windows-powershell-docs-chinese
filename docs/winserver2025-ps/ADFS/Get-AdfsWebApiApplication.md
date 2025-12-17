---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfswebapiapplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsWebApiApplication
---

# 获取 AdfsWebApi 应用程序

## 摘要
在 AD FS 中获取 Web API 应用程序角色。

## 语法

### 标识符（默认值）
```
Get-AdfsWebApiApplication [[-Identifier] <String[]>] [<CommonParameters>]
```

### 名称
```
Get-AdfsWebApiApplication [-Name] <String[]> [<CommonParameters>]
```

### PrefixIdentifier
```
Get-AdfsWebApiApplication [-PrefixIdentifier] <String> [<CommonParameters>]
```

### ApplicationObject
```
Get-AdfsWebApiApplication [-Application] <WebApiApplication> [<CommonParameters>]
```

### ApplicationGroupIdentifier
```
Get-AdfsWebApiApplication [-ApplicationGroupIdentifier] <String> [<CommonParameters>]
```

### ApplicationGroupObject
```
Get-AdfsWebApiApplication [-ApplicationGroup] <ApplicationGroup> [<CommonParameters>]
```

## 描述
`Get-AdfsWebApiApplication` cmdlet 可以获取 Active Directory Federation Services (AD FS) 中的 Web API 应用程序角色。

## 示例

## 参数

### -Application
指定一个要获取的 Web API 应用程序。

```yaml
Type: WebApiApplication
Parameter Sets: ApplicationObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ApplicationGroup
指定一个应用程序组，以便从中获取Web API应用程序。

```yaml
Type: ApplicationGroup
Parameter Sets: ApplicationGroupObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ApplicationGroupIdentifier
指定用于获取 Web API 应用程序的应用程序组的 ID。

```yaml
Type: String
Parameter Sets: ApplicationGroupIdentifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Identifier
指定一个要获取的 Web API 应用程序的 ID。

```yaml
Type: String[]
Parameter Sets: Identifier
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Name
指定一个要获取的 Web API 应用程序名称数组。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PrefixIdentifier
用于指定要获取的 Web API 应用程序的前缀标识符。

```yaml
Type: String
Parameter Sets: PrefixIdentifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftIdentityServer.Management.Resources.WebApiApplication

`WebApiApplication` 对象是通过 `Application` 参数接收到的。

### MicrosoftIdentityServer.ManagementResources.ApplicationGroup

`ApplicationGroup` 对象是通过 `ApplicationGroup` 参数接收到的。

### System.String

字符串对象通过 *ApplicationGroupIdentifier*、*Identifier* 和 *Name* 参数接收。

## 输出

### MicrosoftIdentityServer.Management.Resources.WebApiApplication

返回一个或多个 WebApiApplication 对象，这些对象代表联邦服务（Federation Service）中的 Web API 应用程序。

## 备注

## 相关链接

[Add-AdfsWebApiApplication](./Add-AdfsWebApiApplication.md)

[Remove-AdfsWebApiApplication](./Remove-AdfsWebApiApplication.md)

[Set-AdfsWebApiApplication](./Set-AdfsWebApiApplication.md)
