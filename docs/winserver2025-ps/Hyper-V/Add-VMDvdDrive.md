---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmdvddrive?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMDvdDrive
---

# Add-VMDvdDrive

## 摘要
将 DVD 驱动器添加到虚拟机中。

## 语法

### VMName（默认值）
```
Add-VMDvdDrive [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [[-ControllerNumber] <Int32>] [[-ControllerLocation] <Int32>] [[-Path] <String>]
 [-ResourcePoolName <String>] [-AllowUnverifiedPaths] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Add-VMDvdDrive [-VM] <VirtualMachine[]> [[-ControllerNumber] <Int32>] [[-ControllerLocation] <Int32>]
 [[-Path] <String>] [-ResourcePoolName <String>] [-AllowUnverifiedPaths] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMDriveController
```
Add-VMDvdDrive [-VMDriveController] <VMDriveController[]> [[-ControllerLocation] <Int32>] [[-Path] <String>]
 [-ResourcePoolName <String>] [-AllowUnverifiedPaths] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-VMDvdDrive` cmdlet 可以将 DVD 驱动器添加到虚拟机中。

## 示例

### 示例 1
```
Add-VMDvdDrive -VMName Test -Path D:\ISOs\disc1.iso
```

这个例子通过使用文件 D:\ISOs\disc1.iso 为虚拟机 Test 添加了一个虚拟 DVD 驱动器。

### 示例 2
```
Get-VM Test | Add-VMDvdDrive -ControllerNumber 1
```

这个示例为虚拟机Test添加了一个虚拟DVD驱动器，使用的是控制器编号1。

### 示例 3
```
Get-VMIdeController -VMName Test | Add-VMDvdDrive -Path E:\
```

这个示例使用了虚拟机“Test”中的IDE控制器来添加虚拟DVD驱动器。

## 参数

### -AllowUnverifiedPaths
指定如果集群无法验证指定的路径是否可访问，则不会抛出任何错误。此参数适用于集群化的虚拟机。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
请指定一个或多个用于安装DVD驱动器的Hyper-V主机。可以使用NetBIOS名称、IP地址或完全合格的域名来进行标识。默认值是本地计算机；若需明确指定本地计算机，可使用“localhost”或点（.）。

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
在运行该cmdlet之前，会提示您进行确认。

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

### -ControllerLocation
指定控制器上用于安装DVD驱动器的位置编号。如果未指定，则会使用控制器上第一个可用位置的编号。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerNumber
指定要将DVD驱动器添加到的控制器的编号。如果未指定，则会使用第一个支持该**ControllerLocation**的IDE控制器。

```yaml
Type: Int32
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: 2
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

### -Passthru
将新增的 `Microsoft.HyperV.PowShell.DvdDrive` 对象传递给后续处理流程（即管道）。

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
指定用于新增DVD驱动器的虚拟硬盘文件或物理硬盘卷的完整路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要添加DVD驱动器的虚拟机。

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
指定要将DVD驱动器添加到的硬盘控制器。

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
指定要添加DVD驱动器的虚拟机的名称。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

### Microsoft.HyperV.PowerShell.VMDriveController[]

### Microsoft.HyperV POWERShell.VirtualMachine[]

## 输出

### Microsoft.HyperV.PowerShell.DvdDrive

## 备注

## 相关链接

