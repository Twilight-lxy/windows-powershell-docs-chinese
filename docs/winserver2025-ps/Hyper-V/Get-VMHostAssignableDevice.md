---
description: 检索有关可分配给虚拟机主机设备的详细信息。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmhostassignabledevice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMHostAssignableDevice
---

# Get-VMHostAssignableDevice

## 摘要
检索分配给虚拟机主机的设备信息。

## 语法

```
Get-VMHostAssignableDevice [-InstancePath <String>] [-LocationPath <String>]
 [-ResourcePoolName <String[]>] [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [<CommonParameters>]
```

## 描述

`Get-VMHost assignableDevice` 这个 cmdlet 可以检索可以分配给虚拟机主机的设备信息。这些设备可能包括 GPU、网络适配器或存储控制器等，它们物理上存在于主机系统中。该 cmdlet 可以根据设备的实例路径或位置路径来过滤设备。

## 示例

### 示例 1

```powershell
Get-VMHostAssignableDevice
```

这个示例会检索主机计算机上所有可分配的设备。

### 示例 2

```powershell
Get-VMHostAssignableDevice -ComputerName "MyHost"
```

在这个例子中，该 cmdlet 从名为 **MyHost** 的计算机中检索所有可分配的设备。

## 参数

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者提供一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](/powershell/module/cimcmdlets/get-cimsession) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

指定一个或多个用于获取可分配设备的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址和完全限定的域名作为主机标识。默认值为本地计算机。可以使用 `localhost` 或点（`.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
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

### -InstancePath

表示主机机器中的设备实例路径。

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

### -ResourcePoolName

获取设备所分配到的资源池的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### Microsoft.HyperV POWERShell.VMHost assignableDevice

## 备注

## 相关链接

[Add-VMHost assignableDevice](add-vmhostassignabledevice.md)

[Dismount-VMHost assignableDevice](dismount-vmhostassignabledevice.md)

[Mount-VMHost assignableDevice](mount-vmhostassignabledevice.md)

[Remove-VMHostAssignableDevice](remove-vmhostassignabledevice.md)
