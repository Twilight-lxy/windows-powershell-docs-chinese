---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPointVdi.dll-Help.xml
Module Name: MultiPointVdi
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipointvdi/new-wmsvirtualdesktop?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-WmsVirtualDesktop
---

# 新WMS虚拟桌面

## 摘要
创建一个虚拟桌面。

## 语法

### CreateVirtualDesktopById
```
New-WmsVirtualDesktop [-StationId] <UInt32[]> -InputFilePath <String> [-VhdLocation <String>]
 -TemplatePrefix <String> [-Domain <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### CreateAllVirtualDesktops
```
New-WmsVirtualDesktop [-All] -InputFilePath <String> [-VhdLocation <String>] -TemplatePrefix <String>
 [-Domain <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-WmsVirtualDesktop` cmdlet 根据指定的虚拟桌面模板为某个或多个多点设备（MultiPoint station）创建虚拟桌面，并在此过程中替换现有的所有设备。

## 示例

### 示例 1：为计算机上的所有站点创建一个虚拟桌面
```
PS C:\> New-WmsVirtualDesktop -All -InputFilePath "C:\Images\Windows10Enterprise.iso" -TemplatePrefix "MyVdiImage" -VhdLocation "C:\MultiPointVhdImages"
```

该命令会从位于 C:\Images\Windows10Enterprise.iso 文件夹中的模板为计算机上的所有工作站创建一个虚拟桌面。

## 参数

### -All
表示此操作会为所有站点创建一个虚拟桌面。

```yaml
Type: SwitchParameter
Parameter Sets: CreateAllVirtualDesktops
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

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
指定用于存放虚拟桌面的 Active Directory 域的名称。

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

### -InputFilePath
指定用于虚拟桌面模板的输入文件的完整路径。有效的文件类型包括.wim、.iso或.vhd，这些文件包含了将用作客户操作系统的Windows版本。

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

### -StationId
指定一个车站ID数组，用于创建虚拟桌面。

```yaml
Type: UInt32[]
Parameter Sets: CreateVirtualDesktopById
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TemplatePrefix
指定用于虚拟机模板名称的前缀。

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

### -VhdLocation
指定用于存储模板文件和站点的.vhd文件的路径。

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

### -WhatIf
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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

[Open-WmsVirtualDesktop](./Open-WmsVirtualDesktop.md)

