---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetConnectionProfile.cdxml-help.xml
Module Name: NetConnection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netconnectionprofile/get-netconnectionprofile?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetConnectionProfile
---

# Get-NetConnectionProfile

## 摘要
获取一个连接配置文件。

## 语法

```powershell
Get-NetConnectionProfile [-Name <String[]>] [-InterfaceAlias <String[]>] [-InterfaceIndex <UInt32[]>]
 [-NetworkCategory <NetworkCategory[]>] [-IPv4Connectivity <IPv4Connectivity[]>]
 [-IPv6Connectivity <IPv6Connectivity[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-NetConnectionProfile` cmdlet 可以获取与一个或多个物理网络适配器关联的连接配置文件。连接配置文件表示一种网络连接方式。

## 示例

#### 示例 1：获取连接配置文件
```powershell
PS C:\>Get-NetConnectionProfile -InterfaceAlias "Ethernet1" | Set-NetConnectionProfile -NetworkCategory Public
```

这个命令的第一部分用于获取名为“Ethernet1”的网络适配器的连接配置文件。该命令通过使用管道运算符（|）将获取的结果传递给`Set-NetConnectionProfile` cmdlet。命令的第二部分则用于修改该连接配置文件中的网络类别属性值。

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如使用[NNew-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -IPv4Connectivity
指定一个包含 IPv4 协议连接状态值的数组。该参数的可接受值为：

- Disconnected
- NoTraffic
- Subnet
- LocalNetwork
- Internet

```yaml
Type: IPv4Connectivity[]
Parameter Sets: (All)
Aliases:
Accepted values: Disconnected, NoTraffic, Subnet, LocalNetwork, Internet

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv6Connectivity
Specifies an array of IPv6 protocol connectivity status values.
The acceptable values for this parameter are:

- Disconnected
- NoTraffic
- Subnet
- LocalNetwork
- Internet

```yaml
Type: IPv6Connectivity[]
Parameter Sets: (All)
Aliases:
Accepted values: Disconnected, NoTraffic, Subnet, LocalNetwork, Internet

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InterfaceAlias
指定一个包含网络适配器名称的数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InterfaceIndex
指定与网络适配器相关联的一系列数字索引值。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定一个网络名称数组，表示当前已建立连接的网络。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NetworkCategory
指定一个网络中类别类型的数组。该参数的可接受值为：

- *Public* - Networks in a public place such as an airport or coffee shop. Your PC is hidden from other devices on the network and can't be used for printer and file sharing.
- *Private* - Networks at home or work, where you know and trust the people and devices on the network. Your PC is discoverable and can be used for printer and file sharing if you set it up.
- *DomainAuthenticated* - Networks at a workplace that are joined to a domain.

```yaml
Type: NetworkCategory[]
Parameter Sets: (All)
Aliases:
Accepted values: Public, Private, DomainAuthenticated

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的命令操作的最大数量。如果省略此参数或输入值为 `0`，Windows PowerShell 会根据计算机上正在运行的 CIM 命令的数量来计算该命令的最佳执行限制（即并发操作的最大数量）。这个执行限制仅适用于当前正在运行的命令，而不影响整个会话或整个计算机。

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

## 备注

## 相关链接

[Set-NetConnectionProfile](./Set-NetConnectionProfile.md)

