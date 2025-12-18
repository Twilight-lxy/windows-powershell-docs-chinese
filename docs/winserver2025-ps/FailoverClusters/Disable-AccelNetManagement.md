---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 01/22/2025
online version: https://learn.microsoft.com/powershell/module/failoverclusters/disable-accelnetmanagement?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-AccelNetManagement
---

# 禁用AccelNetManagement

## 摘要
在集群范围内禁用加速网络管理功能。

## 语法

```
Disable-AccelNetManagement [<CommonParameters>]
```

## 描述

在集群范围内禁用AccelNet管理功能。但这并不会关闭虚拟机上的SR-IOV技术。

在集群上禁用此功能不会更改虚拟机上的任何配置设置。这些虚拟机将不再由 AccelNet 管理，也不会被 HUD 跟踪。

## 示例

### 示例 1

```powershell
Disable-AccelNetManagement
```

这个示例会禁用集群上的AccelNet管理层。

## 参数

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接

[Enable-AccelNetManagement](enable-accelnetmanagement.md)

[Get-AccelNetManagement](get-accelnetmanagement.md)

[Get-AccelNetManagementPreReq](get-accelnetmanagementprereq.md)

[Set-AccelNetManagement](set-accelnetmanagement.md)
