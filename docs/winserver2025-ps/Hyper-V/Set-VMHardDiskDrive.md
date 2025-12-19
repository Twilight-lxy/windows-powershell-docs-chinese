---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmharddiskdrive?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMHardDiskDrive
---

# 设置虚拟机的硬盘驱动器

## 摘要
配置一个虚拟硬盘。

## 语法

### VMName（默认值）
```
Set-VMHardDiskDrive [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String> [[-ControllerType] <ControllerType>] [[-ControllerNumber] <Int32>]
 [[-ControllerLocation] <Int32>] [[-Path] <String>] [-ToControllerType <ControllerType>]
 [-ToControllerNumber <Int32>] [-ToControllerLocation <Int32>] [-DiskNumber <UInt32>]
 [-ResourcePoolName <String>] [-SupportPersistentReservations <Boolean>] [-AllowUnverifiedPaths]
 [-MaximumIOPS <UInt64>] [-MinimumIOPS <UInt64>] [-QoSPolicyID <String>] [-QoSPolicy <CimInstance>] [-Passthru]
 [-OverrideCacheAttributes <CacheAttributes>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 对象
```
Set-VMHardDiskDrive [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMHardDiskDrive] <HardDiskDrive[]> [[-Path] <String>] [-ToControllerType <ControllerType>]
 [-ToControllerNumber <Int32>] [-ToControllerLocation <Int32>] [-DiskNumber <UInt32>]
 [-ResourcePoolName <String>] [-SupportPersistentReservations <Boolean>] [-AllowUnverifiedPaths]
 [-MaximumIOPS <UInt64>] [-MinimumIOPS <UInt64>] [-QoSPolicyID <String>] [-QoSPolicy <CimInstance>] [-Passthru]
 [-OverrideCacheAttributes <CacheAttributes>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMHardDiskDrive` cmdlet 用于配置虚拟硬盘。

## 示例

### 示例 1
```
PS C:\> Set-VMHardDiskDrive -VMName TestVM -Path .\Test.vhd
```

将虚拟机TestVM的硬盘配置为使用Test.vhd作为其存储介质。

### 示例 2
```
PS C:\> Get-VMHardDiskDrive -VMName TestVM -ControllerType IDE -ControllerNumber 1 -ControllerLocation 0 | Set-VMHardDiskDrive -ToControllerLocation 1
```

将虚拟机TestVM上的虚拟硬盘从IDE 1.0移动到IDE 1.1。

## 参数

### -AllowUnverifiedPaths
指定即使指定的路径无法被集群访问（即验证结果为“不可访问”），也不应抛出错误。此参数适用于集群化的虚拟机。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于配置虚拟硬盘的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定的域名进行标识。默认值为本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: PSComputerName

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerLocation
指定虚拟硬盘将被连接到控制器上的哪个位置（即控制器上的哪个端口或分区）。如果未指定，则所有硬盘都会被配置。

```yaml
Type: Int32
Parameter Sets: VMName
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerNumber
指定要配置虚拟硬盘所连接的控制器的编号。如果未指定，则所有硬盘都会被配置。

```yaml
Type: Int32
Parameter Sets: VMName
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerType
指定要配置虚拟硬盘所连接的控制器类型。允许的值有 **Floppy**、**IDE** 和 **SCSI**。

```yaml
Type: ControllerType
Parameter Sets: VMName
Aliases:
Accepted values: IDE, SCSI

Required: False
Position: 1
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

### -DiskNumber
指定应作为“直通磁盘”（passthrough disk）连接的离线物理硬盘的磁盘编号。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: Number

Required: False
Position: Named
Default value: None
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinimumIOPS
指定硬盘每秒的最小标准化输入/输出操作次数（IOPS）。Hyper-V 将标准化 IOPS 计算为每秒的输入/输出总大小除以 8 KB。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OverrideCacheAttributes


```yaml
Type: CacheAttributes
Parameter Sets: (All)
Aliases:
Accepted values: Default, WriteCacheEnabled, WriteCacheAndFUAEnabled, WriteCacheDisabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定将一个 **Microsoft.HyperV.PowerShell.HardDiskDrive** 对象传递到管道中，该对象代表需要配置的虚拟硬盘。

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

### -Path
指定虚拟硬盘将要使用的媒体文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -QoSPolicy
指定要与硬盘驱动器关联的存储服务质量（QoS）策略。

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -QoSPolicyID
指定用于与硬盘驱动器关联的存储服务质量（QoS）策略的ID。

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
指定该硬盘所属的虚拟硬盘资源池的名称。

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

### -SupportPersistentReservations
该参数用于指示硬盘是否支持 SCSI 持久预留（persistent reservation）语义。当硬盘是一块被多个虚拟机共享的磁盘时，需要指定此参数。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: ShareVirtualDisk

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ToControllerLocation
指定此驱动器应移动到的控制器位置。对于IDE控制器，允许的值是0和1；对于SCSI控制器，允许的值是从0到63。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ToControllerNumber
指定此硬盘应移动到的控制器位置。对于IDE控制器，允许的值是0和1；对于SCSI控制器，允许的值是从0到3。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ToControllerType
指定此硬盘应移至的控制器类型。允许的值有 IDE 和 SCSI。

```yaml
Type: ControllerType
Parameter Sets: (All)
Aliases:
Accepted values: IDE, SCSI

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMHardDiskDrive
指定一个或多个需要配置的硬盘。

```yaml
Type: HardDiskDrive[]
Parameter Sets: Object
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定用于配置虚拟硬盘的虚拟机的名称。

```yaml
Type: String
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
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
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.HardDiskDrive


## 备注

## 相关链接

