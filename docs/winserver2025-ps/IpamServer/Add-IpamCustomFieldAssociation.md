---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamCustomFieldAssociation.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/add-ipamcustomfieldassociation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-IpamCustomFieldAssociation
---

# Add-IpamCustomFieldAssociation

## 摘要
在IPAM中定义的自定义字段的值之间建立关联关系。

## 语法

```
Add-IpamCustomFieldAssociation [-CustomFieldOne] <String> [-CustomFieldTwo] <String>
 [-AssociationValue] <String[]> [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-IpamCustomFieldAssociation` cmdlet 用于在 IP 地址管理（IPAM）中定义的两个自定义字段的值之间建立关联。请使用 `CustomFieldOne` 和 `CustomFieldTwo` 参数来指定这两个自定义字段，并以 `CustomFieldValue01:CustomFieldValue02` 的格式将关联值作为一对对的数组来提供。

使用 `Get-IpamCustomFieldAssociation` cmdlet 可以查看现有的关联关系。使用 `Set-IpamCustomFieldAssociation` cmdlet 可以修改这些关联关系。使用 `Remove-IpamCustomFieldAssociation` cmdlet 可以删除这些关联关系。

## 示例

### 示例 1：在两个字段之间创建自定义关联
```
PS C:\> Add-IpamCustomFieldAssociation  -CustomFieldOne "VmmLogicalNetwork" -CustomFieldTwo "NetworkSite" -AssociationValue "Storage:Site01","Storage:Site02","Public:Site03" -PassThru
CustomFieldOne   : VmmLogicalNetwork

CustomFieldTwo   : NetworkSite

AssociationValue : {Public:Site03, Storage:Site02, Storage:Site01
```

此命令在两个自定义字段（VmmLogicalNetwork 和 NetworkSite）的值之间建立了关联。该命令指定了三组值组合，并使用了 *PassThru* 参数，因此会将结果显示在控制台上。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -AssociationValue
指定一个值对数组。每个值对（由一个字符串表示）包含两个用冒号（:）分隔的值。值对中的第一个值对应于通过*CustomFieldOne*参数指定的自定义字段，第二个值对应于通过*CustomFieldTwo*参数指定的自定义字段。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，使用的是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前，会提示您进行确认。

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

### -CustomFieldOne
指定一个自定义字段。该字段对应于通过 *AssociationValue* 参数指定的值对中的第一个值。

```yaml
Type: String
Parameter Sets: (All)
Aliases: CustomField1

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CustomFieldTwo
指定一个自定义字段。该字段对应于通过 *AssociationValue* 参数指定的值对中的第二个值。

```yaml
Type: String
Parameter Sets: (All)
Aliases: CustomField2

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
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

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamCustomFieldAssociation
此cmdlet返回一个对象，该对象表示一个自定义字段的值与另一个自定义字段的值之间的关联关系。

## 备注

## 相关链接

[Get-IpamCustomFieldAssociation](./Get-IpamCustomFieldAssociation.md)

[Set-IpamCustomFieldAssociation](./Set-IpamCustomFieldAssociation.md)

[ Remove-IpamCustomFieldAssociation](./Remove-IpamCustomFieldAssociation.md)

