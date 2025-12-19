---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetConnectionProfile.cdxml-help.xml
Module Name: NetConnection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netconnectionprofile/set-netconnectionprofile?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NetConnectionProfile
---

# 设置 NetworkConnectionProfile

## 摘要
更改连接配置文件的网络类别。

## 语法

### 查询（CDXML）（默认值）
```powershell
Set-NetConnectionProfile [-Name <String[]>] [-InterfaceAlias <String[]>] [-InterfaceIndex <UInt32[]>]
 [-IPv4Connectivity <IPv4Connectivity[]>] [-IPv6Connectivity <IPv6Connectivity[]>]
 [-NetworkCategory <NetworkCategory>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```powershell
Set-NetConnectionProfile -InputObject <CimInstance[]> [-NetworkCategory <NetworkCategory>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-NetConnectionProfile` cmdlet 用于更改连接配置文件的网络类别设置。一个连接配置文件代表一个网络连接。

## 示例

### 示例 1：更改连接配置文件的网络类别
```powershell
PS C:\> Set-NetConnectionProfile -InterfaceAlias Ethernet1 -NetworkCategory "Public"
```

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](/powershell/module/cimcmdlets/new-cimsession)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认值是本地计算机上的当前会话。

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

### -IPv4Connectivity
指定一个包含 IPv4 协议连接状态值的数组。该参数的可接受值如下：

- Disconnected
- NoTraffic
- Subnet
- LocalNetwork
- Internet

```yaml
Type: IPv4Connectivity[]
Parameter Sets: Query (cdxml)
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
Parameter Sets: Query (cdxml)
Aliases:
Accepted values: Disconnected, NoTraffic, Subnet, LocalNetwork, Internet

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定要传递给此 cmdlet 的输入数据。你可以使用该参数，也可以将输入数据通过管道（pipe）传递给此 cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -InterfaceAlias
指定一个网络适配器名称数组。

```yaml
Type: String[]
Parameter Sets: Query (cdxml)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InterfaceIndex
指定一个与网络适配器相关联的数值索引值数组。

```yaml
Type: UInt32[]
Parameter Sets: Query (cdxml)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定一个包含当前已建立连接的网络名称的数组。

```yaml
Type: String[]
Parameter Sets: Query (cdxml)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NetworkCategory
用于指定网络中各类类别类型的数组。使用此 cmdlet 无法设置 “DomainAuthenticated” 类型；当网络成功与域控制器进行身份验证时，服务器会自动设置该类型的值。此参数的允许取值为：

- *Public* - Networks in a public place such as an airport or coffee shop. Your PC is hidden from other devices on the network and can't be used for printer and file sharing.
- *Private* - Networks at home or work, where you know and trust the people and devices on the network. Your PC is discoverable and can be used for printer and file sharing if you set it up.
- *DomainAuthenticated* - Networks at a workplace that are joined to a domain.

```yaml
Type: NetworkCategory
Parameter Sets: (All)
Aliases:
Accepted values: Public, Private, DomainAuthenticated

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值`0`，Windows PowerShell将根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值（即并发操作的数量）。此限制仅适用于当前执行的cmdlet，而不适用于整个会话或整个计算机。

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
展示了如果该cmdlet运行会发生什么情况。但实际上这个cmdlet并没有被运行。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-NetConnectionProfile](./Get-NetConnectionProfile.md)
