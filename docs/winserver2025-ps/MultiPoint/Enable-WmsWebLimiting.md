---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/enable-wmsweblimiting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-WmsWebLimiting
---

# 启用 WMS Web 限制功能

## 摘要
为当前会话启用网页访问限制功能。

## 语法

### WebLimitSession
```
Enable-WmsWebLimiting [-SessionId] <UInt32[]> [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### WebLimitAll
```
Enable-WmsWebLimiting [-All] [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Enable-WmsWebLimiting** cmdlet 为指定的会话启用网页访问限制功能。

## 示例

### 示例 1：为某个会话启用网络访问限制功能
```
PS C:\> Enable-WmsWebLimiting -SessionId 2
```

此命令为本地计算机上的会话2启用Web访问限制功能。

### 示例 2：为所有会话启用网络限制功能
```
PS C:\> Enable-WmsWebLimiting -Server "Sample.microsoft.com" -All
```

此命令为Sample.microsoft.com计算机上的所有会话启用Web访问限制功能。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: WebLimitAll
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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
指定作为该命令目标的多点系统（MultiPoint system）的完全限定主机名。此参数是可选的，如果省略，则默认值为“localhost”。

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
指定一个多点（MultiPoint）会话ID数组，这些ID是该命令的目标对象。

```yaml
Type: UInt32[]
Parameter Sets: WebLimitSession
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

### System.UInt32[]

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[ Disable-WmsWebLimiting](./Disable-WmsWebLimiting.md)

[Get-WmsWebLimiting](./Get-WmsWebLimiting.md)

[Set-WmsWebLimiting](./Set-WmsWebLimiting.md)

