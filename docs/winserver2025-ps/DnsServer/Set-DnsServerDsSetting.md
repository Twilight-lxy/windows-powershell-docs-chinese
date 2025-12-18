---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerDsSetting_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverdssetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerDsSetting
---

# Set-DnsServerDsSetting

## 摘要
修改DNS和Active Directory的设置。

## 语法

```
Set-DnsServerDsSetting [-DirectoryPartitionAutoEnlistInterval <TimeSpan>] [-LazyUpdateInterval <UInt32>]
 [-MinimumBackgroundLoadThreads <UInt32>] [-RemoteReplicationDelay <UInt32>] [-ComputerName <String>]
 [-PollingInterval <UInt32>] [-TombstoneInterval <TimeSpan>] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsServerDsSetting` cmdlet 用于修改域名系统（DNS）和 Active Directory 的相关设置。

注意：如果任何集合操作失败，**Set-DnsServerDsSetting** cmdlet 严禁终止。它必须继续执行其他操作，并显示修改后的设置结果。

## 示例

#### 示例 1：为目录分区设置自动加入间隔时间
```
PS C:\> Set-DnsServerDsSetting -DirectoryPartitionAutoEnlistInterval 15.00:00:00 -PassThru

PollingInterval(s)                   : 180
TombstoneInterval                    : 14.00:00:00
DirectoryPartitionAutoEnlistInterval : 15.00:00:00
LazyUpdateInterval(s)                : 3
MinimumBackgroundLoadThreads         : 1
RemoteReplicationDelay(s)            : 30
```

此命令将目录分区的自动注册间隔设置为15天。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
用于指定一个 DNS 服务器。该参数的可接受值包括：IPv4 地址；IPv6 地址；以及任何能够解析为 IP 地址的其他值，例如完全限定域名（FQDN）、主机名或 NETBIOS 名称。

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

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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

### -DirectoryPartitionAutoEnlistInterval
该参数用于指定DNS服务器尝试加入DNS域名分区（DNS Domain Partition）和DNS林分区（DNS Forest Partition）的间隔时间（前提是服务器尚未加入这些分区）。建议将此值限制在1小时到180天之间（包括两端的时间），不过您也可以使用其他任何数值。默认情况下，我们建议您将该值设置为1天。需要注意的是：当需要将某个参数设置为默认值时，必须将其值设为0（零）；不过在这种情况下，0可以被理解为一个普通数值而非特殊标志。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LazyUpdateInterval
该参数用于指定一个以秒为单位的值，用于确定DNS服务器在处理DNS动态更新请求的同时，向目录服务器提交更新的频率（无需同时使用LDAP_SERVER_LAZY_COMMIT OID控制项（[MS-ADTS]第3.1.1.3.4.1.7节））。建议将此值的范围限制在0x00000000到0x0000003c之间。默认值应设置为0x00000003；若要将DNS服务器设置为在处理DNS动态更新请求时不使用LDAP_SERVER_LAZY_COMMIT OID控制项，请将此值设为0。有关LDAP_SERVER_LAZY_COMMITOID的更多信息，请参阅[LDAP_SERVER_LAZY_COMMIT_OID控制项代码](https://technet.microsoft.com/en-us/library/aa366982)。

`LDAP_SERVER_LAZY_COMMIT OID` 控制参数指示 DNS 服务器在内存中完成目录服务修改命令的执行后，但在将结果写入磁盘之前立即返回这些结果。这样一来，服务器可以快速地返回查询结果，并在不会影响性能的情况下将数据保存到磁盘中。

DNS服务器必须仅将此控制信息发送给与该LDAP更新相关联的目录服务器。该LDAP更新是由DNS服务器在接收到DNS动态更新请求后发起的。

如果该值为非零，则在处理DNS动态更新请求期间发生的LDAP更新操作不得指定`LDAP_SERVER_LAZY_COMMIT OID`控制参数（除非自上次使用该控制参数的LDAP更新以来已经过去了小于`DsLazyUpdateInterval`秒的时间）。如果超过了`DsLazyUpdateInterval`秒的时间段，在此期间DNS服务器没有执行任何使用该控制参数的LDAP更新操作，那么在下次更新时DNS服务器必须指定该控制参数。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MinimumBackgroundLoadThreads
指定 DNS 服务器用于从目录服务中加载区域数据的后台线程的最小数量。此值必须限制在 0x00000000 到 0x00000005（包含这两个值）的范围内。默认值应设置为 0x00000001，同时应将值 0 视为该默认值的标志位。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -PollingInterval
指定DNS服务器查询Active Directory域服务（AD DS）以获取与Active Directory集成区域相关的更改的频率。该值必须限制在30秒到3600秒之间的范围内（包括两端）。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RemoteReplicationDelay
该参数指定了DNS服务器在检测到远程目录服务器上的某个对象发生变化后，到尝试复制该对象变化数据之间的最小等待时间间隔（以秒为单位）。此值必须介于0x00000005到0x00000E10之间（包括这两个端点）。默认值为0x0000001E；同时，数值“0”应被视为该默认值的标识符/标志。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最优限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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

### -TombstoneInterval
该参数用于指定 DNS 在 Active Directory 中保持“墓碑记录”（tombstoned records）有效状态的时长。建议将此值设置为 3 天到 8 周之间（包含两端时间），但您可以将其设置为 82 小时到 8 周之间的任何值。推荐将默认值设为 14 天，并将值为 0 的情况视为表示使用默认设置的标志；不过，您也可以允许该值为 0 并按其字面意义进行解析。

每天当地时间凌晨2:00，DNS服务器必须搜索所有目录服务区域中的节点，查找那些将Active Directory的`dnsTombstoned`属性设置为`True`的节点，并且查找其目录服务的`EntombedTime`（MS-DNSP第2.2.2.2.3.23节中定义）值大于之前设置的`DSTombstoneInterval`秒数的节点。你必须将这些节点从目录服务器中永久删除。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerDsSetting

## 备注

## 相关链接

[DNS服务器的整数属性](https://msdn.microsoft.com/en-us/library/cc422472(v=prot.10))

[[MS-DNSP]：域名服务（DNS）服务器管理协议规范](https://msdn.microsoft.com/en-us/library/cc448821(v=prot.10))

[Get-DnsServerDsSetting](./Get-DnsServerDsSetting.md)

