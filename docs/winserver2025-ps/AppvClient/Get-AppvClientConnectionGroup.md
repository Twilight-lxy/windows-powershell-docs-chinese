---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/get-appvclientconnectiongroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppvClientConnectionGroup
---

# Get-AppvClientConnectionGroup

## 摘要
返回一个App-V连接组对象。

## 语法

### 按名称排序（默认设置）
```
Get-AppvClientConnectionGroup [[-Name] <String>] [-All] [<CommonParameters>]
```

### ByGuid
```
Get-AppvClientConnectionGroup [-GroupId] <Guid> [[-VersionId] <Guid>] [-All] [<CommonParameters>]
```

## 描述
`Get-AppvClientConnectionGroup` cmdlet 返回一个特定的 Microsoft 应用虚拟化 (App-V) 连接组对象。

## 示例

### 示例 1：按名称获取某个组的所有版本
```
PS C:\> Get-AppvClientConnectionGroup -Name "MyConnectionGroup"
```

这个命令会获取所有名为“MyConnectionGroup”的已启用连接组的所有版本。

### 示例 2：通过连接组的 ID 获取该连接组
```
PS C:\> Get-AppvClientConnectionGroup -GroupID 793afd37-bd68-4ea1-859a-669f6afd0aa8
```

这条命令用于获取启用的连接组，该连接组的ID为793afd37-bd68-4ea1-859a-669f6afd0aa8。

### 示例 3：获取所有连接组
```
PS C:\> Get-AppvClientConnectionGroup -All
```

这个命令可以获取计算机上的所有连接组信息。

## 参数

### -All
表示该cmdlet会返回所有已添加到计算机的连接组，而不仅仅是那些被当前用户启用的连接组。

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

### -GroupId
指定特定连接组的 GUID。

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

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VersionId
指定一个 GUID，用于区分某个软件包的版本与其他版本（无论是旧版本、新版本，还是属于不同分支的版本）。如果您不指定此参数，该 cmdlet 将对该软件包的所有版本进行操作。

```yaml
Type: Guid
Parameter Sets: ByGuid
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.AppV.AppvClientPowerShell.AppvClientConnectionGroup

## 备注
* The cmdlet returns an error if the name of the specified App-V connection group cannot be found on the target computer.

## 相关链接

[Add-AppvClientConnectionGroup](./Add-AppvClientConnectionGroup.md)

[禁用-AppvClientConnectionGroup](./ Disable-AppvClientConnectionGroup.md)

[Enable-AppvClientConnectionGroup](./Enable-AppvClientConnectionGroup.md)

[Mount-AppvClientConnectionGroup](./Mount-AppvClientConnectionGroup.md)

[Remove-AppvClientConnectionGroup](./Remove-AppvClientConnectionGroup.md)

[修复 AppvClientConnectionGroup](./Repair-AppvClientConnectionGroup.md)

[Stop-AppvClientConnectionGroup](./Stop-AppvClientConnectionGroup.md)

