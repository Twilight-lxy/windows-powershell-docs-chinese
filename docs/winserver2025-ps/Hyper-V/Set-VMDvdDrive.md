---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmdvddrive?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMDvdDrive
---

# Set-VMDvdDrive

## 摘要
配置一个虚拟DVD驱动器。

## 语法

### VMName（默认值）
```
Set-VMDvdDrive [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String> [[-ControllerNumber] <Int32>] [[-ControllerLocation] <Int32>] [-ToControllerNumber <Int32>]
 [-ToControllerLocation <Int32>] [[-Path] <String>] [-ResourcePoolName <String>] [-AllowUnverifiedPaths]
 [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 对象
```
Set-VMDvdDrive [-VMDvdDrive] <DvdDrive[]> [-ToControllerNumber <Int32>] [-ToControllerLocation <Int32>]
 [[-Path] <String>] [-ResourcePoolName <String>] [-AllowUnverifiedPaths] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-VMDvdDrive` cmdlet 用于配置虚拟 DVD 驱动的控制器及其位置。

## 示例

### 示例 1
```
Set-VMDvdDrive -VMName TestVM -Path .\WinBuild.iso
```

将虚拟机 TestVM 的虚拟 DVD 驱动器配置为使用 WinBuild.iso 作为其介质。

### 示例 2
```
Set-VMDvdDrive -VMName TestVM -ControllerNumber 1 -ControllerLocation 0 -Path $null
```

将虚拟机TestVM的IDE 1.0接口上的虚拟DVD驱动器配置为“不使用任何介质”（即该驱动器不会读取或写入任何数据）。这将导致驱动器中现有的所有介质都被自动弹出。

### 示例 3
```
Get-VMDvdDrive -VMName TestVM -ControllerNumber 1 -ControllerLocation 0 | Set-VMDvdDrive -ToControllerLocation 1
```

将虚拟DVD驱动器从虚拟机TestVM上的IDE 1.0移至IDE 1.1。

## 参数

### -AllowUnverifiedPaths
该参数指定：如果集群无法验证指定的路径是否可访问，则不会抛出任何错误。此参数适用于集群化的虚拟机。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
请指定一个或多个用于配置 DVD 驱动器的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全 Qualified Domain Name（FQDN）来进行选择。默认值是本地计算机。如果需要明确指定本地计算机，可以使用 `localhost` 或点号（.）。

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

### -ControllerLocation
指定要配置的DVD驱动器的IDE控制器位置。如果未指定，则会配置所有控制器位置中的DVD驱动器。

```yaml
Type: Int32
Parameter Sets: VMName
Aliases:

Required: False
Position: 2
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerNumber
指定要配置的DVD驱动器的IDE控制器。如果未指定，则会配置连接到所有控制器的DVD驱动器。

```yaml
Type: Int32
Parameter Sets: VMName
Aliases:

Required: False
Position: 1
默认值 value: None
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

### -Passthru
指定将一个 **Microsoft.HyperV.PowerShell.DvdDrive** 对象传递到管道中，该对象代表需要配置的虚拟 DVD 驱动器。

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

### -Path
指定用于虚拟DVD驱动器的ISO文件的路径或物理DVD驱动器。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourcePoolName
指定该DVD驱动器所要关联的ISO资源池的友好名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ToControllerLocation
指定此虚拟DVD驱动器应被移动到的控制器位置。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ToControllerNumber
指定该 VMDvdDrive 应该被移动到的控制器编号。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMDvdDrive
指定要配置的虚拟DVD驱动器。

```yaml
Type: DvdDrive[]
Parameter Sets: Object
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要配置 DVD 驱动的虚拟机的名称。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.DvdDrive
如果指定了 `-PassThru` 参数。

## 备注

## 相关链接

