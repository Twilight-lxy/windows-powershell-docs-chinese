---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPointVdi.dll-Help.xml
Module Name: MultiPointVdi
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipointvdi/open-wmsvirtualdesktop?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Open-WmsVirtualDesktop
---

# Open-WmsVirtualDesktop

## 摘要
打开一个窗口，该窗口连接到虚拟桌面模板。

## 语法

```
Open-WmsVirtualDesktop -TemplateVirtualMachineGuid <String> [-Domain <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Open-WmsVirtualDesktop` 这个 cmdlet 会打开一个窗口，该窗口连接到指定的虚拟桌面模板。通过这个功能，你可以自定义该虚拟桌面模板，从而创建出符合自己需求的虚拟桌面。

## 示例

#### 示例 1：打开一个窗口，进入虚拟桌面模板
```
PS C:\> Open-WmsVirtualDesktop -TemplateVirtualMachineGuid "53F56307-B6BF-11D0-94F2-00A0C91EFB8B"
```

这个命令会打开一个窗口，该窗口连接到虚拟桌面模板，其ID为53F56307-B6BF-11D0-94F2-00A0C91EFB8B。

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

### -Domain
指定包含虚拟桌面模板的活动目录（Active Directory）域的名称。

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

### -TemplateVirtualMachineGuid
指定虚拟桌面模板的 Hyper-V 虚拟机 ID。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Get-WmsVirtualDesktop](./Get-WmsVirtualDesktop.md)

[Import-WmsVirtualDesktop](./Import-WmsVirtualDesktop.md)

[New-WmsVirtualDesktop](./New-WmsVirtualDesktop.md)

