---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Test-LogicalNetworkSupportsJumboPacket.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/test-logicalnetworksupportsjumbopacket?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-LogicalNetworkSupportsJumboPacket
---

# 测试逻辑网络是否支持大尺寸数据包（Jumbo Packet）

## 摘要
测试是否可以在两个节点之间发送一个较大的数据包（即“jumbo packet”）。

## 语法

```
Test-LogicalNetworkSupportsJumboPacket [-SourceHost] <String> [-DestinationHost] <String>
 [[-SourceHostCreds] <PSCredential>] [[-DestinationHostCreds] <PSCredential>] [<CommonParameters>]
```

## 描述
`Test-LogicalNetworkSupportsJumboPacket` 这个 cmdlet 用于测试两个节点之间是否可以发送 jumbo 数据包。

## 示例

### 示例 1：测试一个大型数据包
```
PS C:\> $cred = Get-Credential
Test-LogicalNetworkSupportsJumboPacket -SourceHost "localhost" -SourceHostCreds $cred -DestinationHost "1.1.1.1" -DestinationHostCreds $cred
```

第一个命令获取用户的凭据信息，然后将其存储在 `$cred` 变量中。

第二个命令用于测试在指定的源主机和目标主机之间传输的一个大型数据包（即“jumbo packet”）。

## 参数

### -DestinationHost
指定目标 IP 地址或完全限定域名（FQDN）。

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

### -DestinationHostCreds
指定要在目标主机上使用的凭据。

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

### -SourceHost
指定源IP地址或FQDN。

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

### -SourceHostCreds
指定要在源主机上使用的凭据。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

