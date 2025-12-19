---
description: 将一个可分配的设备安装到虚拟机主机上。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/mount-vmhostassignabledevice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Mount-VMHostAssignableDevice
---

# 将虚拟机主机（VMHost）的可分配设备（AssignableDevice）挂载到其他位置

## 摘要
将设备连接到虚拟机（VM）主机上。

## 语法

### 路径（默认值）

```
Mount-VMHostAssignableDevice [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-InstancePath <String>] [-LocationPath <String>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 对象

```
Mount-VMHostAssignableDevice [-HostAssignableDevice] <VMHostAssignableDevice[]> [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Mount-VMHostAssignableDevice` 这个 cmdlet 可以挂载虚拟机主机上实际存在的设备，例如 GPU、网络适配器或存储控制器等。

## 示例

### 示例 1

```powershell
$device = Get-VMHostAssignableDevice -InstancePath "PCIROOT(0)#PCI(0300)#PCI(0000)"
$params = @{
HostAssignableDevice = $device
VMName = "MyVM"
}
Mount-VMHostAssignableDevice @params
```

在这个示例中，`Get-VMHost assignableDevice` cmdlet 会检索具有指定实例路径的设备，并将其存储在 `$device` 变量中。接着，`Mount-VMHostAssignableDevice` cmdlet 将这个设备分配给名为 **MyVM** 的虚拟机。

## 参数

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如 `[New-CimSession](/powershell/module/cimcmdlets/new-cimsession)` 或 `[Get-CimSession](/powershell/module/cimcmdlets/get-cimsession)` cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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

指定一个或多个用于挂载可分配设备的 Hyper-V 主机。支持使用 NetBIOS 名称、IP 地址和完全限定域名。默认值为本地计算机。可以使用 `localhost` 或点（`.`）来明确表示本地计算机。

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

### -HostAssignableDevice

指定要分配给虚拟机主机的设备。

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

表示主机机器中的设备实例路径。

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

在运行cmdlet之前，会提示您进行确认。

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

展示了如果该 cmdlet 被运行会发生什么情况。但实际上，这个 cmdlet 并没有被运行。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### Microsoft.HyperV.PowerShell.VMHost assignableDevice[]

## 输出

### Microsoft.HyperV.PowShell.VMHost assignableDevice

## 备注

## 相关链接

[Add-VMHost assignableDevice](add-vmhostassignabledevice.md)

[Get-VMHost assignableDevice](get-vmhostassignabledevice.md)

[Dismount-VMHost assignableDevice](dismount-vmhostassignabledevice.md)

[Remove-VMHost assignableDevice](remove-vmhostassignabledevice.md)
