---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsdeviceregistrationupnsuffix?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsDeviceRegistrationUpnSuffix
---

# 获取 Adfs 设备注册的唯一标识符后缀（UPN Suffix）

## 摘要
获取可用于设备注册的 UPN 后缀。

## 语法

```
Get-AdfsDeviceRegistrationUpnSuffix [<CommonParameters>]
```

## 描述
`Get-AdfsDeviceRegistrationUpnSuffix` 这个 cmdlet 可以获取所有可用于在 Active Directory Federation Services (AD FS) 中注册设备的用户主体名称（UPN）后缀。该 cmdlet 会返回一个包含 UPN 后缀的列表，并说明这些后缀是自动检测到的还是由管理员手动配置的，同时还会显示服务器是否为该 UPN 后缀配置了有效的 SSL 绑定。

## 示例

### 示例 1：获取设备注册服务的 UPN 后缀
```
PS C:\> Get-AdfsDeviceRegistrationUpnSuffix | Format-List
Upn               : contoso.com
SslPort           : 443
IsSetAsSslBinding : True
IsCustom          : False
```

此命令用于获取AD FS中的设备注册服务所接受的UPN后缀的相关信息。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### MicrosoftIdentityServer.ManagementCommands.GetAdfsDeviceRegistrationUpnSuffix+DrsBinding

返回一个或多个 `DrsBinding` 对象，这些对象表示联邦服务（Federation Service）的设备注册服务（UPN）后缀资源。

## 备注

## 相关链接

[Add-AdfsDeviceRegistrationUpnSuffix](./Add-AdfsDeviceRegistrationUpnSuffix.md)

[Remove-AdfsDeviceRegistrationUpnSuffix](./Remove-AdfsDeviceRegistrationUpnSuffix.md)

[Set-AdfsDeviceRegistrationUpnSuffix](./Set-AdfsDeviceRegistrationUpnSuffix.md)
