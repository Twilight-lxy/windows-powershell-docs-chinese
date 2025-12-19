---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/set-wmsscheduledupdate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WmsScheduledUpdate
---

# Set-WmsScheduledUpdate

## 摘要
设置Windows更新和自定义维护脚本的调度计划。

## 语法

```
Set-WmsScheduledUpdate [-AutomaticUpdateMode <EAutomaticUpdateMode>] [-HourToScheduleUpdates <UInt32>]
 [-CustomScript <String>] [-MaxTimeAllowedForCustomScript <UInt32>] [-ReturnState <EScheduleUpdateReturnState>]
 [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-WmsScheduledUpdate` cmdlet 用于设置运行 MultiPoint Server 的计算机的 Windows 更新和自定义维护脚本的调度安排。该计算机已启用磁盘保护功能，并且磁盘保护配置为“丢弃模式”（discard mode）。

## 示例

### 示例 1：在多点服务器上启用 Windows 更新
```
PS C:\> Set-WmsScheduledUpdate -AutomaticUpdateMode WindowsOnly -HourToScheduleUpdates 2 -ReturnState PreviousState
```

此命令配置本地多点服务器在凌晨2:00检查是否有可用的Windows更新，应用这些更新，并将计算机恢复到应用更新之前的状态。为了更新多点服务器，该命令会执行以下操作：

- Restart the computer to disable disk protection.
- Apply pending Windows updates.
- Restart the computer to enable disk protection and to return it to the previous power state.

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
指定自动更新应运行的时间小时。此参数的可接受值为：0-23。

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
指定自定义脚本允许运行的最长时间。在此时间限制结束后，相关进程将停止，系统会重新启动以重新启用磁盘保护功能。

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
指定在更新完成后计算机应所处的状态。该参数的可接受值包括：Shutdown（关机）和PreviousState（之前的状态）。

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
指定该命令的目标端——即MultiPoint Server的完全限定主机名。默认值为localhost。

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

### System Nullable`1[[Microsoft.WindowsServerSolutions.MultipointServer.PowerShellcommands.Library.EAutomaticUpdateMode, MultiPoint, Version=10.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35]]

### `SystemNullable`  
1[[`System.UInt32`, `mscorlib`, `Version=4.0.0.0`, `Culture=neutral`, `PublicKeyToken=b77a5c561934e089`]]

### System.String

### SystemNullable  
1[[Microsoft.WindowsServerSolutions.MultipointServer.PowerShell Commands.Library.EScheduleUpdateReturnState, MultiPoint, Version=10.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35]]

## 输出

### Microsoft.WindowsServerSolutions.MultipointServer.PowerShell Commands.Library.WmsScheduledUpdate

## 备注

## 相关链接

[Disable-WmsScheduledUpdate](./Disable-WmsScheduledUpdate.md)

[Enable-WmsScheduledUpdate](./Enable-WmsScheduledUpdate.md)

[Get-WmsScheduledUpdate](./Get-WmsScheduledUpdate.md)

