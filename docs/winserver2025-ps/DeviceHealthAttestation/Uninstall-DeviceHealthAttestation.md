---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/uninstall-devicehealthattestation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Uninstall-DeviceHealthAttestation
---

# 卸载 DeviceHealthAttestation

## 摘要
卸载设备健康证明（Device Health Attestation）服务。

## 语法

```
Uninstall-DeviceHealthAttestation [-RemoveSslBinding] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Uninstall-DeviceHealthAttestation` cmdlet 用于卸载设备健康认证（Device Health Attestation）服务及其依赖项。该 cmdlet 还会删除与传入请求相关的防火墙规则、相关 Web 应用程序以及应用程序池。

您必须具有管理员权限才能运行此cmdlet。

## 示例

### 示例 1：卸载设备健康认证（Device Health Attestation）服务
```
PS C:\> Uninstall-DeviceHealthAttestation
```

此命令用于卸载设备健康认证（Device Health Attestation）服务。

### 示例 2：卸载具有 SSL 绑定的设备健康认证（Device Health Attestation）服务
```
PS C:\> Uninstall-DeviceHealthAttestation -RemoveSslBinding
```

## 参数

### -Confirm
在运行cmdlet之前会提示您进行确认。

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
强制命令执行，而无需请求用户确认。

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

### -RemoveSslBinding
从默认网站中移除SSL绑定（即取消使用SSL加密）。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[安装设备健康认证功能](./Install-DeviceHealthAttestation.md)

