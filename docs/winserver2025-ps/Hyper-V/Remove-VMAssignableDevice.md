---
description: 删除分配给虚拟机的设备。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmassignabledevice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMAssignableDevice
---

# 移除可分配VMA的设备

## 摘要
从特定的虚拟机中删除有关可分配设备的信息。

## 语法

### VMName（默认值）

```
Remove-VMAssignableDevice [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [-InstancePath <String>]
 [-LocationPath <String>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 对象

```
Remove-VMAssignableDevice [-VMAssignableDevice] <VMAssignedDevice[]> [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-VMAssignableDevice` cmdlet 用于从指定的虚拟机（VM）中移除可分配的设备。这种操作通常发生在以下情况下：某个物理设备（如 GPU 或网络适配器）之前已被分配给某个虚拟机，现在需要将其重新释放出来、不再进行分配。

## 示例

### 示例 1

```powershell
$params = @{
VMName = "MyVM"
InstancePath = "PCIROOT(0)#PCI(0300)#PCI(0000)#PCI(0800)#PCI(0000)#PCI(1000)"
}
Remove-VMAssignableDevice $params
```

这个示例会从名为**MyVM**的虚拟机中移除一个特定的可分配设备，该设备的标识是通过其实例路径来确定的。

### 示例 2

```powershell
$params = @{
VMName = "MyVM"
}
$vm = Get-VMAssignableDevice @params | Where-Object { $_.ResourcePoolName -eq "GpuChildPool" }
$vm | Remove-VMAssignableDevice
```

这个示例从名为 **MyVM** 的虚拟机中移除一个特定的可分配设备，该设备的标识符是通过 **ResourcePoolName** 属性 **GpuChildPool** 来识别的。

## 参数

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如 `[New-CimSession`](/powershell/module/cimcmdlets/new-cimsession)` 或 `[Get-CimSession](/powershell/module/cimcmdlets/get-cimsession)` cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

指定要从虚拟网络适配器中检索的一个或多个 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址和完全限定域名。默认值是本地计算机。可以使用 `localhost` 或点（`.`）来明确表示本地计算机。

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

从主机系统中删除设备实例路径。

```yaml
Type: String
Parameter Sets: VMName
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
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru

为cmdlet启动的每个进程返回一个对象。

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

### -VMAssignableDevice

指定您想要从虚拟机中移除的可分配设备对象。该对象通常是通过诸如 `Get-VMAssignableDevice` 之类的 cmdlet 获取的。

```yaml
Type: VMAssignedDevice[]
Parameter Sets: Object
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName

指定您想要从中移除可分配设备的虚拟机的名称。

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

在运行该cmdlet之前，会提示您进行确认。

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

展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### Microsoft.HyperV.PowerShell.VMAssignedDevice[]

## 输出

### Microsoft.HyperV.PowerShell.VMAssignedDevice

## 备注

## 相关链接

[Add-VMAssignableDevice](add-vmassignabledevice.md)

[Get-VMAssignableDevice](get-vmassignabledevice.md)
