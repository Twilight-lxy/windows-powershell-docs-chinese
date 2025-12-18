---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/remove-appvclientconnectiongroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AppvClientConnectionGroup
---

# 删除 AppvClientConnectionGroup

## 摘要
在客户端上删除一个App-V连接组。

## 语法

### 使用 ByGuid（默认值）
```
Remove-AppvClientConnectionGroup [-GroupId] <Guid> [-VersionId] <Guid> [<CommonParameters>]
```

### 按名称查找
```
Remove-AppvClientConnectionGroup [-Name] <String> [<CommonParameters>]
```

### 按连接组（ByConnectionGroup）
```
Remove-AppvClientConnectionGroup [-ConnectionGroup] <AppvClientConnectionGroup> [<CommonParameters>]
```

## 描述
`Remove-AppvClientConnectionGroup` cmdlet 用于删除客户端上现有的 Microsoft 应用虚拟化（App-V）连接组。该连接组中的所有软件包都会被分离出来。

## 示例

### 示例 1：删除一个已命名的连接组
```
PS C:\> Remove-AppvClientConnectionGroup -Name "MyGroup"
```

这个命令会将名为“MyGroup”的连接组从计算机上删除。

### 示例 2：通过使用连接组的 ID 来删除该连接组
```
PS C:\> Remove-AppvClientConnectionGroup -GroupID 35ec9e5f-ab21-463f-8fe6-b90d4b66d182
```

这个命令会删除组ID为35ec9e5f-ab21-463f-8fe6-b90d4b66d182的连接组。

### 示例 3：删除所有名称与特定字符串匹配的连接组
```
PS C:\> Get-AppvClientConnectionGroup -Name "MyGr*" | Remove-AppvClientConnectionGroup
```

这个命令会找到所有名称中包含 “MyGr” 这一字符串的连接组，然后将它们从计算机上删除。

## 参数

### -ConnectionGroup
指定一个 App-V 连接组对象。

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
指定特定连接组的 GUID（全局唯一标识符）。

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
指定App-V连接组的名称。

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
该参数用于指定一个 GUID，该 GUID 用于区分某个软件包的版本与其他版本（无论是旧版本、新版本还是属于不同分支的版本）。如果您不指定此参数，该 cmdlet 将会对该软件包的所有版本进行处理。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.AppvAgent.AppvClientConnectionGroup

## 输出

## 备注
* If any packages in the group are still running, the cmdlet returns an error.
* The cmdlet checks that you have permissions to perform the specific action. If not, the cmdlet returns an error.
* If the remove operation fails, the cmdlet returns the following error:  The remove operation could not be completed. An error code is returned.
* If any package in the specified group is running, the connection group is not removed until all packages in the new group are shutdown. The cmdlet still returns success as long as the file is valid.

## 相关链接

[Add-AppvClientConnectionGroup](./Add-AppvClientConnectionGroup.md)

[Disable-AppvClientConnectionGroup](./Disable-AppvClientConnectionGroup.md)

[Enable-AppvClientConnectionGroup](./Enable-AppvClientConnectionGroup.md)

[Get-AppvClientConnectionGroup](./Get-AppvClientConnectionGroup.md)

[Mount-AppvClientConnectionGroup](./Mount-AppvClientConnectionGroup.md)

[修复 AppvClientConnectionGroup](./Repair-AppvClientConnectionGroup.md)

[Stop-AppvClientConnectionGroup](./Stop-AppvClientConnectionGroup.md)

