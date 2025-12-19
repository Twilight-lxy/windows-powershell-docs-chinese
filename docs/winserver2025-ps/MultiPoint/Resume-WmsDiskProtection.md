---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/resume-wmsdiskprotection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Resume-WmsDiskProtection
---

# WMS磁盘保护方案概述

## 摘要
将磁盘保护模式切换为“丢弃”模式。

## 语法

```
Resume-WmsDiskProtection [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Resume-WmsDiskProtection` cmdlet 将磁盘保护功能从被动模式切换到丢弃模式，并重新启动计算机以应用状态变化。

## 示例

#### 示例 1：切换到丢弃模式
```
PS C:\> Resume-WmsDiskProtection -Server "sample.microsoft.com"
```

此命令将磁盘保护功能的配置从“被动模式”更改为“丢弃模式”，然后重启计算机以应用状态变更。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行操作。

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
指定该命令的目标的多点服务器（MultiPoint Server）的完全限定主机名。默认值为 `localhost`。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[ Disable-WmsDiskProtection](./Disable-WmsDiskProtection.md)

[Enable-WmsDiskProtection](./Enable-WmsDiskProtection.md)

[Get-WmsDiskProtection](./Get-WmsDiskProtection.md)

[暂停 WMS 磁盘保护功能](./Suspend-WmsDiskProtection.md)

