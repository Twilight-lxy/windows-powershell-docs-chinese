---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/disable-adfsdeviceregistration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-AdfsDeviceRegistration
---

# 禁用 AdFS 设备注册功能

## 摘要
将设备注册服务标记为在 AD FS 服务器上处于禁用状态。

## 语法

```
Disable-AdfsDeviceRegistration [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-AdfsDeviceRegistration` cmdlet 用于在 Active Directory Federation Services (AD FS) 服务器上将设备注册服务标记为已禁用状态。若要完全禁用该设备注册服务，必须在您的 AD FS 集群中的每台 AD FS 服务器上运行此命令。

## 示例

### 示例 1：禁用 Windows Server 设备注册服务
```
PS C:\> Disable-AdfsDeviceRegistration
```

此命令会将在活动目录联合服务（AD FS）服务器上的设备注册服务设置为禁用状态。

## 参数

### -Confirm
在运行 cmdlet 之前会提示您确认是否要继续执行该操作。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[ Enable-AdfsDeviceRegistration](./Enable-AdfsDeviceRegistration.md)

[Get-AdfsDeviceRegistration](./Get-AdfsDeviceRegistration.md)

[Set-AdfsDeviceRegistration](./Set-AdfsDeviceRegistration.md)

