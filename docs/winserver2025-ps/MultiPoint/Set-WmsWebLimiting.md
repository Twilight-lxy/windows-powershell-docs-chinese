---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/set-wmsweblimiting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WmsWebLimiting
---

# Set-WmsWebLimiting

## 摘要
为标准用户会话配置网络访问限制功能。

## 语法

### 允许列表（AllowList）
```
Set-WmsWebLimiting [-Allow] [-Sites] <String[]> [-Server <String>] [<CommonParameters>]
```

### BlockList
```
Set-WmsWebLimiting [-Block] [-Sites] <String[]> [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-WmsWebLimiting` cmdlet 用于配置当前 Windows MultiPoint Server 系统中标准用户会话的网页访问限制功能。

## 示例

#### 示例 1：阻止访问某些网站
```
PS C:\> Set-WmsWebLimiting -Sites "www.test.com", "www.test1.com" -Block
```

这个命令会阻止对指定URL的访问。

## 参数

### -Allow
表示此操作允许访问指定的网站。

```yaml
Type: SwitchParameter
Parameter Sets: AllowList
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Block
表示此操作会阻止访问指定的网站。

```yaml
Type: SwitchParameter
Parameter Sets: BlockList
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定该命令的目标多点服务器（MultiPoint Server）的完全限定主机名。默认值为“localhost”。

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

### -Sites
指定一个网站数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Disable-WmsWebLimiting](./Disable-WmsWebLimiting.md)

[Enable-WmsWebLimiting](./Enable-WmsWebLimiting.md)

[Get-WmsWebLimiting](./Get-WmsWebLimiting.md)

