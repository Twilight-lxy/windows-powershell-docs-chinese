---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/set-dhassupportedauthenticationschema?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DHASSupportedAuthenticationSchema
---

# Set-DHASSupportedAuthenticationSchema

## 摘要
设置身份验证方案。

## 语法

```
Set-DHASSupportedAuthenticationSchema [-SupportedAuthenticationSchema] <String> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-DHASSupportedAuthenticationSchema` cmdlet 用于设置设备健康认证（Device Health Attestation）服务所支持的认证方案。

您必须具有管理员权限才能运行此cmdlet。

## 示例

### 示例 1：设置身份验证方案以支持
```
PS C:\> Set-DHASSupportedAuthenticationSchema -SupportedAuthenticationSchema "AikPub,EkCertificate"
```

这个命令用于设置支持的认证模式。

## 参数

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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
强制命令运行，而不需要用户确认。

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

### -SupportedAuthenticationSchema
以逗号分隔的形式指定设备健康证明服务支持的认证方案。该参数的可接受值如下：

- AikPub
- AikCertificate
- EkCertificate

You cannot specify both AikCertificate and EkCertificate in the same command.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

