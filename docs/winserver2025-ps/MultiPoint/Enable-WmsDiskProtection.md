---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/enable-wmsdiskprotection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-WmsDiskProtection
---

# 启用WMS磁盘保护功能

## 摘要
启用磁盘保护功能。

## 语法

```
Enable-WmsDiskProtection [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-WmsDiskProtection` 这个 cmdlet 用于安装磁盘保护过滤器驱动程序，将该驱动程序设置为“丢弃模式”，并重新启动系统以启用磁盘保护功能。

## 示例

### 示例 1：启用磁盘保护
```
PS C:\> Enable-WmsDiskProtection -Server "Sample.microsoft.com"
```

此命令在计算机 Sample.microsoft.com 上安装磁盘保护过滤驱动程序，并将驱动程序配置为“丢弃”模式。随后重新启动计算机以应用该更改。

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

### -Server
指定该命令的目标（即MultiPoint Server）的完全限定主机名。默认值为“localhost”。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ComputerName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Disable-WmsDiskProtection](./Disable-WmsDiskProtection.md)

[Get-WmsDiskProtection](./Get-WmsDiskProtection.md)

[Resume-WmsDiskProtection](./Resume-WmsDiskProtection.md)

[暂停 WMS 磁盘保护功能](./Suspend-WmsDiskProtection.md)

