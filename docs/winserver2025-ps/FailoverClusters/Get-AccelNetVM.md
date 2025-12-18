---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 01/22/2025
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-accelnetvm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AccelNetVM
---

# Get-AccelNetVM

## 摘要
可以获取配备加速网络的虚拟机（VMs）。

## 语法

```
Get-AccelNetVM [[-VMName] <String>] [[-VM] <VirtualMachineBase>] [<CommonParameters>]
```

## 描述

检索启用了AccelNet功能的虚拟机。

## 示例

### 示例 1

```powershell
Get-AccelNetVM -VMName "MyVM"
```

这个示例用于检索一个名为 `MyVM` 的虚拟机。

如果未提供 `-VMName` 参数，则会检索所有虚拟机的名称。

### 示例 2

```powershell
$vm = Get-VM -Name "MyVM"
Get-AccelNetVM -VM $vm
```

这个示例用于检索名为 `MyVM` 的虚拟机（VM）对应的对象信息。

## 参数

### -VMName

虚拟机的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM

VM对象。

```yaml
Type: VirtualMachineBase
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接

[禁用 AccelerNetVM](disable-accelnetvm.md)

[启用-AccelNetVM](enable-accelnetvm.md)

[Set-AccelNetVM](set-accelnetvm.md)
