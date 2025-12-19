---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPointVdi.dll-Help.xml
Module Name: MultiPointVdi
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipointvdi/enable-wmsvirtualdesktoprole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-WmsVirtualDesktopRole
---

# 启用 WMS 虚拟桌面角色

## 摘要
安装Hyper-V虚拟桌面角色，并对其进行定制以便与MultiPoint服务一起使用。

## 语法

```
Enable-WmsVirtualDesktopRole [-Restart] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-WmsVirtualDesktopRole` 这个 cmdlet 会安装虚拟桌面相关的 Hyper-V 角色（如果该角色尚未安装的话），并且还可以选择性地重启计算机以使更改生效。

## 示例

#### 示例 1：安装 Hyper-V 虚拟桌面角色
```
PS C:\> Enable-WmsVirtualDesktopRole -Restart
```

此命令会安装 Hyper-V 虚拟桌面角色，并重新启动计算机以应用该更改。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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
展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行该 cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[禁用 WMS 虚拟桌面角色](./Disable-WmsVirtualDesktopRole.md)

