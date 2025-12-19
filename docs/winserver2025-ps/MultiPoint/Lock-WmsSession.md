---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/lock-wmssession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Lock-WmsSession
---

# Lock-WmsSession

## 摘要
为用户锁定会话。

## 语法

### LockById
```
Lock-WmsSession [-SessionId] <UInt32[]> [-Message] <String> [-Server <String>] [<CommonParameters>]
```

### LockAll
```
Lock-WmsSession [-All] [-Message] <String> [-Server <String>] [<CommonParameters>]
```

## 描述
`Lock-WmsSession` cmdlet 可以阻止特定用户使用桌面功能。您还可以指定一条消息，在用户的屏幕上显示该消息。

## 示例

### 示例 1：锁定会话
```
PS C:\> Lock-WmsSession -SessionId 3 -Message "Your station is locked"
```

此命令会锁定指定的会话，并向用户显示“您的站点已被锁定”的消息。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: LockAll
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Message
指定要显示的消息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定该命令的目标多点服务器（MultiPoint Server）的完全限定主机名。默认值为 localhost。

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
Parameter Sets: LockById
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32[]

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Close-WmsSession](./Close-WmsSession.md)

[ Disconnect-WmsSession](./Disconnect-WmsSession.md)

[Get-WmsSession](./Get-WmsSession.md)

[解锁 WMS 会话](./Unlock-WmsSession.md)

