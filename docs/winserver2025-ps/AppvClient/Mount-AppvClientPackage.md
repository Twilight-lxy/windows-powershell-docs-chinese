---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/mount-appvclientpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Mount-AppvClientPackage
---

# 安装 AppvClient 包

## 摘要
将一个软件包加载到 App-V 缓存中。

## 语法

### 使用 `ByGuid`（默认值）
```
Mount-AppvClientPackage [-Cancel] [-PackageId] <Guid> [-VersionId] <Guid> [<CommonParameters>]
```

### 按包（ByPackage）
```
Mount-AppvClientPackage [-Cancel] [-Package] <AppvClientPackage> [<CommonParameters>]
```

### ByName
```
Mount-AppvClientPackage [-Name] <String> [[-Version] <String>] [<CommonParameters>]
```

## 描述
`Mount-AppvClientPackage` cmdlet 用于启动或恢复将 Microsoft 应用虚拟化（App-V）包加载到缓存中的过程。

## 示例

#### 示例 1：获取某个包的特定版本
```
PS C:\> Mount-AppvClientPackage -Name "MyApp" -Version 2
```

这个命令会下载名为“MyApp”的软件包的第2个版本。

### 示例 2：获取一个包的所有版本
```
PS C:\> Mount-AppvClientPackage -Name "MyApp"
```

这个命令会下载名为“MyApp”的包的所有版本。

### 示例 3：下载所有与指定字符串匹配的包
```
PS C:\> Get-AppvClientPackage -Name "My*" | Mount-AppvClientPackage
```

这个命令会获取所有名称中包含字符串“My”的软件包，然后下载它们。

### 示例 4：下载并发布一个新的软件包
```
PS C:\> Add-AppvClientPackage -Path "http://MyServer/content/package.Appv" | Mount-AppvClientPackage | Publish-AppvClientPackage -Global
```

这个命令会从指定的路径添加该软件包，下载它，然后将其发布给计算机上的所有用户。

### 示例 5：取消下载
```
PS C:\> Mount-AppvClientPackage -Name "MyApp" -Cancel
```

这个命令会取消名为“MyApp”的软件包的下载。

## 参数

### -Cancel
表示该cmdlet会停止加载某个包。

```yaml
Type: SwitchParameter
Parameter Sets: ByGuid, ByPackage
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
指定一个唯一标识该软件包的 GUID。该 GUID 可以在软件包清单中找到，或者通过在 App-V Sequencer 中打开该软件包来获取。同一个特定软件包的所有版本都使用相同的 ID。

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
用于指定某个App-V包在该版本系列中的具体版本。如果您不指定此参数，该cmdlet将作用于计算机上的所有版本。

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
指定一个 GUID，用于区分某个软件包的版本与其他版本（无论是旧版本、新版本还是属于不同分支的版本）。如果未指定此参数，该 cmdlet 将对所有版本的软件包进行操作。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.AppvAgent.AppvClientPackage

## 输出

### Microsoft.AppvAgent.AppvClientPackage

## 备注
* If a previous mount has been canceled, the cmdlet resumes that mount when it is run again. The package must be added to the system before mounting. Otherwise the cmdlet fails. If you do not specify any parameters, the cmdlet mounts all packages on the system.
* This cmdlet is synchronous. It returns when the mount option has completed. To make the cmdlet asynchronous, use the **Start-Job** cmdlet.

## 相关链接

[Add-AppvClientPackage](./Add-AppvClientPackage.md)

[Get-AppvClientPackage](./Get-AppvClientPackage.md)

[Publish-AppvClientPackage](./Publish-AppvClientPackage.md)

[Remove-AppvClientPackage](./Remove-AppvClientPackage.md)

[Repair-AppvClientPackage](./Repair-AppvClientPackage.md)

[Set-AppvClientPackage](./Set-AppvClientPackage.md)

[Stop-AppvClientPackage](./Stop-AppvClientPackage.md)

[Unpublish-AppvClientPackage](./Unpublish-AppvClientPackage.md)

