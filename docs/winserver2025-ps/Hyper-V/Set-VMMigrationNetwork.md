---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmmigrationnetwork?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMMigrationNetwork
---

# Set-VMMigrationNetwork

## 摘要
设置迁移网络的子网、子网掩码和/或优先级。

## 语法

### ComputerName（默认值）
```
Set-VMMigrationNetwork [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-Subnet] <String>
 [[-NewSubnet] <String>] [-NewPriority <UInt32>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### CimSession
```
Set-VMMigrationNetwork [-CimSession <CimSession[]>] [-Subnet] <String> [[-NewSubnet] <String>]
 [-NewPriority <UInt32>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMMigrationNetwork` cmdlet 用于设置迁移网络的子网、子网掩码和/或优先级。

## 示例

### 示例 1
```
PS C:\> Set-VMMigrationNetwork 192.168.10.1 192.168.10.3
```

这个示例用于在迁移网络中修改一个IPv4地址。

### 示例 2
```
PS C:\> Set-VMMigrationNetwork 192.168.10.* 192.168.10.3
```

这个示例会修改在使用通配符选定的迁移网络中的IPv4地址。

### 示例 3
```
PS C:\> Set-VMMigrationNetwork 2001:836c:6456:1c99::/64 -NewPriority 12
```

这个示例将迁移网络的优先级设置为12。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: CimSession
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于运行此 cmdlet 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全合格的域名进行识别。默认值为本地计算机。可以通过使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: ComputerName
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
Parameter Sets: ComputerName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewPriority
指定虚拟机迁移网络的新优先级。多个网络可以具有相同的优先级。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewSubnet
指定一个字符串，该字符串表示要设置在迁移网络上的新子网值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 **Microsoft.HyperV POWERShel.MigrationNetwork** 对象传递给管道，该对象代表要配置的迁移网络。

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

### -Subnet
指定一个字符串，该字符串代表一个 IPv4 或 IPv6 子网掩码，用于标识需要设置属性的迁移网络。允许使用通配符。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.MigrationNetwork
如果指定了 **-PassThru** 参数的话……

## 备注

## 相关链接

