---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Test-VirtualNetworkConnection.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/test-virtualnetworkconnection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-VirtualNetworkConnection
---

# 测试虚拟网络连接

## 摘要
测试虚拟网络连接。

## 语法

```
Test-VirtualNetworkConnection [-OperationId] <String> [[-HostName] <String>] [[-MgmtIp] <String>]
 [[-Creds] <PSCredential>] [[-VMName] <String>] [[-VMNetworkAdapterName] <String>]
 [[-VMNetworkAdapterProfileId] <String>] [-IsSender] <Boolean> [-SenderCAIP] <String> [-SenderVSID] <Int32>
 [-ListenerCAIP] <String> [-ListenerVSID] <Int32> [-SequenceNumber] <Int32> [[-PayloadSize] <Int32>]
 [<CommonParameters>]
```

## 描述
`Test-VirtualNetworkConnection` cmdlet 通过在两个客户地址 IP（CAIP）之间发送互联网控制消息协议（ICMP）数据包来测试虚拟网络上的连通性。这两个节点可以位于相同的虚拟子网 ID（VSID）上，也可以共享同一个 VSID。

## 示例

### 示例 1：通过发送数据来测试虚拟网络连接
```
PS C:\> $cred = Get-Credential
PS C:\> Test-VirtualNetworkConnection -OperationId "27" -HostName "host1.corp.com" -MgmtIP "192.10.10.11" -Creds $creds -VMName "TennantVM1" -VMNetworkAdapterName "Tennant1VMAdapter1" -IsSender $True -SenderCAIP "10.123.176.108" -SenderVSID 6001 -ListenerCAIP "10.123.176.108" -ListenerVSID 6001 -SequenceNumber 33 -PayloadSize 1500
```

第一个命令获取当前用户的凭据信息，然后将其存储在 `$cred` 变量中。

第二个命令用于测试指定的虚拟网络连接。

### 示例 2：通过接收数据来测试虚拟网络连接
```
PS C:\> $password = ConvertTo-SecureString -String "password" -AsPlainText -Force
PS C:\> $cred = New-Object PSCredential -ArgumentList (".\administrator", $password)
PS C:\> Test-VirtualNetworkConnection -OperationId "27" -HostName "host2.corp.com" -MgmtIP "192.10.10.12" -Creds $cred -VMName "TennantVM2" -VMNetworkAdapterName "Tennant1VMAdapter2" -SenderCAIP "10.123.176.108" -SenderVSID 6001 -ListenerCAIP "10.123.176.109" -ListenerVSID 6001
```

第一个命令将明文密码转换为一个安全的字符串，然后将其存储在 `$password` 变量中。

第二个命令创建了一个 **PSCredential** 对象，然后将其存储在 `$cred` 变量中。

第三个命令用于测试指定的虚拟网络连接。

## 参数

### -Creds
指定网络控制器所需的凭据。在部署Kerberos系统时需要设置此参数。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HostName
指定用于运行测试的主机的名称。

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

### -IsSender
表示此操作是针对发送者还是接收者。两者中必须各选择一个。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: True
Position: 7
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ListenerCAIP
指定监听器的CAIP（Certification Authority Information Point）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 10
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ListenerVSID
指定用于启动测试的VSID（虚拟站点标识符）。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: True
Position: 11
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MgmtIp
指定用于启动测试的管理主机的 IP 地址。

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

### -OperationId
为测试指定一个唯一的ID。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
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
Position: 13
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SenderCAIP
指定发送方的CAIP（认证机构信息）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 8
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SenderVSID
指定发送方的 VSID（虚拟站点标识符）。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: True
Position: 9
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SequenceNumber
指定要在 ICMP 数据包中使用的序列号。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: True
Position: 12
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMName
指定虚拟机的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMNetworkAdapterName
指定具有所需CAIP配置的虚拟机的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMNetworkAdapterProfileId
指定所需CAIP适配器的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

