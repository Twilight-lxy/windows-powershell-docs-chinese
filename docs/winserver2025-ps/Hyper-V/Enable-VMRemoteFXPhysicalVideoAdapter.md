---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/enable-vmremotefxphysicalvideoadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-VMRemoteFXPhysicalVideoAdapter
---

# 启用 VMRemoteFXPhysicalVideoAdapter

## 摘要
重新启用在支持远程FX功能的虚拟机上使用物理视频适配器。

## 语法

### GPUByName（默认值）

```
Enable-VMRemoteFXPhysicalVideoAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-Name] <String[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### GPUByObject

```
Enable-VMRemoteFXPhysicalVideoAdapter [-GPU] <VMRemoteFXPhysicalVideoAdapter[]> [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Enable-VMRemoteFXPhysicalVideoAdapter` 这个 cmdlet 允许一个或多个 RemoteFX 物理视频适配器与支持 RemoteFX 的虚拟机一起使用。

## 示例

### 代码示例标题

```powershell
Get-VMRemoteFXPhysicalVideoAdapter -Name *Nvidia* | Enable-VMRemoteFXPhysicalVideoAdapter
```

启用所有名称中包含“Nvidia”字样的RemoteFX物理视频适配器。

## 参数

### -CimSession

在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: GPUByName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName

指定一个或多个用于启用 RemoteFX 物理视频适配器的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行选择。默认值是本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: GPUByName
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

### -Credential

指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: GPUByName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GPU

指定要启用的RemoteFX物理视频适配器。

```yaml
Type: VMRemoteFXPhysicalVideoAdapter[]
Parameter Sets: GPUByObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name

指定一个适配器名称数组。该cmdlet可以启用您所指定的RemoteFX物理视频适配器。

```yaml
Type: String[]
Parameter Sets: GPUByName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Passthru

指定一个或多个 **Microsoft.HyperV POWERShell.VMRemoteFXPhysicalVideoAdapter** 对象需要被传递到管道中，这些对象代表要启用的 RemoteFX 物理视频适配器。

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

### -WhatIf

展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.HyperV.PowerShell.VMRemoteFXPhysicalVideoAdapter[]

### System.String[]

## 输出

### 无

默认情况下，此cmdlet不会返回任何输出。

### Microsoft.HyperV.PowerShell.VMRemoteFXPhysicalVideoAdapter

当你使用 **PassThru** 参数时，该 cmdlet 会返回 **Microsoft.HyperV.PowerShell.VMRemoteFXPhysicalVideoAdapter** 对象。

## 备注

## 相关链接
