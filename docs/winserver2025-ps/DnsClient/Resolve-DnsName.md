---
external help file: dnslookup.dll-Help.xml
Module Name: DnsClient
ms.date: 05/20/2019
online version: https://learn.microsoft.com/powershell/module/dnsclient/resolve-dnsname?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Resolve-DnsName
---

# 解析DNS名称

## 摘要
执行对指定名称的DNS名称查询解析操作。

## 语法

```
Resolve-DnsName [-Name] <String> [[-Type] <RecordType>] [-Server <String[]>] [-DnsOnly] [-CacheOnly]
 [-DnssecOk] [-DnssecCd] [-NoHostsFile] [-LlmnrNetbiosOnly] [-LlmnrFallback] [-LlmnrOnly] [-NetbiosFallback]
 [-NoIdn] [-NoRecursion] [-QuickTimeout] [-TcpOnly] [<CommonParameters>]
```

## 描述
` Resolve-DnsName` cmdlet 用于对指定的名称执行 DNS 查询。该 cmdlet 在功能上类似于 `nslookup` 工具，用户可以使用它来查询各种名称信息。

## 示例

### 示例 1
```
PS C:\> Resolve-DnsName -Name www.bing.com
```

这个示例使用默认选项来解析一个名称。

### 示例 2
```
PS C:\> Resolve-DnsName -Name www.bing.com -Server 10.0.0.1
```

这个示例通过地址为 10.0.0.1 的 DNS 服务器来解析一个名称。

### 示例 3
```
PS C:\> Resolve-DnsName -Name www.bing.com -Type A
```

这个示例用于查询名称为 “www.bing.com” 的 A 类型记录。

### 示例 4
```
PS C:\> Resolve-DnsName -Name www.bing.com -DnsOnly
```

这个示例仅使用 DNS 来解析名称，不会发起 LLMNR 或 NetBIOS 查询。

## 参数

### -CacheOnly
仅使用本地缓存来解决此查询问题。

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

### -DnsOnly
仅使用DNS协议来解决此查询问题。

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

### -DnssecCd
为此次查询设置DNSSEC检查禁用位（即该位被设置为“0”）。

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

### -DnssecOk
为此次查询设置DNSSEC OK标志。

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

### -LlmnrFallback
当使用 DNS 解决此查询失败时，允许回退到 LLMNR 协议。

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

### -LlmnrNetbiosOnly
仅使用 LLMNR 或 NetBIOS 协议来解决此查询。

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

### -LlmnrOnly
仅使用 LLMNR 协议来解决此查询问题。

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

### -Name
指定要解析的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -NetbiosFallback
当使用 DNS 解决此查询失败时，允许回退到 NetBIOS 协议。

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

### -NoHostsFile
在解析此查询时跳过主机文件（hosts file）。

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

### -NoIdn
指定不要对查询使用 IDN 编码逻辑。

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

### -NoRecursion
指示服务器在解析此查询时不要使用递归。

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

### -QuickTimeout
为这个查询使用更短的超时时间。

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

### -Server
指定要查询的DNS服务器的IP地址或主机名。如果未提供此参数，默认情况下会查询接口自带的DNS服务器。

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

### -TcpOnly
此查询仅使用TCP协议进行通信。

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

### -Type
指定要发出的DNS查询类型。默认情况下，查询类型为A_AAAA，此时会同时查询A类型和AAAAA类型的记录。该参数可接受的值包括：

-- UNKNOWN = 0,

-- A_AAAA = 0，表示DNS查询类型为A_AAAA。

-- A 的值为 1，表示 DNS 查询类型为 IPv4 服务器地址。

-- AAAA 的值为 28，表示该 DNS 查询类型是用于获取 IPv6 服务器地址的请求。

-- NS = 2，表示DNS查询类型为“名称服务器”（name server）。

-- MX = 15，表示DNS查询类型是邮件路由信息。

-- MD = 3，表示DNS查询类型为邮件地址（即邮件接收目的地）。

-- MF = 4，表示DNS查询类型为“邮件转发器”（mail forwarder）。

-- CNAME = 5：表示DNS查询类型为“规范名称”（canonical name）。

-- SOA = 6，表示DNS查询类型为“权威区域起始（start of authority zone）”。

-- MB 的值为 7，表示 DNS 查询类型是邮箱域名（mailbox domain name）。

-- MG = 8，表示DNS查询类型为“邮件组成员”（mail group member）。

-- MR = 9，DNS查询类型是“邮件重命名名称”（mail rename name）。

-- NULL = 10：表示DNS查询类型为空资源记录（null resource record）。

-- WKS = 11，表示DNS查询类型为“well-known service”（众所周知的服务）。

-- PTR = 12：表示DNS查询类型为“域名指针”（Domain Name Pointer）。

-- HINFO = 13，表示DNS查询类型为主机信息（host information）。

-- MINFO = 14，表示DNS查询类型是邮件箱信息。

-- TXT = 16：表示DNS查询类型为文本字符串（text strings）。

-- RP = 17，表示DNS查询类型为“负责人”（Responsible Person）。

-- AFSDB = 18：表示DNS查询的类型是AFS数据库服务器。

-- X25 = 19，表示DNS查询类型为分组交换广域网（packet-switched wide area network）。

-- ISDN = 20，表示DNS查询类型是综合业务数字网（Integrated Services Digital Network）。

-- RT = 21，表示DNS查询类型为“DNS路由穿透”（DNS Route Through）。

-- SRV = 33：这种DNS查询类型用于服务器选择。

-- DNAME = 39：表示DNS查询类型为域名别名（domain aliases）。

-- OPT = 41，表示DNS查询类型为DNS选项（DNS Option）。

-- DS = 43，DNS查询类型表示“授权签名者”（delegation signer）。

-- RRSIG = 46，表示DNS查询类型为DNSSEC签名。

-- NSEC = 47，表示DNS查询类型为“下一条安全记录”（next-secure record）。

-- DNSKEY = 48，表示DNS查询类型为DNS密钥记录。

-- DHCID = 49，表示DNS查询类型是动态主机配置协议（Dynamic Host Configuration Protocol）的相关信息。

-- NSEC3 = 50，表示DNS查询类型为NSEC记录的第3版（version 3）。

-- NSEC3PARAM = 51，表示DNS查询类型为NSEC3参数。

-- ANY = 255：表示DNS查询类型为通配符匹配（即匹配所有可能的域名）。

-- ALL = 255，表示DNS查询类型为通配符匹配。

```yaml
Type: RecordType
Parameter Sets: (All)
Aliases:
Accepted values: UNKNOWN, A_AAAA, A, NS, MD, MF, CNAME, SOA, MB, MG, MR, NULL, WKS, PTR, HINFO, MINFO, MX, TXT, RP, AFSDB, X25, ISDN, RT, AAAA, SRV, DNAME, OPT, DS, RRSIG, NSEC, DNSKEY, DHCID, NSEC3, NSEC3PARAM, ANY, ALL, WINS

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无

## 输出

### Microsoft.DnsClient Commands.DnsRecord
DnsRecord对象包含了针对指定DNS查询从网络中返回的所有记录。

## 备注

## 相关链接

[TechNet上的Nslookup介绍](https://go.microsoft.com/fwlink/p/?LinkId=84907)

