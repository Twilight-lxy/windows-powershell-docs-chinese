---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/disconnect-vmnetworkadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disconnect-VMNetworkAdapter
---

# 断开虚拟机网络适配器的连接

## 摘要
断开虚拟网络适配器与虚拟交换机或以太网资源池的连接。

## 语法

### 名称（默认值）
```
Disconnect-VMNetworkAdapter [-VMName] <String[]> [[-Name] <String[]>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### Obj
```
Disconnect-VMNetworkAdapter [-VMNetworkAdapter] <VMNetworkAdapter[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Disconnect-VMNetworkAdapter` cmdlet 用于将虚拟网络适配器从虚拟交换机或以太网资源池中断开连接。

## 示例

### 示例 1
```
PS C:\> Disconnect-VMNetworkAdapter -VMNetworkAdapter Test1
```

断开虚拟网络适配器Test1的连接。

### 示例 2
```
PS C:\> Get-VMNetworkAdapter -VMName * | Where-Object {$_.SwitchName -eq 'InternetAccess'} | Disconnect-VMNetworkAdapter
```

断开本地服务器上所有运行Hyper-V的虚拟机中，SwitchName为“InternetAccess”的所有虚拟网络适配器的连接。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于断开虚拟网络适配器连接的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行指定。默认值是本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: Name
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
Parameter Sets: Name
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要断开的虚拟网络适配器的名称。

```yaml
Type: String[]
Parameter Sets: Name
Aliases: VMNetworkAdapterName

Required: False
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 `Microsoft.HyperV.PowerShell.VMNetworkAdapter` 对象传递给管道，该对象代表要断开的虚拟网络适配器。

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

### -VMName
指定要断开虚拟网络适配器连接的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMNetworkAdapter
指定要断开的虚拟网络适配器。

```yaml
Type: VMNetworkAdapter[]
Parameter Sets: Obj
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
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

### Microsoft.HyperV.PowerShell.VMNetworkAdapter
如果指定了 **-PassThru**。

## 备注

## 相关链接

