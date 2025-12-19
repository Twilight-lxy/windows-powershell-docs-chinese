---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmnetworkadapterextendedacl?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMNetworkAdapterExtendedAcl
---

# Get-VMNetworkAdapterExtendedAcl

## 摘要
获取应用于虚拟网络适配器的扩展ACL信息。

## 语法

### VMName（默认值）
```
Get-VMNetworkAdapterExtendedAcl [[-VMName] <String[]>] [-VMNetworkAdapterName <String>]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [<CommonParameters>]
```

### VMSnapshot
```
Get-VMNetworkAdapterExtendedAcl [-VMSnapshot] <VMSnapshot> [<CommonParameters>]
```

### ResourceObject
```
Get-VMNetworkAdapterExtendedAcl [-VMNetworkAdapter] <VMNetworkAdapterBase[]> [<CommonParameters>]
```

### ManagementOS
```
Get-VMNetworkAdapterExtendedAcl [-ManagementOS] [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [<CommonParameters>]
```

### VMObject
```
Get-VMNetworkAdapterExtendedAcl [-VMNetworkAdapterName <String>] [-VM] <VirtualMachine[]> [<CommonParameters>]
```

## 描述
`Get-VMNetworkAdapterExtendedAcl` cmdlet 用于获取为虚拟网络适配器配置的扩展访问控制列表（ACL）。如果某个 ACL 同时适用于传入和传出数据包，那么它将同时出现在传入和传出数据的访问控制列表中。

## 示例

### 示例 1：获取所有扩展的访问控制列表（ACL）
```
PS C:\> Get-VMNetworkAdapterExtendedAcl -VMName "TSQA01"
```

这个命令可以获取名为TSQA01的虚拟机的所有扩展访问控制列表（extended ACLs）。

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
指定一个Hyper-V主机的数组。该cmdlet会获取与您指定的Hyper-V主机上的虚拟网络适配器相关联的ACL（访问控制列表）。

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
表示该 cmdlet 在父操作系统或主机操作系统上执行操作。如果您指定了此参数，该 cmdlet 将获取与父操作系统或主机操作系统中的网络适配器相关联的 ACL（访问控制列表）。

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

### -VM
指定一组虚拟机作为 **VirtualMachine** 对象。该 cmdlet 会获取属于所指定虚拟机的网卡的访问控制列表（ACL）信息。若要获取虚拟机对象，请使用 **Get-VM** cmdlet。

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
指定一个虚拟机（VM）名称数组。该cmdlet会获取与您指定的虚拟机相关联的网络适配器上的访问控制列表（ACL）。

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
指定一个虚拟网络适配器对象的数组。此 cmdlet 会获取与所指定的适配器关联的访问控制列表（ACL）信息。若需获取某个网络适配器，请使用 **Get-VMNetworkAdapter** cmdlet。

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
用于指定虚拟网络适配器的名称。该cmdlet会获取与该适配器关联的扩展ACL（Access Control Lists）。

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
该命令用于将某个快照指定为一个 **VMSnapshot** 对象。此 cmdlet 会获取属于所指定快照的网络适配器的访问控制列表（ACL）信息。若需获取某个快照，可以使用 **Get-VMSnapshot** cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.HyperV.PowerShell.VMNetworkAdapterExtendedAclSetting


## 备注

## 相关链接

[Add-VMNetworkAdapterExtendedAcl](./Add-VMNetworkAdapterExtendedAcl.md)

[Remove-VMNetworkAdapterExtendedAcl](./Remove-VMNetworkAdapterExtendedAcl.md)

[Get-VM](./Get-VM.md)

[Get-VMNetworkAdapter](./Get-VMNetworkAdapter.md)

[Get-VMSnapshot](./Get-VMSnapshot.md)

