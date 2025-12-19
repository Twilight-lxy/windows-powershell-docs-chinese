---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VM
---

# Set-VM

## 摘要
配置一台虚拟机。

## 语法

### 名称（默认值）
```
Set-VM [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String[]> [-GuestControlledCacheTypes <Boolean>] [-LowMemoryMappedIoSpace <UInt32>]
 [-HighMemoryMappedIoSpace <UInt64>] [-ProcessorCount <Int64>] [-DynamicMemory] [-StaticMemory]
 [-MemoryMinimumBytes <Int64>] [-MemoryMaximumBytes <Int64>] [-MemoryStartupBytes <Int64>]
 [-AutomaticStartAction <StartAction>] [-AutomaticStopAction <StopAction>] [-AutomaticStartDelay <Int32>]
 [-AutomaticCriticalErrorAction <CriticalErrorAction>] [-AutomaticCriticalErrorActionTimeout <Int32>]
 [-AutomaticCheckpointsEnabled <Boolean>]
 [-LockOnDisconnect <OnOffState>] [-Notes <String>] [-NewVMName <String>] [-SnapshotFileLocation <String>]
 [-SmartPagingFilePath <String>] [-CheckpointType <CheckpointType>] [-Passthru] [-AllowUnverifiedPaths]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Set-VM [-VM] <VirtualMachine[]> [-GuestControlledCacheTypes <Boolean>] [-LowMemoryMappedIoSpace <UInt32>]
 [-HighMemoryMappedIoSpace <UInt64>] [-ProcessorCount <Int64>] [-DynamicMemory] [-StaticMemory]
 [-MemoryMinimumBytes <Int64>] [-MemoryMaximumBytes <Int64>] [-MemoryStartupBytes <Int64>]
 [-AutomaticStartAction <StartAction>] [-AutomaticStopAction <StopAction>] [-AutomaticStartDelay <Int32>]
 [-AutomaticCriticalErrorAction <CriticalErrorAction>] [-AutomaticCriticalErrorActionTimeout <Int32>]
 [-AutomaticCheckpointsEnabled <Boolean>]
 [-LockOnDisconnect <OnOffState>] [-Notes <String>] [-NewVMName <String>] [-SnapshotFileLocation <String>]
 [-SmartPagingFilePath <String>] [-CheckpointType <CheckpointType>] [-Passthru] [-AllowUnverifiedPaths]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Set-VM** cmdlet 用于配置虚拟机。

## 示例

### 示例 1
```
PS C:\> Set-VM -Name TestVM -AutomaticStopAction Shutdown
```

配置虚拟机 TestVM，在 Hyper-V 主机关闭时也自动关闭。

### 示例 2
```
PS C:\> Stop-VM -Name TestVM -Passthru | Set-VM -ProcessorCount 2 -DynamicMemory -MemoryMaximumBytes 2GB -Passthru | Start-VM
```

停止虚拟机 TestVM，将其设置为使用动态内存，将其最大内存容量设置为 2GB，将其配置为使用 2 个虚拟处理器，然后重新启动该虚拟机。

## 参数

### -AllowUnverifiedPaths
指定即使指定的路径无法被集群访问（即验证结果为“不可访问”），也不应抛出错误。此参数适用于集群化的虚拟机。

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

### -AutomaticCheckpointsEnabled
指定是否启用自动检查点功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AutomaticCriticalErrorAction
该参数用于指定当虚拟机（VM）遇到严重错误且超出了由 **AutomaticCriticalErrorActionTimeout** cmdlet 指定的超时时间时应执行的操作。此参数的可接受值包括：Pause 和 None。

```yaml
Type: CriticalErrorAction
Parameter Sets: (All)
Aliases:
Accepted values: None, Pause

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AutomaticCriticalErrorActionTimeout
指定在关闭虚拟机之前需要进行关键暂停（critical pause）的时间长度（以分钟为单位）。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AutomaticStartAction
指定虚拟机启动时应执行的操作。允许的值有：**Nothing**（不执行任何操作）、**StartIfRunning**（如果在运行中则启动）和**Start**（直接启动）。

```yaml
Type: StartAction
Parameter Sets: (All)
Aliases:
Accepted values: Nothing, StartIfRunning, Start

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AutomaticStartDelay
指定虚拟机启动应延迟的秒数。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AutomaticStopAction
指定虚拟机在主机关闭时应执行的操作。允许的值有：**TurnOff**（关闭）、**Save**（保存）和**ShutDown**（直接关机）。

```yaml
Type: StopAction
Parameter Sets: (All)
Aliases:
Accepted values: TurnOff, Save, ShutDown

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CheckpointType
允许您配置由 Hyper-V 创建的检查点的类型。该参数的可接受值包括：

- Disabled.
Block creation of checkpoints.
- Standard.
Create standard checkpoints.
- Production.
Create production checkpoints if supported by guest operating system.
Otherwise, create standard checkpoints.
- ProductionOnly.
Create production checkpoints if supported by guest operating system.
Otherwise, the operation fails.

```yaml
Type: CheckpointType
Parameter Sets: (All)
Aliases:
Accepted values: Disabled, Production, ProductionOnly, Standard

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。请输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于配置虚拟机的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名来进行选择。默认值是本地计算机。可以使用 “localhost” 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
默认值 value: None
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
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DynamicMemory
指定要将虚拟机配置为使用动态内存。

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

### -GuestControlledCacheTypes
指定这台虚拟机是否使用由客户操作系统控制的缓存类型。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HighMemoryMappedIoSpace


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

### -LockOnDisconnect
指定在基本模式下，当用户断开连接后，虚拟机连接是否会导致控制台被锁定。

```yaml
Type: OnOffState
Parameter Sets: (All)
Aliases:
Accepted values: On, Off

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LowMemoryMappedIoSpace


```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MemoryMaximumBytes
指定虚拟机可分配的最大内存量。（仅适用于使用动态内存的虚拟机。）

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MemoryMinimumBytes
指定应为虚拟机分配的最小内存量。（仅适用于使用动态内存的虚拟机。）

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MemoryStartupBytes
指定虚拟机启动时所要分配的内存量。（如果虚拟机不使用动态内存，则此即为要分配的静态内存量。）

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要配置的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: Name
Aliases: VMName

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -NewVMName
指定用于重命名虚拟机的名称。

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

### -Notes
指定要与虚拟机关联的备注信息。

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

### -Passthru
指定要将某个对象传递给表示要配置的虚拟机的管道（pipeline）。

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

### -ProcessorCount
指定虚拟机的虚拟处理器数量。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SmartPagingFilePath
指定用于存储“智能分页”文件的文件夹。

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

### -SnapshotFileLocation
指定用于存储虚拟机快照文件的文件夹。

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

### -StaticMemory
此cmdlet用于配置虚拟机以使用静态内存。请使用**MemoryStartupBytes**参数指定要分配的静态内存大小。

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

### -VM
指定要配置的虚拟机。

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

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.VirtualMachine
如果指定了**-PassThru**选项……

## 备注

## 相关链接

