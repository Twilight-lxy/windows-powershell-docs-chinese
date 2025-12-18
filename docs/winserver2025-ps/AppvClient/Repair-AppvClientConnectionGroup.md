---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/repair-appvclientconnectiongroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Repair-AppvClientConnectionGroup
---

# 修复 AppvClientConnectionGroup 的问题

## 摘要
重置连接组对应的用户包设置。

## 语法

### 使用 `ByGuid`（默认值）
```
Repair-AppvClientConnectionGroup [-Global] [-UserState] [-Extensions] [-GroupId] <Guid> [-VersionId] <Guid>
 [<CommonParameters>]
```

### 按名称查找
```
Repair-AppvClientConnectionGroup [-Global] [-UserState] [-Extensions] [-Name] <String> [<CommonParameters>]
```

### 按连接组（ByConnectionGroup）
```
Repair-AppvClientConnectionGroup [-Global] [-UserState] [-Extensions]
 [-ConnectionGroup] <AppvClientConnectionGroup> [<CommonParameters>]
```

## 描述
`Repair-AppvClientConnectionGroup` cmdlet 用于重置连接组的用户设置。重置设置会导致包中所有与用户相关的应用程序设置永久丢失。这些设置会被恢复到该连接组最初被添加到系统时的原始状态。

## 示例

### 示例 1：修复一个已命名的连接组
```
PS C:\> Repair-AppvClientConnectionGroup -Name "MyGroup"
```

这个命令用于修复名为“MyGroup”的连接组。

#### 示例 2：通过使用连接组的 ID 来修复该连接组
```
PS C:\> Repair-AppvClientConnectionGroup -GroupID 793afd37-bd68-4ea1-859a-669f6afd0aa8
```

此命令用于修复组ID为793afd37-bd68-4ea1-859a-669f6afd0aa8的连接组。

### 示例 3：修复所有名称与某个字符串匹配的连接组
```
PS C:\> Get-AppvClientConnectionGroup -Name "MyGr*" | Repair-AppvClientConnectionGroup
```

此命令会找到所有名称中包含“MyGr”这个字符串的连接组，然后对这些连接组进行修复。

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

### -Extensions
表示该cmdlet仅修复连接组的扩展点（extension points），而不会删除该连接组的用户状态（user state）。

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

### -Global
该命令表示会为计算机上所有用户重置指定软件包的相关用户设置。使用 *Global* 参数需要具有管理员权限。

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
指定Microsoft应用程序虚拟化（App-V）连接组的名称。

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

### -UserState
表示该cmdlet仅删除连接组中的用户状态，并不会对扩展点进行修复。

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

### -VersionId
指定一个 GUID，用于区分某个连接组版本与其他版本（无论是旧版本、新版本还是属于不同分支的版本）。如果未指定此参数，则该 cmdlet 将对连接组的所有版本进行操作。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.AppvAgent.AppvClientConnectionGroup

## 输出

## 备注

## 相关链接

[Add-AppvClientConnectionGroup](./Add-AppvClientConnectionGroup.md)

[ Disable-AppvClientConnectionGroup](./Disable-AppvClientConnectionGroup.md)

[Enable-AppvClientConnectionGroup](./Enable-AppvClientConnectionGroup.md)

[Get-AppvClientConnectionGroup](./Get-AppvClientConnectionGroup.md)

[Mount-AppvClientConnectionGroup](./Mount-AppvClientConnectionGroup.md)

[Remove-AppvClientConnectionGroup](./Remove-AppvClientConnectionGroup.md)

[Stop-AppvClientConnectionGroup](./Stop-AppvClientConnectionGroup.md)

