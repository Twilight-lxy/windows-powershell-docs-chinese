---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/new-vmswitch?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-VMSwitch
---

# 新VMSwitch

## 摘要
在一个或多个虚拟机主机上创建一个新的虚拟交换机。

## 语法

### NetAdapterName（默认值）
```
New-VMSwitch [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> [-AllowManagementOS <Boolean>] -NetAdapterName <String[]> [-Notes <String>]
 [-MinimumBandwidthMode <VMSwitchBandwidthMode>] [-EnableIov <Boolean>] [-EnablePacketDirect <Boolean>]
 [-EnableEmbeddedTeaming <Boolean>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### NetAdapterInterfaceDescription
```
New-VMSwitch [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> [-AllowManagementOS <Boolean>] -NetAdapterInterfaceDescription <String[]> [-Notes <String>]
 [-MinimumBandwidthMode <VMSwitchBandwidthMode>] [-EnableIov <Boolean>] [-EnablePacketDirect <Boolean>]
 [-EnableEmbeddedTeaming <Boolean>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchType
```
New-VMSwitch [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> -SwitchType <VMSwitchType> [-Notes <String>] [-MinimumBandwidthMode <VMSwitchBandwidthMode>]
 [-EnableIov <Boolean>] [-EnablePacketDirect <Boolean>] [-EnableEmbeddedTeaming <Boolean>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
**New-VMSwitch** cmdlet 可以在一个或多个虚拟机主机上创建一个新的虚拟交换机。

## 示例

### 示例 1
```
PS C:\> New-VMSwitch "QoS Switch" -NetAdapterName "Wired Ethernet Connection 3" -MinimumBandwidthMode Weight
```

创建一个新的QoS交换机（switch），该交换机绑定到一个名为“Wired Ethernet Connection 3”的网络适配器，并支持基于权重的最低带宽限制功能。

## 参数

### -AllowManagementOS
指定父分区（即管理操作系统）是否可以访问绑定到要创建的虚拟交换机的物理网卡。

```yaml
Type: Boolean
Parameter Sets: NetAdapterName, NetAdapterInterfaceDescription
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于创建虚拟交换机的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行选择。默认值是本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: PSComputerName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableEmbeddedTeaming
指定此cmdlet是否为虚拟交换机启用组队功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableIov
指定要在要创建的虚拟交换机上启用IO虚拟化功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnablePacketDirect
该参数用于指定此cmdlet是否允许数据包通过虚拟交换机直接传输。默认值为$False。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinimumBandwidthMode
该参数用于指定如何在虚拟交换机上配置最小带宽。允许的值包括：**Absolute**（绝对值）、**Default**（默认值）、**None**（禁用）或**Weight**（基于权重的值）。  

- 如果选择 **Absolute**，最小带宽将以“比特每秒”为单位进行设置。  
- 如果选择 **Weight**，最小带宽将是一个介于 1 到 100 之间的数值。  
- 如果选择 **None**，则虚拟交换机上的最小带宽功能将被禁用，即用户无法在连接到该交换机的任何网络适配器上配置最小带宽。  
- 如果选择 **Default**，当交换机未启用 IOV（Input/Output Virtualization）功能时，系统会自动将最小带宽模式设置为 **Weight**；如果交换机启用了 IOV 功能，则最小带宽模式将被设置为 **None**。

```yaml
Type: VMSwitchBandwidthMode
Parameter Sets: (All)
Aliases:
Accepted values: Default, Weight, Absolute, None

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要创建的交换机的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: SwitchName

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NetAdapterInterfaceDescription
指定要绑定到将要创建的交换机的网络适配器的接口描述。您可以使用 **Get-NetAdapter** cmdlet 来获取网络适配器的接口描述。

```yaml
Type: String[]
Parameter Sets: NetAdapterInterfaceDescription
Aliases: InterfaceDescription

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetAdapterName
指定要绑定到所创建交换机的网络适配器的名称。您可以使用 **Get-NetAdapter** cmdlet 来获取网络适配器的接口描述信息。

```yaml
Type: String[]
Parameter Sets: NetAdapterName
Aliases: InterfaceAlias

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Notes
指定一条注释，用于关联要创建的开关。

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

### -SwitchType
指定要创建的交换机的类型。允许的值是 **Internal** 和 **Private**。如果要创建一个外部虚拟交换机，请指定 **NetAdapterInterfaceDescription** 或 **NetAdapterName** 参数，这两个参数会隐式地将虚拟交换机的类型设置为 External。

```yaml
Type: VMSwitchType
Parameter Sets: SwitchType
Aliases:
Accepted values: Internal, Private

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMSwitch

## 备注

## 相关链接

