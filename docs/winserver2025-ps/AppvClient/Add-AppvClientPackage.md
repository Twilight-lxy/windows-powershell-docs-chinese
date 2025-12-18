---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/add-appvclientpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AppvClientPackage
---

# 添加 AppvClient 包

## 摘要
将一个软件包添加到运行App-V客户端程序的计算机上。

## 语法

```
Add-AppvClientPackage [-Path] <String> [[-DynamicDeploymentConfiguration] <String>] [<CommonParameters>]
```

## 描述
`Add-AppvClientPackage` cmdlet 可以向运行 Microsoft 应用程序虚拟化（App-V）客户端的计算机添加新的软件包，也可以升级该计算机上已安装的现有软件包。新添加的软件包或其版本会自动注册到 App-V 客户端中。

如果该软件包已经存在于计算机上，但需要添加的版本有所不同，那么会安装新的版本；现有的版本将保持不变。

## 示例

### 示例 1：向客户端添加一个包
```
PS C:\> Add-AppvClientPackage -Path "http://MyServer/content/package.APPV"
```

此命令会在客户端计算机上添加一个新的软件包。如果该软件包是已存在软件包的另一个版本，App-V代理会添加这个新版本，但不会修改任何现有的版本。由于没有配置任何计算机策略，因此该软件包将遵循默认的计算机策略设置。

### 示例 2：添加一个包含配置文件的包
```
PS C:\> Add-AppvClientPackage -Path "http://MyServer/content/package.appv" -DynamicDeploymentConfiguration "C:\MyConfigfiles\DynamicDeploymentConfig.xml"
```

此命令添加了一个包含动态部署配置文件的包。

### 示例 3：向客户端添加一个包并存储结果
```
PS C:\> $Package = Add-AppvClientPackage -Path "http://MyServer/content/package.APPV"
```

该命令向客户端添加一个新软件包，并将生成的 **AppvClientPackage** 对象赋值给变量 $Package。

## 参数

### -DynamicDeploymentConfiguration
指定要添加的指定 App-V 包的动态部署配置文件的路径。此 cmdlet 使用该动态部署配置文件来覆盖包清单中提供的默认配置。

如果您不指定此参数，App-V 客户端会为要添加的 App-V 包分配默认的计算机策略。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定包含要添加的软件包的.appv文件的位置。该值可以是本地目录、网络目录，或者是HTTP或HTTPS地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases: PSPath

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.AppvAgent.AppvPackage

## 输出

### Microsoft.AppvAgent.AppvClientPackage

## 备注

## 相关链接

[Get-AppvClientPackage](./Get-AppvClientPackage.md)

[Mount-AppvClientPackage](./Mount-AppvClientPackage.md)

[Publish-AppvClientPackage](./Publish-AppvClientPackage.md)

[Remove-AppvClientPackage](./Remove-AppvClientPackage.md)

[修复 AppvClientPackage](./Repair-AppvClientPackage.md)

[Set-AppvClientPackage](./Set-AppvClientPackage.md)

[Stop-AppvClientPackage](./Stop-AppvClientPackage.md)

[Unpublish-AppvClientPackage](./Unpublish-AppvClientPackage.md)

