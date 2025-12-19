---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmreplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMReplication
---

# 设置虚拟机复制（Set-VMReplication）

## 摘要
修改虚拟机的复制设置。

## 语法

### VMName（默认值）
```
Set-VMReplication [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [[-ReplicaServerName] <String>] [[-ReplicaServerPort] <Int32>]
 [[-AuthenticationType] <ReplicationAuthenticationType>] [-CertificateThumbprint <String>]
 [-CompressionEnabled <Boolean>] [-ReplicateHostKvpItems <Boolean>] [-BypassProxyServer <Boolean>]
 [-EnableWriteOrderPreservationAcrossDisks <Boolean>] [-InitialReplicationStartTime <DateTime>]
 [-DisableVSSSnapshotReplication] [-VSSSnapshotFrequencyHour <Int32>] [-RecoveryHistory <Int32>]
 [-ReplicationFrequencySec <Int32>] [-ReplicatedDisks <HardDiskDrive[]>] [-ReplicatedDiskPaths <String[]>]
 [-Reverse] [-AutoResynchronizeEnabled <Boolean>] [-AutoResynchronizeIntervalStart <TimeSpan>]
 [-AutoResynchronizeIntervalEnd <TimeSpan>] [-AsReplica] [-UseBackup] [-AllowedPrimaryServer <String>] [-AsJob]
 [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Set-VMReplication [-Credential <PSCredential[]>] [-VM] <VirtualMachine[]> [[-ReplicaServerName] <String>]
 [[-ReplicaServerPort] <Int32>] [[-AuthenticationType] <ReplicationAuthenticationType>]
 [-CertificateThumbprint <String>] [-CompressionEnabled <Boolean>] [-ReplicateHostKvpItems <Boolean>]
 [-BypassProxyServer <Boolean>] [-EnableWriteOrderPreservationAcrossDisks <Boolean>]
 [-InitialReplicationStartTime <DateTime>] [-DisableVSSSnapshotReplication] [-VSSSnapshotFrequencyHour <Int32>]
 [-RecoveryHistory <Int32>] [-ReplicationFrequencySec <Int32>] [-ReplicatedDisks <HardDiskDrive[]>]
 [-ReplicatedDiskPaths <String[]>] [-Reverse] [-AutoResynchronizeEnabled <Boolean>]
 [-AutoResynchronizeIntervalStart <TimeSpan>] [-AutoResynchronizeIntervalEnd <TimeSpan>] [-AsReplica]
 [-UseBackup] [-AllowedPrimaryServer <String>] [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 虚拟机复制（VMReplication）
```
Set-VMReplication [-Credential <PSCredential[]>] [-VMReplication] <VMReplication[]>
 [[-ReplicaServerName] <String>] [[-ReplicaServerPort] <Int32>]
 [[-AuthenticationType] <ReplicationAuthenticationType>] [-CertificateThumbprint <String>]
 [-CompressionEnabled <Boolean>] [-ReplicateHostKvpItems <Boolean>] [-BypassProxyServer <Boolean>]
 [-EnableWriteOrderPreservationAcrossDisks <Boolean>] [-InitialReplicationStartTime <DateTime>]
 [-DisableVSSSnapshotReplication] [-VSSSnapshotFrequencyHour <Int32>] [-RecoveryHistory <Int32>]
 [-ReplicationFrequencySec <Int32>] [-ReplicatedDisks <HardDiskDrive[]>] [-ReplicatedDiskPaths <String[]>]
 [-Reverse] [-AutoResynchronizeEnabled <Boolean>] [-AutoResynchronizeIntervalStart <TimeSpan>]
 [-AutoResynchronizeIntervalEnd <TimeSpan>] [-AsReplica] [-UseBackup] [-AllowedPrimaryServer <String>] [-AsJob]
 [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMReplication` cmdlet 用于修改虚拟机的复制设置。

## 示例

### 示例 1
```
PS C:\>  Set-VMReplication VM01 -AutoResynchronizedDisabled $true -AutoResynchronizeIntervalStart "18:30:00" -AutoResynchronizeIntervalEnd "06:00:00"
```

这个示例配置了虚拟机VM01的自动同步功能。

### 示例 2
```
PS C:\>  Set-VMReplication VM01 -AsReplica -AllowedPrimaryServer server01.domain01.contoso.com
```

这个示例将虚拟机VM01配置为复制虚拟机，使其能够从域domain01.contoso.com中的主服务器server01进行数据复制。

### 示例 3
```
PS C:\>  Set-VMReplication VM01 -RecoveryHistory 4 -VSSSnapshotFrequency 4
```

这个示例配置了虚拟机VM01的恢复历史记录以及与应用程序一致的恢复点设置。

### 示例 4
```
PS C:\>  Set-VMReplication VM01 -Reverse
```

这个示例会反转虚拟机VM01的复制过程。

### 示例 5
```
PS C:\>  Set-VMReplication * server01.domain01.contoso.com 80
```

这个示例配置了本地 Hyper-V 主机上所有虚拟机的复制功能，将数据复制到 Replica 服务器 server01.domain01.contoso.com，并使用端口 80 进行通信。

### 示例 6
```
PS C:\> $VHDS = @("C:\VHDS\vhd1", "C:\VHDS\vhd2")
PS C:\> Set-VMReplication -VMName "VM01" -ReplicatedDiskPaths $VHDS
```

第一个命令将虚拟硬盘 vhd1 和 vhd2 的路径赋值给 `$VHDS` 变量。

第二条命令指定了**$VHDS**中的两个磁盘，这些磁盘将被纳入用于复制虚拟机VM01的磁盘集中。

## 参数

### -AllowedPrimaryServer
当你使用 `AsReplica` 参数来指定一台虚拟机作为副本虚拟机时，该参数决定了哪些主服务器可以将数据复制到这台副本虚拟机上。只有来自所选身份验证条目中指定的服务器，或者任何具有相同信任组的身份验证条目的服务器，才能接受数据复制请求。

```yaml
Type: String
Parameter Sets: (All)
Aliases: AllowedPS

Required: False
Position: Named
默认值 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
以后台作业的形式运行该cmdlet。

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

### -AsReplica
指定该虚拟机为复制虚拟机（replica virtual machine），从而使其能够作为主虚拟机初始复制的源。

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

### -AuthenticationType
指定用于虚拟机复制的认证类型，可以是 Kerberos 或证书（Certificate）。所指定的复制服务器（Replica server）必须支持所选的认证类型。请运行 **Get-VMReplicationServer** cmdlet 来验证该复制服务器配置的认证方式，或联系该复制服务器的管理员。

```yaml
Type: ReplicationAuthenticationType
Parameter Sets: (All)
Aliases: AuthType
Accepted values: Kerberos, Certificate

Required: False
Position: 3
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AutoResynchronizeEnabled
该功能支持自动重新同步需要再次进行数据同步的虚拟机（例如，当主服务器突然关闭时，相应的虚拟机就需要重新同步数据）。然而，重新同步过程会消耗大量的存储和处理资源。因此，我们建议在非高峰时段安排重新同步操作，以减少对主机以及主机上运行的其他虚拟机的影响。您可以使用 `AutoResynchronizeIntervalStart` 和 `AutoResynchronizeIntervalEnd` 参数来指定开始自动重新同步的非高峰时间。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: AutoResync

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AutoResynchronizeIntervalEnd
指定您希望自动开始重新同步的时间段的结束时间。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases: AutoResyncEnd

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AutoResynchronizeIntervalStart
指定您希望自动开始重新同步的时间段的起始时间。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases: AutoResyncStart

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -BypassProxyServer
指定在将数据复制到副本服务器（Replica server）时是否跳过代理服务器（proxy server）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertificateThumbprint
指定用于复制数据相互认证的证书。仅当将“Certificate”作为认证类型时，才需要此参数。请从个人证书存储中选择有效的计算机证书的指纹（thumbprint）进行指定。

该证书必须具备以下所有属性才能被视为有效：

- It must not be expired.
- It must include both client and server authentication extensions for extended key usage (EKU), and an associated private key.
- It must terminate at a valid root certificate.
- The requirement for the subject common name (CN) differs depending on whether the virtual machine belongs to a cluster. For virtual machines that do not belong to a cluster, the subject common name (CN) must be equal to, or subject alternative name (DNS Name) should contain, the FQDN of the host. For virtual machines that belong to a cluster, the subject common name (CN) must be equal to, or subject alternative name (DNS Name) must contain, the and fully-qualified domain name (FQDN) of the Hyper-V Replica Broker.

要在计算机的“我的证书库”中显示证书列表以及每份证书的摘要（即“指纹”，用于验证证书的真实性），请输入以下命令：

```
PS C:\>\> cd cert:\LocalMachine\My
```

请帮我将以下Markdown内容转换为中文：  

`PS C:\>\dir | format-list`

有关证书存储的更多信息，请参阅 [http://technet.microsoft.com//library/cc757138.aspx](https://technet.microsoft.com//library/cc757138.aspx)。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Thumbprint, Cert

Required: False
Position: Named
默认值 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。您可以输入一台计算机的名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CompressionEnabled
指定通过网络发送的复制数据是否需要进行压缩。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个要启用复制功能的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名来进行选择。默认值为本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行该操作。

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

### -DisableVSSSnapshotReplication
指定是否复制卷影复制服务（VSS）的快照。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: DisableVSS

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableWriteOrderPreservationAcrossDisks
确定所有被选中用于复制的虚拟硬盘是否都复制到了相同的时间点。如果虚拟机运行的应用程序需要在多个虚拟硬盘上保存数据（例如，一个虚拟硬盘专门用于存储应用程序数据，另一个虚拟硬盘专门用于存储应用程序日志文件），那么这个功能就非常有用。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InitialReplicationStartTime
用于指定初始复制开始的时间，特别是在计划将初始复制延迟到以后执行时。您可以指定一个最多在7天后的时间点。如果未指定此参数，则初始复制会立即开始。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases: IRTime

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定将一个 **VMReplication** 对象传递到管道中，该对象用于表示要设置的复制配置。

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

### -RecoveryHistory
指定是否在副本虚拟机上存储额外的恢复点。存储主虚拟机最新的多个恢复点后，您可以恢复到之前的某个时间点。但是，存储额外的恢复点会消耗更多的存储空间和处理资源。您最多可以配置存储24个恢复点。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases: RecHist

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicaServerName
指定该虚拟机将被复制到的副本服务器的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ReplicaServer

Required: False
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicaServerPort
指定复制流量所使用的副本服务器上的端口。请确保您指定的端口号已在副本服务器上配置完毕，并且该端口支持与本cmdlet中使用的`AuthenticationType`参数所指定的相同认证类型。您可以在副本服务器上运行`Get-VMReplicationServer` cmdlet来检查端口的配置情况，或者联系相应的副本服务器管理员获取帮助。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases: ReplicaPort

Required: False
Position: 2
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicateHostKvpItems
指定是否为这台虚拟机复制仅主机可见（host-only）的键值对（Key-Value Pair，KVP）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicatedDiskPaths
指定所有用于复制的虚拟硬盘的完全限定路径名称。请确保包含对虚拟机启动至关重要的虚拟硬盘（例如客户操作系统所在的磁盘）。如果将某个关键磁盘排除在此列表之外，可能会导致复制后的虚拟机无法正常启动。

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

### -ReplicatedDisks
指定所有需要包含在复制过程中的虚拟硬盘。该参数可以包括连接到虚拟机的所有VHD（虚拟硬盘），也可以仅选择其中的一部分。请确保包含对虚拟机启动至关重要的虚拟硬盘，例如宿主操作系统所在的磁盘。如果将某个关键磁盘排除在这个列表之外，可能会导致副本虚拟机无法正常启动。

```yaml
Type: HardDiskDrive[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicationFrequencySec
指定Hyper-V将更改复制到副本服务器的频率（以秒为单位）。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases: RepFreq

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Reverse
反转虚拟机的复制状态，将其从主虚拟机切换为副本虚拟机，或从副本虚拟机切换回主虚拟机。

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

### -UseBackup
指定将副本服务器上的虚拟机恢复后的副本作为初始复制的来源。

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

### -VM
指定要设置复制配置的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要设置复制配置的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases: Name

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMReplication
指定一个虚拟机复制对象，将为该对象设置配置信息。

```yaml
Type: VMReplication[]
Parameter Sets: VMReplication
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VSSSnapshotFrequencyHour
该参数用于指定卷影复制服务（VSS）执行虚拟机快照备份的频率（以小时为单位）。只有在为虚拟机启用了应用程序一致性复制，并且您设置的**RecoveryHistory**参数值不为零的情况下，才需要指定此参数。如果禁用了应用程序一致性复制，该 cmdlet 会将该参数的值设置为零。如果您是从副本虚拟机扩展复制功能，则不要指定此参数。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases: VSSFreq

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### 虚拟机复制（VMReplication）
如果指定了 **-PassThru** 参数的话……

## 备注

## 相关链接

