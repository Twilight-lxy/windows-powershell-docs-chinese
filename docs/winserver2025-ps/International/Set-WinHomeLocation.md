---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/set-winhomelocation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WinHomeLocation
---

# 设置 WinHome 的位置

## 摘要
为当前用户账户设置家庭位置信息。

## 语法

```
Set-WinHomeLocation [-GeoId] <Int32> [<CommonParameters>]
```

## 描述
`Set-WinHomeLocation` cmdlet 用于设置用户 `GeoID` 对象的值。Windows 的 `GeoID` 设置是一种描述当前用户账户所在地的用户配置项。所谓“所在地”，指的是该用户所属的国家或地区。那些需要获取当前用户账户所在地的应用程序（例如电视调谐器的相关驱动程序）就可以使用这一设置。

有关地理ID（GeoIDs）的表格，请参阅[地理位置](https://go.microsoft.com/fwlink/?LinkID=242308)的相关内容。

## 示例

#### 示例 1：设置起始位置
```
PS C:\> Set-WinHomeLocation -GeoId 0xF4
```

此命令将当前用户账户的主位置设置为 0xF4（十六进制）（美国）。

## 参数

### -GeoId
指定一个GeoID设置。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[RegionInfo.GeoId 属性](https://go.microsoft.com/fwlink/?LinkID=242310)

[Get-WinHomeLocation](./Get-WinHomeLocation.md)

