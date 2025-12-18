---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/repair-appvclientpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Repair-AppvClientPackage
---

# 修复 AppvClientPackage

## 摘要
重置某个软件包的用户设置。

## 语法

### ByGuid（默认值）
```
Repair-AppvClientPackage [-Global] [-UserState] [-Extensions] [-PackageId] <Guid> [-VersionId] <Guid>
 [<CommonParameters>]
```

### 按包分类（ByPackage）
```
Repair-AppvClientPackage [-Global] [-UserState] [-Extensions] [-Package] <AppvClientPackage>
 [<CommonParameters>]
```

### 按名称查找
```
Repair-AppvClientPackage [-Global] [-UserState] [-Extensions] [-Name] <String> [[-Version] <String>]
 [<CommonParameters>]
```

## 描述
`Repair-AppvClientPackage` cmdlet 会删除用户设置，并重置该软件包的扩展点（extension points）。重置设置会导致软件包中所有与用户相关的应用程序设置被永久丢失。这些设置会被恢复到该软件包最初被添加到系统时的原始状态。

## 示例

#### 示例 1：删除某个软件包版本的用户状态信息
```
PS C:\> Repair-AppvClientPackage -Name "MyApp" -Version 3
```

此命令会删除名为“MyApp”的包中版本号为3的用户状态数据。

### 示例 2：删除名称与指定字符串匹配的软件包对应的用户状态信息
```
PS C:\> Get-AppvClientPackage -Name "MyA*" | Repair-AppvClientPackage
```

这个命令会获取所有名称中包含 “MyA” 这个字符串的软件包，然后删除这些软件包的用户相关数据（即用户状态信息）。

## 参数

### -Extensions
表示该cmdlet仅修复包的扩展点（extension points），而不会删除该包的用户状态（user state）。

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
该命令用于修复目标计算机上所有登录用户的相应软件包的扩展点（extension points）。如果不使用此命令，软件包的扩展点只会被当前正在运行的用户所对应的系统修复。

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

### -Name
指定在序列化过程中提供的包的友好名称。该值是从包清单中获取的。

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

### -Package
指定一个 App-V 包。

```yaml
Type: AppvClientPackage
Parameter Sets: ByPackage
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PackageId
指定一个唯一标识该软件包的 GUID。该 GUID 可以在软件包清单中找到，或者通过打开 Microsoft 应用程序虚拟化（App-V）序列器来获取。同一个软件包的所有版本都使用相同的 Package ID。

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

### -UserState
表示该 cmdlet 仅删除包的用户状态，并不对扩展点进行修复操作。

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

### -Version
用于指定App-V包在某个版本系列中的具体版本。如果不指定此参数，该cmdlet将作用于计算机上的所有版本。

```yaml
Type: String
Parameter Sets: ByName
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VersionId
指定用于区分某个软件包版本与其他版本的 GUID（全局唯一标识符），无论是旧版本、新版本，还是属于不同分支的版本。如果未指定此参数，该命令行工具将作用于该软件包的所有版本。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.AppvAgent.AppvClientPackage

## 输出

### Microsoft.AppvAgent.AppvClientPackage

## 备注

## 相关链接

[Add-AppvClientPackage](./Add-AppvClientPackage.md)

[Get-AppvClientPackage](./Get-AppvClientPackage.md)

[Mount-AppvClientPackage](./Mount-AppvClientPackage.md)

[发布 AppvClient 包](./Publish-AppvClientPackage.md)

[Remove-AppvClientPackage](./Remove-AppvClientPackage.md)

[Set-AppvClientPackage](./Set-AppvClientPackage.md)

[Stop-AppvClientPackage](./Stop-AppvClientPackage.md)

[Unpublish-AppvClientPackage](./Unpublish-AppvClientPackage.md)

