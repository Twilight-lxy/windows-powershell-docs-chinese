---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDiscoveryDomain.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/set-ipamdiscoverydomain?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IpamDiscoveryDomain
---

# 设置 IpamDiscoveryDomain

## 摘要
修改 IPAM 发现配置。

## 语法

```
Set-IpamDiscoveryDomain [-Name] <String> [-DiscoverDc <Boolean>] [-DiscoverDns <Boolean>]
 [-DiscoverDhcp <Boolean>] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-IpamDiscoveryDomain` cmdlet 用于修改 Active Directory 域的发现配置。通过使用此 cmdlet，可以配置 IPAM 来发现特定类型的服务器，例如域控制器、动态主机配置协议（DHCP）服务器或域名系统（DNS）服务器。

## 示例

### 示例 1：修改现有的发现域
```
PS C:\> Set-IpamDiscoveryDomain -Name "contoso.com" -DiscoverDc $False -PassThru
DomainName                    DiscoverDc                    DiscoverDns                   DiscoverDhcp

----------                    ----------                    -----------                   ------------

contoso.com                   False                         True                          True
```

此命令用于修改现有的发现域设置，以防止服务器在该域中发现域控制器。该命令会输出一个对象，以便与其他cmdlet配合使用。此外，该命令还包含了*PassThru*参数，因此会将执行结果显示在控制台上。

### 示例 2：修改现有的发现域以发现域控制器
```
PS C:\> Set-IpamDiscoveryDomain -Name "contoso.com" -DiscoverDc $True -PassThru
DomainName                    DiscoverDc                    DiscoverDns                   DiscoverDhcp

----------                    ----------                    -----------                   ------------

contoso.com                   True                          True                          True
```

此命令用于修改 IPAM 中现有的发现域配置，以便在该域中检测到更多类型的服务器。该命令包含了 *PassThru* 参数，因此会将检测结果显示在控制台上。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如使用[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet得到的结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
在运行cmdlet之前，会提示您进行确认。

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
该属性用于指示 IPAM 是否能在域中检测到域控制器服务器。默认值为 True（表示可以检测到）。

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
该值表示IPAM是否能在域中检测到DHCP服务器。默认情况下，该值为True（即能检测到DHCP服务器）。

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
该值表示 IPAM 是否能在某个域中检测到 DNS 服务器。默认情况下，该值为 `True`（表示可以检测到 DNS 服务器）。

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
指定要修改发现设置的 Active Directory 域的全限定域名（FQDN）。

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
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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
指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前的cmdlet，而不适用于会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamDiscoveryDomain
此cmdlet返回一个对象，该对象代表Active Directory域，在该域中IPAM将发现基础设施服务器。

## 备注

## 相关链接

[Add-IpamDiscoveryDomain](./Add-IpamDiscoveryDomain.md)

[Get-IpamDiscoveryDomain](./Get-IpamDiscoveryDomain.md)

[Remove-IpamDiscoveryDomain](./Remove-IpamDiscoveryDomain.md)

