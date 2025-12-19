---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmswitchextensionswitchfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMSwitchExtensionSwitchFeature
---

# 移除 VMSwitchExtensionSwitchFeature 功能

## 摘要
从虚拟交换机中移除某个功能。

## 语法

```
Remove-VMSwitchExtensionSwitchFeature -VMSwitchExtensionFeature <VMSwitchExtensionSwitchFeature[]> [-Passthru]
 [-ComputerName <String[]>] [-SwitchName <String[]>] [-VMSwitch <VMSwitch[]>] [-CimSession <CimSession[]>]
 [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-VMSwitchExtensionSwitchFeature` cmdlet 用于从虚拟交换机中删除某个功能。该功能必须已经配置在虚拟交换机上才行。

## 示例

### 示例 1
```
PS C:\> $feature = Get-VMSwitchExtensionSwitchFeature -SwitchName External -FeatureId 3eb2b8e8-4abf-4dbf-9071-16dd47481fbe
PS C:\> Remove-VMSwitchExtensionSwitchFeature External $feature
```

从外部虚拟交换机中删除某个功能。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此 cmdlet 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行标识。默认值是本地计算机。可以使用 `localhost` 或句点（.`）来明确指定本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 `Microsoft.HyperV.PowerShell.VMSwitchExtensionSwitchFeature` 对象传递到管道中，该对象代表需要被删除的功能。

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
指定要从中移除该功能的虚拟交换机的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMSwitch
指定要从哪个虚拟交换机中移除该功能。

```yaml
Type: VMSwitch[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMSwitchExtensionFeature
指定要移除的功能。

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
展示了如果该 cmdlet 被运行会发生什么情况。但实际上该 cmdlet 并没有被运行。

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

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.VMSwitchExtensionSwitchFeature
如果指定了 **-PassThru**。

## 备注

## 相关链接

