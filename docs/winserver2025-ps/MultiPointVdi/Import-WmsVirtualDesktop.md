---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPointVdi.dll-Help.xml
Module Name: MultiPointVdi
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipointvdi/import-wmsvirtualdesktop?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-WmsVirtualDesktop
---

# 导入 WMSVirtualDesktop 模块

## 摘要
创建一个虚拟桌面模板硬盘镜像文件。

## 语法

```
Import-WmsVirtualDesktop -InputFilePath <String> [-VhdLocation <String>] -TemplatePrefix <String> [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Import-WmsVirtualDesktop` cmdlet 会创建 Windows 多点服务（WMS）虚拟交换机（如果该交换机还不存在的话），关闭所有可能正在运行的现有多点服务器虚拟机，并根据指定的 Windows 镜像创建一个模板虚拟机硬盘（.vhd 文件）。

## 示例

### 示例 1：导入模板
```
PS C:\> Import-WmsVirtualDesktop -InputFilePath "C:\Images\Windows10Enterprise.iso" -TemplatePrefix "MyVdiImage" -VhdLocation "C:\MultiPointVhdImages"
```

这个命令创建了一个名为“MyVdiImage”的虚拟机模板，该模板会从C:\images\Windows10Enterprise.iso安装客户操作系统，并将生成的.vhd文件存储在C:\MultiPointVhdImages文件夹中。

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

### -InputFilePath
指定用于虚拟桌面模板的输入文件的完整路径。有效的文件类型包括 `.wim`、`.iso` 或 `.vhd`，这些文件包含将用作客户操作系统的 Windows 版本。

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
指定用于存储模板文件和station.vhd文件的路径。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Get-WmsVirtualDesktop](./Get-WmsVirtualDesktop.md)

[New-WmsVirtualDesktop](./New-WmsVirtualDesktop.md)

[Open-WmsVirtualDesktop](./Open-WmsVirtualDesktop.md)

