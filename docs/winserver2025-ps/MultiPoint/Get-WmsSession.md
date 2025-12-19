---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/get-wmssession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WmsSession
---

# Get-WmsSession

## 摘要
获取会话信息。

## 语法

### getContent
```
Get-WmsSession [-SessionId] <UInt32[]> [-Thumbnail <ThumbnailSizePS>] [-Server <String>] [<CommonParameters>]
```

### GetAll
```
Get-WmsSession [-All] [-Thumbnail <ThumbnailSizePS>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-WmsSession` cmdlet 可以获取指定会话的所有信息，或者获取所有会话的信息。

## 示例

### 示例 1：获取所有会话
```
PS C:\> Get-WmsSession -All
SessionId    : 2
State        : RemoteConnection
IsOrchestratable    : False
IsAdmin      : True
IsMOGUser    : True
UserName     : Test
StationId    : 0
ComputerName : Test1
ClientName   : Test2
DomainName   : TestDomain
IsRail       : False
SessionId    : 3
State        : ConnectedToStation
IsOrchestratable    : False
IsAdmin      : True
IsMOGUser    : True
UserName     : Administrator
StationId    : 1
ComputerName : Test1
ClientName   : Test1
DomainName   : TestDomain
IsRail       : False
```

这个命令可以获取所有会话的会话信息。ID为2的会话是一个远程会话，而ID为3的会话则连接到了一个本地的Windows MultiPoint Server站点上。


## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: GetAll
Aliases:

Required: True
Position: Named
Default value: None
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
指定一个会话ID数组。

```yaml
Type: UInt32[]
Parameter Sets: GetById
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Thumbnail
指定会话缩略图的尺寸。

```yaml
Type: ThumbnailSizePS
Parameter Sets: (All)
Aliases:
Accepted values: Small, Medium, Large, FullScreen

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32[]

### System.String

## 输出

### Microsoft.WindowsServerSolutions.MultipointServer.PowerShellCommands.Library.WmsSession

## 备注

## 相关链接

[关闭WMS会话](./Close-WmsSession.md)

[disconnect-WmsSession](./ Disconnect-WmsSession.md)

[Lock-WmsSession](./Lock-WmsSession.md)

[解锁 WMS 会话](./Unlock-WmsSession.md)

