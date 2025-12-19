---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: TestDtc.psm1-help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/test-dtc?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-Dtc
---

# Test-Dtc

## 摘要
测试两台计算机是否可以参与联网交易。

## 语法

```
Test-Dtc [[-LocalComputerName] <String>] [[-RemoteComputerName] <String>] [[-ResourceManagerPort] <Int32>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Test-Dtc` cmdlet 用于检测两台计算机是否可以参与网络交易。该 cmdlet 执行以下测试：

- Checks whether the required firewall rules are enabled.
- Checks whether the Microsoft Distributed Transaction Coordinator (MSDTC) network security settings are correctly configured for network transactions.
- Checks whether the two computers can ping each other.
- Checks whether a transaction can be propagated between the two computers.

要运行此 cmdlet，您必须首先使用 Netsh 工具在两台计算机上启用分布式事务协调器（Distributed Transaction Coordinator）的防火墙规则，请运行以下命令：

请帮我将以下命令转换为中文：  
`netsh advfirewall firewall set rule group="Distributed Transaction Coordinator" new enable=yes`

有关更多信息，请参阅[Netsh命令语法、上下文和格式化](/windows-server/networking/technologies/netsh/netsh-contexts)。

要使用 PowerShell 启用该规则，请运行以下命令：

`Enable-NetFirewallRule -DisplayGroup "Distributed Transaction Coordinator"`

## 示例

### 示例 1：在本地计算机上测试 MSDTC
```
PS C:\> Test-Dtc -LocalComputerName "$env:COMPUTERNAME" -Verbose
VERBOSE: ": Firewall rule for "RPC Endpoint Mapper" is enabled."
VERBOSE: ": Firewall rule for "DTC incoming connections" is enabled."
VERBOSE: ": Firewall rule for "DTC outgoing connections" is enabled."
VERBOSE: Contoso089: AuthenticationLevel: Mutual
VERBOSE: Contoso089: InboundTransactionsEnabled: True
VERBOSE: Contoso089: OutboundTransactionsEnabled: True
VERBOSE: Contoso089: RemoteClientAccessEnabled: False
VERBOSE: Contoso089: RemoteAdministrationAccessEnabled: True
VERBOSE: Contoso089: XATransactionsEnabled: True
VERBOSE: Contoso089: LUTransactionsEnabled: True
```

此命令用于测试本地计算机上的 MSDTC（Microsoft Distributed Transaction Coordinator）。

### 示例 2：在本地计算机和远程计算机上测试 MSDTC
```
PS C:\> Test-Dtc -LocalComputerName "$env:COMPUTERNAME" -RemoteComputerName "Contoso075" -ResourceManagerPort 17100 -Verbose
VERBOSE: ": Firewall rule for "RPC Endpoint Mapper" is enabled."
VERBOSE: ": Firewall rule for "DTC incoming connections" is enabled."
VERBOSE: ": Firewall rule for "DTC outgoing connections" is enabled."
VERBOSE: Contoso089: AuthenticationLevel: Mutual
VERBOSE: Contoso089: InboundTransactionsEnabled: True
VERBOSE: Contoso089: OutboundTransactionsEnabled: True
VERBOSE: Contoso089: RemoteClientAccessEnabled: False
VERBOSE: Contoso089: RemoteAdministrationAccessEnabled: True
VERBOSE: Contoso089: XATransactionsEnabled: True
VERBOSE: Contoso089: LUTransactionsEnabled: True
VERBOSE: Exporting cmdlet 'Get-CimInstance'.
VERBOSE: Exporting cmdlet 'Get-CimSession'.
VERBOSE: Exporting cmdlet 'New-CimSession'.
VERBOSE: Exporting cmdlet 'New-CimSessionOption'.
VERBOSE: Exporting cmdlet 'Remove-CimSession'.
VERBOSE: Exporting cmdlet 'Get-CimAssociatedInstance'.
VERBOSE: Exporting cmdlet 'Get-CimClass'.
VERBOSE: Exporting cmdlet 'Invoke-CimMethod'.
VERBOSE: Exporting cmdlet 'New-CimInstance'.
VERBOSE: Exporting cmdlet 'Register-CimIndicationEvent'.
VERBOSE: Exporting cmdlet 'Remove-CimInstance'.
VERBOSE: Exporting cmdlet 'Set-CimInstance'.
VERBOSE: Importing cmdlet 'Get-CimAssociatedInstance'.
VERBOSE: Importing cmdlet 'Get-CimClass'.
VERBOSE: Importing cmdlet 'Get-CimInstance'.
VERBOSE: Importing cmdlet 'Get-CimSession'.
VERBOSE: Importing cmdlet 'Invoke-CimMethod'.
VERBOSE: Importing cmdlet 'New-CimInstance'.
VERBOSE: Importing cmdlet 'New-CimSession'.
VERBOSE: Importing cmdlet 'New-CimSessionOption'.
VERBOSE: Importing cmdlet 'Register-CimIndicationEvent'. "
VERBOSE: Importing cmdlet 'Remove-CimInstance'.
VERBOSE: Importing cmdlet 'Remove-CimSession'.
VERBOSE: Importing cmdlet 'Set-CimInstance'.
VERBOSE: "Contoso075 Operating System Version: 6.2.8179."
VERBOSE: "Contoso075: Firewall rule for "RPC Endpoint Mapper" is enabled."
VERBOSE: "Contoso075: Firewall rule for "DTC incoming connections" is enabled."
VERBOSE: "Contoso075: Firewall rule for "DTC outgoing connections" is enabled."
VERBOSE: Contoso075: AuthenticationLevel: Mutual
VERBOSE: Contoso075: InboundTransactionsEnabled: True
VERBOSE: Contoso075: OutboundTransactionsEnabled: True
VERBOSE: Contoso075: RemoteClientAccessEnabled: False
VERBOSE: Contoso075: RemoteAdministrationAccessEnabled: True
VERBOSE: Contoso075: XATransactionsEnabled: True
VERBOSE: Contoso075: LUTransactionsEnabled: True
VERBOSE: "Pinging computer Contoso089 from Contoso075 succeeded."
VERBOSE: "Pinging computer Contoso075 from Contoso089 succeeded."
VERBOSE: Contoso089: OleTx: a9f3f4c0-cc24-4f34-bfc3-6b6d819dab84
VERBOSE: Contoso075: OleTx: 94a24f8a-3040-4fa2-9f27-833ffb2037bc
VERBOSE: Contoso089: XA: f35da6a2-26d2-4d14-98e6-1a8feea41bc8
VERBOSE: Contoso075: XA: 15614187-293b-4a39-92ce-6740b1ea526c
VERBOSE: Contoso089: UIS: 7f8d8ad0-7096-47fd-9aab-5d561852c93b
VERBOSE: Contoso075: UIS: e1a97aaa-003c-4b61-a978-8601e8438d5f
VERBOSE: "This diagnostic test will attempt to carry out a transaction propagation between Contoso089 and
Contoso075. It requires that a TCP port is opened on Contoso089 so that a Test Resource Manager can participate
in network transactions." "You have specified 17100 as the 'ResourceManagerPort'." "Please open port 17100 in the
firewall to proceed with the test."
VERBOSE: "Test resource manager started."
VERBOSE: "A new PSSession to Contoso075 created."
VERBOSE: "Transaction propagated from Contoso089 to Contoso075 using PULL propagation."
VERBOSE: "Transaction propagated from Contoso089 to Contoso075 using PUSH propagation."
VERBOSE: "Test Resource Manager Verbose Log:"
VERBOSE: DtcDiagRM:17100 is now listening at http://Contoso089:17100/DTCDiagRM.
VERBOSE: Resolution of IP address to hostname failed, just using IP address: 2001:0db8:2a:1006:c041:b365:30de:b2e3.
VERBOSE: DtcDiagRM:17100 received a request for PropagationToken from 2001:0db8:2a:1006:c041:b365:30de:b2e3.
VERBOSE: DtcDiagRM:17100 created Transaction 4a546251-db38-4fe9-91bb-22e532deb68b.
VERBOSE: DtcDiagRM:17100 obtained a PropagationToken for Transaction 4a546251-db38-4fe9-91bb-22e532deb68b from DTC.
VERBOSE: Resolution of IP address to hostname failed, just using IP address: 2001:0db8:2a:1006:c041:b365:30de:b2e3.
VERBOSE: ResourceManager DtcDiagRM:17100 received a request for an ExportCookie from
2001:0db8:2a:1006:c041:b365:30de:b2e3.
VERBOSE: DtcDiagRM:17100 created Transaction cc088777-03c6-43cc-83f6-06539b83e1fd.
VERBOSE: DtcDiagRM:17100 obtained an ExportCookie for Transaction cc088777-03c6-43cc-83f6-06539b83e1fd from DTC.
VERBOSE: Resource Manager DtcDiagRM:17100 - 24aeb805-7ef5-4410-9a19-f5fddf93c4d2 is removed.
```

这个命令用于测试本地计算机以及名为Contoso075的计算机。该命令指定了一个资源管理器端口。

### 示例 3：在阻止入站交易的本地计算机上测试 MSDTC
```
PS C:\> Test-Dtc -LocalComputerName "$env:COMPUTERNAME" -RemoteComputerName "Contoso075" -ResourceManagerPort 17100 -Verbose
VERBOSE: ": Firewall rule for "RPC Endpoint Mapper" is enabled."
VERBOSE: ": Firewall rule for "DTC incoming connections" is enabled."
VERBOSE: ": Firewall rule for "DTC outgoing connections" is enabled."
VERBOSE: Contoso089: AuthenticationLevel: Mutual
VERBOSE: Contoso089: InboundTransactionsEnabled: False
WARNING: "Contoso089: Inbound transactions are not allowed and this computer cannot participate in network transactions."
VERBOSE: Contoso089: OutboundTransactionsEnabled: True
VERBOSE: Contoso089: RemoteClientAccessEnabled: False
VERBOSE: Contoso089: RemoteAdministrationAccessEnabled: True
VERBOSE: Contoso089: XATransactionsEnabled: True
VERBOSE: Contoso089: LUTransactionsEnabled: True
VERBOSE: Operation '' complete.
VERBOSE: "Contoso075 Operating System Version: 6.2.8179."
VERBOSE: "Contoso075: Firewall rule for "RPC Endpoint Mapper" is enabled."
VERBOSE: "Contoso075: Firewall rule for "DTC incoming connections" is enabled."
VERBOSE: "Contoso075: Firewall rule for "DTC outgoing connections" is enabled."
VERBOSE: Contoso075: AuthenticationLevel: Mutual
VERBOSE: Contoso075: InboundTransactionsEnabled: True
VERBOSE: Contoso075: OutboundTransactionsEnabled: True
VERBOSE: Contoso075: RemoteClientAccessEnabled: False
VERBOSE: Contoso075: RemoteAdministrationAccessEnabled: True
VERBOSE: Contoso075: XATransactionsEnabled: True
VERBOSE: Contoso075: LUTransactionsEnabled: True
VERBOSE: "Pinging computer Contoso089 from Contoso075 succeeded."
VERBOSE: "Pinging computer Contoso075 from Contoso089 succeeded."
VERBOSE: Contoso089: OleTx: a9f3f4c0-cc24-4f34-bfc3-6b6d819dab84
VERBOSE: Contoso075: OleTx: 94a24f8a-3040-4fa2-9f27-833ffb2037bc
VERBOSE: Contoso089: XA: f35da6a2-26d2-4d14-98e6-1a8feea41bc8
VERBOSE: Contoso075: XA: 15614187-293b-4a39-92ce-6740b1ea526c
VERBOSE: Contoso089: UIS: 7f8d8ad0-7096-47fd-9aab-5d561852c93b
VERBOSE: Contoso075: UIS: e1a97aaa-003c-4b61-a978-8601e8438d5f
"DTC security settings and firewall settings should be fixed in order to complete the transactions propagation test."
```

这个命令用于测试本地计算机和名为Contoso075的计算机。测试结果显示，本地计算机不允许接收入站数据传输（即不允许外部计算机向本地计算机发送数据）。

### 示例 4：在阻止出站交易的本地计算机上测试 MSDTC
```
PS C:\> Test-Dtc -LocalComputerName "$env:COMPUTERNAME" -RemoteComputerName "Contoso075" -ResourceManagerPort 17100 -Verbose
VERBOSE: ": Firewall rule for "RPC Endpoint Mapper" is enabled."
VERBOSE: ": Firewall rule for "DTC incoming connections" is enabled."
VERBOSE: ": Firewall rule for "DTC outgoing connections" is enabled."
VERBOSE: Contoso089: AuthenticationLevel: Mutual
VERBOSE: Contoso089: InboundTransactionsEnabled: True
VERBOSE: Contoso089: OutboundTransactionsEnabled: False
WARNING: "Contoso089: Outbound transactions are not allowed and this computer cannot participate in network transactions."
VERBOSE: Contoso089: RemoteClientAccessEnabled: False
VERBOSE: Contoso089: RemoteAdministrationAccessEnabled: True
VERBOSE: Contoso089: XATransactionsEnabled: True
VERBOSE: Contoso089: LUTransactionsEnabled: True
VERBOSE: Operation '' complete.
VERBOSE: "Contoso075 Operating System Version: 6.2.8179."
VERBOSE: "Contoso075: Firewall rule for "RPC Endpoint Mapper" is enabled."
VERBOSE: "Contoso075: Firewall rule for "DTC incoming connections" is enabled."
VERBOSE: "Contoso075: Firewall rule for "DTC outgoing connections" is enabled."
VERBOSE: Contoso075: AuthenticationLevel: Mutual
VERBOSE: Contoso075: InboundTransactionsEnabled: True
VERBOSE: Contoso075: OutboundTransactionsEnabled: True
VERBOSE: Contoso075: RemoteClientAccessEnabled: False
VERBOSE: Contoso075: RemoteAdministrationAccessEnabled: True
VERBOSE: Contoso075: XATransactionsEnabled: True
VERBOSE: Contoso075: LUTransactionsEnabled: True
VERBOSE: "Pinging computer Contoso089 from Contoso075 succeeded."
VERBOSE: "Pinging computer Contoso075 from Contoso089 succeeded."
VERBOSE: Contoso089: OleTx: a9f3f4c0-cc24-4f34-bfc3-6b6d819dab84
VERBOSE: Contoso075: OleTx: 94a24f8a-3040-4fa2-9f27-833ffb2037bc
VERBOSE: Contoso089: XA: f35da6a2-26d2-4d14-98e6-1a8feea41bc8
VERBOSE: Contoso075: XA: 15614187-293b-4a39-92ce-6740b1ea526c
VERBOSE: Contoso089: UIS: 7f8d8ad0-7096-47fd-9aab-5d561852c93b
VERBOSE: Contoso075: UIS: e1a97aaa-003c-4b61-a978-8601e8438d5f
"DTC security settings and firewall settings should be fixed in order to complete the transactions propagation test."
```

此命令用于测试本地计算机以及名为“Contoso075”的计算机。测试结果显示，本地计算机不允许发起出站数据传输（即不允许数据从本地计算机发送到其他计算机）。

## 参数

### -LocalComputerName
指定要测试的本地计算机上MSDTC实例的虚拟服务器名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemoteComputerName
指定用于测试的远程计算机上MSDTC实例的虚拟服务器名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourceManagerPort
指定 MSDTC 诊断资源管理器使用的端口号。如果您不指定值，此 cmdlet 将使用默认值 3002。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-Dtc](./Get-Dtc.md)

[Install-Dtc](./Install-Dtc.md)

[Start-Dtc](./Start-Dtc.md)

[Stop-Dtc](./Stop-Dtc.md)

[卸载 DTC](./Uninstall-Dtc.md)
