---
description: 使用这个主题来借助 Windows PowerShell 帮助管理 Windows 和 Windows Server 技术。
external help file: Get-VipConnectivityInfo.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/get-networkcontrollervipresource?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetworkControllerVipResource
---

# 获取网络控制器VIP资源

## 摘要
获得一份VIP资源。

## 语法

```
Get-NetworkControllerVipResource [[-RestURI] <String>] [[-CertificateThumbprint] <String>]
 [[-Credential] <PSCredential>] [[-Direction] <String>] [-IPAddress] <String> [[-DstPort] <String>]
 [[-Protocol] <String>] [<CommonParameters>]
```

## 描述
`Get-NetworkControllerVipResource` cmdlet 可以获取指定虚拟 IP 地址（VIP）资源的相关信息，例如多路复用器（MUX）和直接插入式端口（DIP）主机的详细信息。

## 示例

### 示例 1：获取网络控制器 VIP 资源
```
PS C:\> $Cred = Get-Credential
PS C:\> Get-NetworkControllerVipResource -Credential $Cred -DstPort 80 -IPAddress 10.123.176.108 -Direction "In"
```

第一个命令获取凭据，并将它们存储在 `$Cred` 变量中。

第二个命令使用 `$Cred` 中存储的凭据来获取指定的 VIP 资源。

## 参数

### -CertificateThumbprint
为网络控制器指定证书指纹。在部署证书时需要设置此参数。

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

### -Credential
指定用于网络控制器（Network Controller）的身份凭证。在采用 Kerberos 部署方案时需要设置此参数。

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

### -Direction
指定交通流的方向。该参数的可接受值为：

- In
- Out

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Out, In

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DstPort
Specifies the port for the VIP resource to get.

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

### -IPAddress
Specifies the IP address of the VIP resource to get.

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

### -Protocol
Specifies the protocol of the VIP resource to get.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Tcp, Udp, All

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RestURI
Specifies the URI to use for Network Controller REST APIs.
Specify this parameter for a wild card certificate deployment.

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

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

