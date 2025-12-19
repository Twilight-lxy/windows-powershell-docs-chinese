---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmnetworkadapteracl?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMNetworkAdapterAcl
---

# 删除 VMNetworkAdapterAcl

## 摘要
移除应用于通过虚拟网络适配器传输的数据流的访问控制列表（ACL）。

## 语法

### `VMName`（默认值）
```
Remove-VMNetworkAdapterAcl [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-VMName] <String[]>
 -Action <VMNetworkAdapterAclAction> -Direction <VMNetworkAdapterAclDirection> [-LocalIPAddress <String[]>]
 [-LocalMacAddress <String[]>] [-RemoteIPAddress <String[]>] [-RemoteMacAddress <String[]>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ResourceObject
```
Remove-VMNetworkAdapterAcl [-VMNetworkAdapter] <VMNetworkAdapterBase[]> -Action <VMNetworkAdapterAclAction>
 -Direction <VMNetworkAdapterAclDirection> [-LocalIPAddress <String[]>] [-LocalMacAddress <String[]>]
 [-RemoteIPAddress <String[]>] [-RemoteMacAddress <String[]>] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ManagementOS
```
Remove-VMNetworkAdapterAcl [-ManagementOS] [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] -Action <VMNetworkAdapterAclAction>
 -Direction <VMNetworkAdapterAclDirection> [-LocalIPAddress <String[]>] [-LocalMacAddress <String[]>]
 [-RemoteIPAddress <String[]>] [-RemoteMacAddress <String[]>] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMObject
```
Remove-VMNetworkAdapterAcl [-VMNetworkAdapterName <String>] [-VM] <VirtualMachine[]>
 -Action <VMNetworkAdapterAclAction> -Direction <VMNetworkAdapterAclDirection> [-LocalIPAddress <String[]>]
 [-LocalMacAddress <String[]>] [-RemoteIPAddress <String[]>] [-RemoteMacAddress <String[]>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObjectParameter
```
Remove-VMNetworkAdapterAcl [-InputObject] <VMNetworkAdapterAclSetting[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-VMNetworkAdapterAcl` cmdlet 用于删除应用于通过虚拟网络适配器传输的数据流的访问控制列表（ACL）。

## 示例

### 示例 1
```
PS C:\> Remove-VMNetworkAdapterAcl -VMName Redmond -RemoteIPAddress 0.0.0.0/0 -Direction Both -Action Allow
```

从Redmond虚拟机中移除相应的ACL（访问控制列表），从而禁止任何来自或发往该虚拟机的IPv4流量通过。

### 示例 2
```
PS C:\> Remove-VMNetworkAdapterAcl -VMName Redmond -RemoteIPAddress ::/0 -Direction Both -Action Allow
```

从Redmond虚拟机中移除允许任何IPv6流量进出该虚拟机的ACL（访问控制列表）。

### 示例 3
```
PS C:\> Remove-VMNetworkAdapterAcl -VMName Redmond -RemoteMacAddress 03-0f-01-0e-aa-b2 -Direction Both -Action Deny
```

删除MAC地址访问控制列表（ACL），以防止名为“Redmond”的虚拟机向MAC地址为03-0f-01-0e-aa-b2的远程设备发送或接收数据。

### 示例 4
```
PS C:\> Get-VMNetworkAdapterAcl -VMName Redmond | Remove-VMNetworkAdapterAcl
```

检索为虚拟机“Redmond”配置的所有端口ACL（访问控制列表），并将这些ACL传递给`Remove-VMNetworkAdapterAcl`命令，该命令会从虚拟机中删除所有这些ACL。

## 参数

### -Action
指定要删除的ACL的操作类型。允许的值有**Allow**（允许）、**Deny**（拒绝）和**Meter**（计量）。

```yaml
Type: VMNetworkAdapterAclAction
Parameter Sets: VMName, ResourceObject, ManagementOS, VMObject
Aliases:
Accepted values: Allow, Deny, Meter

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个或多个 Hyper-V 主机，要从这些主机上删除应用于虚拟机网络适配器的访问控制列表（ACL）。允许使用 NetBIOS 名称、IP 地址和完全限定域名进行指定。默认值是本地计算机。可以使用 “localhost” 或点号（.）来明确表示本地计算机。

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
在运行 cmdlet 之前会提示您进行确认。

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
网络流量的方向（从虚拟机的角度来看），ACL将应用于该方向的流量。允许的值有：**Inbound**（入站）、**Outbound**（出站）或**Both**（两者）。

```yaml
Type: VMNetworkAdapterAclDirection
Parameter Sets: VMName, ResourceObject, ManagementOS, VMObject
Aliases:
Accepted values: Inbound, Outbound, Both

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定要删除的访问控制列表（ACL）。

```yaml
Type: VMNetworkAdapterAclSetting[]
Parameter Sets: InputObjectParameter
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -LocalIPAddress
指定本地 IP 地址。该地址可以是 IPv4 或 IPv6 格式，也可以是主机地址或子网地址（例如：1.2.3.4、2001::2008、192.168.1.0/24 或 f001:f002:f003:f004::1/64）。IP 地址还可以使用通配符：0.0.0.0/0 表示所有 IPv4 地址，::/0 表示所有 IPv6 地址，ANY 则表示所有 IPv4 和 IPv6 地址。

```yaml
Type: String[]
Parameter Sets: VMName, ResourceObject, ManagementOS, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LocalMacAddress
指定本地MAC地址（例如：00-ab-00-11-22-33）。可以使用通配符**ANY**来指定所有MAC地址。

```yaml
Type: String[]
Parameter Sets: VMName, ResourceObject, ManagementOS, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagementOS
指定要从管理（例如父级操作系统或主机操作系统）中删除该ACL。

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
指定要将一个 `Microsoft.HyperV.PowShell.VMNetworkAdapterAclSetting` 对象传递给管道，该对象表示需要删除的访问控制列表（ACL）。

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

### -RemoteIPAddress
指定远程 IP 地址。该地址可以是 IPv4 或 IPv6 格式，也可以是主机地址或子网地址（例如：1.2.3.4、2001::2008、192.168.1.0/24 或 f001:f002:f003:f004::1/64）。IP 地址还可以使用通配符表示：0.0.0.0/0 表示所有 IPv4 地址；::/0 表示所有 IPv6 地址；ANY 表示所有 IPv4 和 IPv6 地址。

```yaml
Type: String[]
Parameter Sets: VMName, ResourceObject, ManagementOS, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemoteMacAddress
指定远程MAC地址。它可以是一个主机MAC地址（例如：00-ab-00-11-22-33），也可以是一个通配符“ANY”，表示所有MAC地址。

```yaml
Type: String[]
Parameter Sets: VMName, ResourceObject, ManagementOS, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要从该虚拟机中删除访问控制列表（ACL）的虚拟机。

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
指定要从其中删除访问控制列表（ACL）的虚拟机的名称。

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
指定要从哪个虚拟机网络适配器中删除ACL。

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
指定要从其中删除访问控制列表（ACL）的虚拟机网络适配器的名称。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无

默认情况下，此cmdlet不会返回任何输出。

### Microsoft.HyperV.PowerShell.VMNetworkAdapterAclSetting

当你使用 **PassThru** 参数时，此cmdlet会返回一个 **Microsoft.HyperV.PowerShell.VMNetworkAdapterAclSetting** 对象。

## 备注

## 相关链接

