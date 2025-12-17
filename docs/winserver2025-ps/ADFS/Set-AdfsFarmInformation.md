---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsfarminformation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsFarmInformation
---

# 设置 AdFS 农场信息

## 摘要
从农场信息表中删除过时或离线的农场节点。

## 语法

```
Set-AdfsFarmInformation [-RemoveNode <String[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsFarmInformation` cmdlet 用于从Active Directory Federation Services（AD FS）农场节点信息表中删除过时或处于离线状态的农场节点，以确保该列表始终反映最新的农场节点状态。

## 示例

### 示例 1：移除一个不再使用的节点
```
PS C:\> Set-AdfsFarmInformation -RemoveNode "adfs02.contoso.com"
```

此命令会从农场信息表中删除名为 adfs02.contoso.com 的节点。

## 参数

### -RemoveNode
指定一个包含完全限定域名（FQDN）的数组，这些域名对应于需要从AD FS农场信息表中移除的农场节点。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-AdfsFarmInformation](./Get-AdfsFarmInformation.md)

