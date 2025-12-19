---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/get-winhomelocation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WinHomeLocation
---

# Get-WinHomeLocation

## 摘要
获取当前用户账户的 Windows GeoID 家庭位置设置。

## 语法

```
Get-WinHomeLocation [<CommonParameters>]
```

## 描述
`Get-WinHomeLocation` cmdlet 可以获取用户的 GeoID 设置值，并返回一个 .NET GeoID 对象。Windows 的 GeoID 设置是一个描述当前用户账户所在国家或地区的设置。需要知道当前用户账户所在位置的应用程序（例如电视调谐器应用程序的相关驱动程序）可以使用这个设置。

有关地理标识符（GeoIDs）的表格，请参见[地理位置表](https://go.microsoft.com/fwlink/?LinkID=242308)。

## 示例

### 示例 1：显示当前账户的 GeoID
```
PS C:\> Get-WinHomeLocation
HomeLocation     Description
----             -----------
244              United States
```

此命令返回当前用户账户的GeoID设置及其显示名称。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### GeoID
此cmdlet返回一个32位有符号数，该数字唯一地标识了一个地理位置。

## 备注

## 相关链接

[RegionInfo.GeoId 属性](https://go.microsoft.com/fwlink/?LinkID=242310)

[Set-WinHomeLocation](./Set-WinHomeLocation.md)

