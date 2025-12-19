---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDnsResourceRecord.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamdnsresourcerecord?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamDnsResourceRecord
---

# Get-IpamDnsResourceRecord

## 摘要
从 IPAM 数据库中获取 DNS 资源记录。

## 语法

请帮我将这段Markdown文档转换成中文。`
Get-IpamDnsResourceRecord [-ZoneName] <String[]> [[-RecordName] <String[]>]
 [[-RecordType] <DnsResourceRecordType[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
请帮我将这段Markdown文档转换成中文。`

## 描述
`Get-IpamDnsResourceRecord` cmdlet 从 IP 地址管理 (IPAM) 服务器数据库中获取域名系统 (DNS) 资源记录。资源记录用于定义 DNS 命名空间的结构和内容。不同的 DNS 元素（如主机、邮件交换机和动态主机配置协议 (DHCP) 服务器）会对应不同类型的资源记录。

## 示例

#### 示例 1：获取某个区域中所有资源记录的信息
请帮我将这段Markdown文档转换成中文。`
PS C:\> Get-IpamDnsResourceRecord -ZoneName "northamerica.contoso.com"
请帮我将这段Markdown文档转换成中文。`

这个命令可以获取名为northamerica.contoso.com的区域的所有DNS资源记录。

### 示例 2：获取关于某种资源记录类型的信息
请帮我将这段Markdown文档转换成中文。`
PS C:\> Get-IpamDnsResourceRecord -ZoneName "northamerica.contoso.com" -RecordType "AAAA"
请帮我将这段Markdown文档转换成中文。`

此命令仅获取名为 northamerica.contoso.com 的区域中类型为 AAAA 的 IPv6 DNS 资源记录。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业的结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

请帮我将这段Markdown文档转换成中文。`yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
请帮我将这段Markdown文档转换成中文。`

### -CimSession
在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

请帮我将这段Markdown文档转换成中文。`yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
请帮我将这段Markdown文档转换成中文。`

### -RecordName
指定此 cmdlet 获取的资源记录的名称。例如：该命令会返回名称为 “host1” 的资源记录。

`-RecordName "host1"`

请帮我将这段Markdown文档转换成中文。

请帮我将这段Markdown文档转换成中文。`yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
请帮我将这段Markdown文档转换成中文。`

### -RecordType
指定此cmdlet获取的DNS资源记录的类型。

此参数的可接受值为：

- A. Address record. Specifies an IPv4 address that is typically used for a host computer.
- AAAA. IPv6 address record. Specifies an IPv6 address that is typically used for a host computer.
- PTR. Pointer record. Specifies a canonical name that is typically used for reverse DNS lookups.
- SOA. Start of authority record. Specifies authoritative information about a DNS zone.
- NS. Name server record. Specifies an authoritative name server for a DNS zone.
- CNAME. Canonical name record that points to a DNS alias.
- DNAME. Delegation name record. Points to a DNS alias and its subnames. This differs from a CNAME record, which points only to an exact name.
- MX. Mail exchange record. Maps a domain name to the mail transfer agents for that domain.
- SRV. Service location record. Specifies the location of services within the domain.
- TXT. Text record. Maintains descriptive text.
- AFSDB. AFS database record. Specifies the location of a database in an Andrew File System cell.
- ATMA. Asynchronous Transfer Mode Address (ATMA) resource record. Maps a DNS domain name in the owner field to an Asynchronous Transfer Mode (ATM) address referenced in the **atm_address** field.
- DHCID. DHCP identifier record. Points to a DHCP server.
- HINFO. System information record. Specifies the host or server's operating system and CPU type.
- ISDN. Integrated Services Digital Network (ISDN) resource record. Maps a domain name to an ISDN telephone number.
- RP. Responsible person record. Maintains information about the person responsible for a domain.
- RT. Route through (RT) resource record. Provides an intermediate host binding for internal hosts that do not have a direct wide area network (WAN) or external network connection.
- WINS. Windows Internet Name Service record.
- WINSR. Windows Internet Name Service reverse-lookup record.
- WKS. Well-known service (WKS) resource record. Describes the well-known TCP/IP services supported by a particular protocol on a specific IP address.
- X25. X-25 resource record. Maps a domain name to a Public Switched Data Network (PSDN) address number.

例如：

`-RecordType "CNAME"`

请帮我将这段Markdown文档转换成中文。`yaml
Type: DnsResourceRecordType[]
Parameter Sets: (All)
Aliases:
Accepted values: A, AAAA, PTR, SOA, NS, CNAME, DNAME, MX, SRV, TXT, AFSDB, ATMA, DHCID, HINFO, ISDN, RP, RT, WINS, WINSR, WKS, X25

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
请帮我将这段Markdown文档转换成中文。`

### -ThrottleLimit
指定可以同时执行该cmdlet的最大操作数量。如果省略此参数或输入值为`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。这个限制仅适用于当前正在执行的cmdlet，而不适用于整个会话或计算机本身。

请帮我将这段Markdown文档转换成中文。`yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
请帮我将这段Markdown文档转换成中文。`

### -ZoneName
指定此cmdlet从中获取资源记录的DNS区域的名称。

请帮我将这段Markdown文档转换成中文。`yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
请帮我将这段Markdown文档转换成中文。`

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamDnsResourceRecord

此cmdlet返回一个**IpamDnsResourceRecord**对象的实例。

## 备注

## 相关链接

[Get-IpamDnsConditionalForwarder](./Get-IpamDnsConditionalForwarder.md)

[Get-IpamDnsServer](./Get-IpamDnsServer.md)

[Get-IpamDnsZone](./Get-IpamDnsZone.md)
