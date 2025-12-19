---
description: 使用此主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/new-iscsivirtualdisk?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-IscsiVirtualDisk
---

# 新Iscsi虚拟磁盘

## 摘要
创建一个具有指定文件路径和大小的iSCSI虚拟磁盘。

## 语法

### 动态（默认设置）
```
New-IscsiVirtualDisk [-Description <String>] [-Path] <String> [-SizeBytes] <UInt64>
 [-LogicalSectorSizeBytes <UInt32>] [-PhysicalSectorSizeBytes <UInt32>] [-BlockSizeBytes <UInt32>]
 [-ComputerName <String>] [-Credential <PSCredential>] [<CommonParameters>]
```

### 区分（Differences）
```
New-IscsiVirtualDisk [-Description <String>] -ParentPath <String> [-Path] <String> [[-SizeBytes] <UInt64>]
 [-PhysicalSectorSizeBytes <UInt32>] [-BlockSizeBytes <UInt32>] [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

### 已修复
```
New-IscsiVirtualDisk [-Description <String>] [-Path] <String> [-SizeBytes] <UInt64> [-DoNotClearData]
 [-UseFixed] [-LogicalSectorSizeBytes <UInt32>] [-PhysicalSectorSizeBytes <UInt32>] [-BlockSizeBytes <UInt32>]
 [-ComputerName <String>] [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`New-IscsiVirtualDisk` cmdlet 用于创建一个 iSCSI 虚拟硬盘（VHDX）对象，该对象具有指定的文件路径和大小。创建完 iSCSI VHDX 对象后，可以将这个虚拟硬盘分配给某个 iSCSI 目标设备。一旦虚拟硬盘被分配到目标设备，并且有一个启动器连接到该目标设备，那么该启动器就可以访问该虚拟硬盘了。

如果虚拟硬盘文件的路径不存在，则会创建一个新的VHDX文件。

如果 VHDX 文件路径存在，服务器会返回一个错误。请使用 **Import-IscsiVirtualDisk** cmdlet 来导入现有的虚拟硬盘。

如果在创建虚拟磁盘时cmdlet显示错误，请检查以下情况：

- An absolute file path must be specified for the *Path* and *ParentPath* parameters.

- The virtual disk file name must have a .vhdx file name extension.
- The VHDX file cannot be a network file, or be in a compressed, sparse, or transacted folder.

## 示例

### 示例 1：创建一个固定的 VHDX 文件
```
PS C:\> New-IscsiVirtualDisk -UseFixed -Path "E:\temp\test.vhdx" -Size 10GB
```

这个示例创建了一个固定大小的VHDX文件，其大小为10GB。

### 示例 2：创建一个差异化的 VHDX 文件
```
PS C:\> New-IscsiVirtualDisk -ParentPath "E:\temp\test.vhdx" -Path "E:\temp\child\diff.vhdx"
```

这个示例创建了一个差异化的VHDX文件，其父路径为E:\temp\test.vhdx，而差异化VHDX文件的路径为E:\temp\child\diff.vhdx。

### 示例 3：在远程计算机上创建一个动态的 VHDX 文件
```
PS C:\> New-IscsiVirtualDisk -Path "E:\temp\test.vhdx" -Size 10GB -ComputerName "iscsisvr"
```

这个示例在名为 “iscsisvr” 的计算机上，创建了一个大小为 10GB 的动态 VHDX 文件，文件路径是 E:\temp\test.vhdx。

### 示例 4：创建一个 VHDX 文件
```
PS C:\> New-IscsiVirtualDisk -Path "ramdisk:test.vhdx" -Size 20MB
```

这个示例创建了一个大小为20MB的VHDX文件。该VHDX文件不会被保存下来。如果wintarget服务重启或系统重启，那么这个VHDX文件将会丢失。

## 参数

### -BlockSizeBytes
指定VHDX的块大小（以字节为单位）。对于固定大小的VHDX，如果*SizeBytes*参数的值小于32 MB，则默认大小为2 MB；否则，默认大小为32 MB。对于动态大小的VHDX，默认大小也为2 MB。对于差异化VHDX，其默认大小与父VHDX的*BlockSize*相同。

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

### -ComputerName
如果此 cmdlet 在远程计算机上运行，则会指定该远程计算机的名称或 IP 地址。

如果此 cmdlet 在集群配置上运行，则会指定集群资源组的网络名称，或者集群节点的名称。

如果您没有为这个参数指定值，cmdlet 将使用本地计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Credential
指定在连接到远程计算机时所需的凭据信息。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Description
指定 iSCSI 虚拟磁盘的描述信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DoNotClearData
表示该 cmdlet 不会清除已固定的 VHDX 文件。由于未能清除数据可能会导致先前存在的数据被暴露出来，因此我们不建议选择此选项。

```yaml
Type: SwitchParameter
Parameter Sets: Fixed
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogicalSectorSizeBytes
指定VHDX的逻辑扇区大小（以字节为单位）。该参数的可接受值为：512和4096。默认值为512。

```yaml
Type: UInt32
Parameter Sets: Dynamic, Fixed
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ParentPath
如果VHDX是一个差异磁盘（differential disk），则指定其父虚拟磁盘的路径。

```yaml
Type: String
Parameter Sets: Differencing
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path
指定与 iSCSI 虚拟磁盘关联的 VHDX 文件的路径。如果 VHDX 文件路径不存在，则会创建一个新的 VHDX 文件；如果虚拟硬盘文件的路径已经存在，服务器将返回错误信息。请使用 **Import-IscsiVirtualDisk** cmdlet 来导入现有的虚拟硬盘。

```yaml
Type: String
Parameter Sets: (All)
Aliases: DevicePath

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PhysicalSectorSizeBytes
指定VHDX的物理扇区大小（以字节为单位）。该参数的可接受值为：512和4096。默认值为4096。

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

### -SizeBytes
指定 iSCSI 虚拟磁盘的大小（以字节为单位）。

```yaml
Type: UInt64
Parameter Sets: Dynamic, Fixed
Aliases: Size

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

```yaml
Type: UInt64
Parameter Sets: Differencing
Aliases: Size

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -UseFixed
表示该cmdlet会创建一个固定大小的VHDX文件。

```yaml
Type: SwitchParameter
Parameter Sets: Fixed
Aliases: Fixed

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.Iscsi.Target Commands.IscsiVirtualDisk

## 备注

## 相关链接

[Checkpoint-IscsiVirtualDisk](./Checkpoint-IscsiVirtualDisk.md)

[Convert-IscsiVirtualDisk](./Convert-IscsiVirtualDisk.md)

[Get-IscsiVirtualDisk](./Get-IscsiVirtualDisk.md)

[导入-iScsiVirtualDisk](./Import-IscsiVirtualDisk.md)

[Remove-IscsiVirtualDisk](./Remove-IscsiVirtualDisk.md)

[恢复Iscsi虚拟磁盘](./Restore-IscsiVirtualDisk.md)

[Set-IscsiVirtualDisk](./Set-IscsiVirtualDisk.md)

