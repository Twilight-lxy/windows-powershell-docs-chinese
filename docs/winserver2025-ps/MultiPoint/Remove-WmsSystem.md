---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/remove-wmssystem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-WmsSystem
---

# 移除WMS系统

## 摘要
从受管理的系统列表中移除某台计算机。

## 语法

```
Remove-WmsSystem [-ComputerName] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-WmsSystem` cmdlet 会将从指定计算机从受管理系统列表中删除，从而使其不再能够被远程管理。

## 示例

### 示例 1：移除一个多点系统
```
PS C:\> Remove-WmsSystem -ComputerName "sample.microsoft.com"
```

此命令将从可管理的计算机集合中删除名为“sample.microsoft.com”的计算机。

## 参数

### -ComputerName
指定一个包含来自多点系统（MultiPoint System）的计算机主机名称的数组，这些主机名称需要被删除。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### Microsoft.WindowsServerSolutions.MultipointServer.PowerShell Commands.Library.WmsSystem

## 备注

## 相关链接

[Add-WmsSystem](./Add-WmsSystem.md)

[Get-WmsSystem](./Get-WmsSystem.md)

[重启 WMS 系统](./Restart-WmsSystem.md)

[Search-WmsSystem](./Search-WmsSystem.md)

[Set-WmsSystem](./Set-WmsSystem.md)

[Stop-WmsSystem](./Stop-WmsSystem.md)

