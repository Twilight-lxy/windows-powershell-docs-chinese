---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/remove-iissite?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IISSite
---

# 移除 IISSite

## 摘要
从 IIS 服务器中删除一个网站。

## 语法

```
Remove-IISSite [-Name] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-IISSite` cmdlet 用于从 Internet Information Services (IIS) 服务器中删除具有指定名称的网站。

## 示例

### 示例 1：从 IIS 服务器中删除一个网站
```
PS C:\> Remove-IISSite -Name "TestSite"
```

这个命令会从 IIS 服务器中删除一个名为 “TestSite” 的网站。

## 参数

### -Name
指定要删除的 IIS 网站的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
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
展示了如果该cmdlet被运行会发生的后果。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[获取 IISSite 信息](./Get-IISSite.md)

[New-IISSite](./New-IISSite.md)

[开始使用 IISS 网站](./Start-IISSite.md)

[停止攻击IISS网站](./Stop-IISSite.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

