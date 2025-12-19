---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/get-wmsscheduledupdate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WmsScheduledUpdate
---

# Get-WmsScheduledUpdate

## 摘要
获取计划好的更新配置信息。

## 语法

```
Get-WmsScheduledUpdate [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-WmsScheduledUpdate` cmdlet 可以获取在磁盘保护设置为“丢弃模式”时定时更新的当前配置信息。

## 示例

#### 示例 1：获取计划的更新配置
```
PS C:\> Get-WmsScheduledUpdate

IsScheduleUpdateEnabled       : True
AutomaticUpdateMode           : WindowsOnly
HourToScheduleUpdates         : 3
CustomScript                  : c:\myapps\sampleapp.exe
MaxTimeAllowedForCustomScript : 30
ReturnState                   : PreviousState
```

这个命令用于获取当前的定期更新配置信息。

## 参数

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft.WindowsServerSolutions.MultipointServer.PowerShell Commands.Library.WmsScheduledUpdate

## 备注

## 相关链接

[Disable-WmsScheduledUpdate](./Disable-WmsScheduledUpdate.md)

[Enable-WmsScheduledUpdate](./Enable-WmsScheduledUpdate.md)

[Set-WmsScheduledUpdate](./Set-WmsScheduledUpdate.md)

