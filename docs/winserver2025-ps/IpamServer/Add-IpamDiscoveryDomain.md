---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDiscoveryDomain.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/add-ipamdiscoverydomain?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-IpamDiscoveryDomain
---

# Add-IpamDiscoveryDomain

## 摘要
向用于识别IPAM基础设施服务器的域列表中添加一个新的Active Directory域。

## 语法

```
Add-IpamDiscoveryDomain [-Name] <String> [-DiscoverDc <Boolean>] [-DiscoverDns <Boolean>]
 [-DiscoverDhcp <Boolean>] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Add-IpamDiscoveryDomain` cmdlet 用于为 IP 地址管理（IPAM）服务器添加一个 Active Directory 发现域。发现域是 IPAM 在其中搜索基础设施服务器的域名。IPAM 服务器会使用这些发现域的列表来确定需要添加哪种类型的服务器。默认情况下，IPAM 会自动发现所有的域控制器、动态主机配置协议（DHCP）服务器和域名系统（DNS）服务器。在添加发现域时，您可以指定每个域要发现的服务器类型；或者之后也可以使用 `Set-IpamDiscoveryDomain` cmdlet 来修改这些设置。

## 示例

### 示例 1：将域名添加到 IPAM 发现域中
```
PS C:\> Add-IpamDiscoveryDomain -Name "child01.contoso.com" -DiscoverDc $False -PassThru
DomainName            DiscoverDc    DiscoverDhcp    DiscoverDns

child1.contoso.com    false         true            true
```

此命令配置 IPAM 在名为 child01.contoso.com 的域中查找 DHCP 服务器和 DNS 服务器。由于 *DiscoverDhcp*、*DiscoverDns* 和 *DiscoverDc* 参数的默认值为 True，因此该命令将 *DiscoverDc* 参数设置为 False，以指示 IPAM 不在該域中查找域控制器。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

### 示例 2：向发现域中添加域控制器、DHCP 服务器和 DNS 服务器
```
PS C:\> Add-IpamDiscoveryDomain -Name "child01.contoso.com" -PassThru
DomainName            DiscoverDc    DiscoverDhcp    DiscoverDns

child1.contoso.com    true          true            true
```

此命令配置 IPAM 在 child01.contoso.com 域中检测域控制器、DHCP 服务器和 DNS 服务器。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -DiscoverDc
该属性用于指示 IPAM 是否能发现指定域中的所有域控制器。默认值为 True（表示可以发现所有域控制器）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DiscoverDhcp
该参数用于指示 IPAM 是否能发现指定域中的所有 DHCP 服务器。默认值为 True。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DiscoverDns
该属性表示IPAM是否能够发现指定域中的所有DNS服务器。默认值为True（即能够发现所有DNS服务器）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定要添加到 IPAM 发现基础设施服务器的域名列表中的 Active Directory 域的完全限定域名（FQDN）。

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
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算出一个最优的节流限制。这个节流限制仅适用于当前的cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。不过实际上并没有运行该cmdlet。

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

### IpamDiscoveryDomain
此cmdlet返回一个对象，该对象代表Active Directory域，在其中IPAM将搜索基础设施服务器。

## 备注

## 相关链接

[Get-IpamDiscoveryDomain](./Get-IpamDiscoveryDomain.md)

[Remove-IpamDiscoveryDomain](./Remove-IpamDiscoveryDomain.md)

[Set-IpamDiscoveryDomain](./Set-IpamDiscoveryDomain.md)

