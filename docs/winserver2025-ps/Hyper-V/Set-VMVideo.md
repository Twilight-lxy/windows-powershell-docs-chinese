---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmvideo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMVideo
---

# Set-VMVideo

## 摘要
配置虚拟机的视频设置。

## 语法

### VMName（默认值）
```
Set-VMVideo [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [[-ResolutionType] <ResolutionType>] [[-HorizontalResolution] <UInt16>]
 [[-VerticalResolution] <UInt16>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Set-VMVideo [-VM] <VirtualMachine[]> [[-ResolutionType] <ResolutionType>] [[-HorizontalResolution] <UInt16>]
 [[-VerticalResolution] <UInt16>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMVideo
```
Set-VMVideo [-VMVideo] <VMVideo[]> [[-ResolutionType] <ResolutionType>] [[-HorizontalResolution] <UInt16>]
 [[-VerticalResolution] <UInt16>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMVideo` cmdlet 用于配置虚拟机的视频设置。

## 示例

#### 示例 1：为虚拟机显示器设置分辨率
```
PS C:\> Set-VMVideo -VMName "VM06" -HorizontalResolution 1920 -VerticalResolution 1200
```

该命令将名为VM06的虚拟机的视频分辨率设置为1920x1200。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。您可以输入一个计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个或多个运行此 cmdlet 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行指定。默认值为本地计算机。可以使用 “localhost” 或点（.）来明确表示本地计算机。

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

### -HorizontalResolution
指定虚拟机显示器的水平分辨率。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
表示该cmdlet会返回其所修改的`Microsoft.HyperV.PowerShell.VMVideo`对象。

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

### -ResolutionType
指定虚拟机显示器的分辨率类型。该参数的可接受值包括：

- Maximum.
The input HorizontalResolution * VerticalResolution is the maximum supported resolution.
All standard resolutions smaller than HorizontalResolution * VerticalResolution are also supported.
- Single.
The input HorizontalResolution * VerticalResolution is the only supported resolution.
- Default.
The supported resolutions are those in the list of standard resolutions.
Input HorizontalResolution * VerticalResolution is ignored.

```yaml
Type: ResolutionType
Parameter Sets: (All)
Aliases:
Accepted values: Maximum, Single, Default

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定一个虚拟机数组，该cmdlet将为此数组中的虚拟机配置视频设置。要获取一个**VirtualMachine**对象，请使用**Get-VM** cmdlet。

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

### -VMName
指定一个虚拟机名称数组，该cmdlet将针对这些虚拟机配置视频设置。

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

### -VMVideo
指定一个虚拟机视频设置数组，该数组将由此cmdlet进行配置。若要获取一个**VMVideo**对象，请使用**Get-VMVideo** cmdlet。

```yaml
Type: VMVideo[]
Parameter Sets: VMVideo
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VerticalResolution
指定虚拟机显示器的垂直分辨率。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
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
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMVideo
如果指定了 **Passthru** 参数，此 cmdlet 会返回一个 **VirtualMachine** 对象。

## 备注

## 相关链接

[Get-VMVideo](./Get-VMVideo.md)

[Get-VM](./Get-VM.md)

