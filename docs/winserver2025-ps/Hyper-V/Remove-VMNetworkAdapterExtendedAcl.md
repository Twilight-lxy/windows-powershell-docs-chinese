---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmnetworkadapterextendedacl?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMNetworkAdapterExtendedAcl
---

# 删除扩展访问控制列表（Extended ACL）

## 摘要
删除虚拟网络适配器的扩展访问控制列表（ACL）。

## 语法

### VMName（默认值）
```
Remove-VMNetworkAdapterExtendedAcl [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-VMName] <String[]> -Weight <Int32>
 -Direction <VMNetworkAdapterExtendedAclDirection> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ResourceObject
```
Remove-VMNetworkAdapterExtendedAcl [-VMNetworkAdapter] <VMNetworkAdapterBase[]> -Weight <Int32>
 -Direction <VMNetworkAdapterExtendedAclDirection> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ManagementOS
```
Remove-VMNetworkAdapterExtendedAcl [-ManagementOS] [-VMNetworkAdapterName <String>]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] -Weight <Int32>
 -Direction <VMNetworkAdapterExtendedAclDirection> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Remove-VMNetworkAdapterExtendedAcl [-VMNetworkAdapterName <String>] [-VM] <VirtualMachine[]> -Weight <Int32>
 -Direction <VMNetworkAdapterExtendedAclDirection> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObjectParameter
```
Remove-VMNetworkAdapterExtendedAcl [-InputObject] <VMNetworkAdapterExtendedAclSetting[]> [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-VMNetworkAdapterExtendedAcl` cmdlet 用于删除虚拟网络适配器上的扩展访问控制列表（ACL）。

## 示例

### 示例 1：移除特定的访问控制列表（ACL）
```
PS C:\> Remove-VMNetworkAdapterExtendedAcl -VMName "TSQA01" -Direction InBound -Weight 50
```

此命令会从名为TSQA01的虚拟机上删除针对入站流量的ACL（访问控制列表），该入站流量的权重为50。

### 示例 2：删除所有的访问控制列表（ACL）
```
PS C:\> Get-VMNetworkAdapterExtendedAcl -VMName "TSQA01" | Remove-VMNetworkAdapterExtendedAcl
```

此命令使用 **Get-VMNetworkAdapterExtendedAcl** cmdlet 来获取名为 TSQA01 的虚拟机的所有访问控制列表（ACL），然后通过管道运算符将这些 ACL 传递给当前的 cmdlet。最后，该命令会删除所有的 ACL。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
用于指定一组Hyper-V主机。该cmdlet会删除与您指定的Hyper-V主机上的虚拟网络适配器关联的ACL（访问控制列表）。

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
该参数指定了从虚拟机的角度来看，网络流量的方向（即ACL所适用的目标）。此cmdlet会删除具有指定值的ACL。该参数的可接受值包括：

     -- Inbound

     -- Outbound

```yaml
Type: VMNetworkAdapterExtendedAclDirection
Parameter Sets: VMName, ResourceObject, ManagementOS, VMObject
Aliases:
Accepted values: Inbound, Outbound

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定该cmdlet的输入内容。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

```yaml
Type: VMNetworkAdapterExtendedAclSetting[]
Parameter Sets: InputObjectParameter
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -ManagementOS
表示该 cmdlet 操作的是父操作系统或主机操作系统。如果您指定了此参数，该 cmdlet 会删除应用于父操作系统或主机操作系统的访问控制列表（ACL）。

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

### -VM
指定一个由虚拟机对象（**VirtualMachine**）组成的数组。此cmdlet会删除属于所指定虚拟机的网络适配器上的访问控制列表（ACL）。若要获取某个虚拟机对象，请使用**Get-VM** cmdlet。

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
指定一个虚拟机名称数组。该cmdlet会删除属于所指定虚拟机的网络适配器的访问控制列表（ACL）。

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
该命令用于将多个虚拟机网络适配器指定为 **VMNetworkAdapterBase** 对象。同时，它还会删除你所指定的这些网络适配器的访问控制列表（ACL）。若需获取某个网络适配器，请使用 **Get-VMNetworkAdapter** 命令。

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
指定虚拟网络适配器的名称。该cmdlet会删除您所指定的网络适配器的相关ACL（访问控制列表）。

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
用于指定ACL（访问控制列表）条目的权重。由于每个条目的权重都是唯一的，因此如果您为该参数指定了一个值，该cmdlet将会删除相应的扩展ACL条目。

```yaml
Type: Int32
Parameter Sets: VMName, ResourceObject, ManagementOS, VMObject
Aliases:

Required: True
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.HyperV.PowerShell.VMNetworkAdapterExtendedAclSetting

## 备注

## 相关链接

[Add-VMNetworkAdapterExtendedAcl](./Add-VMNetworkAdapterExtendedAcl.md)

[Get-VMNetworkAdapterExtendedAcl](./Get-VMNetworkAdapterExtendedAcl.md)

[Get-VM](./Get-VM.md)

[Get-VMNetworkAdapter](./Get-VMNetworkAdapter.md)

