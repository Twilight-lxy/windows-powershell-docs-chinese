---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/remove-appvclientpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AppvClientPackage
---

# 移除 AppvClient 包

## 摘要
从计算机上删除该软件包。

## 语法

### ByGuid（默认值）
```
Remove-AppvClientPackage [-PackageId] <Guid> [-VersionId] <Guid> [<CommonParameters>]
```

### 按软件包分类
```
Remove-AppvClientPackage [-Package] <AppvClientPackage> [<CommonParameters>]
```

### 按名称查找
```
Remove-AppvClientPackage [-Name] <String> [[-Version] <String>] [<CommonParameters>]
```

## 描述
`Remove-AppvClientPackage` cmdlet 用于从运行 Microsoft 应用虚拟化（App-V）客户端的计算机上删除相应的软件包。该 cmdlet 会删除 `AppvClientPackage` 对象。

## 示例

#### 示例 1：使用管道操作符删除某个包的某个版本
```
PS C:\> Get-AppvPackage -Name "MyPackage" -Version 1 | Remove-Package
```

这个命令会获取名为“MyPackage”的软件包的第1个版本，然后将其从计算机上删除。

### 示例 2：删除软件包的某个版本
```
PS C:\> Remove-Package -Name "MyPackage" -Version 1
```

这个命令会将名为“MyPackage”的软件包的版本1从计算机上删除。

## 参数

### -Name
指定在序列化过程中提供的软件包的友好名称。该值是从软件包清单中获取的。

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
指定一个App-V包。

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
指定用于唯一标识该软件包的ID。该ID可以在软件包清单中找到，或者通过在“Sequencer”中打开该软件包来获取。同一软件包的所有版本都共享相同的ID。

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

### -Version
用于指定App-V包在版本系列中的具体版本。如果您不指定此参数，该cmdlet将作用于计算机上的所有版本。

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
指定一个 GUID，用于区分某个软件包的版本与其他版本（无论是旧版本、新版本还是属于不同分支的版本）。如果不指定此参数，该 cmdlet 将对软件包的所有版本进行操作。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.AppvAgent.AppvClientPackage

## 输出

## 备注

## 相关链接

[Add-AppvClientPackage](./Add-AppvClientPackage.md)

[Get-AppvClientPackage](./Get-AppvClientPackage.md)

[Mount-AppvClientPackage](./Mount-AppvClientPackage.md)

[发布 AppvClient 包](./Publish-AppvClientPackage.md)

[Repair-AppvClientPackage](./Repair-AppvClientPackage.md)

[Set-AppvClientPackage](./Set-AppvClientPackage.md)

[Stop-AppvClientPackage](./Stop-AppvClientPackage.md)

[Unpublish-AppvClientPackage](./Unpublish-AppvClientPackage.md)

