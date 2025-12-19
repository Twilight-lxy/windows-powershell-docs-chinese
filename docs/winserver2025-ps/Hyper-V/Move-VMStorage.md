---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/move-vmstorage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Move-VMStorage
---

# 移动虚拟机存储（Move-VMStorage）

## 摘要
移动虚拟机的存储位置。

## 语法

### 名称：SingleDestination（默认值）
```
Move-VMStorage [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> [-DestinationStoragePath] <String> [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource]
 [-RemoveSourceUnmanagedVhds] [-AllowUnverifiedPaths] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 名称：MultipleDestinations
```
Move-VMStorage [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> [-VirtualMachinePath <String>] [-SnapshotFilePath <String>] [-SmartPagingFilePath <String>]
 [-Vhds <Hashtable[]>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource] [-RemoveSourceUnmanagedVhds]
 [-AllowUnverifiedPaths] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMSingleDestination
```
Move-VMStorage [-VM] <VirtualMachine> [-DestinationStoragePath] <String> [-ResourcePoolName <String>]
 [-RetainVhdCopiesOnSource] [-RemoveSourceUnmanagedVhds] [-AllowUnverifiedPaths] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMMultipleDestinations
```
Move-VMStorage [-VM] <VirtualMachine> [-VirtualMachinePath <String>] [-SnapshotFilePath <String>]
 [-SmartPagingFilePath <String>] [-Vhds <Hashtable[]>] [-ResourcePoolName <String>] [-RetainVhdCopiesOnSource]
 [-RemoveSourceUnmanagedVhds] [-AllowUnverifiedPaths] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Move-VMStorage` cmdlet 用于移动虚拟机的存储资源。

## 示例

### 示例 1
```
PS C:\> Move-VMStorage "Test VM" -DestinationStoragePath D:\TestVM
```

将所有与虚拟机测试（VM）相关的文件移动到 D:\TestVM 目录中。

### 示例 2
```
PS C:\> Move-VMStorage "Test VM" -VirtualMachinePath D:\TestVM\Config -SnapshotFilePath D:\TestVM\Snapshots -SmartPagingFilePath D:\TestVM\SmartPaging -VHDs @(@{"SourceFilePath" = "C:\TestVM\Disk1.VHDX"; "DestinationFilePath" = "D:\TestVM\Disks\Disk1.VHDX"}, @{"SourceFilePath" = "C:\TestVM\Disk2.VHDX"; "DestinationFilePath" = "D:\TestVM\Disks\Disk2.VHDX"})
```

将所有与虚拟机测试相关的文件移动到 D:\TestVM 目录下的不同位置。

## 参数

### -AllowUnverifiedPaths
即使在执行移动操作之前无法验证目标计算机指定的路径，该系统仍允许尝试执行移动操作。

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

### -AsJob
以后台作业的形式运行该cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: NameSingleDestination, NameMultipleDestinations
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个虚拟机主机，用于将虚拟机存储数据迁移到这些主机上。允许使用 NetBIOS 名称、IP 地址或完全限定域名作为主机地址。默认值为本地计算机。可以使用 `localhost` 或点号（.）来明确表示本地计算机。

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

### -DestinationStoragePath
指定一个目标存储路径，所有虚拟机的存储数据都将被移动到该路径。

```yaml
Type: String
Parameter Sets: NameSingleDestination, VMSingleDestination
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个名称。

```yaml
Type: String
Parameter Sets: NameSingleDestination, NameMultipleDestinations
Aliases: VMName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -RemoveSourceUnmanagedVhds
表示在该cmdlet移动差异化虚拟硬盘后，迁移完成后Hyper-V会删除源系统上的父虚拟硬盘。

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

### -ResourcePoolName
指定在移动操作完成后要使用的存储资源池的名称。

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

### -RetainVhdCopiesOnSource
请指定 `$true` 以保留源计算机上的所有父级虚拟硬盘。如果不指定此参数，那么在虚拟机成功迁移后，所有虚拟硬盘都将从源计算机上删除。

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

### -SmartPagingFilePath
指定用于智能分页文件的新路径（如果需要的话）。

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

### -SnapshotFilePath
指定与虚拟机关联的所有快照文件的新路径。

```yaml
Type: String
Parameter Sets: NameMultipleDestinations, VMMultipleDestinations
Aliases: CheckpointFileLocation, SnapshotFileLocation

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要移动其存储数据的虚拟机。

```yaml
Type: VirtualMachine
Parameter Sets: VMSingleDestination, VMMultipleDestinations
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Vhds
指定一个哈希表数组，其中包含每个需要移动的虚拟硬盘的位置信息。每个哈希表应包含两个条目：  
- 第一条目的键为 `SourceFilePath`，表示需要移动的虚拟硬盘当前所在的位置；  
- 第二条目的键为 `DestinationFilePath`，表示虚拟硬盘的新位置。  

这两个条目中的虚拟硬盘名称必须完全相同。

```yaml
Type: Hashtable[]
Parameter Sets: NameMultipleDestinations, VMMultipleDestinations
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VirtualMachinePath
指定虚拟机配置文件及相关内存文件的路径。

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
展示了如果运行该cmdlet会发生什么情况。不过实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

