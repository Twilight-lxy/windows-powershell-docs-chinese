---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmnetworkadapterroutingdomainmapping?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMNetworkAdapterRoutingDomainMapping
---

# 设置虚拟机网络适配器的路由域映射

## 摘要
在路由域上设置虚拟子网。

## 语法

### VMName（默认值）
```
Set-VMNetworkAdapterRoutingDomainMapping [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-VMName] <String[]> [-RoutingDomainID <Guid>]
 [-RoutingDomainName <String>] [-NewRoutingDomainName <String>] [-IsolationID <Int32[]>]
 [-IsolationName <String[]>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ResourceObject
```
Set-VMNetworkAdapterRoutingDomainMapping [-VMNetworkAdapter] <VMNetworkAdapterBase[]> [-RoutingDomainID <Guid>]
 [-RoutingDomainName <String>] [-NewRoutingDomainName <String>] [-IsolationID <Int32[]>]
 [-IsolationName <String[]>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ManagementOS
```
Set-VMNetworkAdapterRoutingDomainMapping [-ManagementOS] [-VMNetworkAdapterName <String>]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-RoutingDomainID <Guid>] [-RoutingDomainName <String>] [-NewRoutingDomainName <String>]
 [-IsolationID <Int32[]>] [-IsolationName <String[]>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Set-VMNetworkAdapterRoutingDomainMapping [-VMNetworkAdapterName <String>] [-VM] <VirtualMachine[]>
 [-RoutingDomainID <Guid>] [-RoutingDomainName <String>] [-NewRoutingDomainName <String>]
 [-IsolationID <Int32[]>] [-IsolationName <String[]>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObjectParameter
```
Set-VMNetworkAdapterRoutingDomainMapping [-InputObject] <VMNetworkAdapterRoutingDomainSetting>
 [-NewRoutingDomainName <String>] [-IsolationID <Int32[]>] [-IsolationName <String[]>] [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMNetworkAdapterRoutingDomainMapping` cmdlet 用于在路由域中设置虚拟子网。

## 示例

### 示例 1：在路由域上设置一个虚拟子网
```
PS C:\> Set-VMNetworkAdapterRoutingDomainMapping -VMName "Gateway01" -VMNetworkAdapterName "Internal NIC" -RoutingDomainID "{5a07361e-6a54-49fc-9210-bfbf14a5c56f}" -IsolationID 6001
```

此命令将虚拟子网的ID设置为6001，并将其关联到指定的路由域。该命令还指明，该路由域位于名为“Internal NIC”的网络适配器上，而这个网络适配器属于名为“Gateway01”的多租户虚拟机。

## 参数

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
指定一个Hyper-V主机的数组。该cmdlet会将虚拟子网添加到您指定的Hyper-V主机上的路由域中。

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

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此 cmdlet。

```yaml
Type: VMNetworkAdapterRoutingDomainSetting
Parameter Sets: InputObjectParameter
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -IsolationID
指定一组虚拟子网的ID。该cmdlet会将您指定的虚拟子网添加到路由域中。这些子网使用VLAN或Hyper-V网络虚拟化技术。有关隔离ID的更多信息，请参阅**Set-VMNetworkAdapterIsolation** cmdlet。

```yaml
Type: Int32[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsolationName
指定一个虚拟子网名称数组。该cmdlet会将您指定的虚拟子网添加到路由域中。这些子网使用VLAN或Hyper-V网络虚拟化技术进行管理。

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

### -ManagementOS
表示该 cmdlet 操作的是父分区或宿主操作系统。

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

### -NewRoutingDomainName
为路由域指定一个新的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
返回一个表示您正在操作的项目的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -RoutingDomainID
用于指定路由域的ID。路由域的ID是由系统分配的GUID（全局唯一标识符）。该cmdlet会将指定的虚拟子网添加到该路由域中。

```yaml
Type: Guid
Parameter Sets: VMName, ResourceObject, ManagementOS, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RoutingDomainName
用于指定路由域的名称。该cmdlet会将虚拟子网添加到您指定的路由域中。

```yaml
Type: String
Parameter Sets: VMName, ResourceObject, ManagementOS, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定一个虚拟机对象数组。该cmdlet会将属于所指定虚拟机的网络接口中的虚拟子网添加到路由域中。若要获取虚拟机对象，请使用**Get-VM** cmdlet。

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
指定一组虚拟机的名称。该 cmdlet 会将这些虚拟机所属的网络接口中的虚拟子网添加到路由域中。若要获取虚拟机对象，请使用 **Get-VM** cmdlet。

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
该命令将一组虚拟网络适配器指定为一个 **VMNetworkAdapterBase** 对象，并将这些虚拟子网添加到所指定的适配器所属的路由域中。若需获取某个网络适配器，请使用 **Get-VMNetworkAdapter** 命令。

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
指定虚拟网络适配器的名称。此cmdlet会将指定的虚拟子网添加到该适配器所属的路由域中。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

### Microsoft.HyperV.PowerShell.VMNetworkAdapterRoutingDomainSetting

## 备注

## 相关链接

[Get-VMNetworkAdapterRoutingDomainMapping](./Get-VMNetworkAdapterRoutingDomainMapping.md)

[Add-VMNetworkAdapterRoutingDomainMapping](./Add-VMNetworkAdapterRoutingDomainMapping.md)

[Remove-VMNetworkAdapterRoutingDomainMapping](./Remove-VMNetworkAdapterRoutingDomainMapping.md)

