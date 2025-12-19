---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamAccessScope.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/set-ipamaccessscope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IpamAccessScope
---

# 设置 Ipam 访问范围（Set-IpamAccessScope）

## 摘要
配置 IPAM 访问范围。

## 语法

### SetRange
```
Set-IpamAccessScope [-IpamRange] [-AccessScopePath <String>] [-IsInheritedAccessScope]
 -InputObject <CimInstance[]> [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SetDnsServer
```
Set-IpamAccessScope [-AccessScopePath <String>] [-IsInheritedAccessScope] -InputObject <CimInstance[]>
 [-PassThru] [-IpamDnsServer] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### SetDhcpServer
```
Set-IpamAccessScope [-AccessScopePath <String>] [-IsInheritedAccessScope] -InputObject <CimInstance[]>
 [-PassThru] [-IpamDhcpServer] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### SetDhcpSuperscope
```
Set-IpamAccessScope [-AccessScopePath <String>] [-IsInheritedAccessScope] -InputObject <CimInstance[]>
 [-PassThru] [-IpamDhcpSuperscope] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### SetDhcpScope
```
Set-IpamAccessScope [-AccessScopePath <String>] [-IsInheritedAccessScope] -InputObject <CimInstance[]>
 [-PassThru] [-IpamDhcpScope] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### SetDnsConditionalForwarder
```
Set-IpamAccessScope [-AccessScopePath <String>] [-IsInheritedAccessScope] -InputObject <CimInstance[]>
 [-PassThru] [-IpamDnsConditionalForwarder] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 设置 DNS 资源记录（SetDnsResourceRecord）
```
Set-IpamAccessScope [-AccessScopePath <String>] [-IsInheritedAccessScope] -InputObject <CimInstance[]>
 [-PassThru] [-IpamDnsResourceRecord] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### SetDnsZone
```
Set-IpamAccessScope [-AccessScopePath <String>] [-IsInheritedAccessScope] -InputObject <CimInstance[]>
 [-PassThru] [-IpamDnsZone] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### SetAddressSpace
```
Set-IpamAccessScope [-AccessScopePath <String>] [-IsInheritedAccessScope] -InputObject <CimInstance[]>
 [-PassThru] [-IpamAddressSpace] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### SetSubnet
```
Set-IpamAccessScope [-AccessScopePath <String>] [-IsInheritedAccessScope] -InputObject <CimInstance[]>
 [-PassThru] [-IpamSubnet] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### SetBlock
```
Set-IpamAccessScope [-AccessScopePath <String>] [-IsInheritedAccessScope] -InputObject <CimInstance[]>
 [-PassThru] [-IpamBlock] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-IpamAccessScope` 用于配置 IP 地址管理（IPAM）服务器的访问范围。访问范围用于管理对 IPAM 对象（如域名系统（DNS）服务器、动态主机配置协议（DHCP）作用域、IP 地址范围等）的权限。

当你安装 IPAM 时，系统会自动为你创建一个全局范围（global scope）。默认情况下，具有该全局范围权限的用户可以访问 IPAM 基础设施中的所有资源。为了更精确地控制访问权限，你可以创建子范围（subscopes），例如基于地理位置或工作角色的子范围。你可以使用 **Set-IpamAccessScope** cmdlet 来为特定的 IPAM 对象分配访问权限。

需要设置访问范围的 IPAM 对象通过 **InputObject** 参数提供。

## 示例

#### 示例 1：配置访问范围
```
PS C:\> $Zone = Get-IpamDnsZone -ZoneType Forward -ZoneName "dublin.contoso.com"
PS C:\> Set-IpamAccessScope -IpamDnsZone -InputObject $Zone -AccessScopePath "\Global\Europe" -PassThru
```

第一个命令获取名为 `dublin.contoso.com` 的 IPAM DNS 区域，并将其存储在变量 `$Zone` 中。第二个命令向访问范围 `Global\Europe` 中添加 DHCP 范围（scope）和超级范围（superscope）。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。世界时坐标（Universal Time Coordinate）

## 参数

### -AccessScopePath
指定访问范围的路径。所有访问范围都必须是全局范围的子元素。

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

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
此参数的可接受值为：

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

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IpamAddressSpace
表示访问范围被分配给了 IPAM（IP Address Management）地址空间对象。一个地址空间包含 IP 块、IP 子网、IP 范围以及 IP 地址。

```yaml
Type: SwitchParameter
Parameter Sets: SetAddressSpace
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IpamBlock
表示访问权限范围被分配给了IP地址块对象。IP地址块是用于地址空间管理的最大单位，它由称为“IP地址范围”的更小单元组成。

```yaml
Type: SwitchParameter
Parameter Sets: SetBlock
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IpamDhcpScope
表示访问范围被分配给了DHCP范围对象。

```yaml
Type: SwitchParameter
Parameter Sets: SetDhcpScope
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IpamDhcpServer
表示访问权限被分配给了DHCP服务器。

```yaml
Type: SwitchParameter
Parameter Sets: SetDhcpServer
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IpamDhcpSuperscope
表示该访问权限被分配给了 DHCP 超范围（DHCP superscopes）。

```yaml
Type: SwitchParameter
Parameter Sets: SetDhcpSuperscope
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IpamDnsConditionalForwarder
表示访问权限被分配给了DNS条件转发器（DNS Conditional Forwarders）。

```yaml
Type: SwitchParameter
Parameter Sets: SetDnsConditionalForwarder
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IpamDnsResourceRecord
表示访问权限范围被分配给了DNS资源记录。

```yaml
Type: SwitchParameter
Parameter Sets: SetDnsResourceRecord
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IpamDnsServer
表示访问权限被分配给了DNS服务器。

```yaml
Type: SwitchParameter
Parameter Sets: SetDnsServer
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IpamDnsZone
表示访问权限被分配给了DNS区域。

```yaml
Type: SwitchParameter
Parameter Sets: SetDnsZone
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IpamRange
表示访问范围被分配给 IPv4 或 IPv6 地址范围。地址范围是根据地址家族、起始地址/结束地址等特征来划分的 IP 地址集合。

```yaml
Type: SwitchParameter
Parameter Sets: SetRange
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IpamSubnet
表示访问权限被分配给了特定的 IP 子网。

```yaml
Type: SwitchParameter
Parameter Sets: SetSubnet
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsInheritedAccessScope
表示输入对象被分配到其父对象的访问范围内。例如，如果输入对象是一个DNS资源记录，那么它的访问范围将被设置为该资源记录所属的DNS区域的访问范围。

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
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不生成任何输出。

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
该参数用于指定可以同时执行该cmdlet的最大操作数量。如果省略此参数或输入值`0`，Windows PowerShell®将根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前执行的cmdlet，而不适用于整个会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Windows PowerShell中的IP地址管理（IPAM）服务器cmdlet](./ipamserver.md)

