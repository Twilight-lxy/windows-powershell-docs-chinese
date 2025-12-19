---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/remove-wmsuser?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-WmsUser
---

# 删除 WMS 用户

## 摘要
从当前的多点服务器系统中删除一个本地用户。

## 语法

```
Remove-WmsUser [-Name] <String> [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-WmsUser` cmdlet 用于从当前的 Windows MultiPoint Server 系统中删除一个本地用户。

## 示例

### 示例 1：删除用户
```
PS C:\> Remove-WmsUser -Name "Student01"
```

这个命令会删除名为Student01的用户。

## 参数

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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

### -Name
指定要删除的用户账户的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Server
指定该命令的目标MultiPoint Server的完全限定主机名。默认值为localhost。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Get-WmsUser](Get-WmsUser.md)

[New-WmsUser](New-WmsUser.md)

[Set-WmsUser](Set-WmsUser.md)
