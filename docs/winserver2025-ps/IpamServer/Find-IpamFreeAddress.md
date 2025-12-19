---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamAddress.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/find-ipamfreeaddress?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Find-IpamFreeAddress
---

# 查找免费的 IPAM 地址

## 摘要
从 IPAM 中的某个 IP 地址范围内获取一个或多个免费的 IP 地址。

## 语法

```
Find-IpamFreeAddress [-InputObject] <CimInstance> [[-NumAddress] <UInt32>] [-TestReachability]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Find-IpamFreeAddress` cmdlet 从 IP 地址管理（IPAM）提供的 IP 地址范围内获取一个或多个空闲的 IP 地址。如果您指定了 `NumAddress` 参数，该 cmdlet 会返回所需数量的空闲 IPv4 地址；如果没有指定该参数，则仅返回一个空闲 IP 地址。该 cmdlet 最多可以返回 1024 个空闲 IP 地址，并且不会将已被排除的地址范围、已预留的地址或已分配的地址包含在结果中。如果无法找到所需数量的空闲 IP 地址，系统会发出警告。如果您指定了 `TestReachability` 参数，IPAM 还会为返回的每个 IP 地址提供相应的 Ping 状态和域名系统（DNS）记录状态信息。

## 示例

### 示例 1：查找一个免费的 IP 地址
```
PS C:\> Get-IpamRange -StartIPAddress "10.12.3.1" -EndIPAddress "10.12.3.254" | Find-IpamFreeAddress

IpAddress       : 10.12.3.1

PingStatus      : Undetected

DnsRecordStatus : Undetected
```

这个命令通过 `Get-IpamRange` cmdlet 获取一系列 IP 地址，然后从中找到一个空闲的 IP 地址。默认情况下，IPAM 不会测试该地址是否可到达，也不会检查是否存在对应的 DNS 记录。

### 示例 2：获取一个免费的 IP 地址，并测试该地址的可达性
```
PS C:\> $FreeIPs = Get-IpamRange -StartIPAddress "10.12.3.1" -EndIPAddress "10.12.3.254" | Find-IpamFreeAddress -NumAddress 10 -TestReachability
PS C:\> $FreeIPs[0]
IpAddress       : 10.12.3.1

PingStatus      : NoReply

DnsRecordStatus : NotFound
```

第一个命令使用 `Get-IpamRange` cmdlet 来获取一系列 IP 地址，然后使用 `Find-IpamFreeAddress` cmdlet 找到 10 个空闲的 IP 地址。接着，该命令会检查这些 IP 地址是否可访问，以及是否存在相应的 DNS 记录。最后，将结果存储在名为 `$FreeIPs` 的变量中。

第二个命令会输出存储在名为 $FreeIPs 的变量中的结果。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -InputObject
指定该cmdlet的输入内容。您可以使用此参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -NumAddress
指定此cmdlet能够获取的可用地址数量。如果返回的可用地址数量少于请求的数量，cmdlet会发出警告。如果您不指定此参数，cmdlet将返回一个可用地址。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TestReachability
表示该cmdlet用于测试IP地址的可访问性（即是否能够成功连接到这些IP地址）。

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
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamFreeAddress
此cmdlet返回一个对象，该对象表示IPAM服务器中未分配的IP地址。除了IP地址外，该对象还包含一些标志，这些标志用于指示IPAM服务器是否能够ping到该IP地址，以及IPAM服务器是否找到了与该IP地址关联的DNS记录。

## 备注

## 相关链接

[Get-IpamRange](./Get-IpamRange.md)

