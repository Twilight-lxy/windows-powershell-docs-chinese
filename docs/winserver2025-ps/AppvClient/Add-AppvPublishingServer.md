---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/add-appvpublishingserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AppvPublishingServer
---

# 添加 AppvPublishingServer

## 摘要
为运行App-V客户端的计算机添加一个发布服务器。

## 语法

```
Add-AppvPublishingServer [-Name] <String> [-URL] <String> [[-GlobalRefreshEnabled] <Boolean>]
 [[-GlobalRefreshOnLogon] <Boolean>] [[-GlobalRefreshInterval] <UInt32>]
 [[-GlobalRefreshIntervalUnit] <IntervalUnit>] [[-UserRefreshEnabled] <Boolean>]
 [[-UserRefreshOnLogon] <Boolean>] [[-UserRefreshInterval] <UInt32>]
 [[-UserRefreshIntervalUnit] <IntervalUnit>] [<CommonParameters>]
```

## 描述
`Add-AppvPublishingServer` cmdlet 为运行 Microsoft 应用虚拟化（App-V）客户端的那台计算机添加一个新的发布服务器，以便该客户端可以连接到这个服务器。添加服务器后，运行 App-V 客户端的计算机就可以使用该服务器来获取发布更新数据、流式传输软件包以及执行其他操作。

## 示例


## 参数

### -GlobalRefreshEnabled
该设置用于指定是否启用对所有全局发布的软件包的更新功能。您可以将其设置为在登录时自动更新，或者按照指定的时间间隔进行更新。

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

### -GlobalRefreshInterval
指定全局发布软件包更新的时间间隔。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GlobalRefreshIntervalUnit
指定时间测量单位。该参数的可接受值为：day（天）和hour（小时）。

```yaml
Type: IntervalUnit
Parameter Sets: (All)
Aliases:
Accepted values: Hour, Day

Required: False
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GlobalRefreshOnLogon
指定每次用户登录目标计算机时，是否都会刷新所有已发布到全局范围内的软件包。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定发布服务器的友好名称（即便于人们识别的名称）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -URL
指定 App-V 发布服务器的 URL 路径。

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

### -UserRefreshEnabled
指定是否启用对发布给用户的所有包的更新机制。更新可以设置在登录时自动进行，或者按照预定义的时间间隔来执行。

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

### -UserRefreshInterval
指定用户发布的软件包更新的时间间隔。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 8
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserRefreshIntervalUnit
指定时间测量单位。该参数的可接受值为：day（天）和hour（小时）。

```yaml
Type: IntervalUnit
Parameter Sets: (All)
Aliases:
Accepted values: Hour, Day

Required: False
Position: 9
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserRefreshOnLogon
指定是否在用户每次登录目标计算机时都会刷新所有发布给该用户的软件包。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 7
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.AppvAgent.AppvPublishingServer

## 备注

## 相关链接

[Get-AppvPublishingServer](./Get-AppvPublishingServer.md)

[Remove-AppvPublishingServer](./Remove-AppvPublishingServer.md)

[Set-AppvPublishingServer](./Set-AppvPublishingServer.md)

[Sync-AppvPublishingServer](./Sync-AppvPublishingServer.md)

