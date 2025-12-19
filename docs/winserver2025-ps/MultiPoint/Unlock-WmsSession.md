---
description: 使用这个主题来借助 Windows PowerShell 帮助管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/unlock-wmssession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Unlock-WmsSession
---

# 解锁 WMS 会话

## 摘要
解封用户，使其能够在桌面设备上使用相关功能/服务。

## 语法

### UnlockById
```
Unlock-WmsSession [-SessionId] <UInt32[]> [-Server <String>] [<CommonParameters>]
```

### 解锁全部
```
Unlock-WmsSession [-All] [-Server <String>] [<CommonParameters>]
```

## 描述
`Unlock-WmsSession` cmdlet 可以解除对用户的限制，使其能够使用桌面功能。

## 示例

### 示例 1：解除对某个车站的封锁
```
PS C:\> Unlock-WmsSession -SessionId 3
```

这个命令用于解封一个车站（或站点）。

注意：如果正在运行多点管理器（Multipoint Manager）会话，并且该会话的状态设置为“阻止所有连接”（Block All），那么多点管理器可能会再次阻止该设备进行连接。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: UnlockAll
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定作为该命令目标的多点服务器（MultiPoint Server）的完全限定主机名。默认值为“localhost”。

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
用于指定会话ID。

```yaml
Type: UInt32[]
Parameter Sets: UnlockById
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32[]

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[关闭WMS会话](./Close-WmsSession.md)

[ Disconnect-WmsSession](./Disconnect-WmsSession.md)

[Get-WmsSession](./Get-WmsSession.md)

[Lock-WmsSession](./Lock-WmsSession.md)

