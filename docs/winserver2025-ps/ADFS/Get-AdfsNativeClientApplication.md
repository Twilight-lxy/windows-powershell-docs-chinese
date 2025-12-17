---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsnativeclientapplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsNativeClientApplication
---

# 获取 AdfsNativeClient 应用程序

## 摘要
从 AD FS 中的应用程序中获取本地的客户端应用程序角色。

## 语法

### 标识符（默认值）
```
Get-AdfsNativeClientApplication [[-Identifier] <String[]>] [<CommonParameters>]
```

### 名称
```
Get-AdfsNativeClientApplication [-Name] <String[]> [<CommonParameters>]
```

### ApplicationObject
```
Get-AdfsNativeClientApplication [-Application] <NativeClientApplication> [<CommonParameters>]
```

### ApplicationGroupIdentifier
```
Get-AdfsNativeClientApplication [-ApplicationGroupIdentifier] <String> [<CommonParameters>]
```

### ApplicationGroupObject
```
Get-AdfsNativeClientApplication [-ApplicationGroup] <ApplicationGroup> [<CommonParameters>]
```

## 描述
`Get-AdfsNativeClientApplication` cmdlet 用于从 Active Directory Federation Services (AD FS) 中的应用程序中获取原生客户端应用程序角色。

## 示例

## 参数

### -Application
指定要获取的原生客户端应用程序。

```yaml
Type: NativeClientApplication
Parameter Sets: ApplicationObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ApplicationGroup
指定用于获取原生客户端应用程序的应用程序组。

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
指定用于获取原生客户端应用程序的应用程序组的ID。

```yaml
Type: String
Parameter Sets: ApplicationGroupIdentifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identifier
指定一个数组，其中包含需要获取的原生客户端应用程序的ID。

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
指定一个包含原生客户端应用程序名称的数组。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftIdentityServer.Management.Resources.NativeClientApplication

`NativeClientApplication` 对象是通过 `Application` 参数接收到的。

### Microsoft IdentityServer.Management.Resources.ApplicationGroup

`ApplicationGroup` 对象是通过 `ApplicationGroup` 参数接收到的。

### System.String

字符串对象通过 *Identifier*（标识符）和 *Name*（名称）参数被接收。

## 输出

### MicrosoftIdentityServer.Management.Resources.NativeClientApplication

返回一个或多个 NativeClientApplication 对象，这些对象表示联邦服务的本机客户端应用程序资源。

## 备注

## 相关链接

[Add-AdfsNativeClientApplication](./Add-AdfsNativeClientApplication.md)

[Remove-AdfsNativeClientApplication](./Remove-AdfsNativeClientApplication.md)

[Set-AdfsNativeClientApplication](./Set-AdfsNativeClientApplication.md)

