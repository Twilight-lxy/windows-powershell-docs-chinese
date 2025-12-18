---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 01/22/2025
online version: https://learn.microsoft.com/powershell/module/failoverclusters/set-accelnetvm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AccelNetVM
---

# Set-AccelNetVM

## 摘要
在虚拟机上启用加速网络功能（Accelerated Networking）。

## 语法

```
Set-AccelNetVM [-VMName] <String> [-Performance] <PerformanceWeight> [<CommonParameters>]
```

## 描述

在虚拟机上启用加速网络功能（Accelerated Networking）。

## 示例

### 示例 1

```powershell
Set-AccelNetVM -VMName "MyVM" -Performance High
```

这个示例为名为“MyVM”的虚拟机设置了加速网络（Accelerated Networking），并将性能级别设置为“High”。

## 参数

### -Performance

设置性能级别。可接受的值有：

- `Low`
- `Medium`
- `High`

```yaml
Type: PerformanceWeight
Parameter Sets: (All)
Aliases:
Accepted values: Low, Medium, High

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMName

指定虚拟机的名称。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接

[Disable-AccelNetVM](disable-accelnetvm.md)

[Enable-AccelNetVM](enable-accelnetvm.md)

[获取 AccelNetVM](get-accelnetvm.md)
