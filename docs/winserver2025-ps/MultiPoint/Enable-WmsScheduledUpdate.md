---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/enable-wmsscheduledupdate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-WmsScheduledUpdate
---

# 启用 WMS 计划更新

## 摘要
在启用磁盘保护功能且处于“丢弃”模式（discard mode）的情况下，该设置允许进行定时更新。

## 语法

```
Enable-WmsScheduledUpdate [-AutomaticUpdateMode <EAutomaticUpdateMode>] [-HourToScheduleUpdates <UInt32>]
 [-CustomScript <String>] [-MaxTimeAllowedForCustomScript <UInt32>] [-ReturnState <EScheduleUpdateReturnState>]
 [-Server <String>] [<CommonParameters>]
```

## 描述
`Enable-WmsScheduledUpdate` cmdlet 允许指定的计算机定期禁用磁盘保护功能，以便能够应用定时更新。更新完成后，磁盘保护功能会自动重新启用。

## 示例

### 示例 1：启用定时更新
```
PS C:\> Enable-WmsScheduledUpdate -Server "Sample.microsoft.com" -AutomaticUpdateMode WindowsOnly -HourToScheduleUpdates 3 -CustomScript "C:\MyApps\SampleApp.exe" -MaxTimeAllowedForCustomScript 30 -ReturnState PreviousState
IsScheduleUpdateEnabled       : True
AutomaticUpdateMode           : WindowsOnly
HourToScheduleUpdates         : 3
CustomScript                  : c:\myapps\sampleapp.exe
MaxTimeAllowedForCustomScript : 30
ReturnState                   : PreviousState
```

该命令使计算机 Sample.microsoft.com 在凌晨 3 点将磁盘保护模式切换为被动模式（需要重启），以便应用所有待定的 Windows 更新并运行 SampleApp.exe 应用程序。之后，系统会恢复到凌晨 3 点之前的正常运行状态。

## 参数

### -AutomaticUpdateMode
指定要处理的自动更新类型。该参数的可接受值包括：

- None
- WindowsOnly
- WindowsAndOtherPrograms

```yaml
Type: EAutomaticUpdateMode
Parameter Sets: (All)
Aliases:
Accepted values: None, WindowsOnly, WindowsAndOtherPrograms

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CustomScript
指定用户在更新时需要运行的命令的完整路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -HourToScheduleUpdates
指定自动更新运行的时间。该参数的可接受值为：0-23。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MaxTimeAllowedForCustomScript
指定自定义脚本允许运行的最长时间。当这个时间期限结束时，该进程将被停止，系统将重新启动以重新启用磁盘保护功能。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReturnState
指定更新完成后计算机的状态。该参数的可接受值为：Shutdown（关机）和PreviousState（之前的状态）。

```yaml
Type: EScheduleUpdateReturnState
Parameter Sets: (All)
Aliases:
Accepted values: Shutdown, PreviousState

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Server
指定该命令的目标MultiPoint Server的完全限定主机名。默认值为localhost。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### scheduledUpdate
此cmdlet返回一个包含当前配置的结构。

## 备注

## 相关链接

[ Disable-WmsScheduledUpdate](./Disable-WmsScheduledUpdate.md)

[Get-WmsScheduledUpdate](./Get-WmsScheduledUpdate.md)

[Set-WmsScheduledUpdate](./Set-WmsScheduledUpdate.md)

