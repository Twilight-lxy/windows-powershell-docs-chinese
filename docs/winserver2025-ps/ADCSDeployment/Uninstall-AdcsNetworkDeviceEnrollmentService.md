---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Deployment.Commands.dll-Help.xml
Module Name: ADCSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsdeployment/uninstall-adcsnetworkdeviceenrollmentservice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Uninstall-AdcsNetworkDeviceEnrollmentService
---

# 卸载 AdcsNetworkDeviceEnrollmentService

## 摘要
卸载NDES角色服务。

## 语法

```
Uninstall-AdcsNetworkDeviceEnrollmentService [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Uninstall-AdcsNetworkDeviceEnrollmentService` cmdlet 用于卸载网络设备注册服务（Network Device Enrollment Service，简称 NDES）角色服务。

## 示例

### 示例 1：卸载 NDES 角色服务

```powershell
Uninstall-AdcsNetworkDeviceEnrollmentService -Force
```

此命令会卸载NDES角色服务，并且不会要求用户输入任何信息。

## 参数

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.CertificateServices.Deployment.Common.NDES.NetworkDeviceEnrollmentServiceResult

## 备注

- Ensure you run Windows PowerShell as an administrator. You can use the **Force** parameter to
  bypass the prompt for confirmation.

## 相关链接

[安装 AdcsNetworkDeviceEnrollmentService](./Install-AdcsNetworkDeviceEnrollmentService.md)
