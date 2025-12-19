---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmnetworkadapterisolation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMNetworkAdapterIsolation
---

# 获取虚拟机网络适配器的隔离状态

## 摘要
获取虚拟网络适配器的隔离设置信息。

## 语法

### VMName（默认值）
```
Get-VMNetworkAdapterIsolation [[-VMName] <String[]>] [-VMNetworkAdapterName <String>]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [<CommonParameters>]
```

### VMSnapshot
```
Get-VMNetworkAdapterIsolation [-VMSnapshot] <VMSnapshot> [<CommonParameters>]
```

### ResourceObject
```
Get-VMNetworkAdapterIsolation [-VMNetworkAdapter] <VMNetworkAdapterBase[]> [<CommonParameters>]
```

### ManagementOS
```
Get-VMNetworkAdapterIsolation [-ManagementOS] [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [<CommonParameters>]
```

### VMObject
```
Get-VMNetworkAdapterIsolation [-VMNetworkAdapterName <String>] [-VM] <VirtualMachine[]> [<CommonParameters>]
```

## 描述
`Get-VMNetworkAdapterIsolation` 这个 cmdlet 可以获取虚拟网络适配器的隔离设置。该 cmdlet 会显示隔离方式以及其他相关信息，例如多租户模式（如果启用了多租户功能），以及发往默认隔间的流量的子网 ID。

## 示例

### 示例 1
```
PS C:\> Get-VMNetworkAdapterIsolation -VMName Multitenant-GW -VMNetworkAdapterName InternalNIC
```

这个示例用于检索虚拟机（VM）的隔离设置信息。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
用于指定一个Hyper-V主机数组。该cmdlet会获取由您指定的计算机托管的虚拟机的隔离设置信息。

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
表示该cmdlet在父操作系统或主机操作系统上执行操作。如果您指定了此参数，该cmdlet将获取父操作系统或主机操作系统的隔离设置信息。

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
指定一个虚拟机数组。该cmdlet会获取属于所指定虚拟机的适配器的隔离设置。若要获取虚拟机对象，请使用**Get-VM** cmdlet。

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
指定一个虚拟机名称数组。该cmdlet会获取属于你所指定虚拟机的适配器的隔离设置信息。

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
该命令用于将多个虚拟机网络适配器指定为 **VMNetworkAdapterBase** 对象。该 cmdlet 会获取所指定适配器的隔离设置信息。若需获取某个网络适配器，可使用 **Get-VMNetworkAdapter** cmdlet。

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
用于指定虚拟网络适配器的名称。该命令行工具会获取您所指定的这些适配器的隔离设置信息。

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
将快照指定为 **VMSnapshot** 对象。此cmdlet会获取属于所指定快照的网络适配器的隔离设置。若要获取快照，请使用 **Get-VMSnapshot** cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.HyperV.PowerShell.VMNetworkAdapterIsolationSetting

## 备注

## 相关链接

[Set-VMNetworkAdapterIsolation](./Set-VMNetworkAdapterIsolation.md)

[Get-VM](./Get-VM.md)

[Get-VMSnapshot](./Get-VMSnapshot.md)

[Get-VMNetworkAdapter](./Get-VMNetworkAdapter.md)

