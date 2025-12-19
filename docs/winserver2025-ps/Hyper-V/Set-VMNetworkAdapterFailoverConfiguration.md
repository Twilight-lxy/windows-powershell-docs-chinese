---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmnetworkadapterfailoverconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMNetworkAdapterFailoverConfiguration
---

# 设置虚拟机网络适配器的故障转移配置

## 摘要
配置虚拟网络适配器的IP地址，以便在虚拟机发生故障转移时使用该IP地址。

## 语法

### VMName（默认值）
```
Set-VMNetworkAdapterFailoverConfiguration [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String> [-VMNetworkAdapterName <String>] [-IPv4Address <String>]
 [-IPv6Address <String>] [-IPv4SubnetMask <String>] [-IPv6SubnetPrefixLength <Int32>]
 [-IPv4PreferredDNSServer <String>] [-IPv4AlternateDNSServer <String>] [-IPv6PreferredDNSServer <String>]
 [-IPv6AlternateDNSServer <String>] [-IPv4默认值Gateway <String>] [-IPv6默认值Gateway <String>]
 [-ClearFailoverIPv4Settings] [-ClearFailoverIPv6Settings] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ResourceObject
```
Set-VMNetworkAdapterFailoverConfiguration [-VMNetworkAdapter] <VMNetworkAdapter> [-IPv4Address <String>]
 [-IPv6Address <String>] [-IPv4SubnetMask <String>] [-IPv6SubnetPrefixLength <Int32>]
 [-IPv4PreferredDNSServer <String>] [-IPv4AlternateDNSServer <String>] [-IPv6PreferredDNSServer <String>]
 [-IPv6AlternateDNSServer <String>] [-IPv4默认值Gateway <String>] [-IPv6默认值Gateway <String>]
 [-ClearFailoverIPv4Settings] [-ClearFailoverIPv6Settings] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMObject
```
Set-VMNetworkAdapterFailoverConfiguration [-VM] <VirtualMachine> [-VMNetworkAdapterName <String>]
 [-IPv4Address <String>] [-IPv6Address <String>] [-IPv4SubnetMask <String>] [-IPv6SubnetPrefixLength <Int32>]
 [-IPv4PreferredDNSServer <String>] [-IPv4AlternateDNSServer <String>] [-IPv6PreferredDNSServer <String>]
 [-IPv6AlternateDNSServer <String>] [-IPv4默认值Gateway <String>] [-IPv6默认值Gateway <String>]
 [-ClearFailoverIPv4Settings] [-ClearFailoverIPv6Settings] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-VMNetworkAdapterFailoverConfiguration` cmdlet 用于设置虚拟网络适配器的 IP 地址配置，该地址将在虚拟机发生故障转移时被使用。

## 示例

### 示例 1
```
PS C:\> Get-VMNetworkAdapter VM01 NetworkAdapter01 | Set-VMNetworkAdapterFailoverConfiguration -IPv4Address 10.100.1.100 -IPv4SubnetMask 255.255.255.0
```

这个示例为虚拟机VM01上的虚拟网络适配器NetworkAdapter01配置了一个用于故障转移的IPv4地址。

### 示例 2
```
PS C:\> Get-VMNetworkAdapter VM01 NetworkAdapter01 | Set-VMNetworkAdapterFailoverConfiguration -ClearFailoverIPv4Settings
```

这个示例会清除虚拟机VM01所使用的虚拟网络适配器NetworkAdapter01上的当前故障转移（failover）IPv4设置。

### 示例 3
```
PS C:\> Get-VMNetworkAdapter VM01 NetworkAdapter01 | Set-VMNetworkAdapterFailoverConfiguration -Ipv6Address aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaa:aaaa -Ipv6SubnetPrefixLength 12
```

这个示例为虚拟机VM01中的虚拟网络适配器NetworkAdapter01配置了一个IPv6地址以及前缀长度为12的参数。

### 示例 4
```
PS C:\> Get-VMNetworkAdapter VM01 NetworkAdapter01 | Set-VMNetworkAdapterFailoverConfiguration -ClearFailoverIPv6Settings
```

这个示例会清除虚拟机VM01所使用的虚拟网络适配器NetworkAdapter01当前的IPv6故障转移设置。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClearFailoverIPv4Settings
清除已配置的 IPv4 故障转移设置。主虚拟机中配置的 IPv4 地址（无论是静态地址还是动态地址）将被复制虚拟机使用。

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

### -ClearFailoverIPv6Settings
清除已配置的 IPv6 故障转移设置。主虚拟机中配置的 IPv6 地址（无论是静态地址还是动态地址）将被复制虚拟机使用。

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

### -ComputerName
指定一个或多个用于设置虚拟网络适配器IP地址配置的Hyper-V主机。允许使用NetBIOS名称、IP地址和完全限定域名作为主机标识。默认值为本地计算机；可以使用`localhost`或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv4Address
指定要设置在 `VMNetworkAdapter` 上的 IPv4 地址，以便在虚拟机发生故障转移时使用。在指定此参数的同时，还必须指定 `IPv4SubnetMask` 参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv4AlternateDNSServer
指定要在 VMNetworkAdapter 上设置的 IPv4 备用 DNS 服务器，以便在虚拟机发生故障转移时使用。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv4默认值Gateway
指定要设置在 `VMNetworkAdapter` 上的 IPv4 默认网关，以便在虚拟机发生故障转移时使用该网关。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv4PreferredDNSServer
指定要在 `VMNetworkAdapter` 上设置的 IPv4 首选 DNS 服务器，以便在虚拟机发生故障转移时使用。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv4SubnetMask
指定要设置在 `VMNetworkAdapter` 上的 IPv4 子网掩码，以便在虚拟机故障转移时使用。在指定此参数时，必须同时指定 `IPv4Address` 参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv6Address
指定要设置在 `VMNetworkAdapter` 上的 IPv6 地址，以便在虚拟机发生故障转移时使用该地址。在指定此参数时，必须同时指定 `IPv6SubnetPrefixLength` 参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv6AlternateDNSServer
指定要在 `VMNetworkAdapter` 上设置的 IPv6 备用 DNS 服务器，以便在虚拟机发生故障转移时使用。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv6默认值Gateway
指定要设置在 `VMNetworkAdapter` 上的 IPv6 默认网关，以便在虚拟机发生故障转移时使用。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv6PreferredDNSServer
指定要在 `VMNetworkAdapter` 上设置的 IPv6 首选 DNS 服务器，以便在虚拟机发生故障转移时使用。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv6SubnetPrefixLength
指定要设置在 `VMNetworkAdapter` 上的 IPv6 子网前缀长度，以便在虚拟机故障转移时使用。在指定此参数时，必须同时指定 `IPv6Address` 参数。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定要将一个 **Microsoft.HyperV.PowerShell.VMNetworkAdapterFailoverConfiguration** 对象传递给管道，该对象代表要设置的 IP 地址配置。

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

### -VM
指定您想要为其配置IP地址的虚拟机。

```yaml
Type: VirtualMachine
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定您想要配置IP地址的虚拟机的友好名称。

```yaml
Type: String
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapter
指定您想要配置IP地址的虚拟网络适配器。

```yaml
Type: VMNetworkAdapter
Parameter Sets: ResourceObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapterName
指定要为其设置 IP 地址的虚拟网络适配器的名称。

```yaml
Type: String
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.VMNetworkAdapterFailoverConfiguration
如果指定了 `-PassThru`。

## 备注

## 相关链接

