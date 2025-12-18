---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/mount-appvclientconnectiongroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Mount-AppvClientConnectionGroup
---

# Mount-AppvClientConnectionGroup

## 摘要
将包的内容流式传输到本地磁盘上。

## 语法

### 使用 `ByGuid`（默认值）
```
Mount-AppvClientConnectionGroup [-GroupId] <Guid> [-VersionId] <Guid> [<CommonParameters>]
```

### 按名称查找
```
Mount-AppvClientConnectionGroup [-Name] <String> [<CommonParameters>]
```

### 按连接组（ByConnectionGroup）
```
Mount-AppvClientConnectionGroup [-ConnectionGroup] <AppvClientConnectionGroup> [<CommonParameters>]
```

## 描述
`Mount-AppvClientConnectionGroup` cmdlet 将连接组中所有包的内容流式传输到本地磁盘。

## 示例

### 示例 1：为某个指定组下载软件包
```
PS C:\> Mount-AppvClientConnectionGroup -Name "MyGroup"
```

此命令会下载所有属于名为“MyGroup”的已启用连接组中的软件包。

### 示例 2：通过组ID为某个组下载软件包
```
PS C:\> Mount-AppvClientConnectionGroup -GroupID 793afd37-bd68-4ea1-859a-669f6afd0aa8
```

此cmdlet会下载属于已启用连接组的所有包，该连接组的ID为793afd37-bd68-4ea1-859a-669f6afd0aa8。

### 示例 3：下载与特定字符串匹配的组对应的包
```
PS C:\> Get-AppvClientConnectionGroup -Name "MyGr*" | Mount-AppvClientConnectionGroup
```

这个命令会获取所有名称中包含“MyGr”字符串的已启用连接组，然后下载这些连接组中的所有包。

## 参数

### -ConnectionGroup
指定 Microsoft 应用程序虚拟化 (App-V) 连接组对象。

```yaml
Type: AppvClientConnectionGroup
Parameter Sets: ByConnectionGroup
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -GroupId
指定特定连接组的组ID。

```yaml
Type: Guid
Parameter Sets: ByGuid
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定 App-V 连接组的名称。

```yaml
Type: String
Parameter Sets: ByName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VersionId
指定用于区分某个连接组版本与其他版本的 GUID。如果您不指定此参数，该 cmdlet 将对连接组的全部版本进行处理。

```yaml
Type: Guid
Parameter Sets: ByGuid
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.AppvAgent.AppvClientConnectionGroup

## 输出

## 备注
* If a previous load has been canceled, the cmdlet resumes that load when it is run again. The package will be added to the system before loading. Otherwise the cmdlet fails. If you do not specify any parameters, the cmdlet loads all packages on the system.
* The cmdlet is synchronous. It returns when the load option has completed. To make the cmdlet asynchronous, use the **Start-Job** cmdlet.
* The cmdlet checks that you have permissions to perform the specific action. If not, the cmdlet returns an error.

## 相关链接

[Add-AppvClientConnectionGroup](./Add-AppvClientConnectionGroup.md)

[disable-AppvClientConnectionGroup](./Disable-AppvClientConnectionGroup.md)

[Enable-AppvClientConnectionGroup](./Enable-AppvClientConnectionGroup.md)

[Get-AppvClientConnectionGroup](./Get-AppvClientConnectionGroup.md)

[Remove-AppvClientConnectionGroup](./Remove-AppvClientConnectionGroup.md)

[修复-AppvClientConnectionGroup](./Repair-AppvClientConnectionGroup.md)

[Stop-AppvClientConnectionGroup](./Stop-AppvClientConnectionGroup.md)

