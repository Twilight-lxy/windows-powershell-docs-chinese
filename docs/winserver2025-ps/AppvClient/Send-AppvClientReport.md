---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/send-appvclientreport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Send-AppvClientReport
---

# Send-AppvClientReport

## 摘要
从客户端发送报告数据。

## 语法

```
Send-AppvClientReport [-NetworkCostAware] [-DeleteOnSuccess] [[-URL] <String>] [<CommonParameters>]
```

## 描述
`Send-AppVClientReport` cmdlet 会将所有可用的报告数据以 XML 格式发送到指定的位置。你可以从客户端删除这些数据，但必须先启用报告功能。默认情况下，数据会被发送到 `ReportingServer` 注册表值中指定的位置；该位置可以是一个 UNC 共享文件夹，也可以是 Microsoft Application Virtualization (App-V) 报告服务器的名称。如果你想更改数据的发送位置，可以使用 `URL` 参数来指定新的路径——该路径同样可以是 UNC 共享文件夹或 App-V 报告服务器的地址。

默认情况下，数据发送后不会从客户端删除，而是会作为下一次定时同步的一部分被发送到报告服务器（如果适用的话）。您可以指定是否要从客户端删除数据。如果指定了“DeleteOnSuccess”参数，那么报告数据将会从客户端被删除。

如果数据成功发送，该cmdlet会显示一条成功消息。

如果未启用报告功能，该cmdlet将会失败。

如果没有指定有效的位置，该cmdlet将会失败。

## 示例

### 示例 1：将数据发送到之前配置的位置
```
PS C:\> Send-AppVClientReport
The Application Virtualization Client Report was sent successfully
```

该命令将数据发送到客户端配置的位置，在数据发送后不会删除这些数据。

### 示例 2：将数据发送到之前配置的位置，并删除该数据
```
PS C:\> Send-AppVClientReport -DeleteOnSuccess
Tee Application Virtualization Client Report was sent successfully
```

此命令会将数据发送到客户端配置的位置，在数据发送完成后将其删除。

### 示例 3：将数据发送到指定位置并删除数据
```
PS C:\> Send-AppVClientReport -URL "http://myreportingserver:port" -DeleteOnSuccess
The Application Virtualization Client Report was sent successfully
```

该命令将数据发送到由URL参数指定的位置，并在数据发送完成后将其删除。

### 示例 4：将数据发送到错误的位置
```
PS C:\> Send-AppVClientReport -URL "http://incorrectservername:port" -DeleteOnSuccess
The reporting server or share location has not been specified.  You must specify the reporting server or share location using the following format: -Url <location>
```

这个命令试图将数据发送到由URL参数指定的位置，但由于服务器名称不正确，发送操作失败并返回了一个错误。数据并没有被删除。

## 参数

### -DeleteOnSuccess
表示该cmdlet在数据发送后会将其删除。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NetworkCostAware
表示此cmdlet具有网络成本意识（即会考虑网络传输所消耗的资源）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -URL
指定报告服务器上保存客户端信息的位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

