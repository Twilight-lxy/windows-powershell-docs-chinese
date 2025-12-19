---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmnetworkadapterextendedacl?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMNetworkAdapterExtendedAcl
---

# 添加扩展访问控制列表（Extended Access Control List, ACL）到虚拟机网络适配器

## 摘要
为虚拟网络适配器创建扩展的访问控制列表。

## 语法

### VMName（默认值）
```
Add-VMNetworkAdapterExtendedAcl [-Action] <VMNetworkAdapterExtendedAclAction>
 [-Direction] <VMNetworkAdapterExtendedAclDirection> [[-LocalIPAddress] <String>] [[-RemoteIPAddress] <String>]
 [[-LocalPort] <String>] [[-RemotePort] <String>] [[-Protocol] <String>] [-Weight] <Int32>
 [-Stateful <Boolean>] [-IdleSessionTimeout <Int32>] [-IsolationID <Int32>] [-Passthru]
 [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ResourceObject
```
Add-VMNetworkAdapterExtendedAcl [-Action] <VMNetworkAdapterExtendedAclAction>
 [-Direction] <VMNetworkAdapterExtendedAclDirection> [[-LocalIPAddress] <String>] [[-RemoteIPAddress] <String>]
 [[-LocalPort] <String>] [[-RemotePort] <String>] [[-Protocol] <String>] [-Weight] <Int32>
 [-Stateful <Boolean>] [-IdleSessionTimeout <Int32>] [-IsolationID <Int32>] [-Passthru]
 [-VMNetworkAdapter] <VMNetworkAdapterBase[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ManagementOS
```
Add-VMNetworkAdapterExtendedAcl [-Action] <VMNetworkAdapterExtendedAclAction>
 [-Direction] <VMNetworkAdapterExtendedAclDirection> [[-LocalIPAddress] <String>] [[-RemoteIPAddress] <String>]
 [[-LocalPort] <String>] [[-RemotePort] <String>] [[-Protocol] <String>] [-Weight] <Int32>
 [-Stateful <Boolean>] [-IdleSessionTimeout <Int32>] [-IsolationID <Int32>] [-Passthru] [-ManagementOS]
 [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Add-VMNetworkAdapterExtendedAcl [-Action] <VMNetworkAdapterExtendedAclAction>
 [-Direction] <VMNetworkAdapterExtendedAclDirection> [[-LocalIPAddress] <String>] [[-RemoteIPAddress] <String>]
 [[-LocalPort] <String>] [[-RemotePort] <String>] [[-Protocol] <String>] [-Weight] <Int32>
 [-Stateful <Boolean>] [-IdleSessionTimeout <Int32>] [-IsolationID <Int32>] [-Passthru]
 [-VMNetworkAdapterName <String>] [-VM] <VirtualMachine[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-VMNetworkAdapterExtendedAcl` cmdlet 用于为虚拟网络适配器创建一个扩展的访问控制列表（ACL）。该 ACL 根据源 IP 地址、目标 IP 地址、协议、源端口和目标端口来允许或拒绝网络数据包对虚拟机网络适配器的访问。

## 示例

### 示例 1：为远程桌面协议（Remote Desktop Protocol）创建访问控制列表（ACL）
```
PS C:\> Add-VMNetworkAdapterExtendedAcl -VMName "TSQA01" -Action Allow -Direction Inbound -LocalPort "3389" -Protocol "TCP" -Weight 10 -Stateful $True
```

这个命令创建了一个有状态的入站访问控制列表（ACL），允许远程设备通过端口3389连接到虚拟机。端口3389是用于远程桌面协议（Remote Desktop Protocol）的端口。

### 示例 2：创建一个访问控制列表（ACL），以在超时情况下发起连接
```
PS C:\> Add-VMNetworkAdapterExtendedAcl -VMName "TSQA03" -Action Allow -Direction Outbound -RemotePort "80" -Protocol "TCP" -Weight 100 -Timeout 3600 -Stateful $True
```

该命令创建了一个有状态（stateful）的访问控制列表（ACL），允许数据包通过TCP协议发送到远程设备。如果3600秒内没有数据传输活动，连接将会超时。

## 参数

### -Action
指定访问控制列表（ACL）的操作类型。该参数允许的值包括：

- Allow
- Deny

```yaml
Type: VMNetworkAdapterExtendedAclAction
Parameter Sets: (All)
Aliases:
Accepted values: Allow, Deny

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: VMName, ManagementOS
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个Hyper-V主机的数组。该cmdlet会为您指定的Hyper-V主机上的网络适配器添加访问控制列表（ACL）。

```yaml
Type: String[]
Parameter Sets: VMName, ManagementOS
Aliases:

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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName, ManagementOS
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Direction
指定网络流量的方向，这是从应用该访问控制列表（ACL）的虚拟机的角度来看的。此cmdlet会添加一个具有您所指定值的ACL。该参数的可接受值包括：

- Inbound
- Outbound

 If you run the **Get-VMNetworkAdapterExtendedAcl** cmdlet, the entry that you create appears in both the inbound ACL and the outbound ACL.

```yaml
Type: VMNetworkAdapterExtendedAclDirection
Parameter Sets: (All)
Aliases:
Accepted values: Inbound, Outbound

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IdleSessionTimeout
指定空闲会话的超时时间（以秒为单位）。

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

### -IsolationID
用于指定一个虚拟子网的 ID。该 cmdlet 会添加一个 ACL（访问控制列表），该 ACL 适用于您所指定的隔离网络中的流量。该子网使用虚拟局域网（VLAN）或 Hyper-V 网络虚拟化技术。有关隔离 ID 的更多信息，请参阅 **Set-VmNetworkAdapterIsolation** cmdlet。

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

### -LocalIPAddress
指定用于访问控制列表（ACL）的本地IP地址。对于入站数据包，该本地地址是目的IP地址；对于出站数据包，该本地地址是源IP地址。您可以指定一个主机地址或子网地址，也可以使用通配符，例如：0.0.0.0/0 表示所有IPv4地址，::/0 表示所有IPv6地址，ANY 表示所有IPv4和IPv6地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LocalPort
指定用于访问控制列表（ACL）的本地端口。也可以使用端口范围格式（例如：“49152-49182”）。对于入站TCP或UDP数据包，本地端口是目标端口；对于出站数据包，本地端口是源端口。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagementOS
表示该cmdlet作用于父操作系统或主机操作系统。如果您指定了此参数，该cmdlet将创建一个适用于父操作系统或主机操作系统的ACL（访问控制列表）。

```yaml
Type: SwitchParameter
Parameter Sets: ManagementOS
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
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

### -Protocol
指定ACL适用的协议。该参数的可接受值包括：

- TCP
- UDP
- an integer IP protocol ID (**use 1 for ICMP**)

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 7
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemoteIPAddress
Specifies the local IP address for the ACL.
For an inbound packet, the remote address is the source IP address.
For an outbound packet, the remote address is the destination IP address.
You can specify a host address or a subnet address, or specify a wildcard, such as 0.0.0.0/0 for all IPv4 addresses, ::/0 for all IPv6 addresses, or ANY for all IPv4 and IPv6 addresses.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemotePort
Specifies the remote port for the ACL. A port range format can also be used (i.e. "49152-49182", for example).
For an inbound TCP or UDP packet, the remote port is the source port.
For an outbound packet, the remote port is the destination port.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Stateful
该属性用于指示访问控制列表（ACL）是否适用于同一会话中数据包的往返方向。如果您指定值为 `$True`，那么即使返回数据包的方向与ACL规定的方向相反，ACL仍然会对其进行应用。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定一个虚拟机对象的数组。该cmdlet会为您指定的虚拟机添加访问控制列表（ACL）。要获取虚拟机对象，请使用**Get-VM** cmdlet。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定一个虚拟机名称数组。该cmdlet会为您指定的虚拟机添加访问控制列表（ACL）。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapter
指定一个由 **VMNetworkAdapterBase** 对象组成的虚拟机（VM）网络适配器数组。该 cmdlet 会为您指定的适配器添加访问控制列表（ACL）。要获取网络适配器，请使用 **Get-VMNetworkAdapter** cmdlet。

```yaml
Type: VMNetworkAdapterBase[]
Parameter Sets: ResourceObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapterName
用于指定虚拟网络适配器的名称。该cmdlet会为您指定的适配器添加一个访问控制列表（ACL）。

```yaml
Type: String
Parameter Sets: VMName, ManagementOS, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Weight
用于指定访问控制列表（ACL）条目的权重。权重值较大的条目会优先被应用；一旦某个ACL条目适用于某个数据包，其他条目对该数据包就不再具有约束作用了。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: True
Position: 8
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。不过实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.HyperV POWERShell.VMNetworkAdapterExtendedAclSetting

## 备注

## 相关链接

[Get-VMNetworkAdapterExtendedAcl](./Get-VMNetworkAdapterExtendedAcl.md)

[Remove-VMNetworkAdapterExtendedAcl](./Remove-VMNetworkAdapterExtendedAcl.md)

[Get-VM](./Get-VM.md)

[Set-VmNetworkAdapterIsolation](./Set-VmNetworkAdapterIsolation.md)

