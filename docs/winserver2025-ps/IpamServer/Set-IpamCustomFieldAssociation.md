---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamCustomFieldAssociation.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/set-ipamcustomfieldassociation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IpamCustomFieldAssociation
---

# 设置 Ipam 自定义字段关联关系

## 摘要
修改在 IPAM 中定义的自定义字段的值之间的关联关系。

## 语法

```
Set-IpamCustomFieldAssociation [-CustomFieldOne] <String> [-CustomFieldTwo] <String>
 [-AddAssociationValue <String[]>] [-RemoveAssociationValue <String[]>] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-IpamCustomFieldAssociation` cmdlet 用于修改在 IP 地址管理（IPAM）中定义的两个自定义字段之间的值关联关系。请使用 `CustomFieldOne` 和 `CustomFieldTwo` 参数来指定这些自定义字段，并以 `CustomFieldName01, CustomFieldValue02` 的格式，将需要添加或删除的值作为值对数组传递给该 cmdlet。

该cmdlet会删除由*RemoveAssociationValue*参数指定的值，然后添加由*AddAssociationValue*参数指定的值。如果您尝试删除不存在的值，cmdlet会返回一个错误，并且不会进行任何更改。

使用 `Get-IpamCustomFieldAssociation` cmdlet 查看现有的关联关系。使用 `Add-IpamCustomFieldAssociation` cmdlet 创建新的关联关系。使用 `Remove-IpamCustomFieldAssociation` cmdlet 删除关联关系。

## 示例

### 示例 1：修改关联关系
```
PS C:\> Set-IpamCustomFieldAssociation -CustomFieldOne "VmmLogicalNetwork" -CustomFieldTwo "NetworkSite" -AddAssociateValue "Storage:Site03" -RemoveAssociationValue "Public:Site03" -PassThru
CustomFieldOne   : VmmLogicalNetwork

CustomFieldTwo   : NetworkSite

AssociationValue : {Storage:Site01, Storage:Site03, Storage:Site02}
```

此命令用于修改两个自定义字段（VmmLogicalNetwork 和 NetworkSite）之间已存在的关联关系。该命令指定了需要添加或删除的值，并包含了 *PassThru* 参数，因此会将执行结果显示在控制台上。

## 参数

### -AddAssociationValue
指定一个值对数组。每个值对都由一个字符串表示，其中包含两个用冒号（:）分隔的值。值对中的第一个值对应于由 *CustomFieldOne* 参数指定的自定义字段；第二个值对应于由 *CustomFieldTwo* 参数指定的自定义字段。

该cmdlet会添加指定的配对项。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，随后显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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

### -CustomFieldOne
用于指定一个自定义字段。该字段对应于通过使用 *AddAssociationValue* 或 *RemoveAssociationValue* 参数指定的值对中的第一个值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CustomFieldTwo
用于指定一个自定义字段。该字段对应于通过使用 *AddAssociationValue* 或 *RemoveAssociationValue* 参数指定的配对中的第二个值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

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

### -RemoveAssociationValue
指定一个值对数组。每个值对都由一个字符串表示，其中包含两个用冒号（:）分隔的值。值对中的第一个值对应于由 *CustomFieldOne* 参数指定的自定义字段；第二个值对应于由 *CustomFieldTwo* 参数指定的自定义字段。

此cmdlet会删除指定的配对信息。如果您指定了一个不存在的配对，cmdlet会返回错误信息。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet被运行会发生的结果。但实际上这个cmdlet并没有被运行。

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

### IpamCustomFieldAssociation
一个用于表示一个自定义字段的值与另一个自定义字段的值之间关联的对象。

## 备注

## 相关链接

[Get-IpamCustomFieldAssociation](./Get-IpamCustomFieldAssociation.md)

[Add-IpamCustomFieldAssociation](./Add-IpamCustomFieldAssociation.md)

[Remove-IpamCustomFieldAssociation](./Remove-IpamCustomFieldAssociation.md)

