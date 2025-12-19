---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmharddiskdrive?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMHardDiskDrive
---

# 为虚拟机添加硬盘驱动器

## 摘要
向虚拟机添加硬盘驱动器。

## 语法

### VMName（默认值）
```
Add-VMHardDiskDrive [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [[-ControllerType] <ControllerType>] [[-ControllerNumber] <Int32>]
 [[-ControllerLocation] <Int32>] [[-Path] <String>] [-DiskNumber <UInt32>] [-ResourcePoolName <String>]
 [-SupportPersistentReservations] [-AllowUnverifiedPaths] [-MaximumIOPS <UInt64>] [-MinimumIOPS <UInt64>]
 [-QoSPolicyID <String>] [-QoSPolicy <CimInstance>] [-Passthru] [-OverrideCacheAttributes <CacheAttributes>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Add-VMHardDiskDrive [-VM] <VirtualMachine[]> [[-ControllerType] <ControllerType>] [[-ControllerNumber] <Int32>]
 [[-ControllerLocation] <Int32>] [[-Path] <String>] [-DiskNumber <UInt32>] [-ResourcePoolName <String>]
 [-SupportPersistentReservations] [-AllowUnverifiedPaths] [-MaximumIOPS <UInt64>] [-MinimumIOPS <UInt64>]
 [-QoSPolicyID <String>] [-QoSPolicy <CimInstance>] [-Passthru] [-OverrideCacheAttributes <CacheAttributes>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMDriveController
```
Add-VMHardDiskDrive [-VMDriveController] <VMDriveController> [[-ControllerLocation] <Int32>] [[-Path] <String>]
 [-DiskNumber <UInt32>] [-ResourcePoolName <String>] [-SupportPersistentReservations] [-AllowUnverifiedPaths]
 [-MaximumIOPS <UInt64>] [-MinimumIOPS <UInt64>] [-QoSPolicyID <String>] [-QoSPolicy <CimInstance>] [-Passthru]
 [-OverrideCacheAttributes <CacheAttributes>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-VMHardDiskDrive` cmdlet 可以将一个硬盘驱动器添加到虚拟机中。

## 示例

### 示例 1
```
PS C:\> Add-VMHardDiskDrive -VMName Test -Path D:\VHDs\disk1.vhdx
```

在虚拟机Test上，使用文件D:\VHDs\disk1.vhdx创建一个虚拟硬盘。

### 示例 2
```
PS C:\> Get-VM Test | Add-VMHardDiskDrive -ControllerType SCSI -ControllerNumber 0
```

为虚拟机“Test”上的SCSI控制器0添加一个虚拟硬盘。

### 示例 3
```
PS C:\> Get-VMScsiController -VMName Test -ControllerNumber 0 | Add-VMHardDiskDrive -DiskNumber 2
```

这个示例会获取名为“Test”的虚拟机上的一个SCSI控制器，然后将物理磁盘2添加到该控制器中。

### 示例 4
```
PS C:\> Get-Disk 2 | Add-VMHardDiskDrive -VMName Test
```

这个示例获取物理磁盘2，然后将其添加到一个名为Test的虚拟机中。

## 参数

### -AllowUnverifiedPaths
指定如果指定的路径无法被集群验证为可访问，则不会抛出任何错误。此参数适用于集群化的虚拟机。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此 cmdlet 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全合格的域名来进行指定。默认值为本地计算机。可以使用 `localhost` 或点号（.`）来明确指出本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases: PSComputerName

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerLocation
指定硬盘驱动器应被添加到控制器上的位置编号。如果未指定，则会使用通过 **ControllerNumber** 参数指定的控制器中的第一个可用位置。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerNumber
指定要添加硬盘驱动器的控制器的编号。如果未指定此参数，系统将使用在 **ControllerLocation** 参数中指定的位置上第一个可用的控制器的编号。

```yaml
Type: Int32
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: 2
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerType
指定要将硬盘驱动器添加到的控制器的类型。如果未指定，默认会尝试使用 **IDE** 控制器。如果在指定的位置和编号的 IDE 控制器端口上已经连接了其他驱动器，系统会尝试在由 **ControllerNumber** 指定的 SCSI 控制器上创建一个新的通道来连接硬盘驱动器。允许的值有 **IDE** 和 **SCSI**。

```yaml
Type: ControllerType
Parameter Sets: VMName, VMObject
Aliases:
Accepted values: IDE, SCSI

Required: False
Position: 1
默认值 value: None
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
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DiskNumber
指定要作为直通磁盘连接的离线物理硬盘的磁盘编号。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: Number

Required: False
Position: Named
默认值 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MaximumIOPS
指定硬盘每秒的最大标准化输入/输出操作次数（IOPS）。Hyper-V 将标准化 IOPS 计算为每秒的总输入/输出数据量除以 8 KB 的结果。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinimumIOPS
指定硬盘每秒的最小标准化输入/输出操作次数（IOPS）。Hyper-V 将标准化 IOPS 计算为每秒的总输入/输出量除以 8 KB。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OverrideCacheAttributes


```yaml
Type: CacheAttributes
Parameter Sets: (All)
Aliases:
Accepted values: 默认值, WriteCacheEnabled, WriteCacheAndFUAEnabled, WriteCacheDisabled

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
将新增的 **Microsoft.HyperV.PowerShell.HardDiskDrive** 对象传递给处理流程（pipeline）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定要添加的硬盘驱动器文件的完整路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -QoSPolicy
指定此cmdlet用于关联到硬盘驱动器的存储服务质量（QoS）策略的名称。

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -QoSPolicyID
用于指定存储服务质量（QoS）策略的唯一标识符，该策略将由此 cmdlet 与硬盘驱动器关联起来。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourcePoolName
指定此虚拟硬盘将要关联到的 ISO 资源池的友好名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SupportPersistentReservations
表示该硬盘支持 SCSI 持久性预留（persistent reservation）机制。当硬盘为被多个虚拟机共享的磁盘时，需要指定此参数。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: ShareVirtualDisk

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要将硬盘驱动器添加到的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMDriveController
指定要将硬盘驱动器添加到的控制器上。

```yaml
Type: VMDriveController
Parameter Sets: VMDriveController
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要添加硬盘驱动器的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.HyperV.Powershell.DriveController[]

### Microsoft.HyperV.Powershell.VirtualMachine[]

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.HardDiskDrive
如果指定了 **-PassThru**，

## 备注

## 相关链接
