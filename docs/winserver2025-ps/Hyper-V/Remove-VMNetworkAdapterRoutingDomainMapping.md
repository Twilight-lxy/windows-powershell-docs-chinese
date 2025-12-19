---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmnetworkadapterroutingdomainmapping?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMNetworkAdapterRoutingDomainMapping
---

# 移除虚拟机网络适配器的路由域映射

## 摘要
从虚拟网络适配器中删除一个路由域。

## 语法

### VMName（默认值）
```
Remove-VMNetworkAdapterRoutingDomainMapping [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-VMName] <String[]> [-RoutingDomainID <Guid>]
 [-RoutingDomainName <String>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ResourceObject
```
Remove-VMNetworkAdapterRoutingDomainMapping [-VMNetworkAdapter] <VMNetworkAdapterBase[]>
 [-RoutingDomainID <Guid>] [-RoutingDomainName <String>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ManagementOS
```
Remove-VMNetworkAdapterRoutingDomainMapping [-ManagementOS] [-VMNetworkAdapterName <String>]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-RoutingDomainID <Guid>] [-RoutingDomainName <String>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Remove-VMNetworkAdapterRoutingDomainMapping [-VMNetworkAdapterName <String>] [-VM] <VirtualMachine[]>
 [-RoutingDomainID <Guid>] [-RoutingDomainName <String>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObjectParameter
```
Remove-VMNetworkAdapterRoutingDomainMapping [-InputObject] <VMNetworkAdapterRoutingDomainSetting[]> [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-VmNetworkAdapterRoutingDomainMapping` 这个cmdlet用于从多租户网关虚拟机上的虚拟网络适配器中删除某个路由域。

## 示例

### 示例 1：从多租户虚拟机中移除某个租户
```
PS C:\> Remove-VMNetworkAdapterRoutingDomainMapping -VMName "Gateway01" -VMNetworkAdapterName "Internal NIC" -RoutingDomainID "{5a07361e-6a54-49fc-9210-bfbf14a5c56f}"
```

此命令将从名为“Internal NIC”的虚拟网络适配器中删除指定的路由域。该命令还指定了该适配器属于名为“Gateway01”的多租户虚拟机。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定一个Hyper-V主机数组。该cmdlet会从您指定的Hyper-V主机中删除相应的虚拟子网。

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
Type: VMNetworkAdapterRoutingDomainSetting[]
Parameter Sets: InputObjectParameter
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -ManagementOS
表示该cmdlet会从父分区或主机操作系统中删除虚拟子网。

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
指定一个路由域的ID。路由域的ID是由系统分配的唯一标识符（GUID）。该cmdlet会从您指定的路由域中删除相应的虚拟子网。

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
指定一个路由域的名称。该cmdlet会从您指定的路由域中删除相应的虚拟子网。

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
指定一个虚拟机数组。该cmdlet会从您指定的虚拟机中删除相应的虚拟子网。若要获取虚拟机对象，请使用**Get-VM** cmdlet。

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
指定一个虚拟机名称数组。该cmdlet会从您指定的虚拟机中删除相应的虚拟子网。

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
指定一个由虚拟机网络适配器组成的数组，这些适配器都是 **VMNetworkAdapterBase** 对象。该 cmdlet 会删除你所指定的适配器所对应的网络子网。若需获取某个网络适配器，请使用 **Get-VMNetworkAdapter** cmdlet。

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
用于指定虚拟网络适配器的名称。该cmdlet会删除您所指定的适配器对应的虚拟子网。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMNetworkAdapterRoutingDomainSetting

## 备注

## 相关链接

[Get-VMNetworkAdapterRoutingDomainMapping](./Get-VMNetworkAdapterRoutingDomainMapping.md)

[Add-VmNetworkAdapterRoutingDomainMapping](./Add-VmNetworkAdapterRoutingDomainMapping.md)

[Set-VmNetworkAdapterRoutingDomainMapping](./Set-VmNetworkAdapterRoutingDomainMapping.md)

