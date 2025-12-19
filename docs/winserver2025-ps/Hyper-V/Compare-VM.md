---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/compare-vm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Compare-VM
---

# 比较虚拟机

## 摘要
比较两台虚拟机之间的兼容性，并生成兼容性报告。

## 语法

### NameSingleDestination（默认值）
```
Compare-VM [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-AsJob] [-Name] <String>
 [-DestinationHost] <String> [-DestinationCredential <PSCredential>] [-IncludeStorage]
 [-DestinationStoragePath <String>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### NameSingleDestinationAndCimSession
```
Compare-VM [-CimSession <CimSession[]>] [-AsJob] [-Name] <String> [-DestinationCimSession] <CimSession>
 [-IncludeStorage] [-DestinationStoragePath <String>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 名称：MultipleDestinationsAndCimSession
```
Compare-VM [-CimSession <CimSession[]>] -VirtualMachinePath <String> [-SnapshotFilePath <String>]
 [-SmartPagingFilePath <String>] [-AsJob] [-Name] <String> [-DestinationCimSession] <CimSession>
 [-Vhds <Hashtable[]>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 注册
```
Compare-VM [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-AsJob]
 [-Path] <String> [-Register] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 复制
```
Compare-VM [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VirtualMachinePath <String>] [-SnapshotFilePath <String>] [-SmartPagingFilePath <String>] [-AsJob]
 [-Path] <String> [[-VhdDestinationPath] <String>] [-Copy] [-VhdSourcePath <String>] [-GenerateNewId] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 名称：MultipleDestinations
```
Compare-VM [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-VirtualMachinePath <String>]
 [-SnapshotFilePath <String>] [-SmartPagingFilePath <String>] [-AsJob] [-Name] <String>
 [-DestinationHost] <String> [-DestinationCredential <PSCredential>] [-Vhds <Hashtable[]>]
 [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMMultipleDestinations
```
Compare-VM [-VirtualMachinePath <String>] [-SnapshotFilePath <String>] [-SmartPagingFilePath <String>] [-AsJob]
 [-VM] <VirtualMachine> [-DestinationHost] <String> [-DestinationCredential <PSCredential>]
 [-Vhds <Hashtable[]>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMMultipleDestinationsAndCimSession
```
Compare-VM -VirtualMachinePath <String> [-SnapshotFilePath <String>] [-SmartPagingFilePath <String>] [-AsJob]
 [-VM] <VirtualMachine> [-DestinationCimSession] <CimSession> [-Vhds <Hashtable[]>]
 [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 兼容性报告
```
Compare-VM [-CompatibilityReport] <VMCompatibilityReport> [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMSingleDestinationAndCimSession
```
Compare-VM [-AsJob] [-VM] <VirtualMachine> [-DestinationCimSession] <CimSession> [-IncludeStorage]
 [-DestinationStoragePath <String>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### VMSingleDestination
```
Compare-VM [-AsJob] [-VM] <VirtualMachine> [-DestinationHost] <String> [-DestinationCredential <PSCredential>]
 [-IncludeStorage] [-DestinationStoragePath <String>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Compare-VM` cmdlet 用于比较两台虚拟机及其主机之间的兼容性，并生成相应的兼容性报告。当尝试导入或迁移一台与运行 Hyper-V 的目标服务器不兼容的虚拟机时，该工具非常有用。

## 示例

### 示例 1
```
PS C:\> Compare-VM -Name TestVM -DestinationHost TestDestinationHost
```

比较虚拟机 TestVM 与 Hyper-V 主机 TestDestinationHost 的兼容性。

### 示例 2
```
Attempts import of a virtual machine; the attempt fails due to incompatibilities with the Hyper-V host.
PS C:\> Import-VM -Path 'D:\vm1\Virtual Machines\53EAE599-4D3B-4923-B173-6AEA29CB7F42.XML'
Import-VM : Unable to import virtual machine due to configuration errors.  Please use Compare-VM to repair the virtual machine.
At line:1 char:1
+ import-vm -Path 'D:\vm1\Virtual Machines\53EAE599-4D3B-4923-B173-6AEA29CB7F42.XM ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Import-VM], VirtualizationOperationFailedException
    + FullyQualifiedErrorId : Microsoft.HyperV.PowerShell.Commands.ImportVMCommand

Gets a compatibility report that describes the attempted import and lists the virtual machine's incompatibilities with the Hyper-V host.
PS C:\> $report = Compare-VM -Path 'D:\vm1\Virtual Machines\53EAE599-4D3B-4923-B173-6AEA29CB7F42.XML'


Displays the compatibility report, revealing that the virtual network adapter was connected to switch Production. The Hyper-V host has no switch by that name.
PS C:\> $report.Incompatibilities | Format-Table -AutoSize
Message                                      MessageId Source
-------                                      --------- ------
Could not find Ethernet switch 'Production'.     33012 Microsoft.HyperV.PowerShell.VMNetworkAdapter

Disconnects the virtual network adapter.
PS C:\> $report.Incompatibilities[0].Source | Disconnect-VMNetworkAdapter


Generates a new compatibility report to determine if the virtual machine is compatible with the Hyper-V host.
PS C:\> Compare-VM -CompatibilityReport $report


Displays the compatibility report.
PS C:\> $report
VM                 : Microsoft.HyperV.PowerShell.VirtualMachine
OperationType      : ImportVirtualMachine
Destination        : HYPER-V-1
Path               : D:\vm1\Virtual Machines\53EAE599-4D3B-4923-B173-6AEA29CB7F42.XML
SnapshotPath       : D:\vm1\Snapshots
VhdDestinationPath :
VhdSourcePath      :
Incompatibilities  :

Imports the virtual machine.
PS C:\> import-vm -CompatibilityReport $report
Name State CPUUsage(%) MemoryAssigned(M) MemoryDemand(M) MemoryStatus Uptime   Status             ReplicationState
---- ----- ----------- ----------------- --------------- ------------ ------   ------             ----------------
VM1  Off   0           0                 0                            00:00:00 Operating normally Disabled
```

导入了一台虚拟机，但其配置与 Hyper-V 主机不兼容。请注意，在第一步中使用 **Compare-VM** 命令来排查导入失败的原因。

## 参数

### -AsJob
将该cmdlet作为后台作业运行。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: NameSingleDestinationAndCimSession, NameMultipleDestinationsAndCimSession, Register, Copy
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CompatibilityReport
指定一份兼容性报告，该报告用于解决虚拟机与虚拟机主机之间的任何不兼容问题。

```yaml
Type: VMCompatibilityReport
Parameter Sets: CompatibilityReport
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此 cmdlet 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名来进行指定。默认值为本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: NameSingleDestination, Register, Copy, NameMultipleDestinations
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
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Copy
指定应针对副本导入操作进行比较。

```yaml
Type: SwitchParameter
Parameter Sets: Copy
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: NameSingleDestination, Register, Copy, NameMultipleDestinations
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DestinationCimSession
指定用于在Hyper-V主机上执行兼容性检查的**CIMSession**对象。该Cmdlet会利用这个CIMSession对象来验证虚拟机的兼容性。

```yaml
Type: CimSession
Parameter Sets: NameSingleDestinationAndCimSession, NameMultipleDestinationsAndCimSession, VMMultipleDestinationsAndCimSession, VMSingleDestinationAndCimSession
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DestinationCredential
指定一个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential
Parameter Sets: NameSingleDestination, NameMultipleDestinations, VMMultipleDestinations, VMSingleDestination
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DestinationHost
指定用于比较虚拟机兼容性的 Hyper-V 主机。

```yaml
Type: String
Parameter Sets: NameSingleDestination, NameMultipleDestinations, VMMultipleDestinations, VMSingleDestination
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DestinationStoragePath
指定一个目标存储路径，所有虚拟机的存储数据都将被移至该路径。

```yaml
Type: String
Parameter Sets: NameSingleDestination, NameSingleDestinationAndCimSession, VMSingleDestinationAndCimSession, VMSingleDestination
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GenerateNewId
指定应复制该虚拟机，并为其分配一个新的唯一标识符。

```yaml
Type: SwitchParameter
Parameter Sets: Copy
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeStorage
指定兼容性比较应同时涵盖虚拟机及其存储设备。

```yaml
Type: SwitchParameter
Parameter Sets: NameSingleDestination, NameSingleDestinationAndCimSession, VMSingleDestinationAndCimSession, VMSingleDestination
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要比较的虚拟机的名称。

```yaml
Type: String
Parameter Sets: NameSingleDestination, NameSingleDestinationAndCimSession, NameMultipleDestinationsAndCimSession, NameMultipleDestinations
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Path
指定要比较的虚拟机配置文件的路径。

```yaml
Type: String
Parameter Sets: Register, Copy
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Register
指定比较应针对就地导入操作（in-place import operation）进行。

```yaml
Type: SwitchParameter
Parameter Sets: Register
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourcePoolName
指定资源池的友好名称。

```yaml
Type: String
Parameter Sets: NameSingleDestination, NameSingleDestinationAndCimSession, NameMultipleDestinationsAndCimSession, NameMultipleDestinations, VMMultipleDestinations, VMMultipleDestinationsAndCimSession, VMSingleDestinationAndCimSession, VMSingleDestination
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RetainVhdCopiesOnSource
表示此 cmdlet 会保留源计算机上的父虚拟硬盘。

```yaml
Type: SwitchParameter
Parameter Sets: NameSingleDestination, NameSingleDestinationAndCimSession, NameMultipleDestinationsAndCimSession, NameMultipleDestinations, VMMultipleDestinations, VMMultipleDestinationsAndCimSession, VMSingleDestinationAndCimSession, VMSingleDestination
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SmartPagingFilePath
指定用于智能分页文件的新路径（如果需要的话）。

```yaml
Type: String
Parameter Sets: NameMultipleDestinationsAndCimSession, Copy, NameMultipleDestinations, VMMultipleDestinations, VMMultipleDestinationsAndCimSession
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SnapshotFilePath
指定与虚拟机关联的所有快照文件的路径。

```yaml
Type: String
Parameter Sets: NameMultipleDestinationsAndCimSession, Copy, NameMultipleDestinations, VMMultipleDestinations, VMMultipleDestinationsAndCimSession
Aliases: CheckpointFileLocation, SnapshotFileLocation

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定一台虚拟机。

```yaml
Type: VirtualMachine
Parameter Sets: VMMultipleDestinations, VMMultipleDestinationsAndCimSession, VMSingleDestinationAndCimSession, VMSingleDestination
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VhdDestinationPath
指定用于复制虚拟机VHD文件的文件夹。

```yaml
Type: String
Parameter Sets: Copy
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VhdSourcePath
指定用于复制虚拟机VHD文件的文件夹。

```yaml
Type: String
Parameter Sets: Copy
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Vhds
该参数用于指定一个哈希表数组，这些哈希表用于确定每个需要比较的虚拟硬盘的位置。每个哈希表包含两条记录：  
1. 第一条记录表示虚拟硬盘当前的位置，其键值为 **SourceFilePath**；  
2. 第二条记录表示虚拟硬盘的新位置，其键值为 **DestinationFilePath**。  
在两条记录中，虚拟硬盘的名称必须完全相同。

```yaml
Type: Hashtable[]
Parameter Sets: NameMultipleDestinationsAndCimSession, NameMultipleDestinations, VMMultipleDestinations, VMMultipleDestinationsAndCimSession
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VirtualMachinePath
指定用于存储生成的虚拟机配置文件的路径。

```yaml
Type: String
Parameter Sets: NameMultipleDestinationsAndCimSession, VMMultipleDestinationsAndCimSession
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: Copy, NameMultipleDestinations, VMMultipleDestinations
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMCompatibilityReport

## 备注

## 相关链接

