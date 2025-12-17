---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsfarminformation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsFarmInformation
---

# 获取 AdFS 农场信息

## 摘要
获取 Active Directory Federation Services (AD FS) 的行为级别信息以及农场节点（farm nodes）的相关数据。

## 语法

```
Get-AdfsFarmInformation [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Get-AdfsFarmInformation` cmdlet 可以获取当前的 Active Directory Federation Services (AD FS) 行为级别以及农场节点信息。

## 示例

#### 示例 1：获取农场信息
```
PS C:\> Get-AdfsFarmInformation
```

这个cmdlet用于获取AD FS的行为级别以及农场节点（farm nodes）的相关信息。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行该操作。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

## 输出

## 备注

## 相关链接

[Set-AdfsFarmInformation](./Set-AdfsFarmInformation.md)

