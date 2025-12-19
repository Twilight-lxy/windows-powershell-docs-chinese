---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPointVdi.dll-Help.xml
Module Name: MultiPointVdi
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipointvdi/get-wmsvirtualdesktop?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WmsVirtualDesktop
---

# Get-WmsVirtualDesktop

## 摘要
获得一个虚拟桌面。

## 语法

```
Get-WmsVirtualDesktop [-VirtualMachineName <String>] [<CommonParameters>]
```

## 描述
`Get-WmsVirtualDesktop` cmdlet 可以获取指定的虚拟桌面；如果未指定 `VirtualMachineName` 参数，则会获取所有虚拟桌面。

## 示例

### 示例 1：通过名称获取虚拟桌面
```
PS C:\> Get-WmsVirtualDesktop -VirtualMachineName "MyDesktop"
```

这个命令用于获取名为“MyDesktop”的虚拟桌面。

## 参数

### -VirtualMachineName
指定要获取的虚拟桌面的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Import-WmsVirtualDesktop](./Import-WmsVirtualDesktop.md)

[New-WmsVirtualDesktop](./New-WmsVirtualDesktop.md)

[Open-WmsVirtualDesktop](./Open-WmsVirtualDesktop.md)

