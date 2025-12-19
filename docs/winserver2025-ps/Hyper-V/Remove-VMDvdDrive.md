---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmdvddrive?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMDvdDrive
---

# 移除VMDVD驱动器

## 摘要
从虚拟机中删除DVD驱动器。

## 语法

### VMName（默认值）
```
Remove-VMDvdDrive [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String> [-ControllerNumber] <Int32> [-ControllerLocation] <Int32> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMDvdDrive
```
Remove-VMDvdDrive [-VMDvdDrive] <DvdDrive[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-VMDvdDrive` cmdlet 用于从虚拟机中删除 DVD 驱动器。

## 示例

### 示例 1
```
PS C:\> Remove-VMDvdDrive -VMName TestVM -ControllerNumber 1 -ControllerLocation 0
```

从虚拟机TestVM上的IDE 1,0中移除虚拟DVD驱动器。

### 示例 2
```
PS C:\> Get-VMDvdDrive -VMName TestVM -ControllerNumber 1 | Remove-VMDvdDrive
```

删除虚拟机TestVM的IDE控制器1上的所有虚拟DVD驱动器。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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
指定一个或多个要从中删除DVD驱动器的Hyper-V主机。可以使用NetBIOS名称、IP地址或完全限定域名进行识别。默认值是本地计算机。可以使用“localhost”或点（.）来明确表示本地计算机。

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
在运行 cmdlet 之前会提示您进行确认。

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
指定控制器上用于删除DVD驱动器的位置的编号。如果未指定，则使用控制器上第一个可用位置的编号。

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

### -ControllerNumber
指定要从哪个控制器中删除DVD驱动器。如果未指定，则会使用第一个支持该**ControllerLocation**的IDE控制器。

```yaml
Type: Int32
Parameter Sets: VMName
Aliases:

Required: True
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
指定要将一个对象传递给表示要删除的DVD驱动器的管道（pipeline）。

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

### -VMDvdDrive
指定要删除的DVD驱动器。

```yaml
Type: DvdDrive[]
Parameter Sets: VMDvdDrive
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要从中删除DVD驱动器的虚拟机的名称。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.DriveController
如果指定了**-PassThru**选项……

## 备注

## 相关链接

