---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsdeviceregistrationupnsuffix?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsDeviceRegistrationUpnSuffix
---

# 设置 AdFS 设备注册 UPN 后缀

## 摘要
用于设置 UPN 后缀的列表。

## 语法

```
Set-AdfsDeviceRegistrationUpnSuffix [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsDeviceRegistrationUpnSuffix` 这个cmdlet用于设置在将设备注册到Active Directory Federation Services（AD FS）时可以使用的用户主体名称（UPN）后缀列表。该cmdlet会检测组织中正在使用的UPN后缀，并配置与这些UPN后缀对应的Secure Sockets Layer（SSL）绑定信息。

任何被发现的 UPN 后缀都必须在 AD FS 的 SSL 证书中具有对应的注册名称；例如，`enterpriseregistration.upn` 后缀。您也可以使用一个通配符 SSL 证书来覆盖所有可能的注册名称。此 cmdlet 不会影响您通过运行 **Add-AdfsDeviceRegistrationUpnSuffix** cmdlet 手动设置的自定义 UPN 后缀。

## 示例

### 示例 1：设置 UPN 后缀列表
```
PS C:\> Set-AdfsDeviceRegistrationUpnSuffix
```

此命令设置了在注册设备时可以使用的UPN后缀列表。

### 示例 2：在不进行确认的情况下设置 UPN 后缀列表
```
PS C:\> Set-AdfsDeviceRegistrationUpnSuffix -Force
```

此命令会直接设置 UPN 后缀列表，而不会询问您是否确认。

## 参数

### -Force
强制命令运行，而无需用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.ManagementAutomation.SwitchParameter

`SwitchParameter` 对象是通过 `Force` 参数接收到的。

## 输出

## 备注

## 相关链接

[Add-AdfsDeviceRegistrationUpnSuffix](./Add-AdfsDeviceRegistrationUpnSuffix.md)

[Get-AdfsDeviceRegistrationUpnSuffix](./Get-AdfsDeviceRegistrationUpnSuffix.md)

[Remove-AdfsDeviceRegistrationUpnSuffix](./Remove-AdfsDeviceRegistrationUpnSuffix.md)

