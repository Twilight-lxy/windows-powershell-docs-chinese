---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmnetworkadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMNetworkAdapter
---

# 添加虚拟机网络适配器

## 摘要
向虚拟机添加虚拟网络适配器。

## 语法

### VMName（默认值）
```
Add-VMNetworkAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-SwitchName <String>] [-IsLegacy <Boolean>] [-Name <String>] [-DynamicMacAddress]
 [-StaticMacAddress <String>] [-Passthru] [-ResourcePoolName <String>] [-DeviceNaming <OnOffState>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### ManagementOS
```
Add-VMNetworkAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-ManagementOS] [-SwitchName <String>] [-Name <String>] [-DynamicMacAddress] [-StaticMacAddress <String>]
 [-Passthru] [-DeviceNaming <OnOffState>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Add-VMNetworkAdapter [-SwitchName <String>] [-IsLegacy <Boolean>] [-Name <String>] [-DynamicMacAddress]
 [-StaticMacAddress <String>] [-Passthru] [-ResourcePoolName <String>] [-VM] <VirtualMachine[]>
 [-DeviceNaming <OnOffState>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-VMNetworkAdapter` cmdlet 用于向虚拟机添加一个虚拟网络适配器。

## 示例

### 示例 1
```
PS C:\> Add-VMNetworkAdapter -VMName Redmond -Name "Redmond NIC1"
```

这个示例为名为“Redmond”的虚拟机添加了一个名为“Redmond NIC1”的虚拟网络适配器。

### 示例 2
```
PS C:\> Add-VMNetworkAdapter -VMName Test -SwitchName Network
```

这个示例为名为“Test”的虚拟机添加了一个虚拟网络适配器，并将其连接到名为“Network”的虚拟交换机上。

### 示例 3
```
PS C:\> Get-VM Test | Add-VMNetworkAdapter -IsLegacy $true -Name Bootable
```

这个示例在一个命令中使用了两个 cmdlet 和管道来执行操作。

### 示例 4
```
PS C:\> Add-VMNetworkAdapter -ManagementOS -Name Secondary
```

这个示例在管理操作系统中添加了第二个虚拟网络适配器。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个或多个用于添加虚拟网络适配器的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址或完全限定域名作为主机标识。默认值为本地计算机。可以使用 `localhost` 或点（.`）来明确表示本地计算机。

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

### -DeviceNaming


```yaml
Type: OnOffState
Parameter Sets: (All)
Aliases:
Accepted values: On, Off

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DynamicMacAddress
为新虚拟网络适配器分配一个动态生成的MAC地址。

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

### -IsLegacy
指定虚拟网络适配器是否属于旧版类型。

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
指定管理操作系统。

```yaml
Type: SwitchParameter
Parameter Sets: ManagementOS
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
为新虚拟网络适配器指定一个名称。默认值为“Network Adapter”。

```yaml
Type: String
Parameter Sets: (All)
Aliases: VMNetworkAdapterName

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定要传递一个对象，该对象将通过管道表示要添加的网络适配器。如果您指定了 **-ManagementOS**，则传递的对象是 **Microsoft.HyperV.PowerShell.VMInternalNetworkAdapter**；否则，传递的对象是 **Microsoft.HyperV POWERShell.VMNetworkAdapter**。

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

### -ResourcePoolName
指定资源池的友好名称。

```yaml
Type: String
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StaticMacAddress
为新虚拟网络适配器分配一个特定的MAC地址。

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

### -SwitchName
指定要连接到新网络适配器的虚拟交换机的名称。如果交换机名称不唯一，则操作会失败。

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
指定要添加网络适配器的虚拟机。

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
指定要添加网络适配器的虚拟机的名称。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

默认情况下，此cmdlet不会返回任何输出。

### Microsoft.HyperV.PowerShell.VMNetworkAdapter

如果指定了 **PassThru**，则默认会输出一个 **Microsoft.HyperV.PowerShell.VMNetworkAdapter** 对象。

### Microsoft.HyperV.PowerShell.VMInternalNetworkAdapter

如果指定了 **PassThru** 和 **ManagementOS**，那么将会输出 **Microsoft.HyperV.PowerShell.VMInternalNetworkAdapter**。

## 备注

## 相关链接

