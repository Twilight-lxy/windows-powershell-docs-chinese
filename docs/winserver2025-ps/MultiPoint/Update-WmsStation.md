---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/update-wmsstation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-WmsStation
---

# 更新 WMS 站点

## 摘要
强制一个站点重新加载其配置设置。

## 语法

### UpdateById
```
Update-WmsStation [-StationId] <UInt32[]> [-Server <String>] [<CommonParameters>]
```

### UpdateAll
```
Update-WmsStation [-All] [-Server <String>] [<CommonParameters>]
```

## 描述
`Update-WmsStation` cmdlet 会强制指定的气象站重新加载其配置设置。

## 示例

### 示例 1：更新车站设置
```
PS C:\> Update-WmsStation -StationId 2
```

该命令强制站点2重新加载其配置设置。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: UpdateAll
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定作为该命令目标的MultiPoint Server的完全限定主机名。默认值为localhost。

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

### -StationId
指定一个车站ID数组。

```yaml
Type: UInt32[]
Parameter Sets: UpdateById
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32[]

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Clear-WmsStation](./Clear-WmsStation.md)

[Get-WmsStation](./Get-WmsStation.md)

[Join-WmsStation](./Join-WmsStation.md)

[Set-WmsStation](./Set-WmsStation.md)

[Split-WmsStation](./Split-WmsStation.md)

