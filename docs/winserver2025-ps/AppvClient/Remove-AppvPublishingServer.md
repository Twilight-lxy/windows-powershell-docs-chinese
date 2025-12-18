---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/remove-appvpublishingserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AppvPublishingServer
---

# 移除 AppV Publishing 服务器

## 摘要
删除一个App-V发布服务器。

## 语法

### ByServerId（默认值）
```
Remove-AppvPublishingServer [-ServerId] <UInt32> [<CommonParameters>]
```

### ByObject
```
Remove-AppvPublishingServer [-Server] <AppvPublishingServer> [<CommonParameters>]
```

### ByNameUrl
```
Remove-AppvPublishingServer [[-Name] <String>] [[-URL] <String>] [<CommonParameters>]
```

## 描述
`Remove-AppvPublishingServer` cmdlet 会从 App-V 客户端列表中删除 Microsoft 应用程序虚拟化（App-V）发布服务器。

## 示例

### 示例 1：移除发布服务器
```
PS C:\> Remove-AppvPublishingServer -Name "Server01"
```

此命令将删除名为 Server01 的发布服务器。

#### 示例 2：移除多个发布服务器
```
PS C:\> Remove-AppvPublishingServer -Name "Server*"
```

此命令会删除所有名称以“Server”开头的所有发布服务器。

## 参数

### -Name
指定该作品的名称。

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
指定发布服务器的ID。

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
指定发布服务器的URL路径。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.AppvAgent.AppvMgmtServer

## 输出

## 备注
* If an operation is being done between the server and targeted App-V agent, the cmdlet deletes the App-V server object, but any operation that had already been initiated finishes. Subsequent actions that may have been queued up fail.
* The cmdlet checks that you have permissions to perform the specific action. If not, the cmdlet returns the following error: The action could not be performed due to current App-V permissions. Please modify the permissions and try the operation again.

## 相关链接

[Add-AppvPublishingServer](./Add-AppvPublishingServer.md)

[Get-AppvPublishingServer](./Get-AppvPublishingServer.md)

[Set-AppvPublishingServer](./Set-AppvPublishingServer.md)

[Sync-AppvPublishingServer](./Sync-AppvPublishingServer.md)

