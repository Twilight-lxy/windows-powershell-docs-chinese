---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamCustomFieldAssociation.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamcustomfieldassociation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamCustomFieldAssociation
---

# Get-IpamCustomFieldAssociation

## 摘要
获取在 IPAM 中定义的两个自定义字段之间的关联关系。

## 语法

```
Get-IpamCustomFieldAssociation [[-CustomFieldOne] <String>] [[-CustomFieldTwo] <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
**Get-IpamCustomFieldAssociation** cmdlet 用于获取在 IP 地址管理（IPAM）中定义的两个自定义字段之间的关联关系。您可以使用 *CustomFieldOne* 和 *CustomFieldTwo* 参数来指定这两个自定义字段。如果您只指定了其中一个参数，该 cmdlet 会获取所有包含所指定字段的关联关系。这些关联关系是双向的，因此您可以任意使用这两个参数中的任何一个来表示任一字段。如果您两个参数都不指定，该 cmdlet 会获取所有的关联关系。

使用 `Add-IpamCustomFieldAssociation` cmdlet 来创建关联关系。使用 `Remove-IpamCustomFieldAssociation` cmdlet 来删除关联关系。使用 `Set-IpamCustomFieldAssociation` cmdlet 来修改关联关系。

## 示例

### 示例 1：获取 IPAM 中所有自定义字段关联信息
```
PS C:\> Get-IpamCustomFieldAssociation
CustomFieldOne   : Region

CustomFieldTwo   : Site

AssociationValue : {Region03,Site09, Region03,Site10, Region03,Site11, Region03,Site12}

CustomFieldOne   : ManagedByService

CustomFieldTwo   : ServiceInstance

AssociationValue : {IPAM,Localhost, MS DHCP,dhcp1.contoso.com}
CustomFieldOne   : VmmLogicalNetwork

CustomFieldTwo   : NetworkSite

AssociationValue : {Public:Site03, Storage:Site02, Storage:Site01}
```

这个命令会获取在 IPAM 中指定的所有自定义字段之间的关联关系。

### 示例 2：获取两个自定义字段之间的关联关系
```
PS C:\> Get-IpamCustomFieldAssociation -CustomFieldOne "ManagedByService" -CustomFieldTwo "ServiceInstance"
CustomFieldOne   : ManagedByService

CustomFieldTwo   : ServiceInstance

AssociationValue : {IPAM:Localhost, MS DHCP:dhcp1.contoso.com}
```

这个命令用于获取两个自定义字段（ManagedByService 和 ServiceInstance）之间的关系。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在该作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列的 cmdlets；要获取作业结果，则可以使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -CustomFieldOne
指定一个自定义字段。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CustomFieldTwo
指定一个自定义字段。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的命令（cmdlet）的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-IpamCustomFieldAssociation](./Add-IpamCustomFieldAssociation.md)

[Remove-IpamCustomFieldAssociation](./Remove-IpamCustomFieldAssociation.md)

[Set-IpamCustomFieldAssociation](./Set-IpamCustomFieldAssociation.md)

