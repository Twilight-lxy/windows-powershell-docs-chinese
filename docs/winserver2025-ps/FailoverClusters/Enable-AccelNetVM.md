---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 01/22/2025
online version: https://learn.microsoft.com/powershell/module/failoverclusters/enable-accelnetvm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-AccelNetVM
---

# 启用AccelNetVM

## 摘要
在虚拟机上启用加速网络功能。

## 语法

```
Enable-AccelNetVM [-VMName] <String> [-Performance] <PerformanceWeight> [[-VM] <VirtualMachineBase>]
 [<CommonParameters>]
```

## 描述

在虚拟机上启用AccelNet功能。

## 示例

### 示例 1

```powershell
Enable-AccelNetVM -VMName "MyVM" -Performance High
```

此示例为名为“MyVM”的虚拟机启用了AccelNet，并将性能级别设置为“高”。

## 参数

### -Performance

设置性能级别。此参数是必需的。可选的值有：

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

指定虚拟机的名称。此参数是必需的。

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

### -VM

这个VM对象。

```yaml
Type: VirtualMachineBase
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接

[Disable-AccelNetVM](disable-accelnetvm.md)

[获取 AccelerNetVM](get-accelnetvm.md)

[Set-AccelNetVM](set-accelnetvm.md)
