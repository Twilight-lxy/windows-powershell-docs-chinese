---
description: 使用这个主题来借助 Windows PowerShell 帮助管理 Windows 和 Windows Server 技术。
external help file: Get-VipConnectivityInfo.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/get-viphostmapping?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VipHostMapping
---

# Get-VipHostMapping

## 摘要
可以获得VIP主机映射功能。

## 语法

```
Get-VipHostMapping [-NetworkController] <String> [[-Credential] <PSCredential>] [-RestURI] <String>
 [[-CertificateThumbprint] <String>] [-VipEndPoint] <String> [-Type] <String> [<CommonParameters>]
```

## 描述
`Get-VipHostMapping` cmdlet 可以获取虚拟 IP（VIP）主机的相关信息，包括其复用器（MUX）和 DIP 主机。

## 示例

### 示例 1：获取 VIP 主机映射信息
```
PS C:\> $Password = ConvertTo-SecureString -String $Pass -AsPlainText -Force
PS C:\> $Cred = New-Object PSCredential -ArgumentList (".\administrator", $Password)
PS C:\> $ncIPAddress = 55.1.1.3
PS C:\> $NCInfo = Get-NetworkControllerDeploymentInfo -NetworkController $ncIPAddress -Credential $Cred
PS C:\> $vipInfo = Get-NetworkControllerVipResource -RestURI $NCInfo.NetworkControllerURI -ClientCertificate $NCInfo.ClientCertificate -IPAddress "72.1.12" -DstPort "2003" -Protocol "Tcp"
PS C:\> Get-VipHostMapping -NetworkController $ncIPAddress -Credential $Cred -RestURI $NCInfo.NetworkControllerURI -CertificateThumbprint $NCInfo.ClientCertificate -VipEndPoint $vipInfo.ResourceRef -L3NAT $vipInfo.L3NAT
```

第一个命令生成一个密码，然后将其存储在 `$Password` 变量中。

第二个命令创建了一个 **PSCredential** 对象，然后将其存储在 `$Cred` 变量中。

第三个命令将指定的网络控制器IP地址赋值给$ncIPAddress变量。

第四条命令获取网络控制器的部署信息，并将其存储在$NCInfo变量中。

第五条命令获取指定的VIP资源，然后将其存储在$vipInfo变量中。

最后一个命令用于获取指定主机的VIP主机映射信息。

## 参数

### -CertificateThumbprint
为网络控制器指定证书指纹。在进行证书部署时需要设置此参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定用于网络控制器的凭据。在采用 Kerberos 部署方案时，请设置此参数。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NetworkController
指定一个网络控制器节点的名称或 IP 地址。

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

### -RestURI
指定用于网络控制器（Network Controller）REST API的URI。在部署通配符证书时需要设置此参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Type
用于指定类型。该参数的可接受值包括：

- L3Nat
- InboundNatRule
- LoadBalancingRule
- OutboundNatRule

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: L3Nat, InboundNatRule, LoadBalancingRule, OutboundNatRule

Required: True
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VipEndPoint
指定VIP端点的REST资源。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Get-NetworkControllerVipResource](./Get-NetworkControllerVipResource.md)

