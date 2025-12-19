---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamServerInventory.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamserverinventory?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamServerInventory
---

# 获取 Ipam 服务器库存信息

## 摘要
获取IPAM服务器库存中托管服务器的属性信息。

## 语法

### 按名称查找
```
Get-IpamServerInventory -Name <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### 按地址家族分类
```
Get-IpamServerInventory [-AddressFamily <AddressFamily[]>] [-ServerType <ServerRole[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-IpamServerInventory` cmdlet 可以获取 IP 地址管理（IPAM）服务器清单中管理的服务器列表。这些被管理的服务器包括扮演域控制器（DC）、动态主机配置协议（DHCP）、域名服务（DNS）或网络策略服务器（NPS）角色的服务器。您可以根据地址类型、服务器角色类型或完全限定域名（FQDN）来过滤服务器列表。

## 示例

### 示例 1：获取 IPAM 服务器库存中的所有 IPv4 服务器
```
PS C:\> Get-IpamServerInventory -AddressFamily IPv4 | Format-List Name, ServerType
Name       : dhcp1.contoso.com

ServerType : DHCP
Name       : DC1.contoso.com

ServerType : DC
```

此命令可获取 IPAM 服务器库存中的所有 IPv4 服务器信息。

### 示例 2：获取 IPAM 服务器库存中的所有 IPv4 DHCP 服务器
```
PS C:\> Get-IpamServerInventory -AddressFamily IPv4 -ServerType DHCP| Format-List Name, ServerType
Name       : dhcp1.contoso.com

ServerType : DHCP
```

此命令可以获取IPAM服务器库存中所有的IPv4 DHCP服务器信息。

## 参数

### -AddressFamily
指定一个地址族数组，该基础设施服务器属于这些地址族之一。

该参数的可接受值为：IPv4 或 IPv6。

```yaml
Type: AddressFamily[]
Parameter Sets: ByAddressFamily
Aliases:
Accepted values: IPv4, IPv6

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定用于获取数据的服务器的完全限定域名（Fully Qualified Domain Names）。

```yaml
Type: String
Parameter Sets: ByName
Aliases: ServerName

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServerType
指定一个服务器角色数组，用于过滤结果。

```yaml
Type: ServerRole[]
Parameter Sets: ByAddressFamily
Aliases:
Accepted values: DC, DNS, DHCP, NPS

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的并发操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前正在运行的 cmdlet，而不影响整个会话或整个计算机。

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

### IpamServerInventory
此 cmdlet 返回一个对象，该对象表示 IPAM 系统中的托管基础设施服务器。

## 备注

## 相关链接

[Add-IpamServerInventory](./Add-IpamServerInventory.md)

[Remove-IpamServerInventory](./Remove-IpamServerInventory.md)

[Set-IpamServerInventory](./Set-IpamServerInventory.md)

