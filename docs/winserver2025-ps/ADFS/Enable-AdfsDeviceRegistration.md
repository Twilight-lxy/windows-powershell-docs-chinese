---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/enable-adfsdeviceregistration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-AdfsDeviceRegistration
---

# 启用 AdFS 设备注册功能

## 摘要
此cmdlet已被弃用。

## 语法

```
Enable-AdfsDeviceRegistration [-Credential <PSCredential>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
此cmdlet在AD FS 2016中已被弃用。有关更多信息，请参阅[使用已注册的设备配置本地条件访问](/windows-server/identity/ad-fs/operations/configure-device-based-conditional-access-on-premises)。

**Enable-AdfsDeviceRegistration** cmdlet 用于配置 Active Directory Federation Services (AD FS) 群集中的某台服务器，以托管设备注册服务（Device Registration Service）。要完全启用该设备注册服务，必须在 AD FS 群集中的每台服务器上运行此命令。在运行此命令之前，必须先执行 **Initialize-ADDeviceRegistration** cmdlet。

## 示例

### 示例 1：启用设备注册服务
```
PS C:\> Enable-AdfsDeviceRegistration
Message                                                     Context                                                                                                          Status
-------                                                     -------                                                                                                          ------
The configuration completed successfully.                   DeploymentSucceeded                                                                                             Success
```

此命令可在AD FS服务器上启用设备注册服务。请注意，您必须对场中的每台AD FS服务器都执行此操作。

## 参数

### -Credential
指定一个 **PSCredential** 对象。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需请求用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行该操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[ Disable-AdfsDeviceRegistration](./Disable-AdfsDeviceRegistration.md)

[Get-AdfsDeviceRegistration](./Get-AdfsDeviceRegistration.md)

[Initialize-ADDeviceRegistration](./Initialize-ADDeviceRegistration.md)

[Set-AdfsDeviceRegistration](./Set-AdfsDeviceRegistration.md)
