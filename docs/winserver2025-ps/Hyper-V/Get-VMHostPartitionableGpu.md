---
description: 获取主机上可分区的GPU。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmhostpartitionablegpu?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMHostPartitionableGpu
---

# Get-VMHostPartitionableGpu

## 摘要
获取主机上可分区的GPU。

## 语法

### ComputerName（默认值）

```
Get-VMHostPartitionableGpu [[-ComputerName] <String[]>] [[-Credential] <PSCredential[]>]
 [-Name <String>] [<CommonParameters>]
```

### CimSession

```
Get-VMHostPartitionableGpu [-CimSession] <CimSession[]> [-Name <String>] [<CommonParameters>]
```

## 描述

`Get-VMHostPartitionableGpu` cmdlet 可用于获取主机上可分割的图形处理单元（GPU）的相关信息。这些信息是由显卡制造商提供的驱动程序所提供的。

## 示例

### 示例 1

```powershell
Get-VMHostPartitionableGpu
```

这个示例获取了主机上本地可分区图形处理单元的详细信息。

### 示例 2

```powershell
Get-VMHostPartitionableGpu -ComputerName "MyHost"
```

这个示例通过使用主机名来获取一个可分区的GPU。该命令将显示主机上所有可用于分区的GPU设备。

### 示例 3

```powershell
Get-VMHostPartitionableGpu -Name "GPUDeviceIDName"
```

### 示例 4

```powershell
Get-VMHostPartitionableGpu | FL Name, ValidPartitionCounts
```

这个示例用于检索虚拟机主机上可用的可分区GPU的信息，并将输出结果格式化为列表，显示每个GPU的名称以及可以在每个GPU上创建的有效分区数量。

## 参数

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，也可以输入会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](/powershell/module/cimcmdlets/get-cimsession) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: CimSession
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName

指定一个或多个运行此cmdlet的Hyper-V主机。允许使用NetBIOS名称、IP地址和完全限定域名作为主机标识。默认值是本地计算机。可以使用`localhost`或点（`.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: ComputerName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential

指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: ComputerName
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

指定要获取的图形处理单元（GPU）的名称。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### Microsoft.ManagementInfrastructure.CimSession[]

## 输出

### Microsoft.HyperV.PowerShell.VMHostPartitionableGpu

## 备注

## 相关链接

[Set-VMHostPartitionableGpu](set-vmhostpartitionable gpu.md)
