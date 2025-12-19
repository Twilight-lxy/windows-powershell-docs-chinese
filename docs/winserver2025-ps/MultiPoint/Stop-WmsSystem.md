---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/stop-wmssystem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-WmsSystem
---

# 停止 WMS 系统

## 摘要
关闭正在运行 Windows MultiPoint Server 的计算机。

## 语法

```
Stop-WmsSystem [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Stop-WmsSystem` cmdlet 通过使用 Windows 管理规范（WMI）调用来关闭正在运行 MultiPoint Server 的计算机。

## 示例

### 示例 1
```
PS C:\> Stop-WmsSystem
```

这个命令会关闭系统。

## 参数

### -Confirm
在运行cmdlet之前会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Add-WmsSystem](Add-WmsSystem.md)

[Get-WmsSystem](Get-WmsSystem.md)

[Remove-WmsSystem](Remove-WmsSystem.md)

[重启 WMS 系统](Restart-WmsSystem.md)

[Search-WmsSystem](Search-WmsSystem.md)

[Set-WmsSystem](Set-WmsSystem.md)
