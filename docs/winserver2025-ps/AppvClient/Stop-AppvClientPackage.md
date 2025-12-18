---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/stop-appvclientpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-AppvClientPackage
---

# Stop-AppvClientPackage

## 摘要
关闭指定软件包对应的虚拟环境。

## 语法

### ByGuid（默认值）
```
Stop-AppvClientPackage [-Global] [-PackageId] <Guid> [-VersionId] <Guid> [<CommonParameters>]
```

### 按包（ByPackage）
```
Stop-AppvClientPackage [-Global] [-Package] <AppvClientPackage> [<CommonParameters>]
```

### 按名称查找
```
Stop-AppvClientPackage [-Global] [-Name] <String> [[-Version] <String>] [<CommonParameters>]
```

## 描述
`Stop-AppvClientPackage` cmdlet 用于关闭指定软件包对应的虚拟环境。该软件包中的所有应用程序和进程都将被强制终止，任何未保存的应用程序数据也会丢失。

## 示例

#### 示例 1：关闭某个软件包版本的虚拟环境
```
PS C:\> Stop-AppvClientPackage -Name "MyPackage" -Version 2
```

这个命令用于关闭名为“MyPackage”的软件包的版本2所对应的虚拟环境。

### 示例 2：关闭某个软件包所有版本的虚拟环境
```
PS C:\> Get-AppvClientPackage -Name "MyPackage" | Stop-AppvClientPackage
```

这个命令会获取名为“MyPackage”的包的所有版本信息，之后会关闭用于处理这些结果的虚拟环境。

## 参数

### -Global
该参数用于指示cmdlet为计算机上所有用户指定的软件包关闭相应的虚拟环境。使用*Global*参数需要具备管理员权限。

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
指定一个用于唯一标识该软件包的 GUID。这个 GUID 可以在软件包清单中找到，或者通过使用 Microsoft 应用程序虚拟化（App-V）序列器来打开该软件包获得。同一个软件包的所有版本都共享相同的 ID。

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
用于指定某个App-V包在版本系列中的具体版本号。如果您不指定此参数，该命令行工具将作用于计算机上所有可用的该包版本。

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
指定一个GUID（全局唯一标识符），用于区分某个软件包的特定版本与其他版本（无论是旧版本、新版本，还是属于不同分支/系列的版本）。如果未指定此参数，该cmdlet将会对软件包的所有版本进行处理。

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

[Unpublish-AppvClientPackage](./Unpublish-AppvClientPackage.md)

