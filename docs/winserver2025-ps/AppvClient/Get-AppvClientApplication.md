---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/get-appvclientapplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppvClientApplication
---

# Get-AppvClientApplication

## 摘要
返回属于 App-V 客户端包的应用程序。

## 语法

```
Get-AppvClientApplication [[-Name] <String>] [[-Version] <String>] [-All] [<CommonParameters>]
```

## 描述
`Get-AppvClientApplication` cmdlet 根据提供的条件，返回一组属于 Microsoft 应用程序虚拟化（App-V）客户端包的应用程序。

## 示例

#### 示例 1：获取当前用户所使用的应用程序版本
```
PS C:\> Get-AppvClientApplication -Name "AppName" -Version 1
```

这个命令用于获取客户端上已发布的应用程序。该应用程序的名称为AppName，版本号为1。

### 示例 2：获取所有应用程序
```
PS C:\> Get-AppvClientApplication -All
```

这个命令可以获取客户端上的所有应用程序。

## 参数

### -All
表示该 cmdlet 返回了所有已添加到计算机上的应用程序，而不仅仅是当前用户可以看到的那些应用程序。

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
指定应用程序的名称。该名称是从软件包清单（package manifest）中获取的。

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

### -Version
指定应用程序的版本。如果不指定此参数，该cmdlet将针对目标计算机上所有可用的应用程序版本进行操作。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.AppV.AppvClientPowerShell.AppvClientApplication

## 备注

## 相关链接

[Get-AppvClientConfiguration](./Get-AppvClientConfiguration.md)

