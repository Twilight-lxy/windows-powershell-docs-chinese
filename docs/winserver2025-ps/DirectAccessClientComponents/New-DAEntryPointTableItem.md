---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DASiteTableEntry.cdxml-help.xml
Module Name: DirectAccessClientComponents
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/directaccessclientcomponents/new-daentrypointtableitem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-DAEntryPointTableItem
---

# New-DAEntryPointTableItem

## 摘要
为多站点DirectAccess配置一个新的入口点。

## 语法

### 使用 ByPolicyStore（默认设置）
```
New-DAEntryPointTableItem [-PolicyStore] <String> -EntryPointName <String> -ADSite <String>
 -EntryPointRange <String[]> [-TeredoServerIP <String>] -EntryPointIPAddress <String> [-GslbIP <String>]
 [-IPHttpsProfile <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ByGpoSession
```
New-DAEntryPointTableItem -EntryPointName <String> -ADSite <String> -EntryPointRange <String[]>
 [-TeredoServerIP <String>] -EntryPointIPAddress <String> [-GslbIP <String>] [-IPHttpsProfile <String>]
 [-GPOSession] <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`New-DAEntryPointTableItem` cmdlet 用于配置多站点 DirectAccess 的新入口点。管理员通过使用组策略（Group Policy）将新的入口点分发到 DirectAccess 客户端计算机上，客户端计算机在适当的情况下会使用这个新的入口点。

## 示例

### 示例1：创建一个新的入口点
```
PS C:\> New-DAEntryPointTableItem -PolicyStore "GPO:Localhost" -ADSite "Paris" -EntryPointRange "2001::/16" -TeredoServerIP "131.107.1.1" -EntryPointIPAddress "200::1" -GslbIP "131.107.0.1" -EntryPointName "Paris"
```

这个cmdlet创建了一个名为“Paris”的简单入口点。

## 参数

### -ADSite
指定与入口点关联的 Active Directory 域服务（AD DS）站点名称。当客户端计算机连接到某个入口点时，该计算机就会与该指定的 AD DS 站点建立关联。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后再显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -EntryPointIPAddress
指定用于连接的入口点的 IPv6 地址。如果指定的 IP 地址不在 *EntryPointRange* 指定的 IP 地址范围内，该 cmdlet 将会失败。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EntryPointName
指定入口点的名称。入口点名称通常是该地点的友好名称，例如“Redmond”（雷德蒙德）或“Paris”（巴黎）。

使用双引号（“”）来指定入口点的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EntryPointRange
指定与此入口点连接的计算机所使用的 IPv6 地址范围。请使用无类别域间路由（CIDR）表示法来指定该 IPv6 地址范围。

以下是一个 *EntryPointRange* 条目的示例：

`{2001:4898:e0:305d::100:1/128, 2001:4898:e0:305d::100:2/128, 2001:4898:e0:3084::/64}`

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GPOSession
指定用于发送配置信息的组策略会话。您可以使用 *GPOSession* 与 **NetGPO** 命令集，来汇总对某个组策略对象执行的多个操作。

*GPOSession* 不能与 *PolicyStore* 同时使用。

```yaml
Type: String
Parameter Sets: ByGpoSession
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GslbIP
如果在使用 DirectAccess 时同时结合全局服务器负载均衡（GSLB）进行站点平衡，那么该字段用于指定与新入口点关联的 IP 地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPHttpsProfile
指定用于连接的 IPHTTPs 配置文件的名称。配置文件的名称需要用双引号 (“”) 括起来。如果该配置文件在包含相关设置的 GPO 中还不存在，`New-DAEntryPointTableItem` 命令将执行失败。有关 IPHTTPs 配置文件的更多信息，请参阅 `NetworkTransition` 模块中的 `NetIPHTTPsConfiguration` cmdlet。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PolicyStore
指定该cmdlet将入口点添加到的策略存储位置。

要将入口点添加到组策略对象（Group Policy Object，简称GPO）中，请使用以下格式指定GPO的名称：“Domain\GPOName”

要将入口点信息添加到计算机的本地组策略对象（GPO）中，请按照以下格式指定该计算机的本地GPO名称：“GPO:\<计算机名称\>”

*PolicyStore* 不能与 *GPOSession* 同时使用。

```yaml
Type: String
Parameter Sets: ByPolicyStore
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TeredoServerIP
为新入口点指定Teredo服务器的IP地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/StandardCimv2/MSFT_DASiteTableEntry
此cmdlet返回一个CIM对象，其中包含新的DA入口点表项。

## 备注

## 相关链接

[Get-DAEntryPointTableItem](./Get-DAEntryPointTableItem.md)

[Remove-DAEntryPointTableItem](./Remove-DAEntryPointTableItem.md)

[ Rename-DAEntryPointTableItem](./Rename-DAEntryPointTableItem.md)

[Reset-DAEntryPointTableItem](./Reset-DA EntryPointTableItem.md)

[Set-DAEntryPointTableItem](./Set-DAEntryPointTableItem.md)

