---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/disable-vmremotefxphysicalvideoadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-VMRemoteFXPhysicalVideoAdapter
---

# 禁用 VMRemoteFXPhysicalVideoAdapter

## 摘要
禁用在支持远程FX功能的虚拟机上使用物理视频适配器。

## 语法

### GPUByName（默认值）
```
Disable-VMRemoteFXPhysicalVideoAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-Name] <String[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### GPUByObject
```
Disable-VMRemoteFXPhysicalVideoAdapter [-GPU] <VMRemoteFXPhysicalVideoAdapter[]> [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
` Disable-VMRemoteFXPhysicalVideoAdapter ` 这个 cmdlet 可以禁用一个或多个 RemoteFX 物理视频适配器，使其无法与启用了 RemoteFX 功能的虚拟机一起使用。

## 示例

#### 示例 1
```
PS C:\> Disable-VMRemoteFXPhysicalVideoAdapter -Name *Nvidia*
```

这个示例会禁用所有名称中包含“Nvidia”字样的RemoteFX物理视频适配器。

### 示例 2
```
PS C:\> Get-VMRemoteFXPhysicalVideoAdapter -Name *Nvidia* | Disable-VMRemotePhysicalVideoAdapter
```

这个示例会禁用所有名称中包含“Nvidia”字样的RemoteFX物理视频适配器。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如使用[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: GPUByName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于禁用 RemoteFX 物理视频适配器的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址或完全限定域名作为主机标识。默认值为本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: GPUByName
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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: GPUByName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GPU
指定一个或多个需要禁用的 RemoteFX 物理视频适配器。

```yaml
Type: VMRemoteFXPhysicalVideoAdapter[]
Parameter Sets: GPUByObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name
指定一个适配器名称数组。该cmdlet会禁用您所指定的RemoteFX物理视频适配器。

```yaml
Type: String[]
Parameter Sets: GPUByName
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Passthru
指定应将 **Microsoft.HyperV.PowerShell.VMRemoteFXPhysicalVideoAdapter** 对象传递给管道，这些对象代表需要被禁用的 RemoteFX 物理视频适配器。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.HyperV POWERShell.VMRemoteFXPhysicalVideoAdapter[]

### System.String[]

## 输出

### 无
默认值

### Microsoft.HyperV POWERShell.VMRemoteFXPhysicalVideoAdapter
如果指定了 **-PassThru** 参数……

## 备注

## 相关链接

