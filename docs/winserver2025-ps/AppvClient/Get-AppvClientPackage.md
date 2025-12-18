---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/get-appvclientpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppvClientPackage
---

# Get-AppvClientPackage

## 摘要
返回App-V客户端软件包。

## 语法

### 按名称查找（默认方式）
```
Get-AppvClientPackage [[-Name] <String>] [[-Version] <String>] [-All] [<CommonParameters>]
```

### 作者：ByGuid
```
Get-AppvClientPackage [-PackageId] <Guid> [[-VersionId] <Guid>] [-All] [<CommonParameters>]
```

## 描述
`Get-AppvClientPackage` cmdlet 根据提供的标准返回一组 Microsoft 应用程序虚拟化（App-V）客户端包。

## 示例

### 示例 1：获取名称与某个字符串匹配的包
```
PS C:\> Get-AppvClientPackage -Name "MyApp*" -All
```

这个命令会获取所有名称以“MyApp”开头的软件包。

#### 示例 2：通过名称获取特定版本的包
```
PS C:\> Get-AppvClientPackage -Name "MyApp" -Version 4
```

这个命令用于获取名为“MyApp”的软件包的第4个版本。

#### 示例 3：通过使用软件包的ID来获取该软件包
```
PS C:\> Get-AppvClientPackage -PackageID 793afd37-bd68-4ea1-859a-669f6afd0aa8
```

这个命令用于获取包ID为793afd37-bd68-4ea1-859a-669f6afd0aa8的软件包。

## 参数

### -All
这表示该cmdlet使用所有添加到计算机上的包作为可搜索的集合。如果未提供该参数，cmdlet仅会使用当前用户有权使用的包。

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
在排序（Sequencing）过程中指定的软件包的友好名称。该名称是从软件包清单（package manifest）中获取的。

```yaml
Type: String
Parameter Sets: ByName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PackageId
指定用于唯一标识该软件包的 GUID。该 GUID 可以在软件包清单中找到，或者通过使用 App-V Sequencer 打开软件包来获取。同一个软件包的所有版本都共享相同的包 ID。

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
指定某个特定App-V包在特定版本系列中的版本号。如果未指定此参数，则该cmdlet将操作目标计算机上可用的该包的所有版本。

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
用于指定一个 GUID，该 GUID 可以区分某个软件包的不同版本（无论是旧版本、新版本，还是属于不同系列的版本）。如果您指定了此参数，那么该 cmdlet 将对该软件包的所有版本进行处理。

```yaml
Type: Guid
Parameter Sets: ByGuid
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.AppV.AppvClientPowerShell.AppvClientPackage

## 备注
* If you do not specify any parameters, the cmdlet returns a set of all packages on the computer.
* The cmdlet checks that you have permissions to perform the specific action. If not, the cmdlet returns the following error: The action could not be performed due to current App-V permissions. Please modify the permissions and try the operation again.
* If the cmdlet cannot find the package, the cmdlet returns the following error: The specified package(s) could not be found. An error code is returned.

## 相关链接

[Add-AppvClientPackage](./Add-AppvClientPackage.md)

[Mount-AppvClientPackage](./Mount-AppvClientPackage.md)

[发布 AppvClient 包](./Publish-AppvClientPackage.md)

[Remove-AppvClientPackage](./Remove-AppvClientPackage.md)

[Repair-AppvClientPackage](./Repair-AppvClientPackage.md)

[Set-AppvClientPackage](./Set-AppvClientPackage.md)

[Stop-AppvClientPackage](./Stop-AppvClientPackage.md)

[Unpublish-AppvClientPackage](./Unpublish-AppvClientPackage.md)

