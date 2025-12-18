---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 01/22/2025
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-accelnetmanagementprereq?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AccelNetManagementPreReq
---

# 获取 AccelNet Management 的先决条件信息

## 摘要
如果集群节点支持加速网络（Accelerated Networking），则会通知用户。

## 语法

```
Get-AccelNetManagementPreReq [[-IntentName] <String>] [<CommonParameters>]
```

## 描述

如果集群节点支持加速网络（Accelerated Networking）功能，该工具会检索相关信息，包括验证操作系统版本和超线程状态。

## 示例

### 示例 1

```powershell
Get-AccelNetManagementPreReq -IntentName "MyIntent"
```

这个示例用于检查集群节点是否支持名为`MyIntent`的意图（intention）所使用的AccelNet技术。

## 参数

### -IntentName

用于加速网络管理的意图名称。此参数是必需的。

这个值必须是一个大于或等于 **0** 且小于或等于 **99** 的整数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Disable-AccelNetManagement](disable-accelnetmanagement.md)

[Enable-AccelNetManagement](enable-accelnetmanagement.md)
