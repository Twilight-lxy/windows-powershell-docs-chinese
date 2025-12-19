---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/search-wmssystem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Search-WmsSystem
---

# Search-WmsSystem

## 摘要
获取在同一网络中运行的多点服务器（MultiPoint Servers）或安装了多点连接器（MultiPoint Connector）的个人电脑。

## 语法

```
Search-WmsSystem [-ManagedSystemsType] <ManagedSystemTypes> [-Server <String>] [<CommonParameters>]
```

## 描述
`Search-WmsSystem` cmdlet 可用于查找在同一网络中运行的其他多点服务器（MultiPoint Server）或安装了 MultiPoint Connector 的个人计算机。该操作完成所需时间为 10 秒。

## 示例

#### 示例 1：在子网中搜索多点服务器
```
PS C:\> Search-WmsSystem -ManagedSystemsType MultiPointServers
Test2
Test3
```

该cmdlet用于查找位于同一子网中的Windows多点服务器。查询完成需要大约10秒的时间，并使用Microsoft Web Services on Devices API（WSDAPI）来发现网络中的其他多点服务器。

## 参数

### -ManagedSystemsType
指定被管理的系统类型。该参数的可接受值为：PersonalComputers（个人电脑）和MultiPointServers（多点服务器）。

```yaml
Type: ManagedSystemTypes
Parameter Sets: (All)
Aliases:
Accepted values: MultiPointServers, PersonalComputers

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.String

## 备注

## 相关链接

[Add-WmsSystem](./Add-WmsSystem.md)

[Get-WmsSystem](./Get-WmsSystem.md)

[Remove-WmsSystem](./Remove-WmsSystem.md)

[重启 WMS 系统](./Restart-WmsSystem.md)

[Set-WmsSystem](./Set-WmsSystem.md)

[Stop-WmsSystem](./Stop-WmsSystem.md)

