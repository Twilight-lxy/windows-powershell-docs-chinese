---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/test-vmnetworkadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-VMNetworkAdapter
---

# 测试虚拟机网络适配器（Test-VMNetworkAdapter）

## 摘要
测试虚拟机之间的连接性。

## 语法

### VMName（默认值）
```
Test-VMNetworkAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String> [-Name <String>] [-Sender] [-Receiver] -SenderIPAddress <String>
 -ReceiverIPAddress <String> [-NextHopMacAddress <String>] [-IsolationId <Int32>] -SequenceNumber <Int32>
 [-PayloadSize <Int32>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ResourceObject
```
Test-VMNetworkAdapter [-VMNetworkAdapter] <VMNetworkAdapter> [-Sender] [-Receiver] -SenderIPAddress <String>
 -ReceiverIPAddress <String> [-NextHopMacAddress <String>] [-IsolationId <Int32>] -SequenceNumber <Int32>
 [-PayloadSize <Int32>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Test-VMNetworkAdapter [-VM] <VirtualMachine> [-Name <String>] [-Sender] [-Receiver] -SenderIPAddress <String>
 -ReceiverIPAddress <String> [-NextHopMacAddress <String>] [-IsolationId <Int32>] -SequenceNumber <Int32>
 [-PayloadSize <Int32>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Test-VMNetworkAdapter` cmdlet 通过使用互联网控制消息协议（ICMP）Ping 数据包来测试虚拟机之间的连接性。Ping 通过发送 ICMP 回显请求消息来验证与另一台 TCP/IP 计算机的 IP 级别连接性。

## 示例

### 示例 1：测试连接性
```
PS C:\> Test-VMNetworkAdapter -VMName "ContosoVM01" -Receiver -SenderIPAddress "10.20.20.5" -ReceiverIPAddress "10.20.20.6" -VMNetworkAdapterName "ContosoNic01"
```

此命令通过使用名为 ContosoNic01 的虚拟网络适配器来测试连接性。该命令的目标是接收方虚拟机。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个或多个用于运行此cmdlet的Hyper-V主机。允许使用NetBIOS名称、IP地址和完全限定域名作为主机标识。默认值为本地计算机。可以使用`localhost`或点（.`）来明确表示本地计算机。

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

### -IsolationId
指定一个虚拟子网的ID。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定虚拟机的名称。

```yaml
Type: String
Parameter Sets: VMName, VMObject
Aliases: VMNetworkAdapterName

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NextHopMacAddress
为非Hyper-V网络虚拟化配置指定了下一跳VM所需的MAC地址。

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

### -Passthru
返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -PayloadSize


```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Receiver
表示该cmdlet是针对接收方虚拟机运行的。

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

### -ReceiverIPAddress
指定接收方虚拟机的IP地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Sender
表示该cmdlet的目标是发送邮件的虚拟机。

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

### -SenderIPAddress
指定发送方虚拟机的IP地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SequenceNumber
指定用于生成 ICMP Ping 数据包的序列编号。默认值为 100。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
用于指定一台虚拟机。该cmdlet会测试属于您所指定的这些虚拟机的适配器的连接性（即检查它们是否能够正常通信）。

```yaml
Type: VirtualMachine
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定虚拟机的名称。

```yaml
Type: String
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapter
将虚拟机网络适配器指定为一个 **VMNetworkAdapterBase** 对象。此 cmdlet 会测试您所指定的这些适配器的连接性。若要获取网络适配器，请使用 **Get-VMNetworkAdapter** cmdlet。

```yaml
Type: VMNetworkAdapter
Parameter Sets: ResourceObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMNetworkAdapterConnectionTestResult

## 备注

## 相关链接

[添加虚拟机网络适配器](./Add-VMNetworkAdapter.md)

[Connect-VMNetworkAdapter](./Connect-VMNetworkAdapter.md)

[断开虚拟机网络适配器的连接](./Disconnect-VMNetworkAdapter.md)

[Get-VMNetworkAdapter](./Get-VMNetworkAdapter.md)

[Remove-VMNetworkAdapter](./Remove-VMNetworkAdapter.md)

[ Rename-VMNetworkAdapter](./Rename-VMNetworkAdapter.md)

[Set-VMNetworkAdapter](./Set-VMNetworkAdapter.md)

