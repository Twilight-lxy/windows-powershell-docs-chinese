---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/get-wmsversion?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WmsVersion
---

# Get-WmsVersion

## 摘要
获取服务器版本、连接器版本以及SKU信息。

## 语法

```
Get-WmsVersion [-Server <String>] [<CommonParameters>]
```

## 描述
**Get-WmsVersion** cmdlet 可以获取多点服务器（MultiPoint Server）的版本信息、多点连接器（MultiPoint Connector）的版本信息，以及多点产品的SKU（产品标识符）。

## 示例

### 示例 1：获取多点（MultiPoint）版本
```
PS C:\> Get-WmsVersion
ServerVersion                 ClientVersion                         SKU     ProtocolVersion
-------------                 -------------                         ---     ---------------
10.0.10586.0                  10.0.10586.0                          77      1
```

这个命令可以获取当前计算机的版本信息。

## 参数

### -Server
指定该命令的目标端——即多点服务器（MultiPoint Server）的完全限定主机名。默认值为 `localhost`。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft.WindowsServerSolutions.MultipointServer POWERShellCommands.Library.WmsVersion

## 备注

## 相关链接

