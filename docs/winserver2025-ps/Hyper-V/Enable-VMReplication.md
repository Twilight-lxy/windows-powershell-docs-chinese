---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/enable-vmreplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-VMReplication
---

# 启用虚拟机复制功能

## 摘要
启用虚拟机的复制功能。

## 语法

### VMName（默认值）
```
Enable-VMReplication [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-ReplicaServerName] <String> [-ReplicaServerPort] <Int32>
 [-AuthenticationType] <ReplicationAuthenticationType> [-CertificateThumbprint <String>]
 [-CompressionEnabled <Boolean>] [-ReplicateHostKvpItems <Boolean>] [-BypassProxyServer <Boolean>]
 [-EnableWriteOrderPreservationAcrossDisks <Boolean>] [-VSSSnapshotFrequencyHour <Int32>]
 [-RecoveryHistory <Int32>] [-ReplicationFrequencySec <Int32>] [-ExcludedVhd <HardDiskDrive[]>]
 [-ExcludedVhdPath <String[]>] [-AutoResynchronizeEnabled <Boolean>]
 [-AutoResynchronizeIntervalStart <TimeSpan>] [-AutoResynchronizeIntervalEnd <TimeSpan>] [-AsJob] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMName_AsReplica
```
Enable-VMReplication [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-AsReplica] [-AllowedPrimaryServer <String>] [-AsJob] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMObject
```
Enable-VMReplication [-Credential <PSCredential[]>] [-VM] <VirtualMachine[]> [-ReplicaServerName] <String>
 [-ReplicaServerPort] <Int32> [-AuthenticationType] <ReplicationAuthenticationType>
 [-CertificateThumbprint <String>] [-CompressionEnabled <Boolean>] [-ReplicateHostKvpItems <Boolean>]
 [-BypassProxyServer <Boolean>] [-EnableWriteOrderPreservationAcrossDisks <Boolean>]
 [-VSSSnapshotFrequencyHour <Int32>] [-RecoveryHistory <Int32>] [-ReplicationFrequencySec <Int32>]
 [-ExcludedVhd <HardDiskDrive[]>] [-ExcludedVhdPath <String[]>] [-AutoResynchronizeEnabled <Boolean>]
 [-AutoResynchronizeIntervalStart <TimeSpan>] [-AutoResynchronizeIntervalEnd <TimeSpan>] [-AsJob] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject_AsReplica
```
Enable-VMReplication [-Credential <PSCredential[]>] [-VM] <VirtualMachine[]> [-AsReplica]
 [-AllowedPrimaryServer <String>] [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Enable-VMReplication** cmdlet 可以使虚拟机复制到指定的副本服务器（Replica server）。

## 示例

### 示例 1
```
PS C:\>  Enable-VMReplication VM01 server01.domain01.contoso.com 80 Kerberos
```

这个示例为本地 Hyper-V 主机上名为 VM01 的虚拟机配置了复制功能，并将复制流量定向到名为 server01.domain01.contoso.com 的副本服务器上的端口 80，同时使用 Kerberos 作为身份验证方式。

### 示例 2
```
PS C:\>  Enable-VMReplication * server01.domain01.contoso.com 80 Kerberos
```

这个示例配置了本地Hyper-V主机上所有虚拟机的复制功能，将数据复制到名为server01.domain01_contoso.com的副本服务器，并通过Kerberos作为身份验证方式，将复制流量定向到该副本服务器的80端口。

### 示例 3
```
PS C:\>  Enable-VMReplication VM01 -AsReplica -AllowedPrimaryServer *.domain01.contoso.com
```

这个示例将虚拟机VM02配置为复制虚拟机，并允许来自名为domain01.contoso.com的域中的所有主服务器对主虚拟机进行复制。

## 参数

### -AllowedPrimaryServer
当你使用 `AsReplica` 参数来指定一台虚拟机作为复制虚拟机时，该参数决定了哪些主服务器可以将其数据复制到这台复制虚拟机上。只有来自所选身份验证条目中指定的服务器，或者任何具有相同信任组的身份验证条目的服务器，才能接收这些复制数据。

```yaml
Type: String
Parameter Sets: VMName_AsReplica, VMObject_AsReplica
Aliases: AllowedPS

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将此cmdlet作为后台作业运行。

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

### -AsReplica
指定该虚拟机为副本虚拟机，从而可以将其用作主虚拟机初始复制的源。

```yaml
Type: SwitchParameter
Parameter Sets: VMName_AsReplica, VMObject_AsReplica
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AuthenticationType
指定用于虚拟机复制的认证类型，可以是 Kerberos 或证书（Certificate）。所指定的副本服务器（Replica server）必须支持所选择的认证类型。请运行 **Get-VMReplicationServer** cmdlet 以验证该副本服务器配置的认证方式，或联系该副本服务器的管理员。

```yaml
Type: ReplicationAuthenticationType
Parameter Sets: VMName, VMObject
Aliases: AuthType
Accepted values: Kerberos, Certificate

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AutoResynchronizeEnabled
该功能支持自动重新同步需要重新同步的虚拟机（例如，当主服务器突然关闭时，相关虚拟机就需要进行重新同步）。然而，重新同步会消耗大量的存储和处理资源。因此，建议在非高峰时段安排重新同步操作，以减少对主机及其他运行在该主机上的虚拟机的影响。可以通过使用 AutoResynchronizeIntervalStart 和 AutoResynchronizeIntervalEnd 参数来指定开始自动重新同步的非高峰时间段。

```yaml
Type: Boolean
Parameter Sets: VMName, VMObject
Aliases: AutoResync

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AutoResynchronizeIntervalEnd
指定您希望自动开始重新同步的时间段的结束时间。

```yaml
Type: TimeSpan
Parameter Sets: VMName, VMObject
Aliases: AutoResyncEnd

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AutoResynchronizeIntervalStart
指定希望自动开始重新同步的时间段的起始时间。

```yaml
Type: TimeSpan
Parameter Sets: VMName, VMObject
Aliases: AutoResyncStart

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -BypassProxyServer
指定在将数据复制到副本服务器（Replica server）时是否绕过代理服务器（proxy server）。

```yaml
Type: Boolean
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertificateThumbprint
指定用于复制数据相互身份验证的证书。仅当将“Certificate”作为身份验证类型时，才需要此参数。请从个人证书存储中选择有效的计算机证书的指纹（即证书的唯一标识符）进行配置。

该证书必须具备以下所有属性才能被视为有效：  
- 证书不能已过期。  
- 证书必须包含用于扩展密钥使用（Extended Key Usage, EKU）的客户端和服务器身份验证扩展功能，以及相应的私钥。  
- 证书必须以一个有效的根证书作为终点（即证书链的终止点）。

对于主题通用名称（Subject Common Name，简称CN）的要求因虚拟机是否属于集群而异：  
- 如果虚拟机不属于集群，则主题通用名称（CN）必须与主机的完全限定域名（Fully Qualified Domain Name，简称FQDN）相等；或者其主题备用名称（Subject Alternative Name，简称DNS Name）中必须包含该主机的FQDN。  
- 如果虚拟机属于集群，则主题通用名称（CN）必须与Hyper-V副本代理（Hyper-V Replica Broker）的完全限定域名（FQDN）相等；或者其主题备用名称（DNS Name）中必须包含该Hyper-V副本代理的FQDN。

要显示计算机“我的证书存储”中的证书列表以及每份证书的摘要信息，请输入以下内容：

```
PS C:\> cd cert:\LocalMachine\My
```

`PS C:\> dir | format-list`

有关证书存储的更多信息，请参阅 [http://technet.microsoft.com//library/cc757138.aspx](https://technet.microsoft.com//library/cc757138.aspx)。

```yaml
Type: String
Parameter Sets: VMName, VMObject
Aliases: Thumbprint, Cert

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: VMName, VMName_AsReplica
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CompressionEnabled
指定在通过网络发送该虚拟机的复制数据时是否对其进行压缩。

```yaml
Type: Boolean
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个Hyper-V主机，这些主机上包含您希望启用复制的虚拟机。允许使用NetBIOS名称、IP地址和完全限定域名（FQDN）。默认值是本地计算机。可以使用“localhost”或句点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName, VMName_AsReplica
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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableWriteOrderPreservationAcrossDisks
确定是否所有被选中用于复制的虚拟硬盘都复制到了相同的时间点。如果虚拟机运行的是一个需要在多个虚拟硬盘之间保存数据的应用程序（例如，一个虚拟硬盘专门用于存储应用程序数据，另一个虚拟硬盘专门用于存储应用程序日志文件），那么这一点非常有用。

```yaml
Type: Boolean
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExcludedVhd
指定一个或多个需要从复制过程中排除的虚拟硬盘（例如，用于存储分页文件的虚拟硬盘）。请注意不要排除对虚拟机启动至关重要的虚拟硬盘，比如存储客户操作系统的那个虚拟硬盘。如果排除了这些关键硬盘，可能会导致副本虚拟机无法正常启动。

```yaml
Type: HardDiskDrive[]
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExcludedVhdPath
指定要从复制中排除的虚拟硬盘的完整路径名称。

```yaml
Type: String[]
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -RecoveryHistory
指定是否在副本虚拟机上存储额外的恢复点。存储多个恢复点（而不仅仅是主虚拟机最新的恢复点）可以让您恢复到更早的时间点。但是，存储额外的恢复点会占用更多的存储空间和处理资源。您可以配置最多存储24个恢复点。

```yaml
Type: Int32
Parameter Sets: VMName, VMObject
Aliases: RecHist

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicaServerName
指定该虚拟机将被复制到的副本服务器的名称。

```yaml
Type: String
Parameter Sets: VMName, VMObject
Aliases: ReplicaServer

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicaServerPort
指定副本服务器上用于复制流的端口。请确保使用的端口号已在副本服务器上进行配置，并且该端口支持与本cmdlet中通过`AuthenticationType`参数指定的身份验证类型相匹配的身份验证方式。你可以在副本服务器上运行`Get-VMReplicationServer` cmdlet来检查端口的配置信息，或者联系相应的副本服务器管理员以获取更多帮助。

```yaml
Type: Int32
Parameter Sets: VMName, VMObject
Aliases: ReplicaPort

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicateHostKvpItems
指定是否为该虚拟机复制仅主机可访问的键值对（Key-Value Pair, KVP）。

```yaml
Type: Boolean
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicationFrequencySec
指定Hyper-V复制更改到副本服务器的频率（以秒为单位）。

```yaml
Type: Int32
Parameter Sets: VMName, VMObject
Aliases: RepFreq

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定您想要配置用于复制的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject, VMObject_AsReplica
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定您想要配置用于复制的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName, VMName_AsReplica
Aliases: Name

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VSSSnapshotFrequencyHour
该参数用于指定卷影复制服务（VSS）对虚拟机执行快照备份的频率（以小时为单位）。仅在为虚拟机启用了应用一致性复制，并且您设置的**RecoveryHistory**参数值不为零的情况下，才需要指定此参数。如果禁用了应用一致性复制，此参数的值将被设置为零。如果您是从副本虚拟机扩展复制功能，则不要指定此参数。

```yaml
Type: Int32
Parameter Sets: VMName, VMObject
Aliases: VSSFreq

Required: False
Position: Named
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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

