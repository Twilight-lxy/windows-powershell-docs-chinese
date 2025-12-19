---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDiscoveryDomain.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamdiscoverydomain?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamDiscoveryDomain
---

# Get-IpamDiscoveryDomain

## 摘要
获取 Active Directory 域的列表，在这些域中，IPAM 可以发现基础设施服务器。

## 语法

```
Get-IpamDiscoveryDomain [[-Name] <String[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-IpamDiscoveryDomain` cmdlet 可以获取 Active Directory 域的列表，在这些域中，IP 地址管理（IPAM）功能能够发现相应的基础设施服务器。你可以通过指定某个域的完全限定域名（FQDN）来检索该域的配置信息。

## 示例

### 示例 1：获取所有发现域（Discovery Domains）
```
PS C:\> Get-IpamDiscoveryDomain
DomainName                    DiscoverDc                    DiscoverDns                   DiscoverDhcp

----------                    ----------                    -----------                   ------------

contoso.com                   True                          True                          True

minings.com                   False                         True                          True
```

这个命令可以获取在 IPAM 中配置的所有发现域（discovery domains）。

### 示例 2：获取特定的发现域
```
PS C:\> Get-IpamDiscoveryDomain -Name "Contoso.com"
DomainName                    DiscoverDc                    DiscoverDns                   DiscoverDhcp

----------                    ----------                    -----------                   ------------

contoso.com                   True                          True                          True
```

此命令会获取一个名为 Contoso.com 的发现域，该域已在 IPAM 中进行配置。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个代表该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet将在本地计算机的当前会话中执行。

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
指定一个Active Directory域中的FQDN（完全 Qualified Domain Name）数组以进行检索。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamDiscoveryDomain
此cmdlet返回一个对象，该对象代表Active Directory域，在该域中IPAM可以发现基础设施服务器。

## 备注

## 相关链接

[Add-IpamDiscoveryDomain](./Add-IpamDiscoveryDomain.md)

[Remove-IpamDiscoveryDomain](./Remove-IpamDiscoveryDomain.md)

[Set-IpamDiscoveryDomain](./Set-IpamDiscoveryDomain.md)

