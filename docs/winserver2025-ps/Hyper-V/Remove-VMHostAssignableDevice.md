---
description: 从虚拟机主机中移除可分配的设备。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmhostassignabledevice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMHostAssignableDevice
---

# 删除 VMHost 可分配的设备

## 摘要
从分配给虚拟机（VM）主机的设备中移除该设备。

## 语法

### 路径（默认值）

```
Remove-VMHostAssignableDevice [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-InstancePath <String>] [-LocationPath <String>]
 -ResourcePoolName <String[]> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 对象

```
Remove-VMHostAssignableDevice [-HostAssignableDevice] <VMHostAssignableDevice[]>
 -ResourcePoolName <String[]> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-VMHostAssignableDevice` cmdlet 用于移除分配给虚拟机主机的设备。根据所指定的参数，您可以通过提供设备的实例路径或位置路径来删除该设备。

## 示例

### 示例 1

```powershell
$params = @{
InstancePath = "PCIROOT(0)#PCI(0300)#PCI(0000)"
ResourcePoolName = "MyResourcePool"
}
Remove-VMHostAssignableDevice $params
```

这个示例会从名为 **MyResourcePool** 的资源池中移除具有指定实例路径的设备。

## 参数

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](/powershell/module/cimcmdlets/get-cimsession) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: Path
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName

指定一个或多个Hyper-V主机，将从这些主机上移除可分配的设备。允许使用NetBIOS名称、IP地址和完全合格的域名作为标识。默认值是本地计算机。可以使用`localhost`或点（`.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: Path
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
Parameter Sets: Path
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令运行，而无需请求用户确认。

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

### -HostAssignableDevice

指定要移除的设备对象。您可以使用 `Get-VMHostAssignableDevice` 来获取该对象。

```yaml
Type: VMHostAssignableDevice[]
Parameter Sets: Object
Aliases: VMHostAssignableDevice

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -InstancePath

指定主机上的设备实例路径。

```yaml
Type: String
Parameter Sets: Path
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
Parameter Sets: Path
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourcePoolName

指定要从其中移除可分配设备的资源池的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果该cmdlet被运行时会发生什么情况。但实际上该cmdlet并没有被运行。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### Microsoft.HyperV POWERShell.VMHost assignableDevice[]

## 输出

### System.Object

## 备注

## 相关链接

[Add-VMHostAssignableDevice](add-vmhostassignabledevice.md)

[Get-VMHostAssignableDevice](get-vmhostassignabledevice.md)

[Dismount-VMHost assignableDevice](dismount-vmhostassignabledevice.md)

[Mount-VMHost assignableDevice](mount-vmhostassignabledevice.md)
