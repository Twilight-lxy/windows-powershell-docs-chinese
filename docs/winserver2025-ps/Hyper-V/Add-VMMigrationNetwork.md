---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmmigrationnetwork?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMMigrationNetwork
---

# Add-VMMigrationNetwork

## 摘要
为虚拟机的迁移添加网络配置。

## 语法

```
Add-VMMigrationNetwork [-CimSession <CimSession[]>] [-Subnet] <String> [[-Priority] <UInt32>] [-Passthru]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-VMMigrationNetwork` 这个 cmdlet 用于为一个或多个虚拟机主机添加一个用于虚拟机迁移的网络。

## 示例

### 示例 1
```
PS C:\> Add-VMMigrationNetwork 192.168.0.1
```

这个示例将一个IPv4地址添加为本地Hyper-V主机上的实时迁移网络。

### 示例 2
```
PS C:\> Add-VMMigrationNetwork 192.168.10.0/24
```

这个示例通过使用子网掩码，在本地 Hyper-V 主机上添加了一个 IPv4 地址范围，作为可能的实时迁移网络。

### 示例 3
```
PS C:\> Add-VMMigrationNetwork 2001:836c:6456:1c99::/32
```

这个示例通过添加子网掩码，将一个 IPv6 地址范围添加为本地 Hyper-V 主机上可能的实时迁移网络。

### 示例 4
```
PS C:\> Add-VMMigrationNetwork 2001:836c:6456:1c99::/64 -Priority 8
```

此示例通过使用子网掩码，并将该网络指定为较低优先级，将一个 IPv6 地址范围添加为本地 Hyper-V 主机上可能的动态迁移网络。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于添加网络以便进行虚拟机迁移的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址和完全限定域名。默认值是本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 `Microsoft.HyperV.PowerShell.MigrationNetwork` 对象传递给管道，该对象代表用于虚拟机迁移的网络。

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

### -Priority
指定用于虚拟机迁移的网络的优先级。多个网络可以具有相同的优先级。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Subnet
指定一个字符串，该字符串表示IPv4或IPv6子网掩码，用于标识虚拟机迁移时要添加的网络。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.MigrationNetwork
如果指定了 **-PassThru**，

## 备注

## 相关链接

