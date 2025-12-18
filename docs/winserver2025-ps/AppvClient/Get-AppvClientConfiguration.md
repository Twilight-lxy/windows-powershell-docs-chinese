---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/get-appvclientconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppvClientConfiguration
---

# 获取 AppVClient 配置信息

## 摘要
返回App-V客户端的相关配置信息。

## 语法

```
Get-AppvClientConfiguration [[-Name] <String>] [<CommonParameters>]
```

## 描述
`Get-AppvClientConfiguration` cmdlet 返回一个对象，其中包含了 Microsoft 应用程序虚拟化（App-V）客户端的所有设置和权限。这些设置既包括 App-V 客户端的配置参数，也包括相应的权限信息。

如果指定了某个特定的设置，该cmdlet会返回该设置的值。

## 示例

#### 示例 1：显示所有配置设置
```
PS C:\> Get-AppvClientConfiguration
```

此命令会显示所有App-V客户端配置设置。

### 示例 2：显示单个配置设置
```
PS C:\> Get-AppvClientConfiguration -Name "PackageSourceRoot"
```

这个命令会显示 **PackageSourceRoot** 设置的值。

## 参数

### -Name
指定一个设置的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.AppV.AppvClientPowerShell.AppvClientConfiguration
如果未指定 *Name* 参数，该cmdlet会返回一个 **AppvClientConfiguration** 对象。该对象以二维表格的形式显示：第一列包含具体的配置信息，第二列包含相应的当前值。

如果您指定了*名称*（Name），该cmdlet会返回相同的二维表格，但仅包含所请求的配置信息。

## 备注

## 相关链接

[Set-AppvClientConfiguration](./Set-AppvClientConfiguration.md)

