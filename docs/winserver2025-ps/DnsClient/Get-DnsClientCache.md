---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DnsClientCache.cdxml-help.xml
Module Name: DnsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsclient/get-dnsclientcache?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsClientCache
---

# Get-DnsClientCache

## 摘要
检索DNS客户端缓存的内容。

## 语法

```
Get-DnsClientCache [[-Entry] <String[]>] [-Name <String[]>] [-Type <Type[]>] [-Status <Status[]>]
 [-Section <Section[]>] [-TimeToLive <UInt32[]>] [-DataLength <UInt16[]>] [-Data <String[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsClientCache` cmdlet 用于检索本地 DNS 客户端缓存的内容。

## 示例

### 示例 1：获取 DNS 客户端缓存
```
PS C:\> Get-DnsClientCache
```

这个示例用于获取DNS客户端缓存中的内容。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

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
在远程会话或远程计算机上运行该cmdlet。输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，使用的是本地计算机上的当前会话。

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

### -Data
指定记录数据。

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

### -DataLength
指定记录数据的长度。

```yaml
Type: UInt16[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Entry
指定缓存条目的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定记录名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RecordName

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Section
指定记录部分（record section）。该参数可接受的值包括：

- Answer
- Authority
- Additional

```yaml
Type: Section[]
Parameter Sets: (All)
Aliases:
Accepted values: Answer, Authority, Additional

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Status
指定记录的状态。该参数的可接受值为：

- Success
- NotExist
- NoRecords

```yaml
Type: Status[]
Parameter Sets: (All)
Aliases:
Accepted values: Success, NotExist, NoRecords

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -TimeToLive
指定记录的生存时间（即数据在系统中保留的时间），单位为秒。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases: TTL

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Type
指定记录类型。该参数的可接受值为：

- A
- NS
- CNAME
- SOA
- PTR
- MX
- AAAA
- SRV

```yaml
Type: Type[]
Parameter Sets: (All)
Aliases: RecordType
Accepted values: A, NS, CNAME, SOA, PTR, MX, AAAA, SRV

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### None

## 输出

### Microsoft.Management.Infrastructure.CimInstance#root\StandardCimv2\MSFT_DnsClientCache
The `Microsoft.Management.Infrastructure.CimInstance` object is a wrapper class that displays Windows Management Instrumentation (WMI) objects.
The path after the pound sign (`#`) provides the namespace and class name for the underlying WMI object.

The **MSFT_DnsClientCache** object contains all of the entries in the DNS client cache.

## 备注

## 相关链接

[Clear-DnsClientCache](./Clear-DnsClientCache.md)

