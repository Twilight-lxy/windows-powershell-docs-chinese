---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDnsConditionalForwarder.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamdnsconditionalforwarder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamDnsConditionalForwarder
---

# 获取 IPAM DNS 条件转发器信息

## 摘要
从 IPAM 数据库中获取有关 DNS 条件转发器的信息。

## 语法

请帮我把这段Markdown格式的文本转换成中文。`
Get-IpamDnsConditionalForwarder [[-ConditionalForwarderName] <String[]>] [[-ServerFqdn] <String[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
请帮我把这段Markdown格式的文本转换成中文。`

## 描述
`Get-IpamDnsConditionalForwarder` cmdlet 可以获取 IP 地址管理（IPAM）数据库中存储的域名系统（DNS）条件转发器的相关信息。条件转发器会根据查询中使用的 DNS 域名，将请求转发到特定的 DNS 服务器。

## 示例

### 示例 1：获取有关所有条件转发器的信息
请帮我把这段Markdown格式的文本转换成中文。`
PS C:\> Get-IpamDnsConditionalForwarder
请帮我把这段Markdown格式的文本转换成中文。`

这个命令可以获取IPAM数据库中所有条件转发器（conditional forwarders）的相关信息。

### 示例 2：获取关于特定条件转发器的信息
请帮我把这段Markdown格式的文本转换成中文。`
PS C:\> Get-IpamDnsConditionalForwarder -ConditionalForwarderName "contoso-internal.com"
请帮我把这段Markdown格式的文本转换成中文。`

这条命令用于获取名为“contoso-internal.com”的条件转发器的相关信息。

### 示例 3：获取服务器上所有条件转发器的信息
请帮我把这段Markdown格式的文本转换成中文。`
PS C:\> Get-IpamDnsConditionalForwarder -ServerFqdn "dns.contoso.com"
请帮我把这段Markdown格式的文本转换成中文。`

这条命令用于获取名为dns.contoso.com的服务器上所有条件转发器（conditional forwarders）的相关信息。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

请帮我把这段Markdown格式的文本转换成中文。`yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
请帮我把这段Markdown格式的文本转换成中文。`

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。请输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

请帮我把这段Markdown格式的文本转换成中文。`yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
请帮我把这段Markdown格式的文本转换成中文。`

### -ConditionalForwarderName
指定此cmdlet获取的条件转发器的名称（以字符串数组的形式）。例如：

`-ConditionalForwarderName "contoso-test.com"`

请帮我把这段Markdown格式的文本转换成中文。

请帮我把这段Markdown格式的文本转换成中文。`yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
请帮我把这段Markdown格式的文本转换成中文。`

### -ServerFqdn
指定托管此cmdlet所获取的条件转发器的DNS服务器的完全限定域名（FQDN）。例如：

`-ServerFqdn "dns.contoso.com"`

请帮我把这段Markdown格式的文本转换成中文。`yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
请帮我把这段Markdown格式的文本转换成中文。`

### -ThrottleLimit
该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算该命令的最佳执行限制。此限制仅适用于当前执行的命令，而不适用于整个会话或计算机本身。

请帮我把这段Markdown格式的文本转换成中文。`yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
请帮我把这段Markdown格式的文本转换成中文。`

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamDnsConditionalForwarder

此cmdlet返回一个对象，该对象表示**IpamDnsConditionalForwarder**类的一个实例。

## 备注

## 相关链接

[Get-IpamDnsResourceRecord](./Get-IpamDnsResourceRecord.md)

[Get-IpamDnsServer](./Get-IpamDnsServer.md)

[Get-IpamDnsZone](./Get-IpamDnsZone.md)
