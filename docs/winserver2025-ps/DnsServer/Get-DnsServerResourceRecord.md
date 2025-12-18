---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerResourceRecord_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsserverresourcerecord?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServerResourceRecord
---

# 获取 DNS 服务器资源记录

## 摘要
从指定的DNS区域获取资源记录。

## 语法

### 未知
```
Get-DnsServerResourceRecord [[-Name] <String>] [-ComputerName <String>] [-ZoneName] <String> [-Node]
 [-ZoneScope <String>] [-VirtualizationInstance <String>] [-Type] <UInt16> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 名称
```
Get-DnsServerResourceRecord [[-Name] <String>] [-ComputerName <String>] [-ZoneName] <String> [-Node]
 [-ZoneScope <String>] [-VirtualizationInstance <String>] [-RRType <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsServerResourceRecord` cmdlet 可以从域名系统（DNS）区域中获取指定资源记录的以下信息：

- **HostName**
- **RecordType**
- **RecordClass**
- **TimeToLive**
- **Timestamp**
- **RecordData**

## 示例

#### 示例 1：获取指定区域内的所有资源记录
```
PS C:\> Get-DnsServerResourceRecord -ZoneName "contoso.com"
```

这个命令会获取名为 “contoso.com” 的区域中的所有 DNS 服务器资源记录。

### 示例 2：获取指定节点所在区域内的所有资源记录
```
PS C:\> Get-DnsServerResourceRecord -ZoneName "contoso.com" -Name "Admin01"
```

这个命令从名为Admin01的节点中获取名为contoso.com的区域中的所有DNS服务器资源记录。

### 示例 3：根据指定的主机名称获取某个区域中的所有资源记录
```
PS C:\> Get-DnsServerResourceRecord -ZoneName "contoso.com" -Name "Host02"
```

这个命令会获取名为“contoso.com”的区域内所有包含主机名“Host02”的DNS服务器资源记录。该命令与示例2中的命令类似，只不过在这里使用的是主机名而不是节点名称。

### 示例 4：根据指定的主机和类型获取某个区域中所有类型为“A”的记录
```
PS C:\> Get-DnsServerResourceRecord -ZoneName "contoso.com" -Name "Host03" -RRType "A"
```

这个命令会获取名为 contoso.com 的区域中所有名称为 Host03 的 A 记录。

#### 示例 5：获取指定区域内所有类型为“A”的记录
```
PS C:\> Get-DnsServerResourceRecord -ZoneName "contoso.com" -RRType "A"
```

这个命令会获取名为“contoso.com”的区域中的所有A记录。

### 示例 6：获取指定区域根目录下的所有 NS 记录
```
PS C:\> Get-DnsServerResourceRecord -ZoneName "contoso.com" -RRType "NS" -Node
```

这个命令可以获取名为“contoso.com”的区域的根目录下的所有NS记录。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后再显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；若要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
用于指定一个DNS服务器。如果您不指定此参数，命令将在本地系统上运行。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Cn, ForwardLookupPrimaryServer

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定所选区域内的一个节点名称。如果未指定，则默认使用根节点（@）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Node
这表示该命令仅返回由 *Name* 参数指定的节点根目录下的资源记录。如果未指定 **Node**，则将返回该节点的根记录及其所有子记录。

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

### -RRType
指定资源记录的类型。

此参数的可接受值为：

- HInfo
- Afsdb
- Atma
- Isdn
- Key
- Mb
- Md
- Mf
- Mg
- MInfo
- Mr
- Mx
- NsNxt
- Rp
- Rt
- Wks
- X25
- A
- AAAA
- CName
- Ptr
- Srv
- Txt
- Wins
- WinsR
- Ns
- Soa
- NasP
- NasPtr
- DName
- Gpos
- Loc
- DhcId
- Naptr
- RRSig
- DnsKey
- DS
- NSec
- NSec3
- NSec3Param

```yaml
Type: String
Parameter Sets: Name
Aliases:
Accepted values: HInfo, Afsdb, Atma, Isdn, Key, Mb, Md, Mf, Mg, MInfo, Mr, Mx, NsNxt, Rp, Rt, Wks, X25, A, AAAA, CName, Ptr, Srv, Txt, Wins, WinsR, Ns, Soa, NasP, NasPtr, DName, Gpos, Loc, DhcId, Naptr, RRSig, DnsKey, DS, NSec, NSec3, NSec3Param, Tlsa

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
Specifies the maximum number of concurrent operations that can be established to run the cmdlet.
If this parameter is omitted or a value of `0` is entered, then Windows PowerShell® calculates an optimum throttle limit for the cmdlet based on the number of CIM cmdlets that are running on the computer.
The throttle limit applies only to the current cmdlet, not to the session or to the computer.

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

### -Type
指定要获取的记录类型。

```yaml
Type: UInt16
Parameter Sets: Unknown
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VirtualizationInstance
指定该区域将被添加到的虚拟化实例。虚拟化实例是DNS服务器中的逻辑分区，它能够独立托管多个区域及其相关范围。相同名称的区域和区域范围可以托管在不同的虚拟化实例中。此参数是可选的；如果未提供该参数，系统会将该区域添加到默认的虚拟化实例中，而这个默认实例在功能上等同于一个标准的DNS服务器。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ZoneName
指定一个DNS服务器区域的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ForwardLookupZone

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ZoneScope
指定区域范围的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerResourceRecord[]

## 备注

## 相关链接

[Set-DnsServerResourceRecord](./Set-DnsServerResourceRecord.md)

[Add-DnsServerResourceRecord](./Add-DnsServerResourceRecord.md)

[Remove-DnsServerResourceRecord](./Remove-DnsServerResourceRecord.md)

