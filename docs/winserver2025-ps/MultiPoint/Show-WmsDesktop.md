---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/show-wmsdesktop?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Show-WmsDesktop
---

# Show-WmsDesktop

## 摘要
将当前共享的桌面显示给指定的会话。

## 语法

### 显示会话列表（ShowSessionList）
```
Show-WmsDesktop [-SessionId] <UInt32[]> -Desktop <WmsDesktop> [-Server <String>] [<CommonParameters>]
```

### ShowAll
```
Show-WmsDesktop [-All] -Desktop <WmsDesktop> [-Server <String>] [<CommonParameters>]
```

### RemoteControl
```
Show-WmsDesktop -Desktop <WmsDesktop> [-Title <String>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Show-WmsDesktop` cmdlet 用于将当前共享的桌面显示给当前 Windows MultiPoint Server 系统中指定的会话。

## 示例

### 示例 1：展示桌面界面
```
PS C:\> Show-WmsDesktop -Invitation "See My Shared Desktop" -SessionId "1,2" -Title "Teacher's Desktop"
```

此命令将桌面显示到指定的会话列表中。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: ShowAll
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Desktop
{{填写桌面描述}}

```yaml
Type: WmsDesktop
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Server
指定作为命令目标的多点服务器（MultiPoint Server）的完全限定主机名。默认值为 localhost。

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
Parameter Sets: ShowSessionList
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Title
指定一个标题。

```yaml
Type: String
Parameter Sets: RemoteControl
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32[]

### Microsoft.WindowsServerSolutions.MultipointServer.PowerShellcommands.Library.WmsDesktop

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Unpublish-WmsDesktop](./Unpublish-WmsDesktop.md)

[发布 WMS 桌面应用](./Publish-WmsDesktop.md)

