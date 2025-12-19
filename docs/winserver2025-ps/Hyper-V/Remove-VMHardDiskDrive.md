---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmharddiskdrive?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMHardDiskDrive
---

# 移除虚拟机的硬盘驱动器

## 摘要
从虚拟机中删除硬盘驱动器。

## 语法

### VMName（默认值）
```
Remove-VMHardDiskDrive [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String> [-ControllerType] <ControllerType> [-ControllerNumber] <Int32>
 [-ControllerLocation] <Int32> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMHardDiskDrive
```
Remove-VMHardDiskDrive [-VMHardDiskDrive] <HardDiskDrive[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-VMHardDiskDrive` cmdlet 可以从虚拟机中删除硬盘驱动器。

## 示例

### 示例 1
```
PS C:\> Remove-VMHardDiskDrive -VMName TestVM -ControllerType IDE -ControllerNumber 1 -ControllerLocation 0
```

从虚拟机TestVM上的IDE 1.0接口中删除该虚拟硬盘。

### 示例 2
```
PS C:\> Get-VMHardDiskDrive -VMName TestVM -ControllerType IDE -ControllerNumber 1 | Remove-VMHardDiskDrive
```

从虚拟机TestVM中移除IDE控制器1上的所有虚拟硬盘。

## 参数

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于删除虚拟硬盘驱动器的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行识别。默认值为本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
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

### -ControllerLocation
指定控制器上用于删除虚拟硬盘驱动器的位置编号。如果未指定，则使用控制器上第一个可用位置的编号。

```yaml
Type: Int32
Parameter Sets: VMName
Aliases:

Required: True
Position: 3
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerNumber
指定要从哪个控制器中删除虚拟硬盘驱动器。如果没有指定，则会使用第一个具备所指定 **ControllerLocation** 的控制器。

```yaml
Type: Int32
Parameter Sets: VMName
Aliases:

Required: True
Position: 2
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerType
指定要删除虚拟硬盘的控制器的类型。允许的值有 **IDE** 和 **SCSI**。

```yaml
Type: ControllerType
Parameter Sets: VMName
Aliases:
Accepted values: IDE, SCSI

Required: True
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值是当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定要将一个对象传递给代表要删除的虚拟硬盘驱动器的管道（pipeline）。

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

### -VMHardDiskDrive
指定要删除的虚拟硬盘驱动器。

```yaml
Type: HardDiskDrive[]
Parameter Sets: VMHardDiskDrive
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要从中删除虚拟硬盘的虚拟机的名称。

```yaml
Type: String
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该 cmdlet 会发生什么情况。但实际上该 cmdlet 并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.HyperV.PowerShell.HardDiskDrive[]

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.DriveController
如果指定了 `-PassThru` 参数。

## 备注

## 相关链接
