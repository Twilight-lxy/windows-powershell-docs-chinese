---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 01/22/2025
online version: https://learn.microsoft.com/powershell/module/failoverclusters/disable-accelnetvm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-AccelNetVM
---

# 禁用 AccelNetVM

## 摘要
禁用虚拟机上的加速网络功能（Accelerated Networking）。

## 语法

```
Disable-AccelNetVM [-VMName] <String> [<CommonParameters>]
```

## 描述

禁用虚拟机上的加速网络功能（Accelerated Networking）。

## 示例

### 示例 1

```powershell
Disable-AccelNetVM -VMName "MyVM"
```

这个示例会禁用名为`MyVM`的虚拟机的加速网络（Accelerated Networking）功能。

## 参数

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接

[启用-AccelNetVM](enable-accelnetvm.md)

[Get-AccelNetVM](get-accelnetvm.md)

[Set-AccelNetVM](set-accelnetvm.md)
