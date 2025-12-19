---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 10/15/2024
online version: https://learn.microsoft.com/powershell/module/hyper-v/new-vm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-VM
---

# 新虚拟机

## 摘要
创建一个新的虚拟机。

## 语法

### 无需使用 VHD（默认设置）

```
New-VM [[-Name] <String>] [[-MemoryStartupBytes] <Int64>] [-BootDevice <BootDevice>] [-NoVHD]
 [-SwitchName <String>] [-Path <String>] [-SourceGuestStatePath <String>] [-Version <Version>]
 [-Prerelease] [-Experimental] [[-Generation] <Int16>]
 [-GuestStateIsolationType <GuestIsolationType>] [-Force] [-AsJob] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 新的VHD

```
New-VM [[-Name] <String>] [[-MemoryStartupBytes] <Int64>] [-BootDevice <BootDevice>]
 [-SwitchName <String>] -NewVHDPath <String> -NewVHDSizeBytes <UInt64> [-Path <String>]
 [-SourceGuestStatePath <String>] [-Version <Version>] [-Prerelease] [-Experimental]
 [[-Generation] <Int16>] [-GuestStateIsolationType <GuestIsolationType>] [-Force] [-AsJob]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 现有的VHD文件

```
New-VM [[-Name] <String>] [[-MemoryStartupBytes] <Int64>] [-BootDevice <BootDevice>]
 [-SwitchName <String>] -VHDPath <String> [-Path <String>] [-SourceGuestStatePath <String>]
 [-Version <Version>] [-Prerelease] [-Experimental] [[-Generation] <Int16>]
 [-GuestStateIsolationType <GuestIsolationType>] [-Force] [-AsJob] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`New-VM` cmdlet 用于创建一个新的虚拟机。

## 示例

### 示例 1

```powershell
New-VM -Name "VM01" -MemoryStartupBytes 512MB
```

这个示例创建了一台名为“VM01”的新虚拟机，该虚拟机拥有512MB的内存。

### 示例 2

```powershell
New-VM -Name "VM01" -MemoryStartupBytes 1GB -NewVHDPath D:\vhd\base.vhdx -NewVHDSizeBytes 40GB
```

这个示例创建了一台名为“VM01”的虚拟机，该虚拟机拥有1GB的内存，并连接到一个新的40GB虚拟硬盘上，该硬盘使用的是“VHDX”格式。

### 示例 3

```powershell
New-VM -Name "VM01" -MemoryStartupBytes 1GB -VHDPath D:\vhd\BaseImage.vhdx
```

这个示例创建了一台名为 `VM01` 的虚拟机，该虚拟机拥有 1GB 的内存，并将其连接到一个使用 `VHDX` 格式的现有虚拟硬盘上。

### 示例 4

```powershell
New-VM -Name "VM01" -MemoryStartupBytes 2GB -Credential (Get-Credential) -ComputerName HostServer01
```

这个示例会要求用户提供凭据，然后在名为 `HostServer01` 的服务器上创建一台名为 `VM01` 的虚拟机。该虚拟机拥有 2GB 的内存。

### 示例 5

```powershell
New-VM -Name "VM01" -Generation 1 -BootDevice CD -NoVHD
```

这个示例创建了一台名为“VM01”的虚拟机。该虚拟机没有任何VHD磁盘，并且设置为从CD启动。

### 示例 6

```powershell
$oldVM = Get-VM "PreviousVM"
$memory = (Get-VMMemory -VMName $oldVM.name).Startup
$switch = (Get-VMNetworkAdapter -VMName $oldVM.name).SwitchName
New-VM -Name "VM01" -Generation $oldVM.Generation -MemoryStartupBytes $memory -SwitchName $switch
```

这个示例创建了一台名为 `VM01` 的虚拟机。这台虚拟机与现有的名为 `PreviousVM` 的虚拟机属于同一代产品，分配的内存量也相同，并且连接到了同一个网络交换机上。

## 参数

### -AsJob

以后台作业的方式运行该cmdlet。

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

### -BootDevice

指定用于新虚拟机启动的设备。可选值包括：

- `CD`
- `Floppy`
- `LegacyNetworkAdapter`
- `IDE`
- `NetworkAdapter`
- `VHD`

When `LegacyNetworkAdapter` is specified, this configures the new virtual machine with a network
adapter that can be used to perform a PXE boot and install a 32-bit operating system from a network
installation server.

Generation 2 virtual machines do not support `Floppy`, `LegacyNetworkAdapter` or `IDE`. Using these
values with a Generation 2 virtual machine will cause an error.

`VHD` and `NetworkAdapter` are new to Generation 2 virtual machines. If you specify them on a
Generation 1 virtual machine, then they are interpreted to be `IDE` and `LegacyNetworkAdapter`
respectively.

```yaml
Type: BootDevice
Parameter Sets: (All)
Aliases:
Accepted values: Floppy, CD, IDE, LegacyNetworkAdapter, NetworkAdapter, VHD

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession

Runs the cmdlet in a remote session or on a remote computer. Enter a computer name or a session
object, such as the output of a [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) or
[Get-CimSession](/powershell/module/cimcmdlets/get-cimsession) cmdlet. The default is the
current session on the local computer.

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

Specifies one or more Hyper-V hosts on which the virtual machine is to be created. NetBIOS names,
IP addresses, and fully qualified domain names are allowable. The default is the local computer.
Use localhost or a dot (`.`) to specify the local computer explicitly.

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

Prompts you for confirmation before running the cmdlet.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential

Specifies one or more user accounts that have permission to perform this action. The default is the
current user.

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

### -Experimental

Specific prerelease VM version 255.0. This parameter is used to experiment with new VM
functionality, but this is not supported and may fail across updates. This VM version is not
supported in release host builds, meaning you can only use this on pre-release host builds (Windows
Insider program).

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

### -Force

Forces the command to run without asking for user confirmation.

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

### -Generation

Specifies the generation, as an integer, for the virtual machine. Acceptable values are:

- `1`
- `2`

```yaml
Type: Int16
Parameter Sets: (All)
Aliases:
Accepted values: 1, 2

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GuestStateIsolationType

Specifies the level of isolation for the virtual machine being created. Acceptable values are:

- `TrustedLaunch`: Enables guest state isolation and Trusted Launch security features for the
  virtual machine.
- `VBS`: Enables Virtualization Based Security (VBS) isolation for the virtual machine.
- `SNP`: Enables AMD Secure Encrypted Virtualization-Secure Nested Paging (SEV-SNP) isolation for
  the virtual machine.
- `TDX`: Enables Intel Trust Domain Extensions (TDX) isolation for the virtual machine.
- `Disabled`: Disables all guest state isolation features for the virtual machine.

```yaml
Type: GuestIsolationType
Parameter Sets: (All)
Aliases:
Accepted values: TrustedLaunch, VBS, SNP, TDX, Disabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MemoryStartupBytes

Specifies the amount of memory, in bytes, to assign to the virtual machine. The default value is
`512 MB`.

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

Specifies the name of the new virtual machine. The default name is New virtual machine.

```yaml
Type: String
Parameter Sets: (All)
Aliases: VMName

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -NewVHDPath

Creates a new virtual hard disk with the specified path and connects it to the new virtual machine.
Absolute paths are allowed. If only a file name is specified, the virtual hard disk is created in
the default path configured for the host.

```yaml
Type: String
Parameter Sets: New VHD
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewVHDSizeBytes

Specifies the size of the dynamic virtual hard disk that is created and attached to the new virtual
machine.

```yaml
Type: UInt64
Parameter Sets: New VHD
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoVHD

Creates a virtual machine without attaching any virtual hard disks.

```yaml
Type: SwitchParameter
Parameter Sets: No VHD
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

Specifies the directory to store the files for the new virtual machine.

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

### -Prerelease

Specific prerelease VM version 254.0. This parameter is used to experiment with new VM
functionality, but this is not supported and may fail across updates. This VM version is not
supported in release host builds, meaning you can only use this on pre-release host builds (Windows
Insider program).

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

### -SourceGuestStatePath

Specifies the path to the guest state file for the virtual machine being created. Specifying the
guest state path allows for creation of a new virtual machine that has the same configuration and
state as the existing virtual machine.

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

### -SwitchName

Specifies the friendly name of the virtual switch if you want to connect the new virtual machine to
an existing virtual switch to provide connectivity to a network. Hyper-V automatically creates a
virtual machine with one virtual network adapter, but connecting it to a virtual switch is
optional.

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

### -VHDPath

指定虚拟硬盘文件的路径。

```yaml
Type: String
Parameter Sets: Existing VHD
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Version

在创建虚拟机（VM）的过程中指定版本。有关给定主机上支持的虚拟机版本，请参阅 [Get-VMHostSupportedVersion](/powershell/module/hyper-v/get-vmhost SupportedVersion)。

```yaml
Type: Version
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### System.String

## 输出

### Microsoft.HyperV.PowerShell.VirtualMachine

## 备注

## 相关链接
