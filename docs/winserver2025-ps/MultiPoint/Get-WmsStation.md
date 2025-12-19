---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/get-wmsstation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WmsStation
---

# Get-WmsStation

## 摘要
获取车站信息。

## 语法

### setId
```
Get-WmsStation [-StationId] <UInt32[]> [-Server <String>] [<CommonParameters>]
```

### GetAll
```
Get-WmsStation [-All] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-WmsStation` cmdlet 可以获取指定站点或所有站点的信息。

## 示例

### 示例 1：获取所有车站的信息
```
PS C:\> Get-WmsStation -All
StationId         : 1
Name              : 1
IsAutoLogOn       : False
IsSplit           : False
CollabId          : 0
RemoteConnectionServerName   :
VirtualMachineName           :
VirtualMachineId  :
AutoLogOnUserName :
AutoLogOnPassword :
DeviceTypes       : {DT_Keyboard, DT_Mouse, DT_Audio, DT_Image...}
DeviceCounts      : {1, 0, 0, 0...}
ComputerName      : Test1
SessionId         : 3
SessionHostServer  : Test1
DisplayOrientation : Landscape
```

这个命令可以获取多点服务器（MultiPoint Server）的工作站信息，同时还会获取与之关联的远程桌面会话ID（如果存在该会话的话）。

如果该站点没有关联任何会话，则会返回 4294967295 作为会话 ID。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: GetAll
Aliases:

Required: False
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

### -StationId
指定一个车站ID数组。

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

### CommonParameters
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32[]

### System.String

## 输出

### Microsoft.WindowsServerSolutions.MultipointServer POWERShell Commands.Library.WmsStation

## 备注

## 相关链接

[Clear-WmsStation](./Clear-WmsStation.md)

[Join-WmsStation](./Join-WmsStation.md)

[Set-WmsStation](./Set-WmsStation.md)

[Split-WmsStation](./Split-WmsStation.md)

[更新 WMS 站点](./Update-WmsStation.md)

