---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmharddiskdrive?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMHardDiskDrive
---

# Get-VMHardDiskDrive

## 摘要
获取连接到一台或多台虚拟机的虚拟硬盘驱动器信息。

## 语法

### VMName（默认值）
```
Get-VMHardDiskDrive [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-ControllerLocation <Int32>] [-ControllerNumber <Int32>]
 [-ControllerType <ControllerType>] [<CommonParameters>]
```

### VMObject
```
Get-VMHardDiskDrive [-VM] <VirtualMachine[]> [-ControllerLocation <Int32>] [-ControllerNumber <Int32>]
 [-ControllerType <ControllerType>] [<CommonParameters>]
```

### VMSnapshot
```
Get-VMHardDiskDrive [-VMSnapshot] <VMSnapshot> [-ControllerLocation <Int32>] [-ControllerNumber <Int32>]
 [-ControllerType <ControllerType>] [<CommonParameters>]
```

### VMDriveController
```
Get-VMHardDiskDrive [-ControllerLocation <Int32>] [-VMDriveController] <VMDriveController[]>
 [<CommonParameters>]
```

## 描述
`Get-VMHardDiskDrive` cmdlet 可用于获取连接到一台或多台虚拟机的虚拟硬盘驱动器。

## 示例

### 示例 1
```
PS C:\> Get-VMHardDiskDrive -VMName TestVM
```

从虚拟机 TestVM 中获取虚拟硬盘。

### 示例 2
```
PS C:\> Get-VM -Name TestVM | Get-VMHardDiskDrive -ControllerType IDE -ControllerNumber 1
```

从虚拟机TestVM的IDE控制器1中获取虚拟硬盘。

### 示例 3
```
PS C:\> Get-VMIdeController -VMName TestVM -ControllerNumber 1 -ComputerName Development | Get-VMHardDiskDrive
```

从位于Hyper-V主机Development上的虚拟机TestVM的IDE控制器1中获取虚拟硬盘。

### 示例 4
```
PS C:\> Get-VMSnapshot -VMName Test -Name 'Before applying updates' | Get-VMHardDiskDrive
```

在应用虚拟机TestVM的更新之前，从快照中获取虚拟硬盘。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于获取虚拟硬盘驱动器的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名来进行选择。默认值是本地计算机。可以使用 “localhost” 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerLocation
指定控制器上用于获取虚拟硬盘驱动器的位置编号。如果未指定，则使用控制器上第一个可用位置的编号。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerNumber
指定用于获取虚拟硬盘驱动器的控制器的编号。如果未指定，则会使用第一个支持所指定的 **ControllerLocation** 的控制器。

```yaml
Type: Int32
Parameter Sets: VMName, VMObject, VMSnapshot
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerType
指定用于获取虚拟硬盘驱动器的控制器的类型。允许的值有 **Floppy**（软盘）、**IDE** 和 **SCSI**。

```yaml
Type: ControllerType
Parameter Sets: VMName, VMObject, VMSnapshot
Aliases:
Accepted values: IDE, SCSI

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定用于获取虚拟硬盘驱动器的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMDriveController
指定用于获取虚拟硬盘驱动器的驱动控制器。

```yaml
Type: VMDriveController[]
Parameter Sets: VMDriveController
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定用于获取虚拟硬盘驱动器的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMSnapshot
指定用于获取虚拟硬盘驱动器的快照。

```yaml
Type: VMSnapshot
Parameter Sets: VMSnapshot
Aliases: VMCheckpoint

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.HyperV POWERShell.ControllerType

### Microsoft.HyperV.PowerShell.VMSnapshot

### Microsoft.HyperV.PowerShell.VMDriveController[]

### Microsoft.HyperV.PowerShell.VirtualMachine[]

## 输出

### Microsoft.HyperV.PowerShell.HardDiskDrive

## 备注

## 相关链接

