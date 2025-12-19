---
description: 使用这个主题来借助 Windows PowerShell 帮助管理 Windows 和 Windows Server 技术。
external help file: Debug-VirtualMachineQueueOperation.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/debug-virtualmachinequeueoperation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Debug-VirtualMachineQueueOperation
---

# 调试虚拟机队列操作（Debug-VirtualMachineQueueOperation）

## 摘要
调试VMQ/VMMQ流量。

## 语法

```
Debug-VirtualMachineQueueOperation [[-HostName] <String>] [[-MgmtIp] <String>] [[-Creds] <PSCredential>]
 [-VMName] <String> [-VMNetworkAdapterName] <String> [[-SampleCount] <UInt32>] [<CommonParameters>]
```

## 描述
`Debug-VirtualMachineQueueOperation` cmdlet 用于分析虚拟机队列（VMQ）和 VMMQ 的通信流量。您可以使用此 cmdlet 来判断 VMQ/VMMQ 是否导致吞吐量下降，或者是否导致了某些核心的高利用率。

## 示例

### 示例 1：在远程计算机上调试 VMMQ
```
PS C:\> $Cred = Get-Credential
PS C:\> Debug-VirtualMachineQueueOperation -HostName "NCHost.corp.com" -MgmtIp "10.123.176.108" -Creds $Cred -VMName "MuxVM" -VMNetworkAdapterName "Ethernet"
```

第一个命令获取当前用户的凭据信息，然后将这些信息存储在 `$Cred` 变量中。

第二个命令用于获取远程计算机上VMMQ的调试信息。

### 示例 2：在本地主机上调试 VMMQ
```
PS C:\> $Cred = Get-Credential
PS C:\> Debug-VirtualMachineQueueOperation -VMName "MuxVM" -VMNetworkAdapterName "Ethernet" -SampleCount 90
```

第一个命令获取当前用户的凭据信息，然后将这些信息存储在 `$Cred` 变量中。

第二个命令用于获取本地主机上VMMQ的调试信息。

## 参数

### -Creds
指定用于连接到远程主机的凭据。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HostName
指定用于运行诊断程序的远程主机。

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

### -MgmtIp
指定远程主机的管理IP地址。

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

### -SampleCount
指定用于分析网络流量的秒数。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMName
指定要分析的虚拟机的名称。

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

### -VMNetworkAdapterName
指定要分析的虚拟机网络适配器的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

