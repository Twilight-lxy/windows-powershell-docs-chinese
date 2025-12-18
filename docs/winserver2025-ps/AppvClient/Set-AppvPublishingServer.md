---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/set-appvpublishingserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AppvPublishingServer
---

# 设置 AppV Publishing 服务器

## 摘要
修改 App-V 发布服务器的属性。

## 语法

### ByServerId（默认值）
```
Set-AppvPublishingServer [-ServerId] <UInt32> [[-GlobalRefreshEnabled] <Boolean>]
 [[-GlobalRefreshOnLogon] <Boolean>] [[-GlobalRefreshInterval] <UInt32>]
 [[-GlobalRefreshIntervalUnit] <IntervalUnit>] [[-UserRefreshEnabled] <Boolean>]
 [[-UserRefreshOnLogon] <Boolean>] [[-UserRefreshInterval] <UInt32>]
 [[-UserRefreshIntervalUnit] <IntervalUnit>] [<CommonParameters>]
```

### ByObject
```
Set-AppvPublishingServer [-Server] <AppvPublishingServer> [[-GlobalRefreshEnabled] <Boolean>]
 [[-GlobalRefreshOnLogon] <Boolean>] [[-GlobalRefreshInterval] <UInt32>]
 [[-GlobalRefreshIntervalUnit] <IntervalUnit>] [[-UserRefreshEnabled] <Boolean>]
 [[-UserRefreshOnLogon] <Boolean>] [[-UserRefreshInterval] <UInt32>]
 [[-UserRefreshIntervalUnit] <IntervalUnit>] [<CommonParameters>]
```

## 描述
`Set-AppvPublishingServer` cmdlet 用于修改已存在的 Microsoft 应用虚拟化（App-V）发布服务器的属性。若要获取一个 App-V 发布服务器对象，请使用 `Get-AppvPublishingServer` cmdlet。

## 示例


## 参数

### -GlobalRefreshEnabled
指定服务器是否会对所有全局发布的软件包自动与发布服务器进行同步。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GlobalRefreshInterval
指定一个时间范围，该范围表示在全球发布的软件包进行更新（刷新）的时间段。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GlobalRefreshIntervalUnit
用于指定时间测量单位。该参数的可接受值为：day（天）和hour（小时）。

```yaml
Type: IntervalUnit
Parameter Sets: (All)
Aliases:
Accepted values: Hour, Day

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GlobalRefreshOnLogon
指定每次用户登录目标计算机时，是否会对所有全球发布的软件包进行更新（即刷新操作）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定一个 **AppvPublishingServer** 对象。要获取一个 **AppvPublishingServer** 对象，请使用 **Get-AppvPublishingServer** cmdlet。

```yaml
Type: AppvPublishingServer
Parameter Sets: ByObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ServerId
指定 App-V 发布服务器的标识符。可以使用 **Get-AppvPublishingServer** cmdlet 来查询该标识符。

```yaml
Type: UInt32
Parameter Sets: ByServerId
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserRefreshEnabled
指定是否启用了用户刷新功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserRefreshInterval
指定 App-V 发布服务器的标识符。可以使用 **Get-AppvPublishingServer** cmdlet 来查询该标识符。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 7
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserRefreshIntervalUnit
用于指定时间测量单位。该参数的可接受值为：day（天）和hour（小时）。

```yaml
Type: IntervalUnit
Parameter Sets: (All)
Aliases:
Accepted values: Hour, Day

Required: False
Position: 8
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserRefreshOnLogon
指定是否每次用户登录计算机时都会自动更新（刷新）界面或数据。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.AppvAgent.AppvPublishingServer

## 输出

### Microsoft.AppvAgent.AppvPublishingServer

## 备注

## 相关链接

[Add-AppvPublishingServer](./Add-AppvPublishingServer.md)

[Get-AppvPublishingServer](./Get-AppvPublishingServer.md)

[Remove-AppvPublishingServer](./Remove-AppvPublishingServer.md)

[Sync-AppvPublishingServer](./Sync-AppvPublishingServer.md)

