---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/publish-wmsdesktop?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Publish-WmsDesktop
---

# 发布 WMS Desktop 版本

## 摘要
允许多人共享同一台桌面电脑，并可选择是否允许远程控制该桌面。

## 语法

```
Publish-WmsDesktop [-SessionId] <UInt32> [-RemoteControl] [-MaxViewers <Int32>] [-Server <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
**Publish-WmsDesktop** 这个cmdlet用于共享指定的会话桌面，从而使其他会话能够查看该桌面。此外，被共享的桌面还可以选择性地进行远程控制。

## 示例

#### 示例 1：发布一个桌面应用程序
```
PS C:\> Publish-WmsDesktop -RemoteControl -MaxViewers 10 -SessionId 2 -TeacherName "PattiFuller"





Invitation string
```

此命令允许最多10个其他会话共享第2个会话的桌面内容进行查看，并支持对这些桌面的远程控制。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -MaxViewers
指定可以查看已发布桌面内容的最大客户端数量。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemoteControl
表示已发布的桌面版本可以远程控制。

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

### -Server
指定作为该命令目标的多点服务器（MultiPoint Server）的完全限定主机名。默认值为 localhost。

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
指定要发布的桌面的会话 ID。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32

### System.String

## 输出

### Microsoft.WindowsServerSolutions.MultipointServer.PowerShell Commands.Library.WmsDesktop

## 备注

## 相关链接

[显示WMS桌面](./Show-WmsDesktop.md)

[Unpublish-WmsDesktop](./Unpublish-WmsDesktop.md)

