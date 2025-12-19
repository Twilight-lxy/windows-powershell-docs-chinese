---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPointVdi.dll-Help.xml
Module Name: MultiPointVdi
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipointvdi/disable-wmsvirtualdesktoprole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-WmsVirtualDesktopRole
---

# 禁用 WMSVirtualDesktopRole 角色

## 摘要
禁用Hyper-V虚拟桌面角色。

## 语法

```
Disable-WmsVirtualDesktopRole [-Restart] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-WmsVirtualDesktopRole` cmdlet 会将所有工作站从虚拟桌面基础设施（VDI）模式切换到远程桌面会话主机（RDSH）模式，然后卸载 Hyper-V 虚拟桌面相关组件。如果指定了 `Restart` 参数，系统将重新启动以应用这些更改。

## 示例

### 示例 1：禁用虚拟桌面
```
PS C:\> Disable-WmsVirtualDesktopRole -Restart
```

此命令会将所有终端从远程桌面虚拟化主机（RDVH）会话切换到RDSH会话，移除Hyper-V虚拟桌面角色，并自动重启计算机以应用这些更改。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Restart
表示此操作会自动重启计算机以应用所做的更改。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生的结果。但实际上该cmdlet并未被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Enable-WmsVirtualDesktopRole](./Enable-WmsVirtualDesktopRole.md)

