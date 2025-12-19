---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmnetworkadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMNetworkAdapter
---

# Get-VMNetworkAdapter

## 摘要
获取虚拟机的虚拟网络适配器信息。

## 语法

### VMName（默认值）
```
Get-VMNetworkAdapter [-IsLegacy <Boolean>] [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [[-Name] <String>] [<CommonParameters>]
```

### VMObject
```
Get-VMNetworkAdapter [-IsLegacy <Boolean>] [-VM] <VirtualMachine[]> [[-Name] <String>] [<CommonParameters>]
```

### ManagementOS
```
Get-VMNetworkAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [[-Name] <String>] [-ManagementOS] [-SwitchName <String>] [<CommonParameters>]
```

### 全部
```
Get-VMNetworkAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [[-Name] <String>] [-All] [<CommonParameters>]
```

### VMSnapshot
```
Get-VMNetworkAdapter [[-Name] <String>] [-VMSnapshot] <VMSnapshot> [<CommonParameters>]
```

## 描述
`Get-VMNetworkAdapter` cmdlet 可以获取指定虚拟机、快照或管理操作系统的虚拟网络适配器信息。

## 示例

### 示例 1
```
PS C:\> Get-VMNetworkAdapter -VMName *
```

从本地 Hyper-V 主机上的所有虚拟机中获取虚拟网络适配器。

### 示例 2
```
PS C:\> Get-VMNetworkAdapter -ManagementOS
```

获取ManagementOS（即本地的Hyper-V主机）中的虚拟网络适配器。

### 示例 3
```
PS C:\> Get-VMNetworkAdapter -All
```

从所有虚拟机以及管理操作系统获取虚拟网络适配器。

## 参数

### -All
指定系统中的所有虚拟网络适配器，无论这些虚拟网络适配器是位于管理操作系统中还是位于虚拟机中。

```yaml
Type: SwitchParameter
Parameter Sets: All
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: VMName, ManagementOS, All
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个虚拟网络适配器上需要检索的Hyper-V主机。可以使用NetBIOS名称、IP地址或完全限定域名进行标识。默认值为本地计算机；可以通过使用“localhost”或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName, ManagementOS, All
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
Parameter Sets: VMName, ManagementOS, All
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsLegacy
请将值指定为 **$TRUE** 以仅检索旧版网络适配器，或指定为 **$FALSE** 以仅检索专为 Hyper-V 设计的网络适配器。如果未进行指定，则会同时检索两种类型的网络适配器。

```yaml
Type: Boolean
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagementOS
指定管理操作系统，即虚拟机宿主操作系统。

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

### -Name
指定要获取的网络适配器的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: VMNetworkAdapterName

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SwitchName
指定要获取其网络适配器信息的虚拟交换机的名称。（此参数仅适用于管理操作系统中的虚拟网络适配器。）

```yaml
Type: String
Parameter Sets: ManagementOS
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要获取其虚拟网络适配器的虚拟机。星号（*）是一个通配符；如果指定了该虚拟机，此cmdlet将从系统中的所有虚拟机中返回相应的虚拟网络适配器。

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
指定要获取其网络适配器信息的虚拟机的名称。

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

### -VMSnapshot
指定要获取其网络适配器信息的快照。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMNetworkAdapter

默认情况下，会输出 `Microsoft.HyperV.PowerShell.VMNetworkAdapter`。

### Microsoft.HyperV.PowerShell.VMInternalNetworkAdapter

如果指定了 `ManagementOS`，则使用 `Microsoft.HyperV.PowerShell.VMInternalNetworkAdapter`。

### Microsoft.HyperV.PowerShell.VMInternalNetworkAdapter 和 Microsoft.HyperV.PowerShell.VMNetworkAdapter

如果指定了“All”，则使用 `Microsoft.HyperV.PowerShell.VMInternalNetworkAdapter` 和 `Microsoft.HyperV.PowerShell.VMNetworkAdapter`。

## 备注

## 相关链接

