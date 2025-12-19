---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 02/08/2023
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmhost?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMHost
---

# Set-VMHost

## 摘要
配置一个Hyper-V主机。

## 语法

### ComputerName（默认值）
```
Set-VMHost [[-ComputerName] <String[]>] [[-Credential] <PSCredential[]>] [-MaximumStorageMigrations <UInt32>]
 [-MaximumVirtualMachineMigrations <UInt32>]
 [-VirtualMachineMigrationAuthenticationType <MigrationAuthenticationType>]
 [-UseAnyNetworkForMigration <Boolean>] [-VirtualMachineMigrationPerformanceOption <VMMigrationPerformance>]
 [-ResourceMeteringSaveInterval <TimeSpan>] [-VirtualHardDiskPath <String>] [-VirtualMachinePath <String>]
 [-MacAddressMaximum <String>] [-MacAddressMinimum <String>] [-FibreChannelWwnn <String>]
 [-FibreChannelWwpnMaximum <String>] [-FibreChannelWwpnMinimum <String>] [-NumaSpanningEnabled <Boolean>]
 [-EnableEnhancedSessionMode <Boolean>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### CimSession
```
Set-VMHost [-CimSession] <CimSession[]> [-MaximumStorageMigrations <UInt32>]
 [-MaximumVirtualMachineMigrations <UInt32>]
 [-VirtualMachineMigrationAuthenticationType <MigrationAuthenticationType>]
 [-UseAnyNetworkForMigration <Boolean>] [-VirtualMachineMigrationPerformanceOption <VMMigrationPerformance>]
 [-ResourceMeteringSaveInterval <TimeSpan>] [-VirtualHardDiskPath <String>] [-VirtualMachinePath <String>]
 [-MacAddressMaximum <String>] [-MacAddressMinimum <String>] [-FibreChannelWwnn <String>]
 [-FibreChannelWwpnMaximum <String>] [-FibreChannelWwpnMinimum <String>] [-NumaSpanningEnabled <Boolean>]
 [-EnableEnhancedSessionMode <Boolean>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMHost` cmdlet 用于配置 Hyper-V 主机。

## 示例

#### 示例 1
```
PS C:\> Set-VMHost -MaximumVirtualMachineMigrations 10 -MaximumStorageMigrations 10
```

这个示例配置了本地的Hyper-V主机，使其允许多达10个同时进行的实时迁移和存储迁移操作。

### 示例 2
```
PS C:\> Set-VMHost -MacAddressMinimum 00155D020600 -MacAddressMaximum 00155D0206FF
```

这个示例为本地 Hyper-V 主机配置了一组 MAC 地址范围。

### 示例 3
```
PS C:\> Set-VMHost -UseAnyNetworkForMigration $true
```

这个示例允许使用任何网络来执行对本地Hyper-V主机的实时迁移操作（即将虚拟机从远程主机迁移到本地主机）。

### 示例 4
```
PS C:\> Set-VMHost -VirtualHardDiskPath "C:\Hyper-V\Virtual Hard Disks" -VirtualMachinePath "C:\Hyper-V"
```

这个示例为本地Hyper-V主机上的虚拟硬盘和虚拟机指定了新的默认位置。在这种情况下：

- Virtual machines are stored in "C:\Hyper-V\Virtual Machines" (not "C:\Hyper-V")
- Virtual hard disks are stored in "C:\Hyper-V\Virtual Hard Disks"

### 示例 5
```
PS C:\> Set-VMHost -FibreChannelWwnn C003FF0000FFFF00 -FibreChannelWwpnMinimum C003FF661D200000 -FibreChannelWwpnMaximum C003FF661D200000
```

这个示例配置了本地Hyper-V主机上的Fibre Channel主机设置。

### 示例 6
```
PS C:\> Set-VMHost -NumaSpanningEnabled $false
```

这个示例禁用了本地 Hyper-V 主机上跨 NUMA 的功能。

### 示例 7
```
PS C:\> Set-VMHost -ResourceMeteringSaveInterval 01:30:00
```

这个示例配置了本地的 Hyper-V 主机，使其每小时保存一次数据，用于记录资源消耗情况。

### 示例 8
```
PS C:\> Set-VMHost -VirtualMachineMigrationAuthenticationType Kerberos
```

该示例配置了本地 Hyper-V 主机，使其使用 Kerberos 来验证传入的实时迁移请求。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: CimSession
Aliases:

Required: True
Position: 0
默认值；常规设置 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于运行此 cmdlet 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行选择。默认值是本地计算机。可以通过使用 `localhost` 或点号（.）来明确指定本地计算机。

```yaml
Type: String[]
Parameter Sets: ComputerName
Aliases:

Required: False
Position: 0
默认值；常规设置 value: None
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
默认值；常规设置 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: ComputerName
Aliases:

Required: False
Position: 1
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableEnhancedSessionMode
该选项用于指示用户在使用“虚拟机连接”功能连接到该服务器上的虚拟机时是否可以使用增强模式。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FibreChannelWwnn
指定Hyper-V主机上“World Wide Node Name”（全局节点名称）的默认值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FibreChannelWwpnMaximum
指定可用于在 Hyper-V 主机上生成全球通用端口名称（WWPN）的最大值。结合使用 **FibreChannelWwpnMinimum** 参数，可以确定该 Hyper-V 主机能够分配给虚拟光纤通道适配器的 WWPN 范围。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FibreChannelWwpnMinimum
指定可用于在 Hyper-V 主机上生成全球通用端口名称（WWPN）的最小值。请与 **FibreChannelWwpnMaximum** 参数一起使用，以确定指定的 Hyper-V 主机可以分配给虚拟光纤通道适配器的 WWPN 范围。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MacAddressMaximum
使用有效的十六进制值指定最大MAC地址。结合**MacAddressMinimum**参数一起使用，可以确定指定的Hyper-V主机能够分配给配置为接收动态MAC地址的虚拟机的MAC地址范围。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MacAddressMinimum
使用有效的十六进制值指定最小的MAC地址。请与**MacAddressMaximum**参数一起使用，以确定指定的Hyper-V主机可以分配给配置为接收动态MAC地址的虚拟机的MAC地址范围。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumStorageMigrations
指定在同一时间可以在Hyper-V主机上执行的存储迁移操作的最大数量。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumVirtualMachineMigrations
该参数指定了可以在 Hyper-V 主机上同时进行的最大实时迁移（live migration）次数。如果您的主机属于故障转移集群（Failover Cluster），则集群的配置会优先于 **MaximumVirtualMachineMigrations** 参数所设置的任何值。要查看集群的设置，您可以运行 PowerShell 命令 `(Get-Cluster).MaximumParallelMigrations`。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NumaSpanningEnabled
指定Hyper-V主机上的虚拟机是否可以使用来自多个NUMA节点的资源。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 **Microsoft.HyperV.PowerShell.Host** 对象传递给相应的管道，该对象代表要配置的 Hyper-V 主机。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourceMeteringSaveInterval
指定 Hyper-V 主机保存用于跟踪资源使用情况的数据的频率。时间范围最小为 1 小时，最大为 24 小时。您可以使用 `hh:mm:ss` 的格式来指定具体的时间（其中 `hh` 表示小时，`mm` 表示分钟，`ss` 表示秒）。也可以使用 `Timespan` 对象来设置时间间隔。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseAnyNetworkForMigration
用于指定如何为进入的实时迁移流量选择网络。如果设置为 `$True`，则主机上的任何可用网络都可以用于该流量；如果设置为 `$False$`，则进入的实时迁移流量仅会通过主机上 `**MigrationNetworks**` 属性中指定的网络传输。`Get-VMMigrationNetwork` cmdlet 可以返回可用于迁移流量的网络列表。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VirtualHardDiskPath
指定用于在 Hyper-V 主机上存储虚拟硬盘的默认文件夹。这并非一个具有实际功能的设置：虽然 Hyper-V 管理器插件和 Windows Admin Center 会查询该默认路径并提供给用户，但 Hyper-V API（例如 `CreateFixedVirtualHardDisk`）以及 `New-VHD` 命令并不会使用这个默认路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VirtualMachineMigrationAuthenticationType
指定用于实时迁移的身份验证类型。该参数的可接受值为：Kerberos 和 CredSSP。

```yaml
Type: MigrationAuthenticationType
Parameter Sets: (All)
Aliases:
Accepted values: CredSSP, Kerberos

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VirtualMachineMigrationPerformanceOption
指定用于实时迁移的性能选项。该参数的可接受值为：

- Compression.
Compress data to speed up live migration on constrained networks.
- SMBTransport.
Use server message block (SMB) to get the highest throughput possible.
- None.
Perform standard live migration.

```yaml
Type: VMMigrationPerformance
Parameter Sets: (All)
Aliases:
Accepted values: TCPIP, Compression, SMB

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VirtualMachinePath
指定用于在 Hyper-V 主机上存储虚拟机配置文件的默认文件夹。这是一个功能性设置，也就是说，如果您没有为虚拟机创建工具（例如 `New-VM`）提供路径，Hyper-V 将使用此路径。Hyper-V 会在此路径下至少创建一个名为 “Virtual Machines” 的子文件夹。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。不过实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值；常规设置 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值；常规设置

### Microsoft.HyperV.PowShell.VMHost
如果指定了**-PassThru**选项。

## 备注

## 相关链接
