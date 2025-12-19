---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/test-vmreplicationconnection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-VMReplicationConnection
---

# 测试虚拟机复制连接

## 摘要
测试主服务器与副本服务器之间的连接。

## 语法

```
Test-VMReplicationConnection [-ReplicaServerName] <String> [-ReplicaServerPort] <Int32>
 [-AuthenticationType] <ReplicationAuthenticationType> [[-CertificateThumbprint] <String>]
 [-BypassProxyServer <Boolean>] [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [<CommonParameters>]
```

## 描述
`Test-VMReplicationConnection` cmdlet 用于测试主服务器与副本服务器之间的连接，以确定是否可以为主服务器上的虚拟机启用复制功能，并将这些虚拟机复制到指定的副本服务器上。

## 示例

### 示例 1
```
PS C:\> Test-VMReplicationConnection server01.domain01.contoso.com 80 Kerberos
```

这个示例测试了本地主机与名为 server01.domain01.contoso.com 的副本服务器之间的连接，使用端口 80 和 Kerberos 身份验证机制。

## 参数

### -AuthenticationType
指定用于测试连接的认证类型，可以是“Kerberos”或“Certificate”。所选的副本服务器必须支持所选择的认证类型。运行 **Get-VMReplicationServer** cmdlet 以验证为该副本服务器配置的认证方式，或者联系该副本服务器的管理员。

```yaml
Type: ReplicationAuthenticationType
Parameter Sets: (All)
Aliases: AuthType
Accepted values: Kerberos, Certificate

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -BypassProxyServer
指定在测试连接性时是否跳过代理服务器。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertificateThumbprint
指定用于复制数据相互认证的证书。仅当指定的认证类型为“Certificate”时，此参数才是必需的。请从个人证书存储中选择有效的计算机证书，并提供该证书的指纹信息。

该证书必须具备以下所有属性才能被视为有效：

它必须没有过期。

它必须同时包含客户端和服务器的身份验证扩展功能（用于扩展密钥使用，即Extended Key Usage，简称EKU），以及相应的私钥。

它必须以一个有效的根证书作为终止点。

对于主题通用名称（Subject Common Name，简称 CN）的要求取决于虚拟机是否属于某个集群。如果虚拟机不属于集群，则其主题通用名称（CN）必须与主机的完全 Qualified Domain Name（FQDN）相同，或者其主题备用名称（Subject Alternative Name，简称 DNS Name）中必须包含该主机的 FQDN；如果虚拟机属于集群，则其主题通用名称（CN）必须与 Hyper-V 复制代理服务器的 FQDN 相同，或者其主题备用名称（DNS Name）中必须包含该 Hyper-V 复制代理服务器的 FQDN。

要在计算机的“我的证书库”中显示证书列表以及每份证书的摘要（即“指纹”），请输入以下内容：

```
PS C:\> cd cert:\LocalMachine\My
```

`PS C:\> dir | format-list`

有关证书存储的更多信息，请参阅 [http://technet.microsoft.com//library/cc757138.aspx](https://technet.microsoft.com//library/cc757138.aspx)。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Thumbprint

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
请指定一个或多个 Hyper-V 主机，这些主机上托管着您想要测试复制连接的虚拟机。允许使用 NetBIOS 名称、IP 地址或完全限定域名（FQDN）来进行指定。默认值是本地计算机；可以使用 `localhost` 或`.` 来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicaServerName
指定用于测试与要复制的虚拟机之间连接性的副本服务器的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ReplicaServer

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicaServerPort
指定用于测试连接性的副本服务器上的端口。请确保选择的端口已在副本服务器上配置为支持与此cmdlet中使用的AuthenticationType参数所指定的相同身份验证类型。您可以在副本服务器上运行**Get-VMReplicationServer** cmdlet来检查端口的配置情况，或者联系该副本服务器的管理员获取相关信息。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases: ReplicaPort

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

