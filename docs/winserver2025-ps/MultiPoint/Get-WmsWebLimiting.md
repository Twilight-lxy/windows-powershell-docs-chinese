---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/get-wmsweblimiting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WmsWebLimiting
---

# Get-WmsWebLimiting

## 摘要
获取网络限制配置信息。

## 语法

```
Get-WmsWebLimiting [-SessionId <UInt32>] [-Server <String>] [<CommonParameters>]
```

## 描述
**Get-WmsWebLimiting** cmdlet 可以获取网页访问限制配置信息，包括允许访问的 URL、被阻止的 URL 以及系统当前处于“允许访问”模式还是“禁止访问”模式。

## 示例

#### 示例 1：获取网页限制信息
```
PS C:\> Get-WmsWebLimiting
Sites             IsInLimiting                IsAllowList
-----             -----------                 ----------
{test.com}        True                        False
```

这个命令可以获取当前计算机的网络限制信息。


## 参数

### -Server
指定作为该命令目标的多点服务器（MultiPoint Server）的完全限定主机名。默认值为 `localhost`。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ComputerName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SessionId
指定一个包含多点会议 ID（MultiPoint Session IDs）的数组。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### `System Nullable`  
1[[`System.UInt32`, `mscorlib`, `Version=4.0.0.0`, `Culture=neutral`, `PublicKeyToken=b77a5c561934e089`]]

### System.String

## 输出

### Microsoft.WindowsServerSolutions.MultipointServer.PowerShell Commands.Library.WebLimitSetting

## 备注

## 相关链接

[Disable-WmsWebLimiting](./Disable-WmsWebLimiting.md)

[Enable-WmsWebLimiting](./Enable-WmsWebLimiting.md)

[Set-WmsWebLimiting](./Set-WmsWebLimiting.md)

