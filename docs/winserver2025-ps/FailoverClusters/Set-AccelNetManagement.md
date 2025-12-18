---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 01/22/2025
online version: https://learn.microsoft.com/powershell/module/failoverclusters/set-accelnetmanagement?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AccelNetManagement
---

# Set-AccelNetManagement

## 摘要
在整个集群范围内设置加速网络管理功能。

## 语法

```
Set-AccelNetManagement [[-IntentName] <String>] [[-NodeReservePercentage] <UInt32>]
 [<CommonParameters>]
```

## 描述

在集群范围内设置 AccelNet Management 的相关配置。同时会指定需要预留的节点数量，并启用AccelNet Management的相关功能。操作成功时返回 `$true`，否则返回 `$false`。

如果 AccelNet Management 当前处于活动状态并具有某种特定的意图（即正在执行某个任务），那么为 `-IntentName` 参数提供一个值将会使当前的 AccelNet Management 配置失效。在当前配置失效后，AccelNet Management 会根据新的意图设置重新启用。

## 示例

### 示例 1

```powershell
Set-AccelNetManagement -IntentName "LowPerformance" -NodeReservePercentage 10
```

这个示例为 AccelNet Management 启用了 `LowPerformance` 意图（即降低性能的运行模式），并为此目的预留了 10% 的节点资源。如果命令执行成功，它将返回 `$true`；如果出现错误，则会返回 `$false`。

## 参数

### -IntentName

用于AccelNet管理的意图名称。此参数是必需的。

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

在保持为每个被选用于加速网络管理的虚拟机提供足够虚拟函数的前提下，能够同时宕机的集群节点所占的百分比。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接

[禁用 AccelerNet Management](disable-accelnetmanagement.md)

[启用加速网络管理功能](enable-accelnetmanagement.md)

[Get-AccelNetManagement](get-accelnetmanagement.md)

[Get-AccelNetManagementPreReq](get-accelnetmanagementprereq.md)
