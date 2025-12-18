---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/get-appvpublishingserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppvPublishingServer
---

# Get-AppvPublishingServer

## 摘要
返回 App-V 服务器对象。

## 语法

### ByServerId（默认值）
```
Get-AppvPublishingServer [[-ServerId] <UInt32>] [<CommonParameters>]
```

### ByNameUrl
```
Get-AppvPublishingServer [[-Name] <String>] [[-URL] <String>] [<CommonParameters>]
```

## 描述
`Get-AppvPublishingServer` cmdlet 根据所提供的标准返回一个或多个 Microsoft 应用程序虚拟化（App-V）服务器对象。

## 示例

### 示例 1：通过友好名称获取服务器
```
PS C:\> Get-AppvPublishingServer -Name "Server*"
```

这个命令会获取所有具有以“Server”开头的好记名称（friendly names）的发布服务器。

### 示例 2：根据服务器 ID 名获取服务器
```
PS C:\> Get-AppvPublishingServer -ServerId 1
```

这个命令用于获取具有指定ID的发布服务器。

## 参数

### -Name
指定 App-V 发布服务器的名称。

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

### -ServerId
指定 App-V 发布服务器的唯一标识符。

```yaml
Type: UInt32
Parameter Sets: ByServerId
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -URL
指定 App-V 发布服务器的 URL 路径。

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

### Microsoft.AppV.AppvClientPowerShell.AppvPublishingServer

## 备注
* The cmdlet checks that you have permissions to perform the specific action. If not, the cmdlet returns the following error:  The action could not be performed due to current App-V permissions. Please modify the permissions and try the operation again.
* If the get operation fails, the cmdlet returns the following error: The get operation could not be completed. An error code is returned.
* If the cmdlet cannot find the servers, the cmdlet returns the following error: The specified App-V publishing server(s) could not be found. An error code is returned.

## 相关链接

[Add-AppvPublishingServer](./Add-AppvPublishingServer.md)

[Remove-AppvPublishingServer](./Remove-AppvPublishingServer.md)

[Set-AppvPublishingServer](./Set-AppvPublishingServer.md)

[Sync-AppvPublishingServer](./Sync-AppvPublishingServer.md)

