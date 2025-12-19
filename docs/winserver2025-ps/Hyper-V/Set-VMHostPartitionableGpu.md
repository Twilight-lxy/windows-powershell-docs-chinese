---
description: 将主机上的可分区GPU配置为制造商支持的分区数量。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/12/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmhostpartitionablegpu?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMHostPartitionableGpu
---

# 设置虚拟机是否支持可分割的 GPU

## 摘要
将主机上的可分区GPU配置为制造商支持的分区数量。

## 语法

### ComputerName（默认值）

```
Set-VMHostPartitionableGpu [[-ComputerName] <String[]>] [[-Credential] <PSCredential[]>] [-Passthru]
 [-PartitionCount <UInt16>] [<CommonParameters>]
```

### CimSession

```
Set-VMHostPartitionableGpu [-CimSession] <CimSession[]> [-Passthru] [-PartitionCount <UInt16>]
 [<CommonParameters>]
```

### 对象

```
Set-VMHostPartitionableGpu [-HostPartitionableGpu] <VMHostPartitionableGpu[]> [-Passthru]
 [-PartitionCount <UInt16>] [<CommonParameters>]
```

### 名称

```
Set-VMHostPartitionableGpu [-Passthru] [-Name <String>] [-PartitionCount <UInt16>]
 [<CommonParameters>]
```

## 描述

`Set-VMHostPartitionableGpu` cmdlet 将主机上的可分割 GPU 配置为制造商支持的分区数量。

## 示例

### 示例 1

```powershell
Set-VMHostPartitionableGpu -ComputerName "MyHost" -PartitionCount 8
```

这个示例将特定主机上的GPU划分为八个部分（即八个分区）。

### 示例 2

```powershell
$GPU = Get-VMHostPartitionableGpu -Name "GPUDeviceIDName"
Set-VMHostPartitionableGpu -Name $GPU -PartitionCount 4
```

这个示例通过使用GPU设备ID名称，将主机中的GPU划分为四个部分。

## 参数

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](/powershell/module/cimcmdlets/get-cimsession) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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

指定要从虚拟网络适配器中检索的一个或多个 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址和完全限定域名作为标识。默认值为本地计算机。可以使用 `localhost` 或点号（`.`）来明确表示本地计算机。

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

指定一个或多个具有执行此操作权限的用户账户。默认值是当前用户。

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

### -HostPartitionableGpu

完整的GPU对象，通过执行`Get-VMHostPartitionableGpu`命令获得。

```yaml
Type: VMHostPartitionableGpu[]
Parameter Sets: Object
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name

指定GPU的名称。

```yaml
Type: String
Parameter Sets: Name
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PartitionCount

指定 GPU 将分配的分区数量。分区数量由制造商确定。

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

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### Microsoft.ManagementInfrastructure.CimSession[]

### Microsoft.HyperV.PowerShell.VMHostPartitionableGpu[]

## 输出

### Microsoft.HyperV.PowerShell.VMHostPartitionableGpu

## 备注

## 相关链接

[Get-VMHostPartitionableGpu](get-vmhostpartitionable gpu.md)
