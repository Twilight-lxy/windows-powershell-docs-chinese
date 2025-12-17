---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsattributestore?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsAttributeStore
---

# Get-AdfsAttributeStore

## 摘要
获取联邦服务的属性存储信息。

## 语法

```
Get-AdfsAttributeStore [[-Name] <String[]>] [<CommonParameters>]
```

## 描述
`Get-AdfsAttributeStore` cmdlet 用于获取联邦服务的属性存储信息。如果您不指定任何参数，该 cmdlet 将获取联邦服务的所有属性存储信息。

## 示例

## 参数

### -Name
指定一个属性存储名称数组，该cmdlet将从这些存储中获取数据。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

*Name* 参数接收的是一个字符串对象。

## 输出

### MicrosoftIdentityServer.Management.Resources.AttributeStore

返回一个或多个 `AttributeStore` 对象，这些对象代表了联邦服务的属性存储机制。

## 备注

## 相关链接

[添加 AdFS 属性存储](./Add-AdfsAttributeStore.md)

[Remove-AdfsAttributeStore](./Remove-AdfsAttributeStore.md)

[Set-AdfsAttributeStore](./Set-AdfsAttributeStore.md)

