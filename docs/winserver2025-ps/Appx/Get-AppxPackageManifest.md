---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/get-appxpackagemanifest?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppxPackageManifest
---

# Get-AppxPackageManifest

## 摘要
获取应用程序包的清单文件（manifest）。

## 语法

```
Get-AppxPackageManifest [-Package] <String> [[-User] <String>] [<CommonParameters>]
```

## 描述

`Get-AppxPackageManifest` cmdlet 可以获取应用程序包的清单文件。应用程序包的文件扩展名通常是 `.msix` 或 `.appx`。清单文件是一个 `.xml` 格式的文档，其中包含了关于该包的信息，例如包的 ID。

## 示例

#### 示例 1：获取应用程序包的清单文件

```powershell
Get-AppxPackageManifest -Package "package1_1.0.0.0_neutral__8wekyb3d8bbwe"
```

这个命令用于获取名为“package1_1.0.0.0_neutral__8wekyb3d8bbwe”的应用程序包的清单文件（manifest）。

### 示例 2：获取应用程序包的应用程序 ID

```powershell
(Get-AppxPackage -Name "*WinJS*" | Get-AppxPackageManifest).package.applications.application.id
```

这个命令用于获取名称中包含“WinJS”字符串的应用包对应的应用程序ID。

### 示例 3

```powershell
(Get-AppxPackage -Name "*ZuneMusic*" | Get-AppxPackageManifest).Package.Capabilities
```

这个命令用于获取名称中包含字符串“ZuneMusic”的应用程序包的功能。

## 参数

### -Package

指定一个 `AppxPackage` 对象或包的完整名称。若要获取当前用户未安装的计算机上的某个包的清单文件（manifest），必须以管理员权限运行此命令。允许使用通配符。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -User

用于指定某个用户。此cmdlet会获取为该用户安装的软件包的相关信息（即软件包清单）。若需获取当前用户之外的其他用户配置文件中的软件包列表，必须以管理员权限运行此命令。用户名可以采用以下格式之一：

- `domain\user_name`
- `user_name@fqn.domain.tld`
- `user_name`
- `SID-string`

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Windows.AppxPackageManager Commands.AppxPackage[]

这个cmdlet接受一个包含**AppxPackage**对象的数组，这些对象中包含了各种信息，包括应用程序包的完整名称。

## 输出

### System.XML.XMLDocument

此 cmdlet 会返回一个只读的 `.xml` 文档，其中包含有关应用程序包的信息（例如包 ID）。

## 备注

## 相关链接

[包管理器 API](https://go.microsoft.com/fwlink/?LinkId=245447)

[如何添加和删除应用程序](https://go.microsoft.com/fwlink/?LinkID=231020)

[Get-AppxPackage](./Get-AppxPackage.md)

[Add-AppxPackage](./Add-AppxPackage.md)
