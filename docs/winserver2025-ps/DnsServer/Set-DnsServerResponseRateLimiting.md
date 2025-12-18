---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerResponseRateLimiting_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverresponseratelimiting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerResponseRateLimiting
---

# Set-DnsServerResponseRateLimiting

## 摘要
在DNS服务器上启用RRL功能。

## 语法

```
Set-DnsServerResponseRateLimiting [-ResponsesPerSec <UInt32>] [-ErrorsPerSec <UInt32>] [-WindowInSec <UInt32>]
 [-IPv4PrefixLength <UInt32>] [-IPv6PrefixLength <UInt32>] [-LeakRate <UInt32>] [-ResetToDefault]
 [-TruncateRate <UInt32>] [-MaximumResponsesPerWindow <UInt32>] [-Mode <String>] [-ComputerName <String>]
 [-PassThru] [-Force] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-DnsServerResponseRateLimiting` cmdlet 可用于在 Windows DNS 服务器上启用响应速率限制（Response Rate Limiting，简称 RRL）。

## 示例

### 示例 1：在 DNS 服务器上设置 RRL 参数
```
PS C:\> Set-DnsServerResponseRateLimiting -WindowInSec 7 -LeakRate 4 -TruncateRate 3 -ErrorsPerSec 8 -ResponsesPerSec 8
```

此命令用于设置DNS服务器上的RRL参数。

### 示例 2：将 RRL 设置重置为默认值
```
PS C:\> Set-DnsServerResponseRateLimiting -ResetToDefault
```

此命令将DNS服务器上的所有RRL参数重置为默认值。

### 示例 3：将 RRL 设置为仅记录日志（LogOnly）模式
```
PS C:\> Set-DnsServerRRL -Mode LogOnly
```

此命令将DNS服务器上的RRL（记录保留逻辑）设置为**LogOnly**模式。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
用于指定远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全qualified域名（FQDN）、主机名或NetBIOS名称。

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
在运行cmdlet之前会提示您确认是否要执行该操作。

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

### -ErrorsPerSec
该参数规定了服务器在一秒钟内向客户端发送错误响应的最大次数。这些错误响应包括：REFUSED、FORMERR 和 SERVFAIL。

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

### -Force
强制命令在不需要用户确认的情况下运行。

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

### -IPv4PrefixLength
指定 IPv4 前缀的长度，该长度表示用于分组传入查询的子网的大小。如果在指定的时间窗口内，导致相同响应的查询发生频率高于预期，服务器会应用 RRL（Rate Limiting）机制。此参数的默认值为 24。

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

### -IPv6PrefixLength
该参数用于指定 IPv6 前缀的长度，这决定了接收到的查询请求被分组的 IPv6 子网的大小。如果在指定的时间窗口内，导致相同响应的查询请求发生频率超过预期，则服务器会应用 RRL（Rate Limiting）机制。此参数的默认值为 56。

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

### -LeakRate
该参数用于指定服务器对因RRL（速率限制）而被丢弃的查询作出响应的频率。对于那些由于符合RRL条件而被丢弃的查询，DNS服务器仍然会按照*LeakRate*的值进行响应。例如，如果*LeakRate*为3，则服务器每3个查询中会回应1个请求。*LeakRate*的有效取值范围是2到10。如果将*LeakRate*设置为0，则不会因为RRL而产生任何响应。这样的设置能够确保使用伪造IP地址的攻击者所在子网内的合法用户仍能收到其有效查询的响应。*LeakRate*的默认值为3。

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

### -MaximumResponsesPerWindow


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

### -Mode
指定DNS服务器上的RRL（Response Rate Limiting）状态。该参数的允许取值为：Enable、Disable或LogOnly。如果模式设置为LogOnly，DNS服务器会执行所有的RRL计算，但不会采取预防性措施（如丢弃或截断响应），而是仅记录这些潜在的操作（就好像RRL处于启用状态一样），并继续发送正常的响应。默认值为Enable。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: LogOnly, Enable, Disable

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -ResetToDefault
表示此 cmdlet 将所有 RRL 设置恢复为其默认值。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ResponsesPerSec
指定服务器在一秒钟的时间间隔内向客户端发送相同响应的最大次数。

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
指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或整个计算机。

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

### -TruncateRate
该参数指定了服务器返回截断响应的频率。对于因符合“RRL（快速丢弃规则，Rapid Rate Dropping）”条件而被丢弃的查询请求，DNS服务器仍会在每 *TruncateRate* 次查询时返回一次截断响应。例如，如果 *TruncateRate* 设置为 2，则每 2 个查询请求中就有 1 个会收到截断响应。通过设置 *TruncateRate*，允许客户端使用 TCP 协议重新连接服务器。该参数的有效取值范围是 2 到 10；如果将其设置为 0，则该功能将被禁用。默认值为 2。

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

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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

### -WindowInSec
指定用于测量和计算RRL（Rate Limiting）指标的时间间隔（以秒为单位）。当来自同一子网的查询在指定时间窗口内频繁触发且每次查询都返回相同的结果时，就会应用RRL机制。默认值为5秒。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerResponseRateLimiting
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DnsServerResponseRateLimitingExceptionlist](./Add-DnsServerResponseRateLimitingExceptionlist.md)

[Get-DnsServerResponseRateLimiting](./Get-DnsServerResponseRateLimiting.md)

[Set-DnsServerResponseRateLimitingExceptionlist](./Set-DnsServerResponseRateLimitingExceptionlist.md)

