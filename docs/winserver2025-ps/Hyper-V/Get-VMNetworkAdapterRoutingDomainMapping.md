---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmnetworkadapterroutingdomainmapping?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMNetworkAdapterRoutingDomainMapping
---

# 获取虚拟机网络适配器路由域映射信息

## 摘要
获取路由域成员信息。

## 语法

### VMName（默认值）
```
Get-VMNetworkAdapterRoutingDomainMapping [-RoutingDomainID <Guid>] [-RoutingDomainName <String>]
 [[-VMName] <String[]>] [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [<CommonParameters>]
```

### VMSnapshot
```
Get-VMNetworkAdapterRoutingDomainMapping [-RoutingDomainID <Guid>] [-RoutingDomainName <String>]
 [-VMSnapshot] <VMSnapshot> [<CommonParameters>]
```

### ResourceObject
```
Get-VMNetworkAdapterRoutingDomainMapping [-RoutingDomainID <Guid>] [-RoutingDomainName <String>]
 [-VMNetworkAdapter] <VMNetworkAdapterBase[]> [<CommonParameters>]
```

### ManagementOS
```
Get-VMNetworkAdapterRoutingDomainMapping [-RoutingDomainID <Guid>] [-RoutingDomainName <String>]
 [-ManagementOS] [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [<CommonParameters>]
```

### VMObject
```
Get-VMNetworkAdapterRoutingDomainMapping [-RoutingDomainID <Guid>] [-RoutingDomainName <String>]
 [-VMNetworkAdapterName <String>] [-VM] <VirtualMachine[]> [<CommonParameters>]
```

## 描述
`Get-VmNetworkAdapterRoutingDomainMapping` cmdlet 用于获取路由域中的成员信息。

## 示例

### 示例 1：获取路由域中的成员
```
PS C:\> Get-VMNetworkAdapterRoutingDomainMapping -VMName "Gateway01" -VMNetworkAdapterName "Internal NIC"
```

此命令从名为“Internal NIC”的网络适配器中获取路由域的成员信息，该网络适配器属于名为“Gateway01”的虚拟机。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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
指定一个Hyper-V主机的数组。该cmdlet会获取您所指定的Hyper-V主机上所属路由域的成员信息。

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

### -ManagementOS
表示该cmdlet作用于父分区或主机操作系统。

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

### -RoutingDomainID
用于指定路由域的ID。路由域的ID是由系统分配的唯一标识符（GUID）。该cmdlet会获取您所指定的路由域中的成员信息。

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RoutingDomainName
指定一个路由域的名称。该 cmdlet 会获取您所指定的路由域中的成员信息。

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

### -VM
指定一个虚拟机对象的数组。此cmdlet会从属于您所指定的虚拟机的网络接口中获取路由域的成员信息。若要获取某个虚拟机对象，请使用**Get-VM** cmdlet。

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
指定一组虚拟机的友好名称（即易于理解的名称）。该cmdlet会从属于所指定虚拟机的网络接口中获取路由域的成员信息。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapter
将一组虚拟网络适配器指定为一个 **VMNetworkAdapterBase** 对象。此 cmdlet 会获取你所指定的适配器上的路由域成员信息。若要获取某个网络适配器，可以使用 **Get-VMNetworkAdapter** cmdlet。

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
用于指定虚拟网络适配器的名称。该cmdlet会获取您所指定的适配器上所属的路由域成员信息。

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

### -VMSnapshot
该命令用于将某个快照指定为一个 **VMSnapshot** 对象。该 cmdlet 会获取属于所指定快照的所有网络适配器的路由域成员信息。若需获取一个快照对象，可以使用 **Get-VMSnapshot** cmdlet。

```yaml
Type: VMSnapshot
Parameter Sets: VMSnapshot
Aliases: VMCheckpoint

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMNetworkAdapterRoutingDomainSetting

## 备注

## 相关链接

[Add-VmNetworkAdapterRoutingDomainMapping](./Add-VmNetworkAdapterRoutingDomainMapping.md)

[Set-VmNetworkAdapterRoutingDomainMapping](./Set-VmNetworkAdapterRoutingDomainMapping.md)

[Remove-VMNetworkAdapterRoutingDomainMapping](./Remove-VMNetworkAdapterRoutingDomainMapping.md)

