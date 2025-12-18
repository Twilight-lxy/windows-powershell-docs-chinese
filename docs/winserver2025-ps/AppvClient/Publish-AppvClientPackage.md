---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/publish-appvclientpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Publish-AppvClientPackage
---

# 发布 AppvClient 包

## 摘要
发布App-V包。

## 语法

### 使用 `ByGuid`（默认值）
```
Publish-AppvClientPackage [-Global] [-UserSID <String>] [[-DynamicUserConfigurationPath] <String>]
 [-DynamicUserConfigurationType <DynamicUserConfiguration>] [-PackageId] <Guid> [-VersionId] <Guid>
 [<CommonParameters>]
```

### 按软件包分类
```
Publish-AppvClientPackage [-Global] [-UserSID <String>] [[-DynamicUserConfigurationPath] <String>]
 [-DynamicUserConfigurationType <DynamicUserConfiguration>] [-Package] <AppvClientPackage> [<CommonParameters>]
```

### 按名称查找
```
Publish-AppvClientPackage [-Global] [-UserSID <String>] [[-DynamicUserConfigurationPath] <String>]
 [-DynamicUserConfigurationType <DynamicUserConfiguration>] [-Name] <String> [[-Version] <String>]
 [<CommonParameters>]
```

## 描述
`Publish-AppvClientPackage` cmdlet 用于发布一组 Microsoft 应用虚拟化 (App-V) 包所对应的扩展点。常见的扩展点包括快捷方式（shortcuts）和文件传输协议 (FTA, File Transfer Protocol) 配置等。你可以将包发布给当前用户，或者发布给所有登录到目标计算机的用户。此外，你还可以为该包提供一个动态用户配置文件（Dynamic User Configuration file）。

## 示例

### 示例 1：将一个软件包的版本发布给所有用户
```
PS C:\> Publish-AppvClientPackage -Name "MyApp" -Version 1 -Global -DynamicUserConfiguration "C:\content\policies\MyApp.policy"
```

此命令将名为“MyApp”的软件包的版本1发布给计算机上的所有用户，并应用“动态用户配置”策略文件。

### 示例 2：将软件包的一个版本发布给用户
```
PS C:\> Publish-AppvClientPackage -Name "MyApp" -Version 1 -UserPolicy "C:\content\policies\MyAppConfiguration.xml"
```

该命令将名为“MyApp”的软件包的第1个版本发布给用户，并应用动态用户配置策略文件。

### 示例 3：将软件包的最新版本发布给所有用户
```
PS C:\> Publish-AppvClientPackage -Name "MyApp" -Global
```

这条命令会将名为“MyApp”的软件包发布给计算机上的所有用户。

## 参数

### -DynamicUserConfigurationPath
指定要添加的特定 App-V 包对应的动态用户配置文件的路径。该 cmdlet 使用该动态用户配置文件来覆盖包清单中用户部分所提供的默认行为或动态部署配置中的设置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DynamicUserConfigurationType
指定在没有定义动态用户配置文件的情况下应执行哪些操作。该参数的可接受值包括：

- UseDeploymentConfiguration.
The package uses the user configuration part of deployment configuration.
- UseNoConfiguration.
Clear any previous configuration and use settings from the manifest.
- UseExistingConfiguration.
Make no changes to the configuration and use the last published configuration.

如果您不指定此参数，那么当该包已经发布时，此cmdlet会使用“UseExistingConfiguration”；如果包尚未发布，则会使用“UseDeploymentConfiguration”。

仅在用户发布数据时使用此参数。该参数不适用于全局发布操作。

```yaml
Type: DynamicUserConfiguration
Parameter Sets: (All)
Aliases:
Accepted values: UseDeploymentConfiguration, UseNoConfiguration, UseExistingConfiguration

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Global
这表示所提供的软件包会发布给所有登录到目标计算机的用户；否则，这些软件包只会发布给当前正在使用的用户。

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
指定该软件包在序列化（即进行版本管理或打包等操作）时所使用的名称。此值是从软件包的清单文件（package manifest）中获取的。

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
指定一个App-V软件包。

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
指定一个用于识别该软件包的 GUID。相关信息可以在软件包清单中找到，或者通过在 App-V 序列器中打开该软件包来获取。同一个软件包的所有版本都使用相同的包 ID。

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
指定目标用户的SID，格式为S-1-2-34-56789012-3456789012-345678901-2345。运行此参数需要具有提升的权限。

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
用于指定 App-V 包在某个版本系列中的具体版本。如果不指定此参数，该 cmdlet 将操作运行 App-V 客户端的计算机上最新的那个 App-V 包。

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
指定一个GUID，用于区分某个软件包的版本与其他版本。如果未指定此参数，该cmdlet将操作该软件包的最新版本。

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

### Microsoft.AppvAgent.AppvClientPackage

## 输出

## 备注

## 相关链接

[Add-AppvClientPackage](./Add-AppvClientPackage.md)

[Get-AppvClientPackage](./Get-AppvClientPackage.md)

[Mount-AppvClientPackage](./Mount-AppvClientPackage.md)

[Remove-AppvClientPackage](./Remove-AppvClientPackage.md)

[Repair-AppvClientPackage](./Repair-AppvClientPackage.md)

[Set-AppvClientPackage](./Set-AppvClientPackage.md)

[Stop-AppvClientPackage](./Stop-AppvClientPackage.md)

[Unpublish-AppvClientPackage](./Unpublish-AppvClientPackage.md)

