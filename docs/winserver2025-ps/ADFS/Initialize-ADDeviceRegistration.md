---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/initialize-addeviceregistration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Initialize-ADDeviceRegistration
---

# 初始化 AD 设备注册

## 摘要
在 Active Directory 林中初始化设备注册服务的配置。

## 语法

```
Initialize-ADDeviceRegistration -ServiceAccountName <String> [-DeviceLocation <String>]
 [-RegistrationQuota <UInt32>] [-MaximumRegistrationInactivityPeriod <UInt32>] [-Credential <PSCredential>]
 [-Force] [-DiscoveryName <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Initialize-ADDeviceRegistration` cmdlet 用于初始化 Active Directory 林中的设备注册服务配置。要运行此 cmdlet，您必须使用企业管理员权限登录，并且您的 Active Directory 林必须包含 Windows Server 2012 R2 的架构。要将设备加入工作场所，在成功运行此 cmdlet 后，还需要在每台 Active Directory Federation Services (AD FS) 服务器上运行 `Enable-AdfsDeviceRegistration` cmdlet。

## 示例

#### 示例 1：初始化设备注册服务
```
PS C:\> Initialize-ADDeviceRegistration -ServiceAccountName "CONTOSO\svc_adfs" -DeviceLocation "Contoso.com" -RegistrationQuota 10 -MaximumRegistrationInactivityPeriod 90 -Credential ContosoAdmin
```

此命令用于在 Active Directory 林中初始化设备注册服务（Device Registration Service）。

## 参数

### -Credential
指定一个基于用户名和密码的 **PSCredential** 对象。该账户必须是 Enterprise Admins 组的成员。要获取 **PSCredential** 对象，请使用 **Get-Credential** cmdlet。有关更多信息，请输入 `Get-Help Get-Credential`。

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

### -DeviceLocation
指定用于存储设备对象的域。请在当前的森林（domain structure）中选择一个域。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DiscoveryName
指定一个发现名称（discovery name）。

```yaml
Type: String
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

### -MaximumRegistrationInactivityPeriod
指定由于设备对象处于不活动状态而将其删除之前的最长等待天数。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RegistrationQuota
指定单个用户可以注册的最大设备数量。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ServiceAccountName
指定要授予其读写权限的账户，以便该账户能够访问 Active Directory 中的设备注册服务配置文件及相关容器。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Enable-AdfsDeviceRegistration](./Enable-AdfsDeviceRegistration.md)

