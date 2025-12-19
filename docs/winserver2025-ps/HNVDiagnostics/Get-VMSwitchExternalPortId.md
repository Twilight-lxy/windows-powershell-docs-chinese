---
description: 使用这个主题来借助 Windows PowerShell 帮助管理 Windows 和 Windows Server 技术。
external help file: Get-VMSwitchExternalPortId.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/get-vmswitchexternalportid?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMSwitchExternalPortId
---

# Get-VMSwitchExternalPortId

## 摘要
获取虚拟交换机的外部端口的VFP/VSwitch端口ID。

## 语法

```
Get-VMSwitchExternalPortId [-SwitchName] <String> [<CommonParameters>]
```

## 描述
`Get-VMSwitchExternalPortId` 这个 cmdlet 可以获取虚拟交换机外部端口的 VFP/VSwitch 端口 ID。

## 示例

### 示例 1：获取虚拟交换机的端口 ID
```
PS C:\> Get-VMSwitchExternalPortId -SwitchName "ExternalPrivate"
```

此命令用于获取名为“ExternalPrivate”的交换机的VFP/VSwitch端口ID。

## 参数

### -SwitchName
用于指定虚拟交换机的名称。此 cmdlet 会获取您所指定的交换机的端口 ID。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

