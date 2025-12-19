---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/get-iisapppool?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IISAppPool
---

# Get-IISAppPool

## 摘要
获取IIS应用程序池的配置信息。

## 语法

```
Get-IISAppPool [[-Name] <String[]>] [<CommonParameters>]
```

## 描述
`Get-IISAppPool` cmdlet 可以获取关于应用程序池及其当前状态等关键信息。如果请求的是某个特定的应用程序池，或者是一个用逗号分隔的应用程序池列表，那么只会返回那些名称作为参数传递的应用程序池；否则会返回所有的应用程序池。

## 示例

### 示例 1：获取关于特定应用池的信息
```powershell
PS C:\> Get-IISAppPool "DefaultAppPool","NewAppPool"
Name                 Status       CLR Ver  Pipeline Mode  Start Mode
----                 ------       -------  -------------  ----------
DefaultAppPool       Started      v4.0     Integrated     OnDemand
NewAppPool           Started      v4.0     Integrated     OnDemand
```

这个命令用于获取DefaultAppPool和NewAppPool这两个池的配置信息。

### 示例 2：获取有关所有应用程序池的信息
```powershell
PS C:\> Get-IISAppPool
Name                 Status       CLR Ver  Pipeline Mode  Start Mode
----                 ------       -------  -------------  ----------
DefaultAppPool       Started      v4.0     Integrated     OnDemand
.NET v4.5 Classic    Started      v4.0     Classic        OnDemand
.NET v4.5            Started      v4.0     Integrated     OnDemand
PattiFul             Stopped      v4.0     Integrated     OnDemand
```

这个命令可以获取所有应用程序池的配置信息。

## 参数

### -Name
指定用于返回配置信息的应用程序池的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### System.Object

## 备注

## 相关链接

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

[适用于 Windows PowerShell 的 Web 管理 cmdlet](../webadministration/WebAdministration.md)

