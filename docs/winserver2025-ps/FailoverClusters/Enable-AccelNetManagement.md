---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 01/22/2025
online version: https://learn.microsoft.com/powershell/module/failoverclusters/enable-accelnetmanagement?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-AccelNetManagement
---

# 启用AccelNet管理功能

## 摘要
在整个集群范围内启用加速网络管理功能。

## 语法

```
Enable-AccelNetManagement [-IntentName] <String> [[-NodeReservePercentage] <UInt32>]
 [<CommonParameters>]
```

## 描述

该设置可全局启用 AccelNet Management 功能；同时还会指定需要预留的节点数量，并实现 AccelNet Management 所要求的各项功能。

## 示例

### 示例 1

```powershell
Enable-AccelNetManagement -IntentName "MyIntent" -NodeReservePercentage 25
```

这个示例用于启用用于加速网络管理的`MyIntent`意图，并为此目的预留了25%的节点资源。如果命令执行成功，它将返回 `$true`；如果出现错误，则会返回 `$false`。

## 参数

### -IntentName

用于加速网络管理的意图名称。此参数是必需的。

这个值必须是一个大于或等于 0 且小于或等于 99 的整数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NodeReservePercentage

在同时保持每个被选用于加速网络管理的虚拟机所需的足够虚拟函数的情况下，可以宕机的集群节点所占的百分比。

如果此参数留空，则会默认设置为 **50%**。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: $NODE_RESERVE_PERCENTAGE_DEFAULT
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接

[禁用AccelerNet管理功能](disable-accelnetmanagement.md)

[Get-AccelNetManagement](get-accelnetmanagement.md)

[获取AccelerNet管理前置要求](get-accelnetmanagementprereq.md)

[Set-AccelNetManagement](set-accelnetmanagement.md)
