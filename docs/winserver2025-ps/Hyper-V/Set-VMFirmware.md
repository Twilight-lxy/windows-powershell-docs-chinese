---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmfirmware?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMFirmware
---

# 设置虚拟机固件

## 摘要
用于设置虚拟机的固件配置。

## 语法

### VMName（默认值）
```
Set-VMFirmware [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-BootOrder <VMComponentObject[]>] [-FirstBootDevice <VMComponentObject>]
 [-EnableSecureBoot <OnOffState>] [-SecureBootTemplate <String>] [-SecureBootTemplateId <Guid>]
 [-PreferredNetworkBootProtocol <IPProtocolPreference>] [-ConsoleMode <ConsoleModeType>]
 [-PauseAfterBootFailure <OnOffState>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Set-VMFirmware [-VM] <VirtualMachine[]> [-BootOrder <VMComponentObject[]>]
 [-FirstBootDevice <VMComponentObject>] [-EnableSecureBoot <OnOffState>] [-SecureBootTemplate <String>]
 [-SecureBootTemplateId <Guid>] [-PreferredNetworkBootProtocol <IPProtocolPreference>]
 [-ConsoleMode <ConsoleModeType>] [-PauseAfterBootFailure <OnOffState>] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 虚拟机固件（VM Firmware）
```
Set-VMFirmware [-VMFirmware] <VMFirmware[]> [-BootOrder <VMComponentObject[]>]
 [-FirstBootDevice <VMComponentObject>] [-EnableSecureBoot <OnOffState>] [-SecureBootTemplate <String>]
 [-SecureBootTemplateId <Guid>] [-PreferredNetworkBootProtocol <IPProtocolPreference>]
 [-ConsoleMode <ConsoleModeType>] [-PauseAfterBootFailure <OnOffState>] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-VMFirmware` cmdlet 用于设置第 2 代虚拟机的固件配置。

## 示例

### 示例 1
```
PS C:\> Set-VMFirmware "Test VM" -EnableSecureBoot On
```

这个示例使得虚拟机“Test VM”具备了安全启动（secure boot）的功能。

### 示例 2
```
PS C:\> Set-VMFirmware "Test VM" -FirstBootDevice $vmNetworkAdapter
```

这个示例将虚拟机“Test VM”设置为从存储在 $vmNetworkAdapter 中的虚拟机网络适配器对象启动。该对象是通过使用 get-VMNetworkAdapter 命令获取的。

### 示例 3
```
PS C:\> Set-VMFirmware "Test VM" -BootOrder $vmNetworkAdapter, $vmHardDiskDrive
```

为虚拟机“Test VM”设置启动顺序。$vmNetworkAdapter 包含一个虚拟机网络适配器对象（通过 get-VMNetworkAdapter 获取），而 $vmHardDiskDrive 包含一个虚拟机硬盘对象（通过 get-VMHardDiskDrive 获取）。此命令未指定的任何现有启动项将从虚拟机中删除。

## 参数

### -BootOrder
指定一个设备数组。启动顺序决定了从哪些设备开始进行启动。该参数的可接受值包括：


-- VMBootSource

-- VMNetworkAdapter

-- 硬盘驱动器

-- DVDDrive


VMBootSource值描述了固件中非易失性随机存取存储器（NVRAM）中的一个启动条目。

```yaml
Type: VMComponentObject[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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
指定您想要修改其固件配置的 Hyper-V 主机的名称。

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

### -Confirm
在运行cmdlet之前会提示您进行确认。

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

### -ConsoleMode
指定虚拟机的控制台模式类型。该参数允许虚拟机在无需图形用户界面的情况下运行。

```yaml
Type: ConsoleModeType
Parameter Sets: (All)
Aliases:
Accepted values: Default, COM1, COM2, None

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

### -EnableSecureBoot
指定是否启用安全启动功能。该参数的可接受值为：


-- 进行中

-- 关闭


安全启动（Secure Boot）采用公钥基础设施来保护操作系统的完整性。

```yaml
Type: OnOffState
Parameter Sets: (All)
Aliases:
Accepted values: On, Off

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FirstBootDevice
指定首先尝试从哪个设备启动。该参数的可接受值为：


-- VMBootSource

-- VMNetworkAdapter

-- 硬盘驱动器

-- DVDDrive


VMBootSource值描述了固件NVRAM中的一个启动条目（即用于系统启动的信息）。

```yaml
Type: VMComponentObject
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -PauseAfterBootFailure
指定虚拟机在启动失败后的行为。当设置为“On”时，如果虚拟机无法从设备中成功启动，则该虚拟机会被暂停。

```yaml
Type: OnOffState
Parameter Sets: (All)
Aliases:
Accepted values: On, Off

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PreferredNetworkBootProtocol
指定在网络启动过程中使用的 IP 协议版本。

```yaml
Type: IPProtocolPreference
Parameter Sets: (All)
Aliases:
Accepted values: IPv4, IPv6

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SecureBootTemplate
指定安全启动模板（secure boot template）的名称。如果启用了安全启动功能，则必须拥有一个有效的安全启动模板，才能让客户操作系统（guest operating system）正常启动。

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

### -SecureBootTemplateId
指定安全启动模板的ID。

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定需要修改固件配置的虚拟机对象。要获取一个虚拟机对象，请使用 **Get-VM** cmdlet。

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

### -VMFirmware
指定一个虚拟机固件配置数组。该cmdlet会设置您所指定的固件配置。

```yaml
Type: VMFirmware[]
Parameter Sets: VMFirmware
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定一个虚拟机名称数组，您希望修改这些虚拟机的固件配置。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.Powershell.VMFirmware

## 备注
* Note: This cmdlet is supported only when run against Generation 2 virtual machines.

## 相关链接

[Get-VMFirmware](./Get-VMFirmware.md)

