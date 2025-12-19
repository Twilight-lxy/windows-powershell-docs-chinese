---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/hide-wmsidentifier?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Hide-WmsIdentifier
---

# 隐藏 WMS 标识符

## 摘要
隐藏车站或会话的识别窗口。

## 语法

### HideIdentifyBySessionId
```
Hide-WmsIdentifier [-SessionId <UInt32[]>] [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 隐藏通过车站ID进行识别（HideIdentifyByStationId）
```
Hide-WmsIdentifier [-StationId <UInt32[]>] [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 隐藏所有识别信息
```
Hide-WmsIdentifier [-All] [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Hide-WmsIdentifier** cmdlet 用于隐藏指定站点或会话的识别窗口。

## 示例

### 示例 1：隐藏会话的识别窗口
```
PS C:\> Hide-WmsIdentifier -SessionID 2
```

这个命令会隐藏ID为2的会话的识别窗口。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: HideIdentifyAll
Aliases:

Required: True
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

### -Server
指定该命令的目标即多点服务器（MultiPoint Server）的完全限定主机名。默认值为“localhost”。

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

### -SessionId
指定一个会话ID数组。

```yaml
Type: UInt32[]
Parameter Sets: HideIdentifyBySessionId
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StationId
指定一个车站ID数组。

```yaml
Type: UInt32[]
Parameter Sets: HideIdentifyByStationId
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32[]

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Show-WmsIdentifier](./Show-WmsIdentifier.md)

