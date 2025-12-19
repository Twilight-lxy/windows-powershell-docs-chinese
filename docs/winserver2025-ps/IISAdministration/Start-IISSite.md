---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/start-iissite?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-IISSite
---

# 启动 IISSite

## 摘要
在 IIS 服务器上启动一个已存在的网站。

## 语法

```
Start-IISSite [-Name] <String> [-Passthru] [<CommonParameters>]
```

## 描述
`Start-IISSite` cmdlet 用于在 Internet Information Services (IIS) 服务器上启动一个已存在的网站。

## 示例

### 示例 1：启动一个 IIS 网站
```
PS C:\> Start-IISSite -Name "Default Web Site"
```

这个命令用于启动一个名为“Default Web Site”的IIS网站。

## 参数

### -Name
指定 IIS 网站的名字。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Passthru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[获取 IISSite](./Get-IISSite.md)

[New-IISSite](./New-IISSite.md)

[Remove-IISSite](./Remove-IISSite.md)

[停止-IISSite](./Stop-IISSite.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

