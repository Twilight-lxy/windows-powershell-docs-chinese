---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamCustomField.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamcustomfield?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamCustomField
---

# Get-IpamCustomField

## 摘要
从 IPAM 中获取自定义字段信息。

## 语法

```
Get-IpamCustomField [[-Name] <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-IpamCustomField` 命令用于获取有关 IP 地址管理（IPAM）中自定义字段的信息。如果您不指定 `Name` 参数，该命令将检索 IPAM 中的所有自定义字段。对于多值自定义字段，该命令会同时检索自定义字段对象及其对应的自定义值。

## 示例

### 示例 1：获取所有自定义字段
```
PS C:\> Get-IpamCustomField
Name                 Category               Multivalue          CustomValue
----------------------------------------------------------------------------------------------------------------------------
AdSite                BuiltIn               False
CountryOrRegion       BuiltIn               True                {Afghanistan, Alfand Islands,...}
.....
.....
```

此命令可以检索IPAM服务器中所有的内置自定义字段和用户定义的自定义字段。对于多值字段，该命令会同时检索对应的自定义字段对象及其关联的自定义值对象。

### 示例 2：获取自定义字段
```
PS C:\> Get-IpamCustomField -Name "ManagedByService"
Name                 Category               Multivalue          CustomValue
----------------------------------------------------------------------------------------------------------------------------
ManagedByService      BuiltIn                True               {IPAM,MS DHCP,Non-MS DHCP...}
```

这个命令用于检索名为“ManagedByService”的自定义字段，然后获取该字段对应的自定义值。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Name
指定一个自定义字段的名称。

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

### -ThrottleLimit
指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.Windows.IpamCommands.IpamCustomField
此cmdlet返回一个对象，其中包含一个IPAM自定义字段。

## 备注

## 相关链接

[Add-IpamCustomField](./Add-IpamCustomField.md)

[Add-IpamCustomValue](./Add-IpamCustomValue.md)

