---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsdeviceregistration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsDeviceRegistration
---

# 获取 Adfs 设备注册信息

## 摘要
获取设备注册服务的管理策略。

## 语法

```
Get-AdfsDeviceRegistration [<CommonParameters>]
```

## 描述
**Get-AdfsDeviceRegistration** cmdlet 用于获取 Active Directory Federation Services (AD FS) 中的设备注册服务所使用的管理策略。

## 示例

### 示例 1：获取设备注册服务的设置信息
```
PS C:\> Get-AdfsDeviceRegistration


DrsObjectDN          : CN=DeviceRegistrationService,CN=Device Registration Services,CN=Device Registration Configuration,CN=Services,CN=Configuration,DC=contoso,DC=com
DevicesPerUser       : 10
MaximumInactiveDays  : 90
IsEnabledOnPremises  : True
IsEnabledInCloud     : False
DeviceObjectLocation : CN=RegisteredDevices,DC=contoso,DC=com
```

此命令用于获取 Active Directory Federation Services (AD FS) 中设备注册服务的当前设置。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### DeviceRegistrationServiceObject
此 cmdlet 生成一个 **DeviceRegistrationServiceObject** 对象，该对象表示设备注册服务。该对象包含以下属性：

- DevicesPerUser Type: **Int**
- MaximumInactiveDays Type: **Int**
- IsEnabledOnPremises: Type: **bool**
- IsEnabledInCloud: Type: **bool**
- DeviceObjectLocation: Type: **string**
- DrsObjectDN: Type: **string**

## 备注

## 相关链接

[ Disable-AdfsDeviceRegistration](./Disable-AdfsDeviceRegistration.md)

[ Enable-AdfsDeviceRegistration](./Enable-AdfsDeviceRegistration.md)

[Set-AdfsDeviceRegistration](./Set-AdfsDeviceRegistration.md)

