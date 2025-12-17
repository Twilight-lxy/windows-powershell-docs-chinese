---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsapplicationgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsApplicationGroup
---

# 获取 AdFS 应用程序组

## 摘要
获取一个应用程序组。

## 语法

### ApplicationGroupIdentifier（默认值）
```
Get-AdfsApplicationGroup [[-ApplicationGroupIdentifier] <String[]>] [<CommonParameters>]
```

### 名称
```
Get-AdfsApplicationGroup [-Name] <String[]> [<CommonParameters>]
```

### ApplicationGroupObject
```
Get-AdfsApplicationGroup [-ApplicationGroup] <ApplicationGroup> [<CommonParameters>]
```

## 描述
`Get-AdfsApplicationGroup` cmdlet 用于获取 Active Directory Federation Services (AD FS) 应用程序组。

## 示例

## 参数

### -ApplicationGroup
指定一个应用程序组。

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
指定一个应用程序组的ID。

```yaml
Type: String[]
Parameter Sets: ApplicationGroupIdentifier
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Name
指定一个应用程序组名称的数组。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.IdentityServer.Management.Resources.ApplicationGroup

`ApplicationGroup` 对象是通过 `ApplicationGroup` 参数接收到的。

### System.String

字符串对象通过 *ApplicationGroupIdentifier* 和 *Name* 参数被接收。

## 输出

### Microsoft.IdentityServer.Management.Resources.ApplicationGroup

返回一个或多个 `ApplicationGroup` 对象，这些对象表示联邦服务的应用程序组。

## 备注

## 相关链接

[Disable-AdfsApplicationGroup](./Disable-AdfsApplicationGroup.md)

[Enable-AdfsApplicationGroup](./Enable-AdfsApplicationGroup.md)

[New-AdfsApplicationGroup](./New-AdfsApplicationGroup.md)

[Remove-AdfsApplicationGroup](./Remove-AdfsApplicationGroup.md)

[Set-AdfsApplicationGroup](./Set-AdfsApplicationGroup.md)
