---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/new-vhd?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-VHD
---

# 新VHD

## 摘要
创建一个或多个新的虚拟硬盘。

## 语法

### DynamicWithoutSource（默认值）
```
New-VHD [-Path] <String[]> [-SizeBytes] <UInt64> [-Dynamic] [-BlockSizeBytes <UInt32>]
 [-LogicalSectorSizeBytes <UInt32>] [-PhysicalSectorSizeBytes <UInt32>] [-AsJob] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 区分（Differencing）
```
New-VHD [-Path] <String[]> [-ParentPath] <String> [[-SizeBytes] <UInt64>] [-Differencing]
 [-BlockSizeBytes <UInt32>] [-PhysicalSectorSizeBytes <UInt32>] [-AsJob] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### FixedWithoutSource
```
New-VHD [-Path] <String[]> [-SizeBytes] <UInt64> [-Fixed] [-BlockSizeBytes <UInt32>]
 [-LogicalSectorSizeBytes <UInt32>] [-PhysicalSectorSizeBytes <UInt32>] [-AsJob] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 使用源代码修复问题
```
New-VHD [-Path] <String[]> -SourceDisk <UInt32> [-Fixed] [-BlockSizeBytes <UInt32>] [-AsJob]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### DynamicWithSource
```
New-VHD [-Path] <String[]> -SourceDisk <UInt32> [-Dynamic] [-BlockSizeBytes <UInt32>] [-AsJob]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`New-VHD` cmdlet 可以创建一个或多个新的虚拟硬盘，这些硬盘可以是 VHD 格式，也可以是更新的 VHDX 格式。您指定的文件扩展名决定了硬盘的格式。

## 示例

### 示例 1
```
PS C:\> New-VHD -Path c:\Base.vhdx -SizeBytes 10GB
```

这个示例创建了一个大小为10GB的VHDX格式的动态虚拟硬盘。文件扩展名决定了硬盘的格式；由于没有指定具体的类型，因此系统会使用默认的动态硬盘类型。

### 示例 2
```
PS C:\> New-VHD -ParentPath c:\Base.vhdx -Path c:\Diff.vhdx -Differencing
```

这个示例创建了一个采用VHDX格式的差异虚拟硬盘，其父路径为c:\Base.vhdx。

### 示例 3
```
PS C:\> New-VHD -Path C:\fixed.vhd -Fixed -SourceDisk 2 -SizeBytes 1TB
```

这个示例会在指定的路径上创建一个大小为1 TB的VHD格式的固定虚拟硬盘。该虚拟硬盘的数据来源于系统中编号为2的磁盘。你可以使用`Get-Disk` cmdlet来列出连接到系统的所有磁盘以及每个磁盘的编号。

### 示例 4
```
PS C:\> New-VHD -Path c:\LargeSectorBlockSize.vhdx -BlockSizeBytes 128MB -LogicalSectorSize 4KB -SizeBytes 1TB
```

这个示例会在指定的路径下创建一个新的、容量为1 TB的VHDX格式动态虚拟硬盘，该硬盘的块大小为128 MB，逻辑扇区大小为4 KB。

### 示例 5
```
PS C:\> $vhdpath = "C:\VHDs\Test.vhdx"
PS C:\> $vhdsize = 127GB
PS C:\> New-VHD -Path $vhdpath -Dynamic -SizeBytes $vhdsize | Mount-VHD -Passthru |Initialize-Disk -Passthru |New-Partition -AssignDriveLetter -UseMaximumSize |Format-Volume -FileSystem NTFS -Confirm:$false -Force
```

这个示例创建了一个新的 127GB 大小的虚拟硬盘（VHD），然后将其挂载到系统中，对其进行初始化和格式化处理，使得该磁盘可以正常使用了。

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。

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

### -BlockSizeBytes
指定要创建的虚拟硬盘的块大小（以字节为单位）。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定一个或多个用于创建虚拟硬盘文件的Hyper-V主机。可以使用NetBIOS名称、IP地址或完全限定的域名进行选择。默认值是本地计算机。可以使用`localhost`或点（.）来明确表示本地计算机。

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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Differencing
指定要创建一个差异化虚拟硬盘。

```yaml
Type: SwitchParameter
Parameter Sets: Differencing
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Dynamic
指定要创建一个动态虚拟硬盘。

```yaml
Type: SwitchParameter
Parameter Sets: DynamicWithoutSource
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: SwitchParameter
Parameter Sets: DynamicWithSource
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Fixed
指定要创建一个固定的虚拟硬盘。

```yaml
Type: SwitchParameter
Parameter Sets: FixedWithoutSource, FixedWithSource
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogicalSectorSizeBytes
指定要创建的虚拟硬盘的逻辑扇区大小（以字节为单位）。有效值为 512 和 4096。

```yaml
Type: UInt32
Parameter Sets: DynamicWithoutSource, FixedWithoutSource
Aliases:
Accepted values: 512, 4096

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ParentPath
指定要创建的差异磁盘父目录的路径（此参数仅用于创建差异磁盘时）。

```yaml
Type: String
Parameter Sets: Differencing
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
这是创建新的虚拟硬盘文件时所使用的路径。如果指定了文件名或相对路径，那么新虚拟硬盘文件的路径将会相对于当前工作目录来计算。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PhysicalSectorSizeBytes
指定物理扇区的大小（以字节为单位）。有效值为 512 和 4096。

```yaml
Type: UInt32
Parameter Sets: DynamicWithoutSource, Differencing, FixedWithoutSource
Aliases:
Accepted values: 512, 4096

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SizeBytes
要创建的虚拟硬盘的最大大小（以字节为单位）。

```yaml
Type: UInt64
Parameter Sets: DynamicWithoutSource, FixedWithoutSource
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: UInt64
Parameter Sets: Differencing
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SourceDisk
指定要用作创建的虚拟硬盘源的物理磁盘。

```yaml
Type: UInt32
Parameter Sets: FixedWithSource, DynamicWithSource
Aliases: Number

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Vhd.PowerShell.VirtualHardDisk

## 备注

## 相关链接

