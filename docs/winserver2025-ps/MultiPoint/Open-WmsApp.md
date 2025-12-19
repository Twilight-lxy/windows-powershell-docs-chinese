---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/open-wmsapp?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Open-WmsApp
---

# Open-WmsApp

## 摘要
在一个会话中启动一个应用程序。

## 语法

```
Open-WmsApp [-SessionId] <UInt32[]> [-FileToRun] <String> [-Server <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Open-WmsApp` cmdlet 会根据该 cmdlet 中指定的应用程序，在指定的会话中启动相应的应用程序。

## 示例

### 示例 1：打开一个应用程序
```
PS C:\> Open-WmsApp -SessionId 3 -FileToRun "notepad.exe"
```

这个命令会在会话3中启动记事本（Notepad）。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您确认是否要执行该操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -FileToRun
指定要启动的文件。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定作为该命令目标的多点服务器（MultiPoint Server）的完全限定主机名。默认值为“localhost”。

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
指定一个会话ID数组。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32[]

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Close-WmsApp](./Close-WmsApp.md)

[Get-WmsApp](./Get-WmsApp.md)

