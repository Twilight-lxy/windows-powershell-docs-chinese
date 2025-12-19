---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/optimize-vhd?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Optimize-VHD
---

# 优化VHD文件

## 摘要
优化虚拟硬盘文件所占空间的分配情况（固定大小的虚拟硬盘除外）。

## 语法

```
Optimize-VHD [-Path] <String[]> [-Mode <VhdCompactMode>] [-AsJob] [-Passthru] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Optimize-VHD` cmdlet 用于优化一个或多个虚拟硬盘文件中的空间分配（固定大小的虚拟硬盘除外）。为了实现优化，会使用 `Compact` 操作。该操作会回收未使用的磁块，并重新排列这些磁块以便更高效地存储数据，从而减小虚拟硬盘文件的大小。

要使用 Optimize-VHD，虚拟硬盘不能被挂载，或者必须以只读模式进行挂载。

如果无法进行任何优化，那么“压缩操作”仍然可以成功完成，且文件大小不会发生变化。

## 示例

### 示例 1
```
PS C:\> Optimize-VHD -Path c:\test\dynamic.vhdx -Mode Full
```

在全模式下执行压缩操作。（如果VHDX格式文件在操作前没有以只读方式被附加，则系统会默认使用“预清零”模式。）

### 示例 2
```
PS C:\> Optimize-VHD -Path c:\test\dynamic.vhdx -Mode Retrim
```

在“Retrim”模式下执行压缩操作。（如果在操作之前没有将VHDX格式的磁盘设置为只读模式，那么运行此cmdlet会返回错误。）

### 示例 3
```
PS C:\> Optimize-VHD -Path c:\test\dynamic.vhdx -Mode Quick
```

在快速模式下执行压缩操作。（如果VHDX格式的文件在操作之前没有以只读方式附加，则默认使用“预修剪”模式。）

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet将在本地计算机的当前会话中运行。

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
指定一个或多个用于优化虚拟机的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全合格的域名进行指定。默认值为本地计算机。可以使用 “localhost” 或点（.）来明确表示本地计算机。

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

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Mode
指定虚拟硬盘的优化模式。对于 **VHD** 磁盘，默认模式为 **Full**（完全优化）；对于 **VHDX** 磁盘，默认模式为 **Quick**（快速优化）。有效的模式如下：

- **Full** scans for zero blocks and reclaims unused blocks. (Allowable only if the virtual hard disk is mounted read-only.)
- **Pretrimmed** performs as **Quick** mode, but does not require the virtual hard disk to be mounted read-only. The detection of unused space is less effective than **Quick** mode (in which the virtual hard disk had been mounted read-only) because the scan cannot query information about free space in the NTFS file system within the virtual hard disk. Useful when the VHDX-format file has been used by operating system instances that are at least Windows 8 or Windows Server 2012, or when this cmdlet has already been run on a .vhdx file in **Retrim** mode.
- **Prezeroed** performs as **Quick** mode, but does not require the virtual hard disk to be mounted read-only. The unused space detection will be less effective than if the virtual hard disk had been mounted read-only as the scan will be unable to query information about free space in the NTFS file system within the virtual hard disk. Useful if a tool was run previously to zero all the free space on the virtual disk as this mode of compaction can then reclaim that space for subsequent block allocations. This form of compaction can also be useful in handling virtual hard disk containing file systems other than NTFS.
- **Quick** reclaims unused blocks, but does not scan for zero blocks. (Allowable only if the virtual hard disk is mounted read-only.)
- **Retrim** sends down retrims without scanning for zero blocks or reclaiming unused blocks. (Allowable only if the virtual hard disk is mounted read-only.)

```yaml
Type: VhdCompactMode
Parameter Sets: (All)
Aliases:
Accepted values: Full, Quick, Retrim, Pretrimmed, Prezeroed

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定要将某个对象传递给用于表示待优化虚拟硬盘的处理流程（即管道）。

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
指定一个或多个路径，这些路径指向需要优化的动态虚拟硬盘文件或差异备份虚拟硬盘文件。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: FullName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生的结果。但实际上并没有运行该cmdlet。

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

### Microsoft.Vhd.PowerShellVirtualHardDisk

## 备注

## 相关链接

