---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamAddressSpace.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/add-ipamaddressspace?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-IpamAddressSpace
---

# Add-IpamAddressSpace

## 摘要
向 IPAM（IP Address Management）系统中添加一个地址空间。

## 语法

### ProviderAddressSpace（默认值）
```
Add-IpamAddressSpace -Name <String> [-ProviderAddressSpace] [-Owner <String>] [-Description <String>]
 [-CustomConfiguration <String>] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### CustomerAddressSpace
```
Add-IpamAddressSpace -Name <String> [-Owner <String>] [-Description <String>] [-CustomConfiguration <String>]
 [-PassThru] [-CustomerAddressSpace] -AssociatedProviderAddressSpace <String> [-Tenant <String>]
 [-VmNetwork <String>] -IsolationMethod <String> [-Force] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-IpamAddressSpace` cmdlet 用于将地址空间添加到 IP 地址管理 (IPAM) 中。一组相互连接的网络构成一个地址空间。在 IPAM 中，这些网络中的所有 IP 块、IP 子网、IP 范围和 IP 地址都被归类到一个地址空间容器中。为了支持网络虚拟化，IPAM 提供了两种类型的地址空间：提供商地址空间（provider address space）和客户地址空间（customer address space）。默认情况下，所有 IPAM 实体都位于名为 “Default” 的内置地址空间中；非虚拟化的网络实体（如子网或 IP 地址范围）也位于 “Default” 地址空间中。

## 示例

#### 示例 1：添加提供商地址空间
```
PS C:\> Add-IpamAddressSpace -Name "ProviderAddSpace01" -ProviderAddressSpace -Description "Provider address space for Contoso"
Name                           : ProviderAddSpace01

Type                           : ProviderAddressSpace

Owner                          :
Description                    : Provider address space for Contoso

AssociatedProviderAddressSpace :
Tenant                         :
VMNetwork                      :
IsolationMethod                :
Ipv4PercentageUtilized         : 0

Ipv6PercentageUtilized         : 0

CustomConfiguration            :
```

该命令向 IPAM 添加了一个名为 “ProviderAddSpace01” 的提供者地址空间，并为其提供了相应的描述信息。

### 示例 2：添加客户地址空间
```
PS C:\> Add-IpamAddressSpace -Name "CustomerAddSpace01" -CustomerAddressSpace -AssociatedProviderAddressSpace "ProviderAddSpace01" -IsolationMethod NVGRE -PassThru
Name                           : CustomerAddSpace01

Type                           : CustomerAddressSpace

Owner                          :

Description                    :

AssociatedProviderAddressSpace : TestProviderAddressSpace

Tenant                         :

VMNetwork                      :

IsolationMethod                : NVGRE

Ipv4PercentageUtilized         : 0

Ipv6PercentageUtilized         : 0

CustomConfiguration            :
```

此命令将一个名为“CustomerAddSpace01”的客户地址空间添加到 IPAM（IP Address Management）系统中。该命令指定，名为“ProviderAddSpace01”的提供商地址空间应与该客户地址空间相关联，并且该地址空间采用通用路由封装（NVGRE: Network Virtualization using Generic Routing Encapsulation）网络虚拟化机制进行管理。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -AssociatedProviderAddressSpace
指定与客户地址空间关联的提供商地址空间。IPAM中的客户地址空间属于同一个提供商地址空间。

```yaml
Type: String
Parameter Sets: CustomerAddressSpace
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
在运行该cmdlet之前，会提示您确认是否要继续执行。

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

### -CustomConfiguration
指定用分号分隔的名/值对。此参数用于定义与地址空间相关联的自定义元数据。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CustomerAddressSpace
表示您添加的地址空间类型是客户地址空间。

```yaml
Type: SwitchParameter
Parameter Sets: CustomerAddressSpace
Aliases: CA

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Description
指定地址空间的描述信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Force
强制命令执行，而不需要用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: CustomerAddressSpace
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsolationMethod
指定地址空间的网络虚拟化机制。该参数的可接受值为：

- NVGRE
- IPRewrite

```yaml
Type: String
Parameter Sets: CustomerAddressSpace
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
为地址空间指定一个名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Owner
指定地址空间的所有者。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
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

### -ProviderAddressSpace
表示您添加的地址空间类型是提供商地址空间。

```yaml
Type: SwitchParameter
Parameter Sets: ProviderAddressSpace
Aliases: PA

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Tenant
指定与客户地址空间相关联的租户ID（以字符串形式表示）。您必须指定一个与该虚拟机网络兼容的租户ID，该虚拟机网络是通过*VmNetwork*参数指定的。

```yaml
Type: String
Parameter Sets: CustomerAddressSpace
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -VmNetwork
指定用于客户地址空间的虚拟机网络的名称。您必须指定一个与所指定的租户（即*Tenant*参数对应的租户）相关联的虚拟机网络。

```yaml
Type: String
Parameter Sets: CustomerAddressSpace
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamAddressSpace
此 cmdlet 返回一个对象，该对象表示 IPAM 中的一个地址空间。

## 备注

## 相关链接

[Get-IpamAddressSpace](./Get-IpamAddressSpace.md)

[Set-IpamAddressSpace](./Set-IpamAddressSpace.md)

[Remove-IpamAddressSpace](./Remove-IpamAddressSpace.md)

