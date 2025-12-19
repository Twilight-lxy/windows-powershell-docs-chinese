---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmswitchextensionswitchfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMSwitchExtensionSwitchFeature
---

# Add-VMSwitchExtensionSwitchFeature

## 摘要
为虚拟交换机添加扩展功能。

## 语法

### SwitchName
```
Add-VMSwitchExtensionSwitchFeature [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] -VMSwitchExtensionFeature <VMSwitchExtensionSwitchFeature[]>
 [-SwitchName] <String[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchObject
```
Add-VMSwitchExtensionSwitchFeature -VMSwitchExtensionFeature <VMSwitchExtensionSwitchFeature[]>
 [-VMSwitch] <VMSwitch[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-VMSwitchExtensionSwitchFeature` cmdlet 可将虚拟交换机扩展程序所支持的某个功能添加到虚拟交换机中。

## 示例

### 示例 1
```
PS C:\> $feature = Get-VMSwitchExtensionSwitchFeature -FeatureName "Ethernet Switch BandwidthSettings"
PS C:\> $feature.SettingData.默认值FlowReservation = 300000000
PS C:\> Add-VMSwitchExtensionSwitchFeature "External" -VMSwitchExtensionSwitchFeature $feature
```

为虚拟交换机“External”添加了一项新功能。

## 参数

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: SwitchName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
用于指定一个或多个Hyper-V主机，该虚拟交换机上的某个功能将被添加到这些主机上。允许使用NetBIOS名称、IP地址或完全限定域名作为主机标识。默认值是本地计算机；可以使用“localhost”或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: SwitchName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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
Parameter Sets: SwitchName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定一个对象将被传递到管道中，该对象代表要添加的特征。

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

### -SwitchName
指定要添加该功能的虚拟交换机的名称。

```yaml
Type: String[]
Parameter Sets: SwitchName
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMSwitch
指定要添加该功能的虚拟交换机。

```yaml
Type: VMSwitch[]
Parameter Sets: SwitchObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMSwitchExtensionFeature
指定要添加到虚拟交换机中的功能。

```yaml
Type: VMSwitchExtensionSwitchFeature[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生的后果。但实际上，这个cmdlet并没有被执行。

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

### Microsoft.HyperV.PowerShell.VMSwitchExtensionSwitchFeature
如果指定了 **-PassThru**，

## 备注

## 相关链接

