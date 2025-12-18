---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/set-appvclientpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AppvClientPackage
---

# Set-AppvClientPackage

## 摘要
配置一个App-V客户端软件包。

## 语法

### 使用 ByGuid（默认值）
```
Set-AppvClientPackage [-Path <String>] [-DynamicDeploymentConfiguration <String>] [-UseNoConfiguration]
 [-PackageId] <Guid> [-VersionId] <Guid> [<CommonParameters>]
```

### 按软件包分类
```
Set-AppvClientPackage [-Path <String>] [-DynamicDeploymentConfiguration <String>] [-UseNoConfiguration]
 [-Package] <AppvClientPackage> [<CommonParameters>]
```

### 按名称查找
```
Set-AppvClientPackage [-Path <String>] [-DynamicDeploymentConfiguration <String>] [-UseNoConfiguration]
 [-Name] <String> [[-Version] <String>] [<CommonParameters>]
```

## 描述
`Set-AppvClientPackage` cmdlet 用于修改微软应用程序虚拟化（App-V）包的配置文件。

## 示例

### 示例 1：为某个软件包设置部署配置
```
PS C:\> Set-AppvClientPackage -Name "MyApp" -Version 1 -DynamicDeploymentConfiguration "C:\policies\MyApp.xml"
```

此命令为某个软件包设置新的部署配置。

## 参数

### -DynamicDeploymentConfiguration
指定要添加的 App-V 包的动态部署配置文件的路径。此cmdlet使用该动态部署配置文件来覆盖包清单中提供的默认行为。

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
指定用于唯一标识该软件包的 GUID。该 GUID 可以在软件包清单中找到，或者通过在 App-V Sequencer 中打开该软件包来获取。同一个软件包的所有版本都使用相同的包 ID。

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

### -Path
指定包含要添加的包的.APPV文件的路径。该路径可以是本地目录、网络目录，或者是HTTP或HTTPS URL。

```yaml
Type: String
Parameter Sets: (All)
Aliases: PSPath

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseNoConfiguration
表示此cmdlet会将默认的计算机策略应用到所选的软件包上。

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
用于指定App-V包在版本系列中的具体版本。如果您不指定此参数，该cmdlet将会针对目标计算机上所有可用的版本执行操作。

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
指定一个GUID，用于区分某个软件包的版本与其他版本（无论是旧版本、新版本，还是属于不同系列的版本）。如果未指定此参数，该cmdlet将对该软件包的所有版本执行操作。

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

[Stop-AppvClientPackage](./Stop-AppvClientPackage.md)

[Unpublish-AppvClientPackage](./Unpublish-AppvClientPackage.md)

