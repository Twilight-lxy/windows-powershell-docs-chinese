---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerSetting_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsserversetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServerSetting
---

# Get-DnsServerSetting

## 摘要
检索DNS服务器设置。

## 语法

### 简介（默认设置）
```
Get-DnsServerSetting [-ComputerName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### 所有
```
Get-DnsServerSetting [-All] [-ComputerName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsServerSetting` cmdlet 可以检索基本的域名系统（DNS）服务器设置，即默认的参数配置。如果要获取更高级的 DNS 服务器设置，请使用 `All` 参数。

## 示例

### 示例 1：获取所有 DNS 服务器设置
```
PS C:\> Get-DnsServerSetting -All

ComputerName                            : WIN-OLPN33S5Q3M.mytest.contoso.com
MajorVersion                            : 6
MinorVersion                            : 2
BuildNumber                             : 8230
IsReadOnlyDC                            : False
EnableDnsSec                            : True
EnableIPv6                              : True
EnableOnlineSigning                     : True
NameCheckFlag                           : 2
AddressAnswerLimit                      : 0
XfrConnectTimeout(s)                    : 30
BootMethod                              : 3
AllowUpdate                             : True
UpdateOptions                           : 783
DsAvailable                             : True
DisableAutoReverseZone                  : False
AutoCacheUpdate                         : False
RoundRobin                              : True
LocalNetPriority                        : True
StrictFileParsing                       : False
LooseWildcarding                        : False
BindSecondaries                         : False
WriteAuthorityNS                        : False
ForwardDelegations                      : False
AutoConfigFileZones                     : 1
EnableDirectoryPartitions               : True
RpcProtocol                             : 5
EnableVersionQuery                      : 0
EnableDuplicateQuerySuppression         : True
LameDelegationTTL                       : 00:00:00
AutoCreateDelegation                    : 2
AllowCnameAtNs                          : True
RemoteIPv4RankBoost                     : 5
RemoteIPv6RankBoost                     : 0
EnableRsoForRodc                        : True
MaximumRodcRsoQueueLength               : 300
MaximumRodcRsoAttemptsPerCycle          : 100
OpenAclOnProxyUpdates                   : True
NoUpdateDelegations                     : False
EnableUpdateForwarding                  : False
MaxResourceRecordsInNonSecureUpdate     : 30
EnableWinsR                             : True
LocalNetPriorityMask                    : 255
DeleteOutsideGlue                       : False
AppendMsZoneTransferTag                 : False
AllowReadOnlyZoneTransfer               : False
MaximumUdpPacketSize                    : 4000
TcpReceivePacketSize                    : 65536
EnableSendErrorSuppression              : True
SelfTest                                : 4294967295
XfrThrottleMultiplier                   : 10
SilentlyIgnoreCnameUpdateConflicts      : False
EnableIQueryResponseGeneration          : False
SocketPoolSize                          : 2500
AdminConfigured                         : True
SocketPoolExcludedPortRanges            : {}
ForestDirectoryPartitionBaseName        : ForestDnsZones
DomainDirectoryPartitionBaseName        : DomainDnsZones
ServerLevelPluginDll                    :
EnableRegistryBoot                      :
PublishAutoNet                          : False
QuietRecvFaultInterval(s)               : 0
QuietRecvLogInterval(s)                 : 0
ReloadException                         : False
SyncDsZoneSerial                        : 2
EnableDuplicateQuerySuppression         : True
SendPort                                : Random
MaximumSignatureScanPeriod              : 2.00:00:00
MaximumTrustAnchorActiveRefreshInterval : 15.00:00:00
ListeningIPAddress                      : {172.23.90.136}
AllIPAddress                            : {172.23.90.136}
```

这个命令可以获取DNS服务器的所有设置信息。

## 参数

### -All
表示该cmdlet会获取所有DNS服务器的设置信息。

```yaml
Type: SwitchParameter
Parameter Sets: All
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个DNS服务器。该参数的合法取值包括：IP V4地址；IP V6地址；以及任何能够解析为IP地址的其他值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Cn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerSetting

## 备注

## 相关链接

[Set-DnsServerSetting](./Set-DnsServerSetting.md)

