---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamCustomFieldAssociation.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/remove-ipamcustomfieldassociation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IpamCustomFieldAssociation
---

# 删除 Ipam 自定义字段关联

## 摘要
删除在 IPAM 中定义的两个自定义字段之间的关联关系。

## 语法

```
Remove-IpamCustomFieldAssociation [-CustomFieldOne] <String> [-CustomFieldTwo] <String> [-Force] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-IpamCustomFieldAssociation` cmdlet 用于删除在 IP 地址管理（IPAM）中定义的两个自定义字段之间的关联关系。您可以通过 `CustomFieldOne` 和 `CustomFieldTwo` 参数来指定这两个自定义字段。如果找不到同时包含这两个指定字段的关联关系，该 cmdlet 会向您提示错误信息；不过该 cmdlet 不会删除这些自定义字段本身。

使用 **Get-IpamCustomFieldAssociation** cmdlet 可以查看现有的关联关系。使用 **Add-IpamCustomFieldAssociation** cmdlet 可以创建新的关联关系。使用 **Set-IpamCustomFieldAssociation** cmdlet 可以修改关联关系。

## 示例

#### 示例 1：删除字段之间的关联
```
The first command removes the association between the two custom fields, VmmLogicalNetwork and NetworkSite. The cmdlet prompts you before it removes associations.
PS C:\> Remove-IpamCustomFieldAssociation -CustomFieldOne "VmmLogicalNetwork" -CustomFieldTwo "NetworkSite"
Confirm

This will permanently delete the Custom Field Association between Custom Field VmmLogicalNetwork and

NetworkSite.Do you want to continue?

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y


The second command uses the Get-IpamCustomFieldAssociation to get all associations. The associations that the first command removed do not appear.
PS C:\> Get-IpamCustomFieldAssociation
CustomFieldOne   : Region

CustomFieldTwo   : Site

AssociationValue : {Region01:Site09, Region01:Site10, Region01:Site11}
CustomFieldOne   : ManagedByService

CustomFieldTwo   : ServiceInstance

AssociationValue : {IPAM:Localhost, MS DHCP:dhcp1.contoso.com}
```

这个示例删除了字段之间的关联关系，然后验证了该删除操作是否成功。

### 示例 2：删除某个字段的所有关联关系
```
The first command uses the **Get-IpamCustomFieldAssociation** cmdlet to get all the associations specified by the ManagedByService custom field, and then passes them to the current cmdlet by using the pipeline operator. The cmdlet prompts you for confirmation, and then removes all the associations.
PS C:\> Get-IpamCustomFieldAssociation -CustomFieldOne "ManagedByService" | Remove-IpamCustomFieldAssociation
Confirm

This will permanently delete the Custom Field Association between Custom Field ManagedByService and

ServiceInstance.Do you want to continue?

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y

The second command uses the Get-IpamCustomFieldAssociation to get all associations. The associations that the first command removed do not appear.
PS C:\> Get-IpamCustomFieldAssociation
CustomFieldOne   : Region

CustomFieldTwo   : Site

AssociationValue : {Region01:Site09, Region01:Site10, Region01:Site11}
```

这个示例会删除指定字段的所有关联关系，然后验证这些关联关系是否已经被成功删除。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -CustomFieldOne
用于指定一个自定义字段。该cmdlet会删除此字段与由*CustomFieldTwo*参数指定的字段之间的关联。

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
用于指定一个自定义字段。该cmdlet会删除此字段与由*CustomFieldOne*参数指定的字段之间的关联关系。

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

### -Force
强制命令运行，而无需请求用户确认。

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

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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
指定可以同时运行的命令行参数（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令行参数的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-IpamCustomFieldAssociation](./Add-IpamCustomFieldAssociation.md)

[Get-IpamCustomFieldAssociation](./Get-IpamCustomFieldAssociation.md)

[Set-IpamCustomFieldAssociation](./Set-IpamCustomFieldAssociation.md)

