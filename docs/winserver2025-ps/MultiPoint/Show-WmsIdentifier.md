---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/show-wmsidentifier?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Show-WmsIdentifier
---

# 显示 WMS 标识符

## 摘要
显示车站的识别屏幕。

## 语法

### IdentifyBySession
```
Show-WmsIdentifier -SessionId <UInt32[]> [-Server <String>] [<CommonParameters>]
```

### 通过站点名称进行识别（IdentifyByStation）
```
Show-WmsIdentifier -StationId <UInt32[]> [-Server <String>] [<CommonParameters>]
```

### IdentifyAll
```
Show-WmsIdentifier [-All] [-Server <String>] [<CommonParameters>]
```

## 描述
`Show-WmsIdentifier` cmdlet 用于显示指定站点的识别信息界面。界面顶部的显示内容是客户端名称；对于 Windows MultiPoint Server 站点而言，会使用与该站点更相关的名称作为客户端名称。界面底部显示的内容则是承载该会话的系统的名称。

## 示例

### 示例 1：显示身份验证界面
```
PS C:\> Show-WmsIdentifier -SessionId 2
PS C:\> Show-WmsIdentifier -StationId 1
```

这个示例显示了指定会话的 ID 界面。第一个命令用于显示运行远程桌面客户端（remote desktop client）的系统信息。

第二个命令会显示本地服务器的名称。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: IdentifyAll
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定作为该命令目标的多点服务器（MultiPoint Server）的完全限定主机名。默认值为 localhost。

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
指定一个包含多点会议 ID 的数组。

```yaml
Type: UInt32[]
Parameter Sets: IdentifyBySession
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StationId
指定一个多点站ID数组。

```yaml
Type: UInt32[]
Parameter Sets: IdentifyByStation
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32[]

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[隐藏WMS标识符](./Hide-WmsIdentifier.md)

