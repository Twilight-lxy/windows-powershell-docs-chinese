---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 01/22/2025
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-vmadaptersconnectedtoenabledintentswitch?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMAdaptersConnectedToEnabledIntentSwitch
---

# 获取连接到已启用意图切换器的虚拟机适配器

## 摘要
获取连接到已启用意图切换器的虚拟机（VM）上的适配器。

## 语法

```
Get-VMAdaptersConnectedToEnabledIntentSwitch [[-VMName] <String>] [[-VM] <VirtualMachineBase>]
 [<CommonParameters>]
```

## 描述

检索连接到已启用意图交换机的虚拟机上的适配器。

## 示例

### 示例 1

```powershell
Get-VMAdaptersConnectedToEnabledIntentSwitch -VMName "MyVM"
```

这个示例从名为`MyVM`的虚拟机中检索连接到已启用意图交换机（intent switch）的网络适配器。

## 参数

### -VMName

指定虚拟机的名称。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接
