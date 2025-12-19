---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmnetworkadapterroutingdomainmapping?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMNetworkAdapterRoutingDomainMapping
---

# 添加 VMNetworkAdapterRoutingDomainMapping

## 摘要
为虚拟网络适配器配置路由域及子网信息。

## 语法

### VMName（默认值）
```
Add-VMNetworkAdapterRoutingDomainMapping [-RoutingDomainID] <Guid> [-RoutingDomainName] <String>
 [-IsolationID] <Int32[]> [[-IsolationName] <String[]>] [-Passthru] [-VMNetworkAdapterName <String>]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-VMName] <String[]>
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ResourceObject
```
Add-VMNetworkAdapterRoutingDomainMapping [-RoutingDomainID] <Guid> [-RoutingDomainName] <String>
 [-IsolationID] <Int32[]> [[-IsolationName] <String[]>] [-Passthru]
 [-VMNetworkAdapter] <VMNetworkAdapterBase[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ManagementOS
```
Add-VMNetworkAdapterRoutingDomainMapping [-RoutingDomainID] <Guid> [-RoutingDomainName] <String>
 [-IsolationID] <Int32[]> [[-IsolationName] <String[]>] [-Passthru] [-ManagementOS]
 [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Add-VMNetworkAdapterRoutingDomainMapping [-RoutingDomainID] <Guid> [-RoutingDomainName] <String>
 [-IsolationID] <Int32[]> [[-IsolationName] <String[]>] [-Passthru] [-VMNetworkAdapterName <String>]
 [-VM] <VirtualMachine[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-VMNetworkAdapterRoutingDomainMapping` cmdlet 用于将路由域和虚拟子网添加到虚拟网络适配器中。该 cmdlet 会将关于路由域和虚拟子网的信息同步到连接到该虚拟网络适配器的多租户虚拟机上。

## 示例

#### 示例 1：向多租户虚拟网络中添加一个租户和虚拟子网
```
PS C:\> Add-VMNetworkAdapterRoutingDomainMapping -VMName "Gateway01" -VMNetworkAdapterName "Internal NIC" -RoutingDomainID "{5a07361e-6a54-49fc-9210-bfbf14a5c56f}" RoutingDomainName "Contoso" -IsolationID 6000 -IsolationName "ContosoGatewayVsid"
```

此命令向名为Gateway01的多租户虚拟机所属的虚拟网络适配器（Internal NIC）添加一个租户，并为该虚拟网络适配器配置指定的路由域。同时，该命令还向同一虚拟网络适配器添加了一个ID为6000的虚拟子网。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定一个Hyper-V主机的数组。该cmdlet会将路由域和虚拟子网添加到您指定的Hyper-V主机上的虚拟网络适配器中。

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
在运行 cmdlet 之前会提示您确认是否要继续。

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

### -IsolationID
用于指定一组虚拟子网的ID。该cmdlet会将您指定的虚拟子网添加到虚拟网络适配器中。您可以通过使用虚拟局域网（VLAN）、Hyper-V网络虚拟化或第三方虚拟化解决方案来隔离虚拟机适配器。有关隔离ID的更多信息，请参阅**Set-VMNetworkAdapterIsolation** cmdlet。

```yaml
Type: Int32[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsolationName
指定一组虚拟子网的名称。此cmdlet会将您指定的虚拟子网添加到虚拟网络适配器中。这些子网使用VLAN或Hyper-V网络虚拟化技术进行管理。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagementOS
表示该cmdlet作用于父操作系统或主机操作系统。

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

### -RoutingDomainID
用于指定路由域的ID。路由域的ID是由系统分配的唯一标识符（GUID）。该cmdlet会将您指定的路由域添加到虚拟网络适配器中。

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RoutingDomainName
指定一个路由域的名称。该cmdlet会将您指定的路由域添加到虚拟网络适配器中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定一个虚拟机对象数组。该cmdlet会将路由域添加到属于所指定虚拟机的网络接口中。若要获取虚拟机对象，请使用**Get-VM** cmdlet。

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
指定一组虚拟机的友好名称（即易于理解的名称）。该cmdlet会将相应的路由域添加到属于所指定虚拟机的网络接口中。

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
指定一个由虚拟网络适配器（`VMNetworkAdapterBase`对象）组成的数组。此cmdlet会在您指定的适配器上添加路由域。要获取网络适配器，请使用`Get-VMNetworkAdapter` cmdlet。

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
用于指定虚拟网络适配器的名称。该cmdlet会在您指定的适配器上添加路由域。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMNetworkAdapter RoutingDomainSetting

## 备注

## 相关链接

[Get-VMNetworkAdapterRoutingDomainMapping](./Get-VMNetworkAdapterRoutingDomainMapping.md)

[Set-VMNetworkAdapterRoutingDomainMapping](./Set-VMNetworkAdapterRoutingDomainMapping.md)

[Remove-VMNetworkAdapterRoutingDomainMapping](./Remove-VMNetworkAdapterRoutingDomainMapping.md)

[Get-VM](./Get-VM.md)

