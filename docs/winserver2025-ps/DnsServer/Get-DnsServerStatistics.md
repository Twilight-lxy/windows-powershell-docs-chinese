---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerStatistics_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsserverstatistics?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServerStatistics
---

# 获取 DNS 服务器统计信息

## 摘要
检索DNS服务器的统计信息或区域的统计信息。

## 语法

### ServerStatistics（默认设置）
```
Get-DnsServerStatistics [-ComputerName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ZoneStatistics
```
Get-DnsServerStatistics [-ComputerName <String>] [-Clear] -ZoneName <String[]> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsServerStatistics` cmdlet 可用于检索域名系统（DNS）服务器的统计信息。如果指定了 `ZoneName` 参数，该 cmdlet 会获取由该参数指定的区域的统计信息；如果没有指定 `ZoneName` 参数，则会获取整个服务器的汇总统计信息。

如果同时指定了 *Clear* 参数和 *ZoneName* 参数，那么指定区域的统计数据也将被清除。

## 示例

### 示例 1：获取本地 DNS 服务器的统计信息
```
PS C:\> Get-DnsServerStatistics
```

这个命令用于获取本地DNS服务器的统计信息。

### 示例 2：获取特定区域的服务器统计信息
```
PS C:\> Get-DnsServerStatistics -ZoneName "contoso.com"
```

这个命令用于获取名为“contoso.com”的DNS区域的统计信息。

### 示例 3：特定区域的清晰统计数据
```
PS C:\> Get-DnsServerStatistics -ZoneName "contoso.com" -Clear
```

这个命令会获取当前的DNS区域统计信息，并将名为“contoso.com”的DNS区域的统计计数器重置为初始值。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -Clear
表示该cmdlet会清除你在*ZoneName*参数中指定的区域的统计信息。

```yaml
Type: SwitchParameter
Parameter Sets: ZoneStatistics
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
用于指定一个DNS服务器。该参数的可接受值包括：IP V4地址；IP V6地址；以及任何能够解析为IP地址的其他值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -ZoneName
指定一个DNS区域名称数组，用于获取这些区域的DNS统计信息。该参数对于ZoneStatistics参数集来说是必需的。

```yaml
Type: String[]
Parameter Sets: ZoneStatistics
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输出

### DNSServer01Infrastructure.CimInstance#DnsServerStatistics
**CacheStatistics** 包含以下内容：FailedFreePasses（失败的自由通行尝试次数）、PassesRequiringAggressiveFree（需要采取激进策略才能完成自由通行的尝试次数）、PassesWithNoFrees（无需任何特殊操作即可完成自由通行的尝试次数）以及 SuccessfulFreePasses（成功完成自由通行的尝试次数）。

`DatabaseStatistics` 包含以下字段：`NodeInUse`、`NodeMemory`、`NodeReturn` 和 `NodeUsed`。

`DnssecStatistics` 包含以下内容：`FailedValidations`（验证失败次数）、`RecursionFailures`（递归调用失败次数）以及 `SuccessfulValidations`（验证成功次数）。

**DsStatistics** 包含以下字段：DsNodesAdded、DsNodesDeleted、DsNodesLoaded、DsNodesModified、DsNodesTombstoned、DsRecordsAdded、DsRecordsLoaded、DsRecordsReplaced、DsSerialWrites、DsTombstonesRead、DsTotalNodesRead、DsTotalRecordsRead、DsUpdateNodesRead、DsUpdateRecordsRead、DsUpdate Searches、DsWriteSuppressed、DsWriteType、FailedDeleteDsEntries、FailedLdapAdd、FailedLdapModify、FailedReadRecords、LdapReconnects、LdapSearchTime、LdapTimedWrites、LdapWriteAverage、LdapWriteBucket0、LdapWriteBucket1、LdapWriteBucket2、LdapWriteBucket3、LdapWriteBucket4、LdapWriteBucket5、LdapWriteMax、LdapWriteTimeTotal、PollingPassesWithDsErrors、UpdateAdmin、UpdateAgingOff、UpdateAgingOn、UpdateAginRefresh、UpdateAutoConfig、UpdateLists、UpdateNodes、UpdatePacket、UpdateRecordChange、UpdateScavenge、UpdatePacketPrecon、UpdateSuppressed、UpdateTombstones 和 UpdateWrites。

**ErrorStatistics** 包含以下错误类型：BadKey、BadSig、BadTime、FormError、Max、NoError、NotAuthoritative、NotImpl、NotZone、NxDomain、NxRRSet、Refused、ServFail、UnknownError、YxDomain 和 YxRRSet。

**MasterStatistics** 包含以下字段：AxfrLimit、AxfrRequest、AxfrSuccess、Failure、FormError、IxfrAxfr、IxfrNoVersion、IxfrRequest、IxfrTcpRequest、IxfrTcpSuccess、IxfrUdpForceAxfr、IxfrUdpForceTcp、IxfrUdpRequest、IxfrUdpSuccess、IxfrUpdateSuccess、NameError、NotifySent、Refused、RefuseLoading、RefuseNotAuth、RefuseReadOnly、RefuseSecurity、RefuseServerFailure、RefuseShutdown、RefuseZoneLocked、Request 以及 StubAxfrRequest。

**MemoryStatistics** 包含以下内容：Alloc、Free、Memory、MemTags、StdBlockAlloc、StdBlockFreeList、StdBlockFreeListMemory、StdBlockInUse、StdBlockMemory、StdBlockReturn、StdBlockUsed、StdInUse、StdMemory、StdReturn、StdToHeapAlloc、StdToHeapFree、StdToHeapMemory 以及 StdUsed。

**NetBiosStatistics** 包含以下内容：NbstatAlloc、NbstatFree、NbstatInFreeList、NbstatInUse、NbstatMemory、NbstatNetAllocs、NbstatReturn、NbstatUsed 以及 PSComputerName。

**PacketStatistics** 包含以下字段：PacketsForNsListInUse、PacketsForNsListReturned、PacketsForNsListUsed、RecursePacketReturn、RecursePacketUsed、TcpAlloc、TcpFree、cpMemory、TcpNetAllocs、UdpAlloc、UdpFree、UdpInFreeList、UdpInUse、UdpMemory、UdpNetAllocs、UdpQueryReturn、UdpResponseReturn、UdpReturn 和 UdpUsed。

**PrivateStatistics** 包含以下内容：SecBigTimeSkewBypass、TcpConnect、TcpDisconnect、TpQuery、UdpConnResetRetryOverflow、UdpConnResets、UdpErrorMessageSize、UdpGQCSConnReset、UdpGQCSFailure、UdpGQCSFailureWithContext、UdpIndicateRecvFailures、UdpRecvFailure、UdpRestartRecvOnSockets、UdpSocketPnpDelete、ZoneLoadInit 以及 PSComputerName。

**Query2Statistics** 包含以下类别：Notify、Standard、KeyNego、TotalQueries、TypeA、TypeAll、TypeAxfr、TypeIxfr、TypeMx、TypeNs、TypeOther、TypePtr、TypeSoa、TypeSrv 和 Update。

**QueryStatistics** 包含以下内容：TcpClientConnections、TcpQueries、TcpQueriesSent、TcpResponses、Tcp ResponsesReceived、UdpQueries、UdpQueriesSent、UdpResponses 以及 UdpResponsesReceived。

`RecordStatistics` 包含以下字段：`CacheCurrent`、`CacheTimeouts`、`CacheTotal`、`InUse`、`Memory`、`Return`、`SlowFreeFinished`、`SlowFreeQueued` 和 `Used`。

**RecursionStatistics** 包含以下内容：AdditionalRecurred、CacheLockingDiscards、CacheUpdateAlloc、CacheUpdateFailure、CacheUpdateFree、CacheUpdateResponse、CacheUpdateRetry、ContinueCurrentLookup、ContinueCurrentRecursion、ContinueNextLookup、DiscardedDuplicateQueries、DuplicateCoalesedQueries、FailureReachAuthority、FailureReachPreviousResponse、FinalTimeoutExpired、FinalTimeoutQueued、Forwards、GnzLocalQuery、GnzRemoteQuery、GnzRemoteResponse、GnzRemoteResponseCacheFailure、GnzRemoteResponseCacheSuccess、 LookupPasses、OriginalQuestionRecursed、PartialFailure、QueriesRecursed、RecursePassFailure、RecursionFailure、ReferalPasses、ResponseAnswer、ResponseAuthoritative、ResponseBadPacket、ResponseDelegation、ResponseEmpty、ResponseFromForwarder、ResponseNameError、ResponseNonZoneData、ResponseNotAuthoritative、ResponseRCode、Responses、ResponsesMismatched、ResponsesUnmatched、ResponseUnsecure、ResumeSuspendedQuery、Retries、RootNsQuery、RootNsResponse、SendResponseDirect、Sends、ServerFailure、SuspendedQuery、TcpConnect、TcpDisconnect、TcpQuery、TcpResponse、TcpTry、TimedoutQueries 以及 TotalQuestionsRecursed。

**SecondaryStatistics** 包含以下内容：AxfrInvalid、AxfrRefused、AxfrRequest、AxfrResponse、AxfrSuccess、IxfrTcpAxfr、IxfrTcpFormError、IxfrTcpInvalid、IxfrTcpRefused、IxfrTcpRequest、IxfrTcpResponse、IxfrTcpSuccess、IxfrUdpFormError、xfrUdpInvalid、IxfrUdpNewPrimary、IxfrUdpNoUpdate、IxfrUdpRefused、IxfrUdpRequest、IxfrUdpResponse、IxfrUdpSuccess、IxfrUdpUseAxfr、IxfrUdpUseTcp、IxfrUdpWrongServer、NotifyCurrentVersion、NotifyInvalid、NotifyMasterUnknown、NotifyNewVersion、NotifyNonPrimary、NotifyNoVersion、NotifyOldVersion、NotifyPrimary、NotifyReceived、SoaRequest、SoaResponse、SoaResponseInvalid、StubAxfrInvalid、StubAxfrRefused、StubAxfrRequest、StubAxfrResponse 和 StubAxfrSuccess。

**SecurityStatistics** 包含以下方法：SecurityContextCreate、SecurityContextDequeue、SecurityContextFree、SecurityContextQueue、SecurityContextQueueInNego、SecurityContextQueueInNegoComplete、SecurityContextQueueLength、SecurityContextTimeout、SecurityPackAlloc、SecurityPackFree、SecurityTKeyBadTime、SecurityTKeyInvalid、SecurityTSigBadKey、SecurityTSigEcho、SecurityTSigFormError、SecurityTSigVerifyFailed 以及 SecurityTSigVerifySuccess。

**TimeoutStatistics** 包含以下字段：ActiveRecord、AlreadyInSystem、ArrayBlocksCreated、ArrayBlocksDeleted、CanNotDelete、Checks、DelayedFreesExecuted、DelayedFreesExecutedWithFunction、DelayedFreesQueued、DelayedFreesQueuedWithFunction、Deleted、RecentAccess、SetDirect、SetFromChildDelete、SetFromDereference 以及 SetTotal。

`TimeStatistics` 包含以下字段：`LastClearTime`、`ServerStartTime`、`TimeElapsedSinceLastClearedStatistics`、`TimeElapsedSinceLastClearedStatisticsBetweenRestart`、`TimeElapsedSinceServerStart` 以及 `TimeElapsedSinceServerStartBetweenRestart`。

**UpdateStatistics** 包含以下字段：Completed、DsSuccess、DsWriteFailure、Empty、FormError、ForwardInQueue、ForwardResponses、Forwards、ForwardTimeouts、InQueue、NoOps、NotAuthoritative、 NotImplemented、NotZone、NxDomain、NxRRset、Queued、Received、Refused、RefusedAccessDenied、RefusedNonSecure、Rejected、SecureDsWriteFailure、SecureFailure、SecureSuccess、TcpForwards、Timeout、UpdateType、YxDomain 和 YxRRset。

**WinsStatistics** 包含以下内容：WinsLookups、Wins Responses、WinsReverseLookups 和 WinsReverseResponses。

### DNSServer01Infrastructure.CimInstance#DnsServerStatistics
此cmdlet为ZoneStatistics参数集输出该对象。该对象包含以下属性：

**名称：** 区域的名称。

`StatsCollectionStartTime` 包含了区域统计数据收集开始的时间。

**ZoneQueryStatistics** 包含以下字段：QueriesFailure、QueriesResponded、QueriesNameError 和 QueriesReceived。查询信息适用于以下资源记录类型：A、AAAA、PTR、CNAME、MX、AFSDB、ATMA、DHCID、DNAME、HINFO、ISDN、MG（邮件组）、MB（邮箱）、MINFO（邮箱信息）、NAPTR（命名权威指针）、NXT（下一个域名）、KEY（公钥）、MR（重命名的邮箱）、RP（负责人）、RT（路由通过）、SRV（服务位置）、SIG（签名）、TXT（文本）、WKS（知名服务）、X.25、DNSKEY、DS、NS 和 SOA。其他记录的相关信息被归类在 “OTHER” 记录类型下；而 “ANY” 类型记录的统计数据则被归类在 “ALL” 记录类型下。

`ZoneTransferStatistics` 包含以下内容：`SuccessSent`、`ResponseReceived`、`RequestSent`、`SuccessReceived`，以及 `TransferType`（可以是 IXFR 或 AXR）。

`ZoneUpdateStatistics` 包含以下两个字段：`DynamicUpdateReceived` 和 `DynamicUpdateRejected`。

## 备注

## 相关链接

[Clear-DnsServerStatistics](./Clear-DnsServerStatistics.md)

