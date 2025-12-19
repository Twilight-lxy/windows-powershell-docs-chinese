---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/resize-vhd?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Resize-VHD
---

# 调整VHD的大小

## 摘要
调整虚拟硬盘的大小。

## 语法

### 大小（默认值）
```
Resize-VHD [-Path] <String[]> [-SizeBytes] <UInt64> [-AsJob] [-Passthru] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 最小尺寸（MinimumSize）
```
Resize-VHD [-Path] <String[]> [-ToMinimumSize] [-AsJob] [-Passthru] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Resize-VHD` cmdlet 可以更改虚拟硬盘的最大物理容量。它可以扩展 VHD 和 VHDX 文件，但只能缩小 VHDX 文件。如果缩小后的虚拟硬盘容量小于其最小容量（该最小容量可通过 VHDX 对象的 `MinimumSize` 属性获取），则缩小操作会失败。

如果虚拟磁盘文件连接到虚拟机的 IDE 链接上，那么在虚拟机处于在线状态时**无法**调整虚拟磁盘的容量。如果虚拟磁盘文件连接到虚拟机的 SCSI 链接上，则可以在虚拟机处于在线状态时调整其容量。

> [!注意] > `Resize-VHD` 不会从动态扩展的虚拟硬盘文件中删除空闲的数据块。请使用 `Optimize-VHD` 代替它。

## 示例

### 示例 1
```
PS C:\> Resize-VHD -Path c:\BaseVHD.vhd -SizeBytes 1099511627776
```

如果VHD的原始大小小于1TB，该命令会将VHD扩展到1TB。如果原始大小已经大于1TB，命令将报告错误，因为无法缩小VHD的大小。

### 示例 2
```
PS C:\> Resize-VHD -Path c:\BaseVHDX.vhdx -SizeBytes 20GB
```

将VHDX的大小更改为20吉字节（21,474,836,480字节）。如果VHDX的大小大于20吉字节，那么只有当`MinimumSize`小于或等于20吉字节时，该cmdlet才能成功执行。

### 示例 3
```
PS C:\> Resize-VHD -Path c:\BaseVHDX.vhdx -ToMinimumSize
```

将VHDX文件压缩到其**MinimumSize**属性所指定的最小可能大小。

## 参数

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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于调整虚拟硬盘大小的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址或完全限定的域名作为主机标识。默认值是本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

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
在运行cmdlet之前会提示您确认是否要执行该操作。

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

### -Passthru
指定需要将一个表示已调整大小虚拟硬盘的对象传递给后续处理流程（即管道）。

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
指定需要调整大小的虚拟硬盘的路径。

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

### -SizeBytes
指定虚拟硬盘需要调整到的大小。

```yaml
Type: UInt64
Parameter Sets: Size
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ToMinimumSize
指定将虚拟硬盘的大小调整为其可能的最小值。

```yaml
Type: SwitchParameter
Parameter Sets: MinimumSize
Aliases:

Required: True
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Vhd.PowerShell.VirtualHardDisk

## 备注

## 相关链接

