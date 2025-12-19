---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: VipReachability.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/test-vipreachability?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-VipReachability
---

# 测试VIP可达性

## 摘要
测试数据接口（DIPs）是否可以被访问/使用。

## 语法

```
Test-VipReachability [[-OperationId] <String>] [-SourceIP] <String> [[-CompartmentId] <String>]
 [-TargetVIP] <String> [-Muxes] <Hashtable[]> [-Dips] <Hashtable[]> [[-SequenceNumber] <Int32>]
 [[-PayloadSize] <Int32>] [<CommonParameters>]
```

## 描述
`Test-VipReachability` cmdlet 用于测试是否可以通过指定的复用器（MUX）访问一系列数据中心 IP 地址（DIP）。

该测试涵盖了与MUX节点的第3层（数据链路层）连接，以及从MUX节点到DIP主机之间的连接。

该测试首先向虚拟IP（VIP）地址发送互联网控制消息协议（ICMP）的回显请求。MUX拦截这些回显请求，并发送看似来自目标VIP的响应。

然后，测试会从MUX主机向提供商网络中的DIP主机发送ICMP回显请求。测试的结果会记录在输出对象中。

## 示例

#### 示例 1：测试 VIP 的可达性
```
PS C:\> for ($mux in $VipHostMapping.MuxList) {
    $secpasswd = ConvertTo-SecureString <plaintext password> -AsPlainText -Force
    $creds = New-Object System.Management.Automation.PSCredential (<username>, $secpasswd)
    $mux.Credentials = $creds
}
PS C:\> for ($dip in $VipHostMapping.DIPHosts) {
    $secpasswd = ConvertTo-SecureString <plaintext password> -AsPlainText -Force
    $creds = New-Object System.Management.Automation.PSCredential (<username>, $secpasswd)
    $dip.HostInfo.Credentials = $creds
}
PS C:\> Test-VIPReachability -OperationId 1 -SourceIP "10.123.176.108" -TargetVIP "10.123.177.110" -Muxes $VipHostMapping.MuxList -Dips $VipHostMapping.DIPHosts
```

第一个命令用于设置要测试的MUX节点所需的凭据信息。

第二个命令用于填充用于测试的DIPs的凭据信息。

最后一个命令用于测试指定MUX和DIP的VIP是否可访问（即是否能够与它们建立通信连接）。

## 参数

### -CompartmentId
指定用于发送 ICMP 回显请求的网络分区的 ID。

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

### -Dips
指定一个用于测试的DIP（数字接口封装）数组。

```yaml
Type: Hashtable[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Muxes
指定一个 MUX（多路复用器）数组，以实现 DIP（数字集成电路）的负载均衡。

```yaml
Type: Hashtable[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OperationId
为该操作指定一个ID。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PayloadSize
指定在 ICMP 消息中传输的有效载荷（payload）的大小。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 7
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SequenceNumber
指定 ICMP 序列号。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SourceIP
指定源节点的IP地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetVIP
指定目标VIP的IP地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

