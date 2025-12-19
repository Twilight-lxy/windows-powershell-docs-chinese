---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/connect-vmnetworkadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Connect-VMNetworkAdapter
---

# 连接虚拟机网络适配器

## 摘要
将虚拟网络适配器连接到虚拟交换机。

## 语法

### Name_SwitchName（默认值）
```
Connect-VMNetworkAdapter [[-Name] <String[]>] [-SwitchName] <String> [-Passthru] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-VMName] <String[]> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### Object_SwitchName
```
Connect-VMNetworkAdapter [-VMNetworkAdapter] <VMNetworkAdapter[]> [-SwitchName] <String> [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### Object_SwitchObject
```
Connect-VMNetworkAdapter [-VMNetworkAdapter] <VMNetworkAdapter[]> [-VMSwitch] <VMSwitch> [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### Object_UseAutomaticConnection
```
Connect-VMNetworkAdapter [-VMNetworkAdapter] <VMNetworkAdapter[]> [-UseAutomaticConnection] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### Name_SwitchObject
```
Connect-VMNetworkAdapter [[-Name] <String[]>] [-VMSwitch] <VMSwitch> [-Passthru] [-VMName] <String[]> [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 名称：UseAutomaticConnection
```
Connect-VMNetworkAdapter [[-Name] <String[]>] [-UseAutomaticConnection] [-Passthru]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-VMName] <String[]>
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Connect-VMNetworkAdapter` cmdlet 用于将虚拟网络适配器连接到虚拟交换机。

## 示例

### 示例 1
```
PS C:\> Connect-VMNetworkAdapter -VMName Test1,Test2 -Name Internet -SwitchName InternetAccess
```

将名为“Internet”的虚拟网络适配器连接到虚拟机Test1和Test2中，并将这些虚拟网络适配器连接到虚拟交换机“InternetAccess”。

### 示例 2
```
PS C:\> Get-VMNetworkAdapter -VMName Test1 | Connect-VMNetworkAdapter -SwitchName InternetAccess
```

将虚拟机Test1中的虚拟网络适配器连接到虚拟交换机InternetAccess。

### 示例 3
```
PS C:\> Get-VMSwitch InternetAccess | Connect-VMNetworkAdapter -VMName Test1
```

将虚拟机Test1中的虚拟网络适配器连接到switch InternetAccess上。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称或会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: Name_SwitchName, Name_UseAutomaticConnection
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个虚拟机主机，以便将虚拟网络适配器连接到这些主机上。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行连接。默认值为本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: Name_SwitchName, Name_UseAutomaticConnection
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前会提示您进行确认。

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
Parameter Sets: Name_SwitchName, Name_UseAutomaticConnection
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要连接的虚拟网络适配器的名称。

```yaml
Type: String[]
Parameter Sets: Name_SwitchName, Name_SwitchObject, Name_UseAutomaticConnection
Aliases: VMNetworkAdapterName

Required: False
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定要将一个 **Microsoft.HyperV POWERShell.VMNetworkAdapter** 对象传递到管道中，该对象代表要连接的虚拟网络适配器。

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
指定虚拟网络适配器要连接的虚拟交换机的名称。

```yaml
Type: String
Parameter Sets: Name_SwitchName, Object_SwitchName
Aliases:

Required: True
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseAutomaticConnection
指定网络适配器应连接到资源池中的任意一个虚拟交换机，而不是某个特定的虚拟交换机。

```yaml
Type: SwitchParameter
Parameter Sets: Object_UseAutomaticConnection, Name_UseAutomaticConnection
Aliases:

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMName
指定要连接网络适配器的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: Name_SwitchName, Name_SwitchObject, Name_UseAutomaticConnection
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMNetworkAdapter
指定要连接的虚拟网络适配器。

```yaml
Type: VMNetworkAdapter[]
Parameter Sets: Object_SwitchName, Object_SwitchObject, Object_UseAutomaticConnection
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMSwitch
指定虚拟网络适配器应连接的虚拟交换机。

```yaml
Type: VMSwitch
Parameter Sets: Object_SwitchObject, Name_SwitchObject
Aliases:

Required: True
Position: 2
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.VMNetworkAdapter
如果指定了 **-PassThru** 参数的话……

## 备注

## 相关链接

