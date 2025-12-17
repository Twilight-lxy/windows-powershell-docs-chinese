---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Deployment.Commands.dll-Help.xml
Module Name: ADCSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsdeployment/uninstall-adcswebenrollment?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Uninstall-AdcsWebEnrollment
---

# 卸载 AdcsWebEnrollment

## 摘要
卸载CA Web Enrollment角色服务。

## 语法

```
Uninstall-AdcsWebEnrollment [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Uninstall-AdcsWebEnrollment` cmdlet 用于删除证书颁发机构（CA）的 Web 注册角色服务。

## 示例

#### 示例 1：卸载 CA Web Enrollment 角色服务

```powershell
Uninstall-AdcsWebEnrollment -Force
```

此命令会卸载“CA Web Enrollment”角色服务，且无需用户确认。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.CertificateServices.Deployment(Common.WEP.WebEnrollmentResult

## 备注

- Ensure you run Windows PowerShell as an administrator. You can use the **Force** parameter to
  bypass the prompt for confirmation.

## 相关链接

[Install-AdcsWebEnrollment](./Install-AdcsWebEnrollment.md)
