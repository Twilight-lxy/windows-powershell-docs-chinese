---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vhd?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VHD
---

# Set-VHD

## 摘要
设置与虚拟硬盘相关的属性。

## 语法

### 父级（默认值）
```
Set-VHD [-Path] <String> [-ParentPath] <String> [-LeafPath <String>] [-IgnoreIdMismatch] [-Passthru]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### PhysicalSectorSize
```
Set-VHD [-Path] <String> -PhysicalSectorSizeBytes <UInt32> [-Passthru] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### DiskIdentifier
```
Set-VHD [-Path] <String> [-ResetDiskIdentifier] [-Force] [-Passthru] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VHD` cmdlet 用于设置虚拟硬盘的 `ParentPath` 或 `PhysicalSectorSizeBytes` 属性。这两个属性必须通过不同的操作分别进行设置。

## 示例

### 示例 1
```
PS C:\> Set-VHD -Path Child1.vhd -ParentPath ParentCopy.vhd -LeafPath Child2.vhd
```

这个示例将与 ParentCopy.vhd 相关联的虚拟硬盘的父级设置为与 Child1.vhd 相关联的链式虚拟硬盘的父级，而该链式虚拟硬盘的末端节点则是与 Child2.vhd 相关联的虚拟硬盘。整个操作是在在线模式下完成的。

### 示例 2
```
PS C:\> Set-VHD -Path Child1.vhd -ParentPath ParentCopy.vhd
```

这个示例将与 ParentCopy.vhd 相关联的虚拟硬盘的父级设置为与 Child1.vhd 相关联的链式虚拟硬盘的父级。当虚拟硬盘链已连接时，无法执行此操作。

### 示例 3
```
PS C:\> Set-VHD -Path Child1.vhd -parentpath parentcopywithnewid.vhd -IgnoreIdMismatch
```

这个示例将 Child1.vhd 的父文件设置为指向 parentcopywithnewid.vhd，尽管 parentcopywithnewid.vhd 的 ID 与 Child1.vhd 原始父文件的 ID 不同。该操作是在离线模式下进行的。使用这种模式时需要格外谨慎，只有在新旧父文件的块内容完全相同时才能使用它；否则可能会导致数据丢失。

### 示例 4
```
PS C:\> Set-VHD -Path c:\test.vhdx -PhysicalSectorSizeBytes 512
```

这个示例将VHDX的物理扇区大小设置为512字节。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个或多个 Hyper-V 主机，用于设置差异磁盘链中虚拟硬盘的父级。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行指定。默认值是本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

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
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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

### -Force
强制命令运行，而无需请求用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: DiskIdentifier
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IgnoreIdMismatch
指定应跳过对父虚拟硬盘和子虚拟硬盘之间的标识符是否不匹配的检查。

```yaml
Type: SwitchParameter
Parameter Sets: Parent
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LeafPath
指定虚拟硬盘文件的路径，该文件表示虚拟硬盘链中的叶子节点。在在线模式下执行操作时此参数是必需的。

```yaml
Type: String
Parameter Sets: Parent
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ParentPath
指定差异化虚拟硬盘父磁盘的路径。无论该磁盘是否处于在线状态，都可以执行此操作。

```yaml
Type: String
Parameter Sets: Parent
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定要将某个对象传递给表示虚拟硬盘的管道，以便设置该虚拟硬盘的父级（即其所属的容器或系统层级）。

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
指定虚拟硬盘驱动器的虚拟硬盘文件的路径；该虚拟硬盘驱动器在虚拟硬盘链中的父节点需要被设置（即进行相应的配置）。

```yaml
Type: String
Parameter Sets: (All)
Aliases: FullName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PhysicalSectorSizeBytes
指定物理扇区的大小（以字节为单位）。有效值为 512 和 4096。此参数仅支持在操作开始时未连接的 VHDX 格式磁盘上使用。

```yaml
Type: UInt32
Parameter Sets: PhysicalSectorSize
Aliases:
Accepted values: 512, 4096

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResetDiskIdentifier
该参数表示此cmdlet会修改与虚拟硬盘文件关联的虚拟磁盘的磁盘标识符。磁盘标识符是指与磁盘相关联的SCSI重要产品数据（VPD）页面0x83h中的标识符。请仅针对VHDX格式的磁盘使用此参数。

```yaml
Type: SwitchParameter
Parameter Sets: DiskIdentifier
Aliases:

Required: True
Position: Named
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Vhd.PowerShell.VirtualHardDisk

## 备注

## 相关链接

