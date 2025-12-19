---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/disable-wmsweblimiting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-WmsWebLimiting
---

# 禁用 WMS Web 限制功能

## 摘要
禁用某个会话期间的网络限制功能。

## 语法

### WebLimitSession
```
Disable-WmsWebLimiting [-SessionId] <UInt32[]> [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### WebLimitAll
```
Disable-WmsWebLimiting [-All] [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-WmsWebLimiting` cmdlet 会禁用指定会话中的网页访问限制功能。

## 示例

#### 示例 1：禁用指定会话的网页访问限制功能
```
PS C:\> Disable-WmsWebLimiting -SessionId 2,4,5,6
```

此命令会禁用本地计算机上第2、4、5和6个会话的网页访问限制功能。

#### 示例 2：禁用所有会话的网络限制功能
```
PS C:\> Disable-WmsWebLimiting -Server "sampleserver.microsoft.com" -All
```

此命令将取消对 computersampleserver.microsoft.com 上所有会话的网络限制功能。

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
指定作为该命令目标的多点服务器（MultiPoint Server）的完全限定主机名。默认值为 `localhost`。

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
指定一个包含多个多点（MultiPoint）会话 ID 的数组。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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

### uint[]
你可以将一个会话ID数组传递给这个cmdlet。

## 输出

## 备注

## 相关链接

[Enable-WmsWebLimiting](./Enable-WmsWebLimiting.md)

[Get-WmsWebLimiting](./Get-WmsWebLimiting.md)

[Set-WmsWebLimiting](./Set-WmsWebLimiting.md)

