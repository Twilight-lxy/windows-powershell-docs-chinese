---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmreplicationserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMReplicationServer
---

# 设置虚拟机复制服务器（Set-VMReplicationServer）

## 摘要
将一台主机配置为副本服务器。

## 语法

### AuthenticationPort（默认值）
```
Set-VMReplicationServer [[-ReplicationEnabled] <Boolean>]
 [[-AllowedAuthenticationType] <RecoveryAuthenticationType>] [[-ReplicationAllowedFromAnyServer] <Boolean>]
 [-CertificateThumbprint <String>] [-默认值StorageLocation <String>] [-KerberosAuthenticationPort <Int32>]
 [-CertificateAuthenticationPort <Int32>] [-MonitoringInterval <TimeSpan>] [-MonitoringStartTime <TimeSpan>]
 [-Force] [-Passthru] [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### AuthenticationPortMapping
```
Set-VMReplicationServer [[-ReplicationEnabled] <Boolean>]
 [[-AllowedAuthenticationType] <RecoveryAuthenticationType>] [[-ReplicationAllowedFromAnyServer] <Boolean>]
 [-CertificateThumbprint <String>] [-默认值StorageLocation <String>]
 [-KerberosAuthenticationPortMapping <Hashtable>] [-CertificateAuthenticationPortMapping <Hashtable>]
 [-MonitoringInterval <TimeSpan>] [-MonitoringStartTime <TimeSpan>] [-Force] [-Passthru]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-VMReplicationServer` cmdlet 可将一台主机配置为复制服务器，并允许你指定用于接收复制流量的身份验证类型和端口。

要限制副本服务器接受的复制流量，仅允许来自特定服务器的请求，请使用 **New-VMReplicationAuthorizationEntry** cmdlet。

## 示例

### 示例 1
```powershell
PS C:\>  Set-VMReplicationServer $true -AllowedAuthenticationType Kerberos
```

这个示例将本地主机配置为副本服务器，并指定使用Kerberos进行身份验证。

### 示例 2
```powershell
PS C:\>  Set-VMReplicationServer -ReplicationEnabled $true -AllowedAuthenticationType Kerberos -ReplicationAllowedFromAnyServer $true -默认值StorageLocation d:\默认值ReplicaStorage
```

这个示例配置了一个副本服务器，该服务器接受来自所有已认证服务器的复制请求，并使用默认的存储位置“d:\默认值ReplicaStorage”。

### 示例 3
```powershell
PS C:\>  Set-VMReplicationServer -MonitoringInterval "12:00:00" -MonitoringStartTime "17:00:00"
```

这个示例配置了副本服务器，使其从17:00开始，以12小时的间隔进行监控。

### 示例 4
```powershell
PS C:\> $portmapping = @{"Server1.contoso.com" = 82; "Server2.contoso.com" = 81; "Broker.contoso.com" = 80}
PS C:\> Set-VMReplicationServer -KerberosAuthenticationPortMapping $portmapping
```

这个示例配置了集群中的节点，使它们能够在不同的端口上接收复制数据。第一个命令声明了一个名为 `portmapping` 的变量，并使用它来存储各个节点的服务器名称以及每个节点应使用的端口信息。第二个命令则配置集群中的每个节点，在进行 Kerberos 认证时使用 `portmapping` 变量中存储的值。

## 参数

### -AllowedAuthenticationType
指定副本服务器将使用哪些认证类型。允许的值包括 Kerberos、Certificate 或 CertificateAndKerberos。

```yaml
Type: RecoveryAuthenticationType
Parameter Sets: (All)
Aliases: AuthType
Accepted values: Kerberos, Certificate, CertificateAndKerberos

Required: False
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertificateAuthenticationPort
指定副本服务器用于接收基于证书的身份验证的复制数据的端口。只有当 `AllowedAuthType` 参数的值为 `Certificate` 或 `CertificateAndKerberos` 时，才能设置此参数。

```yaml
Type: Int32
Parameter Sets: AuthenticationPort
Aliases: CertAuthPort

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertificateAuthenticationPortMapping
在使用基于证书授权的 Hyper-V 复制功能（结合故障转移集群）时，您可以使用此参数为集群中的每个节点指定不同的端口以接收复制数据。我们建议为集群中的每个节点指定一个唯一的端口，并为 Hyper-V 复制代理指定另一个唯一的端口。只有当复制服务器配置为“Certificate”或“CertificateAndKerberos”身份验证类型时，才能设置此参数。

```yaml
Type: Hashtable
Parameter Sets: AuthenticationPortMapping
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertificateThumbprint
指定用于复制数据相互认证的证书。仅当认证类型设置为“Certificate”时，才需要此参数。请从个人证书存储中选择有效的计算机证书，并提供该证书的指纹（thumbprint）。

该证书必须具备以下所有属性才能被视为有效：

- It must not be expired.
- It must include both client and server authentication extensions for extended key usage (EKU), and an associated private key.
- It must terminate at a valid root certificate.
- It must meet the requirements for the subject common name (CN):
  - For servers that are not clustered, the subject common name (CN) must be equal to, or subject alternative name (DNS Name) should contain, the FQDN of the host.
  - For servers that are clustered, each node must have two certificates - one in which the subject common name (CN) or subject alternative name (DNS Name) is the name of the node, and the other in which subject common name (CN) or subject alternative name (DNS Name) is FQDN of the Hyper-V Replica Broker.

要显示计算机“我的证书库”中的证书列表以及每份证书的摘要（即“指纹”），请运行以下命令：

`PS C:\> cd cert:\LocalMachine\My`

`PS C:\> dir | format-list`

有关证书存储的更多信息，请参阅[证书存储](/previous-versions/windows/it-pro/windows-server-2003/cc757138(v=ws.10))。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Thumbprint

Required: False
Position: Named
默认值 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
配置一个或多个 Hyper-V 主机的副本服务器设置。允许使用 NetBIOS 名称、IP 地址和完全限定域名作为标识符。默认设置为“本地计算机”。可以使用 “localhost” 或句点（.）来明确指定“本地计算机”。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -默认值StorageLocation
指定在创建副本虚拟机时用于存储虚拟硬盘文件的默认位置。当 ReplicationAllowedFromAnyServer 的值为 True 时，必须设置此参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases: StorageLoc

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
指定该命令是否可以在不需要确认的情况下直接运行。

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

### -KerberosAuthenticationPort
指定HTTP监听器在副本服务器主机上使用的端口。

```yaml
Type: Int32
Parameter Sets: AuthenticationPort
Aliases: KerbAuthPort

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -KerberosAuthenticationPortMapping
在使用具有故障转移集群和Kerberos授权功能的Hyper-V副本时，您可以使用此参数为集群中的每个节点指定不同的端口以接收复制数据。我们建议为集群中的每个节点指定一个唯一的端口，并为Hyper-V副本代理指定另一个唯一的端口。只有当副本服务器配置的认证类型为Kerberos或CertificateAndKerberos时，才能设置此参数。

```yaml
Type: Hashtable
Parameter Sets: AuthenticationPortMapping
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MonitoringInterval
指定复制统计数据的计算频率（即监控间隔）。有效值包括：1小时、2小时、3小时、4小时、6小时、8小时、12小时、24小时、2天、3天、4天、5天、6天、7天。格式应为“天数:小时:分钟:秒”，例如01:00:00表示1小时，1.00:00:00表示1天。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MonitoringStartTime
指定监控间隔开始的时间。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 **VMReplicationServer** 对象传递给流水线，该对象用于表示复制服务器的复制设置。

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

### -ReplicationAllowedFromAnyServer
指定是否接受来自任何服务器的复制请求。当该参数设置为**true**时，还必须指定**默认值StorageLocation**。虚拟机副本将使用默认存储位置和DEFAULT信任组标签。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: AllowAnyServer

Required: False
Position: 2
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicationEnabled
指定该主机是否被启用为副本服务器（Replica server）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: RepEnabled

Required: False
Position: 0
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### VMRecoveryServer
如果指定了**-PassThru**选项的话……

## 备注

## 相关链接
