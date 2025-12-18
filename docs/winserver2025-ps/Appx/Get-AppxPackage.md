---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/get-appxpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppxPackage
---

# Get-AppxPackage

## 摘要
获取用户配置文件中安装的应用程序包列表。

## 语法

```
Get-AppxPackage [-AllUsers] [-PackageTypeFilter <PackageTypes>]
 [[-Name] <String>] [[-Publisher] <String>] [-User <String>]
 [-Volume <AppxVolume>] [<CommonParameters>]
```

## 描述

`Get-AppxPackage` cmdlet 可以获取用户配置文件中安装的应用程序包列表。应用程序包的文件扩展名为 `.msix` 或 `.appx`。如果要获取当前用户之外的其他用户配置文件中的应用程序包列表，必须以管理员权限运行此命令。

## 示例

#### 示例 1：获取每个用户账户的所有应用程序包

```powershell
Get-AppxPackage -AllUsers
```

这个命令会列出计算机上每个用户账户所安装的应用程序包。

### 示例 2：获取特定用户的应用程序包

```powershell
Get-AppxPackage -Name "Package17" -User "Contoso\EvanNarvaez"
```

如果 `Package17` 已安装在指定的用户配置文件中，此命令将显示有关它的信息。

### 示例 3：获取特定应用程序包的信息

```powershell
Get-AppxPackage -Name Microsoft.ScreenSketch
```

这个命令会显示有关ScreenSketch应用程序的信息。

### 示例 4：获取某个发布者的所有应用包

```powershell
Get-AppxPackage -Publisher "CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US"
```

这个命令会列出计算机上安装的所有Microsoft应用程序包。

### 示例 5：使用 PackageTypeFilter 获取所有应用程序包

```powershell
Get-AppxPackage -PackageTypeFilter Bundle,Framework,Main,Resource
```

这个命令会列出计算机上安装了 PackageTypeFilter 的所有应用程序包。

## 参数

### -AllUsers

表示此 cmdlet 会列出计算机上所有用户账户的应用程序包。要使用此参数，必须以管理员权限运行命令。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Name

用于指定某个特定软件包的名称。如果您指定了此参数，该cmdlet将仅返回与该软件包相关的结果。允许使用通配符。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PackageTypeFilter

指定一个或多个用逗号分隔的包类型，这些包类型是该 cmdlet 从包仓库中获取的。

默认情况下，此cmdlet仅返回类型为`Main`和`Framework`的包。

```yaml
Type: PackageTypes
Parameter Sets: (All)
Aliases:
Accepted values: None, Main, Framework, Resource, Bundle, Xap, Optional

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Publisher

用于指定某个特定软件包的发行商。如果指定了此参数，该 cmdlet 仅会返回与该发行商相关的结果。支持使用通配符。

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

### -User

用于指定一个用户。如果指定了此参数，cmdlet 将返回仅针对该用户安装的应用包列表。若要获取当前用户之外的其他用户配置文件中的应用包列表，必须以管理员权限运行此命令。用户名可以采用以下格式之一：

- `domain\user_name`
- `user_name@fqn.domain.tld`
- `user_name`
- `SID-string`

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Volume

指定一个 **AppxVolume** 对象。如果您指定了此参数，该 cmdlet 仅返回与该参数指定的卷相关的包。

```yaml
Type: AppxVolume
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### Microsoft.Windows.AppxPackageManager Commands.AppxPackage

此cmdlet返回一个**AppxPackage**对象，其中包含相关信息，包括应用程序包的完整名称。

## 备注

## 相关链接

[包管理器 API](https://go.microsoft.com/fwlink/?LinkId=245447)

[如何添加和删除应用程序](https://go.microsoft.com/fwlink/?LinkID=231020)

[Add-AppxPackage](./Add-AppxPackage.md)

[Get-AppxPackageManifest](./Get-AppxPackageManifest.md)

[Move-AppxPackage](./Move-AppxPackage.md)

[Remove-AppxPackage](./Remove-AppxPackage.md)
