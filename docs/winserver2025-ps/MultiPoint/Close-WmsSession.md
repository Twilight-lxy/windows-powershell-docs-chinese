---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/close-wmssession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Close-WmsSession
---

# 关闭 WMS 会话

## 摘要
将用户从指定的会话中登出。

## 语法

### CloseById
```
Close-WmsSession [-SessionId] <UInt32[]> [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### CloseAll
```
Close-WmsSession [-All] [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Close-WmsSession` cmdlet 会注销指定会话中的用户。只有管理员才能关闭管理员会话。你无法关闭使用该 cmdlet 启动的会话。

## 示例

### 示例 1：关闭会话
```
PS C:\> Close-WmsSession -SessionId 3
```

这个命令会关闭ID为3的远程桌面会话。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: CloseAll
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
指定该命令的目标端——即多点服务器（MultiPoint Server）的完整限定主机名。默认值为“localhost”。

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
Parameter Sets: CloseById
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无
如果指定的会话ID找不到，此cmdlet将返回一个**ItemNotFoundException**。

## 备注

## 相关链接

[ Disconnect-WmsSession](./Disconnect-WmsSession.md)

[Get-WmsSession](./Get-WmsSession.md)

[Lock-WmsSession](./Lock-WmsSession.md)

[解锁 WMS 会话](./Unlock-WmsSession.md)

