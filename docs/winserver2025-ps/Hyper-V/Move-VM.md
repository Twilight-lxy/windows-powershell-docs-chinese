---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/move-vm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Move-VM
---

# 移动虚拟机

## 摘要
将虚拟机迁移到新的 Hyper-V 主机上。

## 语法

### 名称：SingleDestination（默认值）
```
Move-VM [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-Name] <String> [-DestinationHost] <String>
 [-DestinationCredential <PSCredential>] [-IncludeStorage] [-DestinationStoragePath <String>]
 [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource] [-RemoveSourceUnmanagedVhds] [-AsJob] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### NameSingleDestinationAndCimSession
```
Move-VM [-CimSession <CimSession[]>] [-Name] <String> [-DestinationCimSession] <CimSession> [-IncludeStorage]
 [-DestinationStoragePath <String>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource]
 [-RemoveSourceUnmanagedVhds] [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### NameMultipleDestinationsAndCimSession
```
Move-VM [-CimSession <CimSession[]>] [-Name] <String> [-DestinationCimSession] <CimSession>
 -VirtualMachinePath <String> [-SnapshotFilePath <String>] [-SmartPagingFilePath <String>]
 [-Vhds <Hashtable[]>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource] [-RemoveSourceUnmanagedVhds]
 [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### NameMultipleDestinations
```
Move-VM [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-Name] <String> [-DestinationHost] <String>
 [-DestinationCredential <PSCredential>] [-VirtualMachinePath <String>] [-SnapshotFilePath <String>]
 [-SmartPagingFilePath <String>] [-Vhds <Hashtable[]>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource]
 [-RemoveSourceUnmanagedVhds] [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 兼容性报告
```
Move-VM [-CompatibilityReport] <VMCompatibilityReport> [-AsJob] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMSingleDestinationAndCimSession
```
Move-VM [-VM] <VirtualMachine> [-DestinationCimSession] <CimSession> [-IncludeStorage]
 [-DestinationStoragePath <String>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource]
 [-RemoveSourceUnmanagedVhds] [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMSingleDestination
```
Move-VM [-VM] <VirtualMachine> [-DestinationHost] <String> [-DestinationCredential <PSCredential>]
 [-IncludeStorage] [-DestinationStoragePath <String>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource]
 [-RemoveSourceUnmanagedVhds] [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMMultipleDestinations
```
Move-VM [-VM] <VirtualMachine> [-DestinationHost] <String> [-DestinationCredential <PSCredential>]
 [-VirtualMachinePath <String>] [-SnapshotFilePath <String>] [-SmartPagingFilePath <String>]
 [-Vhds <Hashtable[]>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource] [-RemoveSourceUnmanagedVhds]
 [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMMultipleDestinationsAndCimSession
```
Move-VM [-VM] <VirtualMachine> [-DestinationCimSession] <CimSession> -VirtualMachinePath <String>
 [-SnapshotFilePath <String>] [-SmartPagingFilePath <String>] [-Vhds <Hashtable[]>]
 [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource] [-RemoveSourceUnmanagedVhds] [-AsJob] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Move-VM` cmdlet 可以将虚拟机移动到新的 Hyper-V 主机上。

## 示例

### 示例 1：将虚拟机迁移到远程计算机
```powershell
PS C:\> Move-VM -Name "Test VM" -DestinationHost remoteServer
```

当虚拟机存储在SMB共享资源上时，将其转移到远程计算机（remoteServer）上。

### 示例 2：将虚拟机及其所有存储资源迁移到远程计算机上
```powershell
PS C:\> Move-VM -Name "Test VM" -DestinationHost remoteServer -IncludeStorage -DestinationStoragePath D:\TestVM
```

将虚拟机 `testVM` 移动到远程计算机 `remoteServer`，并将与该虚拟机关联的所有文件移动到远程计算机上的 `D:\TestVM` 目录中。

### 示例 3：将虚拟机及指定的存储文件迁移到远程计算机
```powershell
PS C:\> Move-VM  -Name "Test VM" -DestinationHost remoteServer -VirtualMachinePath D:\TestVM\Config -SnapshotFilePath D:\TestVM\Snapshots -SmartPagingFilePath D:\TestVM\SmartPaging -IncludeStorage -VHDs @(@{"SourceFilePath" = "C:\TestVM\Disk1.VHDX"; "DestinationFilePath" = "D:\TestVM\Disks\Disk1.VHDX"}, @{"SourceFilePath" = "C:\TestVM\Disk2.VHDX"; "DestinationFilePath" = "D:\TestVM\Disks\Disk2.VHDX"})
```

将虚拟机“Test VM”迁移到远程计算机“remoteServer”，并将与该虚拟机相关的文件放置在远程计算机上D:\TestVM目录下的指定位置。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: NameSingleDestinationAndCimSession, NameMultipleDestinationsAndCimSession
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CompatibilityReport
指定一份兼容性报告，其中包含迁移过程中所需的任何调整措施。

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
指定一个或多个运行此 cmdlet 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行指定。默认值是本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: NameSingleDestination, NameMultipleDestinations
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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: NameSingleDestination, NameMultipleDestinations
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DestinationCimSession
指定虚拟机要迁移到的Hyper-V主机上的**CIMSession**（即用于与虚拟机进行通信的会话对象）。

```yaml
Type: CimSession
Parameter Sets: NameSingleDestinationAndCimSession, NameMultipleDestinationsAndCimSession, VMSingleDestinationAndCimSession, VMMultipleDestinationsAndCimSession
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
Parameter Sets: NameSingleDestination, NameMultipleDestinations, VMSingleDestination, VMMultipleDestinations
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DestinationHost
指定要将虚拟机移动到的 Hyper-V 主机。

```yaml
Type: String
Parameter Sets: NameSingleDestination, NameMultipleDestinations, VMSingleDestination, VMMultipleDestinations
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DestinationStoragePath
指定一个目标路径，所有虚拟机数据都将被移动到该路径。

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

### -IncludeStorage
指定需要同时迁移虚拟机及其存储资源。

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
指定要移动的虚拟机的友好名称。

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

### -Passthru
指定需要将某个对象传递给表示被迁移虚拟机的管道（pipeline）。

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

### -RemoveSourceUnmanagedVhds
该说明表明：在完成迁移后，当此 cmdlet 移动了一个差异化虚拟硬盘时，Hyper-V 会删除源系统上的父虚拟硬盘。

```yaml
Type: SwitchParameter
Parameter Sets: NameSingleDestination, NameSingleDestinationAndCimSession, NameMultipleDestinationsAndCimSession, NameMultipleDestinations, VMSingleDestinationAndCimSession, VMSingleDestination, VMMultipleDestinations, VMMultipleDestinationsAndCimSession
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourcePoolName
指定要使用的处理器资源池的名称。

```yaml
Type: String
Parameter Sets: NameSingleDestination, NameSingleDestinationAndCimSession, NameMultipleDestinationsAndCimSession, NameMultipleDestinations, VMSingleDestinationAndCimSession, VMSingleDestination, VMMultipleDestinations, VMMultipleDestinationsAndCimSession
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
Parameter Sets: NameSingleDestination, NameSingleDestinationAndCimSession, NameMultipleDestinationsAndCimSession, NameMultipleDestinations, VMSingleDestinationAndCimSession, VMSingleDestination, VMMultipleDestinations, VMMultipleDestinationsAndCimSession
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
Parameter Sets: NameMultipleDestinationsAndCimSession, NameMultipleDestinations, VMMultipleDestinations, VMMultipleDestinationsAndCimSession
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SnapshotFilePath
指定与虚拟机相关的任何快照文件的路径。

```yaml
Type: String
Parameter Sets: NameMultipleDestinationsAndCimSession, NameMultipleDestinations, VMMultipleDestinations, VMMultipleDestinationsAndCimSession
Aliases: CheckpointFileLocation, SnapshotFileLocation

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要迁移的虚拟机。

```yaml
Type: VirtualMachine
Parameter Sets: VMSingleDestinationAndCimSession, VMSingleDestination, VMMultipleDestinations, VMMultipleDestinationsAndCimSession
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Vhds
指定一个哈希表数组，该数组包含每个需要移动的虚拟硬盘的位置信息。每个哈希表应包含两个条目：  
1. 第一条目用于存储虚拟硬盘当前的位置，其键为 **SourceFilePath**；  
2. 第二条目用于存储虚拟硬盘的新位置，其键为 **DestinationFilePath**。  

在两个条目中，虚拟硬盘的名称必须保持一致。

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
指定用于存储虚拟机配置文件的路径。

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
Parameter Sets: NameMultipleDestinations, VMMultipleDestinations
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无

默认情况下，此 cmdlet 不会返回任何输出。

### Microsoft.HyperV.PowShell.VirtualMachine

当您使用 **PassThru** 参数时，如果迁移成功，此 cmdlet 会返回一个 **Microsoft.HyperV.PowerShell.VirtualMachine** 对象。

### Microsoft.HyperV.PowerShell.CompatibilityReport

当你使用 **PassThru** 参数时，如果迁移因不兼容性问题而失败，此 cmdlet 会返回一个 **Microsoft.HyperV.PowerShell.CompatibilityReport** 对象。

## 备注

## 相关链接
