---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmbios?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMBios
---

# Set-VMBios

## 摘要
配置第一代虚拟机的BIOS设置。

## 语法

### VMName（默认值）
```
Set-VMBios [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-DisableNumLock] [-EnableNumLock] [-StartupOrder <BootDevice[]>] [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### VMObject
```
Set-VMBios [-VM] <VirtualMachine[]> [-DisableNumLock] [-EnableNumLock] [-StartupOrder <BootDevice[]>]
 [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMBios
```
Set-VMBios [-VMBios] <VMBios[]> [-DisableNumLock] [-EnableNumLock] [-StartupOrder <BootDevice[]>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMBios` cmdlet 用于配置第 1 代虚拟机的 BIOS。注意：此 cmdlet 不适用于第 2 代虚拟机；如果尝试使用该 cmdlet，将会引发错误。

## 示例

### 示例 1
```
PS C:\> Set-VMBios TestVM -DisableNumLock
```

这个示例默认会禁用虚拟机TestVM上的NumLock键。

### 示例 2
```
PS C:\> Set-VMBios TestVM -StartupOrder @("Floppy", "LegacyNetworkAdapter", "CD", "IDE")
```

此示例配置虚拟机 TestVM 以以下顺序检查启动设备：软盘、网络、CD 驱动器、硬盘。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个或多个需要配置 BIOS 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行标识。默认值为本地计算机。可以通过使用 `localhost` 或点号（.`）来明确表示本地计算机。

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
在运行该 cmdlet 之前，会提示您进行确认。

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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

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

### -DisableNumLock
指定在要配置的虚拟机的BIOS中禁用NumLock键。

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

### -EnableNumLock
指定需要在要配置的虚拟机的BIOS中启用NumLock功能。

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

### -Passthru
指定需要将一个 `Microsoft.HyperV.PowerShell.Bios` 对象传递给管道，该对象代表要配置的 BIOS。

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

### -StartupOrder
指定一组启动设备，这些设备代表了虚拟机BIOS中的启动顺序。启动设备作为**Boot Devices**枚举类型的成员来定义（包括**CD**、**IDE**、**LegacyNetworkAdapter**、**Floppy**）。

注意：VHD 和 NetworkAdapter 这两个 BootDevices 枚举值仅适用于第 2 代虚拟机（Generation 2 VMs），因此使用此 cmdlet 时它们无效。

```yaml
Type: BootDevice[]
Parameter Sets: (All)
Aliases:
Accepted values: Floppy, CD, IDE, LegacyNetworkAdapter, NetworkAdapter, VHD

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要配置 BIOS 的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMBios
指定一个包含 BIOS 对象的数组。该 cmdlet 会为指定的虚拟机配置相应的 BIOS 设置。若需获取某个 BIOS 对象，可使用 **Get-VMBios** cmdlet。

```yaml
Type: VMBios[]
Parameter Sets: VMBios
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要配置 BIOS 的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
默认值 value: None
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
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.Bios
如果指定了 **-PassThru** 参数的话……

## 备注

## 相关链接

