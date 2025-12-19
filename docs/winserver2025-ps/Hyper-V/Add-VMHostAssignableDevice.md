---
description: 将设备分配给虚拟机主机。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmhostassignabledevice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMHostAssignableDevice
---

# 添加可分配给虚拟机主机的设备

## 摘要
向虚拟机主机添加可分配的设备。

## 语法

### 路径（默认值）

```
Add-VMHostAssignableDevice [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-Force] [-InstancePath <String>] [-LocationPath <String>]
 -ResourcePoolName <String[]> [<CommonParameters>]
```

### 对象

```
Add-VMHostAssignableDevice [-Force] [-HostAssignableDevice] <VMHostAssignableDevice[]>
 -ResourcePoolName <String[]> [<CommonParameters>]
```

## 描述

`Add-VMHost assignableDevice` cmdlet 用于将硬件设备分配给虚拟机主机。您可以通过提供设备的实例路径或位置路径，或者指定一个现有的、可供主机使用的设备对象，来为虚拟机主机添加设备。

## 示例

### 示例 1

```powershell
$params = @{
ComputerName = "MyVM01"
InstancePath = "PCI\VEN_8086&DEV_0F48&SUBSYS_72708086&REV_0B\3&11583659&0&D8"
ResourcePoolName = "MyResourcePool"
}
Add-VMHostAssignableDevice $params
```

这个例子将一个通过其实例路径识别的设备分配给资源池 **MyResourcePool** 中的虚拟机主机 **MyVM01**。

### 示例 2

```powershell
$gpu = Get-VMHostAssignableDevice
Add-VMHostAssignableDevice -HostAssignableDevice $gpu -ResourcePoolName "GpuChildPool"
```

这个示例会获取一组 GPU 或其他可分配的设备，并将这些设备添加到一个名为 **GpuChildPool** 的资源池中，从而使这些设备可以被该资源池中的虚拟机使用。

## 参数

### -CimSession

在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](/powershell/module/cimcmdlets/new-cimsession)` 或 `[Get-CimSession](/powershell/module/cimcmdlets/get-cimsession)` cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

指定要添加设备的 Hyper-V 主机的名称。允许使用 NetBIOS 名称、IP 地址和完全限定域名作为主机名称。默认值为本地计算机。可以使用 `localhost` 或点（`.`）来明确表示本地计算机。

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

指定要分配给虚拟机的设备对象。

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

### -ResourcePoolName

指定设备被分配到的资源池的名称。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### Microsoft.HyperV.PowerShell.VMHost assignableDevice[]

## 输出

### System.Object

## 备注

## 相关链接

[Get-VMHost assignableDevice](get-vmhostassignabledevice.md)

[Dismount-VMHost assignableDevice](dismount-vmhostassignabledevice.md)

[Mount-VMHost assignableDevice](mount-vmhostassignabledevice.md)

[Remove-VMHost assignableDevice](remove-vmhostassignabledevice.md)
