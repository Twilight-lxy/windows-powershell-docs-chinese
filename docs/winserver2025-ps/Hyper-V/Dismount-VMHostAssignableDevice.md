---
description: 从虚拟机主机上卸载可分配的设备。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/dismount-vmhostassignabledevice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Dismount-VMHostAssignableDevice
---

# 卸载 VMHost 可分配设备

## 摘要
从虚拟机主机上卸载设备。

## 语法

```
Dismount-VMHostAssignableDevice [-InstancePath <String>] [-LocationPath <String>] [-Force]
 [-Passthru] [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Dismount-VMHostAssignableDevice` cmdlet 用于从虚拟机主机上卸载可分配的设备。当您需要重新分配设备或解决设备与虚拟机之间的冲突时，请使用此 cmdlet。

## 示例

### 示例 1

```powershell
Dismount-VMHostAssignableDevice -InstancePath "PCIROOT(0)#PCI(1D02)#PCI(0000)"
```

这个示例将从主机上卸载具有指定实例路径的设备，使其可以用于分配给虚拟机。

## 参数

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](/powershell.module/cimcmdlets/get-cimsession) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName

指定一个或多个 Hyper-V 主机，这些主机上的设备将被卸载。允许使用 NetBIOS 名称、IP 地址和完全合格的域名作为标识。默认值为本地计算机。可以使用 `localhost` 或点号（`.`）来明确表示本地计算机。

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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令执行，而不需要用户确认。

使用 **Force** 参数还会覆盖平台中的一些安全检查。欲了解更多信息，请参阅 [从主机分区卸载设备](/windows-server/virtualization/hyper-v/deploy/deploying-graphics-devices-using-dda#dismount-the-device-from-the-host-partition)。

如果未提供任何分区驱动程序，在卸载设备时必须使用 `-Force` 选项来忽略安全警告。有关安全影响的更多信息，请参阅 [使用离散设备分配计划进行设备部署](/windows-server/virtualization/hyper-v/plan/plan-for-deploying-devices-using-discrete-device-assignment)。

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

展示了如果该cmdlet运行会发生什么情况。但实际上该cmdlet并没有被运行。

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

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### Microsoft.HyperV.PowerShell.VMHost assignableDevice

## 备注

## 相关链接

[Add-VMHost assignableDevice](add-vmhostassignabledevice.md)

[Get-VMHost assignableDevice](get-vmhostassignabledevice.md)

[Mount-VMHost assignableDevice](mount-vmhostassignabledevice.md)

[Remove-VMHost assignableDevice](remove-vmhostassignabledevice.md)
