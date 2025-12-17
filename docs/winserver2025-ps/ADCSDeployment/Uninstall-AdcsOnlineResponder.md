---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Deployment.Commands.dll-Help.xml
Module Name: ADCSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsdeployment/uninstall-adcsonlineresponder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Uninstall-AdcsOnlineResponder
---

# 卸载 AdcsOnlineResponder

## 摘要
卸载“在线响应器”服务。

## 语法

```
Uninstall-AdcsOnlineResponder [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Uninstall-AdcsOnlineResponder` cmdlet 用于卸载在线响应程序（Online Responder）角色服务。

## 示例

#### 示例 1：卸载“Online Responder”角色服务

```powershell
Uninstall-AdcsOnlineResponder -Force
```

此命令会删除“Online Responder”角色服务，且无需确认操作。

## 参数

### -Confirm

在运行该 cmdlet 之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

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

### -WhatIf

展示了如果该cmdlet被运行会发生什么情况。但实际上这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.CertificateServices.Deployment.Common.OCSP.OnlineResponderResult

## 备注

- Ensure you run Windows PowerShell as an administrator. You can use the **Force** parameter to
  bypass the prompt for confirmation.

## 相关链接

[安装 AdcsOnlineResponder](./Install-AdcsOnlineResponder.md)
