---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/unpublish-appvclientpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Unpublish-AppvClientPackage
---

# 取消发布 AppvClientPackage

## 摘要
移除了包的扩展点（extension points）。

## 语法

### ByGuid（默认值）
```
Unpublish-AppvClientPackage [-Global] [-UserSID <String>] [-PackageId] <Guid> [-VersionId] <Guid>
 [<CommonParameters>]
```

### 按包（ByPackage）
```
Unpublish-AppvClientPackage [-Global] [-UserSID <String>] [-Package] <AppvClientPackage> [<CommonParameters>]
```

### 按名称查找
```
Unpublish-AppvClientPackage [-Global] [-UserSID <String>] [-Name] <String> [[-Version] <String>]
 [<CommonParameters>]
```

## 描述
`Unpublish-AppvClientPackage` cmdlet 会删除指定包的所有扩展点。包的内容仍然保留在目标计算机上，该包仍会被添加到客户端中，并且相应的 `AppvClientPackage` 对象也会继续存在。

该软件包可以针对当前用户进行“取消发布”操作；或者，也可以对所有登录到目标计算机的用户都执行相同的操作。

## 示例

### 示例 1：取消发布软件包的某个版本
```
PS C:\> Unpublish-AppvClientPackage -Name "MyApp" -Version 3
```

这个命令会取消名为“MyApp”的软件包的第3个版本的发布。

### 示例 2：取消发布某个软件包的版本，使其对所有用户不可用
```
PS C:\> Unpublish-AppvClientPackage -Name "MyApp" -Version 3 -Global
```

此命令会取消名为“MyApp”的包的第3个版本的发布，使得该包不再对计算机上的所有用户可用。

## 参数

### -Global
这表示这些软件包对所有登录到目标计算机的用户都是不可用的（即无法使用的）。如果未指定这一设置，那么这些软件包仅会对当前正在使用该计算机的用户不可用。

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
在序列化过程中指定该包的友好名称。此值是从包清单中获取的。

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
指定一个用于唯一标识该软件包的 GUID（全局唯一标识符）。该 GUID 可以在软件包清单中找到，或者通过使用 Microsoft 应用虚拟化（App-V）序列器来打开软件包获取。同一个软件包的所有版本都会共享相同的 ID。

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

### -UserSID
指定目标用户的 SID，格式为 S-1-2-34-56789012-3456789012-345678901-2345。此 cmdlet 参数需要提升权限才能运行。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Version
用于指定某个特定App-V软件包版本所属的系列（lineage）。如果未指定此参数，该cmdlet将使用找到的最新版本进行操作。

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
指定一个GUID，用于区分某个软件包的版本与其他版本（无论是旧版本、新版本，还是属于不同分支的版本）。如果未指定此参数，该cmdlet将操作该软件包的最新版本。

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

[Repair-AppvClientPackage](./Repair-AppvClientPackage.md)

[Set-AppvClientPackage](./Set-AppvClientPackage.md)

[Stop-AppvClientPackage](./Stop-AppvClientPackage.md)

