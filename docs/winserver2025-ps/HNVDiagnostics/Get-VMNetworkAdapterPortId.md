---
description: 使用这个主题来借助 Windows PowerShell 帮助管理 Windows 和 Windows Server 技术。
external help file: Get-VMNetworkAdapterPortId.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/get-vmnetworkadapterportid?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMNetworkAdapterPortId
---

# Get-VMNetworkAdapterPortId

## 摘要
获取 VFP/VSwitch 端口 ID。

## 语法

```
Get-VMNetworkAdapterPortId [[-VMName] <String>] [[-VMNetworkAdapterName] <String>] [<CommonParameters>]
```

## 描述
`Get-VMNetworkAdapterPortId` cmdlet 可用于获取虚拟机或基础设施端口的 VFP/VSwitch 端口 ID。此外，该 cmdlet 还会返回与该端口相连的虚拟交换机的友好名称以及端口的名称。

## 示例

### 示例 1：获取虚拟机网络适配器的端口 ID
```
PS C:\> ($switchName, $portId, $portName) = Get-VMNetworkAdapterPortId -VMName "vm1" -VMNetworkAdapterName "VMAdapter"
```

### 示例 2：获取基础设施端口的端口 ID
```
PS C:\> ($switchName, $portId, $portName) = Get-VMNetworkAdapterPortId -VMNetworkAdapterName "HostAdapter"
```

这个命令用于获取某个基础设施端口的端口ID，然后将其保存到指定的变量中。

## 参数

### -VMName
指定要检索端口ID的虚拟机的名称。

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

### -VMNetworkAdapterName
指定用于检索端口ID的虚拟机网络适配器的名称。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

