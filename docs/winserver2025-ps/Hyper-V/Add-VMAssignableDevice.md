---
description: 将一台设备分配给虚拟机。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmassignabledevice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMAssignableDevice
---
# Add-VMAssignableDevice

## 摘要

将可分配的设备添加到特定的虚拟机中。

## 语法

### VMName (Default)

```
Add-VMAssignableDevice [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [-InstancePath <String>]
 [-LocationPath <String>] [-VirtualFunction <UInt16>] [-ResourcePoolName <String>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject

```
Add-VMAssignableDevice [-VM] <VirtualMachine[]> [-InstancePath <String>] [-LocationPath <String>]
 [-VirtualFunction <UInt16>] [-ResourcePoolName <String>] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Add-VMAssignableDevice cmdlet` 用于将物理设备分配给指定的虚拟机（VM）。该命令常用于将 GPU 或网络适配器直接连接到虚拟机上，从而提升特定应用程序或工作负载的性能。设备的指定方式可以是通过其实例路径、位置路径，或是使用 assignable device object 来进行。

## 示例

### Example 1

```powershell
Add-VMAssignableDevice -VMName "MyVM" -InstancePath "PCIROOT(0)#PCI(0300)#PCI(0000)"
```

这个示例将一个物理设备（该设备的唯一标识是通过其实例路径来确定的）连接到名为 **MyVM** 的虚拟机上。

## 参数

### -CimSession

该 cmdlet 可在远程会话或远程计算机上执行。您可以输入计算机的名称，或者提供一个会话对象，例如通过 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](/powershell/module/cimcmdlets/get-cimsession) cmdlet 生成的会话对象。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName

指定一个或多个用于检索可分配设备的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址或完全 Qualified Domain Name（FQDN）。默认值为本地计算机；可以使用 localhost 或点号（`.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
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
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InstancePath

表示主机上的设备实例路径。

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

### -LocationPath

指定可分配设备的路径位置。

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

为每个由该 cmdlet 启动的进程返回一个对象。

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

指定要将设备分配到的资源池的名称。

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

### -VirtualFunction

该参数用于指定分配给虚拟机的、支持 SR-IOV（Scalable I/O Virtualization）的网络适配器的虚拟函数（Virtual Function，简称 VF）的编号。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM

指定要将设备分配到的虚拟机。

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

指定要将设备分配到的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm

在运行该 cmdlet 之前，系统会提示用户确认是否要继续执行该操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

显示如果运行了某个命令行工具（cmdlet），将会发生什么。但实际上，这个命令行工具并未被真正执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅
[about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters).

## 输入

### Microsoft.HyperV.PowerShell.VirtualMachine[]

## 输出

### Microsoft.HyperV.PowerShell.VMAssignedDevice

## 备注

## 相关链接

[Get-VMAssignableDevice](get-vmassignabledevice.md)

[Remove-VMAssignableDevice](remove-vmassignabledevice.md)
