---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmnetworkadapteracl?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMNetworkAdapterAcl
---

# 添加虚拟机网络适配器访问控制列表（Add-VMNetworkAdapterAcl）

## 摘要
创建用于控制通过该虚拟网络适配器传输的数据流量的访问控制列表（ACL）。

## 语法

### VMName（默认值）
```
Add-VMNetworkAdapterAcl -Action <VMNetworkAdapterAclAction> -Direction <VMNetworkAdapterAclDirection>
 [-LocalIPAddress <String[]>] [-LocalMacAddress <String[]>] [-RemoteIPAddress <String[]>]
 [-RemoteMacAddress <String[]>] [-Passthru] [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-VMName] <String[]> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ResourceObject
```
Add-VMNetworkAdapterAcl -Action <VMNetworkAdapterAclAction> -Direction <VMNetworkAdapterAclDirection>
 [-LocalIPAddress <String[]>] [-LocalMacAddress <String[]>] [-RemoteIPAddress <String[]>]
 [-RemoteMacAddress <String[]>] [-Passthru] [-VMNetworkAdapter] <VMNetworkAdapterBase[]> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ManagementOS
```
Add-VMNetworkAdapterAcl -Action <VMNetworkAdapterAclAction> -Direction <VMNetworkAdapterAclDirection>
 [-LocalIPAddress <String[]>] [-LocalMacAddress <String[]>] [-RemoteIPAddress <String[]>]
 [-RemoteMacAddress <String[]>] [-Passthru] [-ManagementOS] [-VMNetworkAdapterName <String>]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMObject
```
Add-VMNetworkAdapterAcl -Action <VMNetworkAdapterAclAction> -Direction <VMNetworkAdapterAclDirection>
 [-LocalIPAddress <String[]>] [-LocalMacAddress <String[]>] [-RemoteIPAddress <String[]>]
 [-RemoteMacAddress <String[]>] [-Passthru] [-VMNetworkAdapterName <String>] [-VM] <VirtualMachine[]> [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Add-VMNetworkAdapterAcl` cmdlet 用于创建一个访问控制列表（ACL），以便应用于通过虚拟机网络适配器传输的流量。在创建虚拟网络适配器时，该适配器上默认没有 ACL。如果提供了基于 IP 地址的 ACL 规则列表，并且这些规则需要应用于相同方向的流量，那么系统会根据匹配度最高的规则来决定应该将哪个规则应用到特定的数据包上。

## 示例

### 示例 1
```
PS C:\> Add-VMNetworkAdapterAcl -VMName Redmond -RemoteIPAddress 10.0.0.0/8 -Direction Both -Action Allow
```

这个示例添加了一个访问控制列表（ACL），以允许虚拟机“Redmond”与IP子网10.0.0.8/8上的其他设备进行数据的发送和接收。

### 示例 2
```
PS C:\> Add-VMNetworkAdapterAcl -VMName Redmond -RemoteIPAddress ANY -Direction Both -Action Deny
```

这个示例添加了一个访问控制列表（ACL），以禁止虚拟机“Redmond”向任何地方发送IPv4或IPv6流量，同时也禁止它从任何地方接收此类流量。

### 示例 3
```
PS C:\> Get-VM Redmond | Add-VMNetworkAdapterAcl -RemoteMacAddress 03-0f-01-0e-aa-b2 -Direction Both -Action Deny
```

这个示例获取名为“Redmond”的虚拟机，并为其添加了一个访问控制列表（ACL），以禁止该虚拟机向MAC地址为03-0f-01-0e-aa-b2的设备发送任何流量，或者从该设备接收任何流量。

### 示例 4
```
PS C:\> Get-VMNetworkAdapter -VMName Redmond | Add-VMNetworkAdapterAcl -RemoteIPAddress 192.168.0.0/16 -Direction Outbound -Action Meter
```

这个示例从名为“Redmond”的虚拟机中获取虚拟网络适配器，并为发送到IP子网192.168.0.0/16的出站流量添加一个访问控制列表（ACL）。

## 参数

### -Action
指定ACL（访问控制列表）的操作类型。允许的值有**Allow**（允许）、**Deny**（拒绝）和**Meter**（计量）。用于计量的ACL必须基于IP地址进行配置，也就是说必须要指定`-RemoteIPAddress`或`-LocalIPAddress`中的一个参数。

```yaml
Type: VMNetworkAdapterAclAction
Parameter Sets: (All)
Aliases:
Accepted values: Allow, Deny, Meter

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: VMName, ManagementOS
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于创建访问控制列表（ACL）的Hyper-V主机。允许使用NetBIOS名称、IP地址或完全合格的域名作为主机标识。默认值为本地计算机；可以使用“localhost”或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName, ManagementOS
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您确认是否要执行该操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
默认值 value: False
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
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Direction
指定要应用ACL的网络流量的方向。允许的值为**Inbound**（入站）、**Outbound**（出站）或**Both**（两者）。如果指定了**Both**，则新的ACL条目会同时添加到入站和出站方向中。在Get-VMNetworkAdapterAcl的输出结果中，该ACL条目会同时出现在入站ACL列表和出站ACL列表中。

```yaml
Type: VMNetworkAdapterAclDirection
Parameter Sets: (All)
Aliases:
Accepted values: Inbound, Outbound, Both

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LocalIPAddress
指定要应用访问控制列表（ACL）的本地IP地址。对于入站数据包，该地址是数据包头部中的目标IP地址；对于出站数据包，该地址是数据包头部中的源IP地址。该地址可以是IPv4地址或IPv6地址，也可以是主机地址或子网地址（例如：1.2.3.4、2001::2008、192.168.1.0/24 或 f001:f002:f003:f004::1/64）。IP地址还可以是通配符：0.0.0.0/0 表示所有IPv4地址，::/0 表示所有IPv6地址，ANY 表示所有IPv4和IPv6地址。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LocalMacAddress
指定要应用ACL的本地MAC地址。对于入站数据包，该地址是数据包头中的目标MAC地址；对于出站数据包，该地址是数据包头中的源MAC地址。它可以是主机MAC地址（例如00-ab-00-11-22-33），也可以是通配符“ANY”，表示所有MAC地址。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagementOS
指定该访问控制列表（ACL）应用于管理操作系统（即父级操作系统或主机操作系统）。

```yaml
Type: SwitchParameter
Parameter Sets: ManagementOS
Aliases:

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定将一个对象传递给表示要添加的ACL（访问控制列表）的处理流程。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemoteIPAddress
指定此ACL应应用的远程IP地址。对于入站数据包，该地址是数据包头中的源IP地址；对于出站数据包，该地址是数据包头中的目的IP地址。该地址可以是IPv4地址或IPv6地址，也可以是主机地址或子网地址（例如：1.2.3.4、2001::2008、192.168.1.0/24或f001:f002:f003:f004::1/64）。此外，该IP地址还可以使用通配符表示：0.0.0.0/0表示所有IPv4地址；::/0表示所有IPv6地址；ANY则表示所有IPv4和IPv6地址。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemoteMacAddress
指定此ACL应应用于的远程MAC地址。对于入站数据包，该地址是数据包头中的源MAC地址；对于出站数据包，该地址是数据包头中的目标MAC地址。它可以是一个主机MAC地址（例如00-ab-00-11-22-33），也可以是一个通配符“ANY”，表示所有MAC地址。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要应用访问控制列表（ACL）的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要应用访问控制列表（ACL）的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapter
指定要应用访问控制列表（ACL）的虚拟机网络适配器。

```yaml
Type: VMNetworkAdapterBase[]
Parameter Sets: ResourceObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapterName
指定要应用访问控制列表（ACL）的虚拟机网络适配器的名称。

```yaml
Type: String
Parameter Sets: VMName, ManagementOS, VMObject
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.VMNetworkAdapterAclSetting
如果指定了**-PassThru**选项的话……

## 备注

## 相关链接

