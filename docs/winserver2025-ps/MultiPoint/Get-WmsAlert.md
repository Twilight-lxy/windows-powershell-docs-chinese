---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/get-wmsalert?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WmsAlert
---

# Get-WmsAlert

## 摘要
获取警报信息。

## 语法

```
Get-WmsAlert [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-WmsAlert` cmdlet 从 Windows MultiPoint Server 核心服务中获取警报信息。

## 示例

### 示例 1：获取警报信息
```
PS C:\> Get-WmsAlert
TimeStampInUtc : 12/7/2010 12:17:15 AM
AlertType      : HubMissingRequiredDevice
AlertSeverity  : Warning
ComputerName   : TEST
StationId      : 1
```

此cmdlet从MultiPoint Server核心服务中返回警报信息。在这个示例中，站点1缺少键盘。

## 参数

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft.WindowsServerSolutions.MultipointServer.PowerShellcommands.Library.WmsAlert

## 备注

## 相关链接

