---
description: 检索关于分配给虚拟机的设备的信息。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmassignabledevice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMAssignableDevice
---

# 获取可分配给虚拟机的设备

## 摘要
检索与特定虚拟机相关联的可分配设备的信息。

## 语法

### VMName（默认值）

```
Get-VMAssignableDevice [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [-InstancePath <String>]
 [-LocationPath <String>] [<CommonParameters>]
```

### VMObject

```
Get-VMAssignableDevice [-VM] <VirtualMachine[]> [-InstancePath <String>] [-LocationPath <String>]
 [<CommonParameters>]
```

## 描述

`Get-VMAssignableDevice` cmdlet 可以检索与特定虚拟机（VM）相关联的可分配设备的信息。该 cmdlet 既可以用来列出所有可以连接到 VM 的可分配设备，也可以用来获取已经分配给 VM 的具体设备的详细信息。检索到的信息可能包括设备的实例路径、位置路径以及其他相关属性。

## 示例

### 示例 1

```powershell
Get-VMAssignableDevice -VMName "MyVM"
```

这个示例会检索与名为 **MyVM** 的虚拟机关联的所有可分配设备。

## 参数

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](/powershell/module/cimcmdlets/get-cimsession) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

指定一个或多个用于检索可分配设备的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址和完全限定域名。默认值为本地计算机。可以使用 `localhost` 或点（`.`）来明确表示本地计算机。

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

检索一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

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

### -VM

检索设备所分配到的虚拟机。

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

检索分配给指定虚拟机的可分配设备的名称。

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

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### System.String[]

### Microsoft.HyperV.PowerShell.VirtualMachine[]

## 输出

### Microsoft.HyperV.PowerShell.VMAssignedDevice

## 备注

## 相关链接

[Add-VMAssignableDevice](add-vmassignabledevice.md)

[Remove-VMAssignableDevice](remove-vmassignabledevice.md)
