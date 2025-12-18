---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/sync-appvpublishingserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Sync-AppvPublishingServer
---

# 同步应用发布服务器（Sync-AppvPublishingServer）

## 摘要
启动App-V发布刷新操作。

## 语法

### ByServerId（默认值）
```
Sync-AppvPublishingServer [-ServerId] <UInt32> [-Global] [-Force] [-NetworkCostAware]
 [-HidePublishingRefreshUI] [<CommonParameters>]
```

### ByObject
```
Sync-AppvPublishingServer [-Server] <AppvPublishingServer> [-Global] [-Force] [-NetworkCostAware]
 [-HidePublishingRefreshUI] [<CommonParameters>]
```

### ByNameUrl
```
Sync-AppvPublishingServer [[-Name] <String>] [[-URL] <String>] [-Global] [-Force] [-NetworkCostAware]
 [-HidePublishingRefreshUI] [<CommonParameters>]
```

## 描述
`Sync-AppvPublishingServer` cmdlet 在当前用户的上下文中启动 Microsoft 应用虚拟化 (App-V) 的发布刷新操作。该操作会连接到客户端上所有已添加的服务器，并向用户展示新的 App-V 包及其相应的扩展点。

## 示例

### 示例 1：开始发布刷新内容
```
PS C:\> Sync-AppvPublishingServer -Name "MyServer"
```

此命令会开始为当前用户在名为“MyServer”的服务器上发布刷新（refresh）操作。

## 参数

### -Force
表示该cmdlet会强制执行所有包的发布（publish）和取消发布（unpublish）操作。

“Force”开关用于决定是否抑制警告消息和确认消息。在脚本编写中，它可以帮助屏蔽交互式提示信息。如果命令中没有使用“Force”开关，那么在需要时系统会要求用户提供管理员权限（即进行身份验证）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Global
表示该cmdlet会同步从App-V发布服务器下载到的软件包，这些软件包会被安装到计算机上，并且会推送给计算机上的所有用户。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HidePublishingRefreshUI
表示该cmdlet会隐藏发布更新进度条。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定服务器的友好名称（即易于人们理解的名称）。

```yaml
Type: String
Parameter Sets: ByNameUrl
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NetworkCostAware
表示此 cmdlet 具有网络成本意识（即会在执行操作时考虑网络使用的成本）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定一个 **AppvPublishingServer** 对象。要获取一个 **AppvPublishingServer** 对象，可以使用 **Get-AppvPublishingServer** cmdlet。

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
用于指定 App-V 发布服务器的标识符。可以使用 **Get-AppvPublishingServer** cmdlet 来查询该标识符。

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

### -URL
指定服务器的URL路径。

```yaml
Type: String
Parameter Sets: ByNameUrl
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AppvPublishingServer](./Add-AppvPublishingServer.md)

[Get-AppvPublishingServer](./Get-AppvPublishingServer.md)

[Remove-AppvPublishingServer](./Remove-AppvPublishingServer.md)

[Set-AppvPublishingServer](./Set-AppvPublishingServer.md)

