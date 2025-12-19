---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDhcpScope.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamdhcpscope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamDhcpScope
---

# Get-IpamDhcpScope

## 摘要
从 IPAM 数据库中获取有关 DHCP 范围的信息。

## 语法

```
Get-IpamDhcpScope [-AddressFamily] <AddressFamily[]> [[-ScopeId] <IPAddress[]>] [[-ServerFqdn] <String[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-IpamDhcpScope` cmdlet 可以检索 IP 地址管理（IPAM）数据库中关于动态主机配置协议（DHCP）作用域的信息。这些作用域表示 DHCP 服务器可以租发给客户端的 IP 地址。在大多数情况下，这些作用域对应于特定的 IP 子网。

一般来说，DHCP服务器只能从一个作用域中租用地址。但是，超作用域（superscopes）提供了一种机制，使DHCP服务器能够从多个作用域中租用地址。有关更多信息，请参阅**Get-IpamDhcpSuperscope** cmdlet。

## 示例

### 示例 1：获取有关所有 IPv4 范围的信息
```
PS C:\> Get-IpamDhcpScope -AddressFamily "IPv4"
```

该命令会返回在 IPAM 数据库中找到的所有 IPv4 DHCP 范围（scope）。

### 示例 2：获取特定服务器上的 IPv4 范围信息
```
PS C:\> Get-IpamDhcpScope -AddressFamily "IPv4" -ServerFqdn "dhcp.contoso.com"
```

此命令还会返回 IPv4 DHCP 范围（scope）信息。不过，在这种情况下，返回的仅限于在服务器 dhcp.contoso.com 上找到的那些 DHCP 范围。

## 参数

### -AddressFamily
指定此 cmdlet 获取的 DHCP 范围所使用的地址族。

此参数的可接受值为：

- IPv4
- IPv6

```yaml
Type: AddressFamily[]
Parameter Sets: (All)
Aliases:
Accepted values: IPv4, IPv6

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个代表该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -ScopeId
指定此cmdlet所获取的DHCP作用域的ID。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServerFqdn
指定托管该cmdlet获取的DHCP作用域的DHCP服务器的完全限定域名（FQDN）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamDhcpScope

此cmdlet返回一个对象，该对象代表一个**IpamDhcpScope**对象。

## 备注

## 相关链接

[Get-IpamDhcpServer](./Get-IpamDhcpServer.md)

[Get-IpamDhcpSuperscope](./Get-IpamDhcpSuperscope.md)
