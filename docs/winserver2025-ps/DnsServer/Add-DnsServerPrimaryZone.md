---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerPrimaryZone_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverprimaryzone?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerPrimaryZone
---

# Add-DnsServerPrimaryZone

## 摘要
向DNS服务器添加一个主区域。

## 语法

### ADForward LookupZone（默认值）
```
Add-DnsServerPrimaryZone [-ResponsiblePerson <String>] [-DynamicUpdate <String>] [-LoadExisting]
 [-ComputerName <String>] [-PassThru] [-Name] <String> [-ReplicationScope] <String>
 [[-DirectoryPartitionName] <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### FileReverseLookupZone
```
Add-DnsServerPrimaryZone [-ResponsiblePerson <String>] [-DynamicUpdate <String>] [-LoadExisting]
 [-ComputerName <String>] [-PassThru] -NetworkId <String> -ZoneFile <String> [-VirtualizationInstance <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### FileForward LookupZone
```
Add-DnsServerPrimaryZone [-ResponsiblePerson <String>] [-DynamicUpdate <String>] [-LoadExisting]
 [-ComputerName <String>] [-PassThru] [-Name] <String> -ZoneFile <String> [-VirtualizationInstance <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ADReverse LookupZone
```
Add-DnsServerPrimaryZone [-ResponsiblePerson <String>] [-DynamicUpdate <String>] [-LoadExisting]
 [-ComputerName <String>] [-PassThru] [-ReplicationScope] <String> [[-DirectoryPartitionName] <String>]
 -NetworkId <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-DnsServerPrimaryZone` cmdlet 可用于在域名系统（DNS）服务器上添加指定的主区域。

您可以添加一个与 Active Directory 集成的正向查找区域（forward lookup zone）、一个与 Active Directory 集成的反向查找区域（reverse lookup zone），或者一个基于文件的正向查找区域，以及一个基于文件的反向查找区域。

## 示例

#### 示例 1：创建一个主区域
```
PS C:\> Add-DnsServerPrimaryZone -Name "west01.contoso.com" -ReplicationScope "Forest" -PassThru
```

此命令创建了一个与 Active Directory 集成的正向查找区域（forward lookup zone），名为 west01.contoso.com，其复制范围为整个目录林（Forest-wide replication）。

### 示例 2：创建一个基于文件的主区域（primary zone）
```
PS C:\> Add-DnsServerPrimaryZone -Name "west02.contoso.com" -ZoneFile "west02.contoso.com.dns"
```

此命令使用指定的DNS文件创建一个基于文件的primary正向查找区域（forward lookup zone），该区域的名称为west02.contoso.com。

### 示例 3：创建反向查找区域
```
PS C:\> Add-DnsServerPrimaryZone -NetworkID "10.1.0.0/24" -ReplicationScope "Forest"

ZoneName                            ZoneType        IsAutoCreated   IsDsIntegrated  IsReverseLookupZone  IsSigned
--------                            --------        -------------   --------------  -------------------  --------
1.10.in-addr.arpa                   Primary         False           True            True                 False
```

此命令创建了一个与 Active Directory 集成的 Class C 反向查找区域 0.1.10.in-addr.arpa，其复制范围为整个森林（Forest-wide）。

### 示例 4：创建一个基于文件的反向查找区域
```
PS C:\> Add-DnsServerPrimaryZone -NetworkID 10.3.0.0/24 -ZoneFile "0.3.10.in-addr.arpa.dns"
```

此命令创建了一个基于文件的反向查找区域文件 0.3.10.in-addr.arpa。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
Aliases: Cn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -DirectoryPartitionName
指定用于存储区域（zone）的目录分区。当 *ReplicationScope* 参数的值为 “Custom” 时，请使用此参数。

```yaml
Type: String
Parameter Sets: ADForwardLookupZone
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: ADReverseLookupZone
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DynamicUpdate
指定一个区域如何接收动态更新。该参数的可接受值包括：

- None
- Secure
- NonsecureAndSecure

Secure DNS updates are available only for Active Directory-integrated zones.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: None, Secure, NonsecureAndSecure

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LoadExisting
表示服务器会加载该区域对应的现有文件；否则，此cmdlet会自动创建默认的区域记录。此参数仅适用于基于文件的区域（file-backed zones）。

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

### -Name
为该cmdlet创建的区域指定一个名称。

```yaml
Type: String
Parameter Sets: ADForwardLookupZone, FileForwardLookupZone
Aliases: ZoneName

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkId
用于指定反向查找区域的网络ID和前缀长度。对于IPv4，使用格式A.B.C.D/prefix；对于IPv6，使用格式1111:2222:3333:4444::/prefix。

对于 IPv4，该 cmdlet 只能创建 A、B、C 或 D 类的反向查找区域。如果您指定了一个介于不同类别之间的前缀，cmdlet 会使用能够被 8 整除的较长前缀。例如，当输入前缀 “10.2.10.0/23” 时，系统会创建 “10.2.10.0/24” 的反向查找区域，而不会创建 “10.2.11.0/24” 的反向查找区域。如果您输入的前缀长度超过 /24，cmdlet 会创建一个 /32 类型的反向查找区域。

对于 IPv6，该 cmdlet 会为前缀范围从 /16 到 /128 内、且能被 4 整除的地址段创建 ip6.arpa 区域。如果您指定的前缀位于这两个值之间，cmdlet 会使用其中更长且能被 4 整除的前缀。例如，输入 AAAA::/58 时，系统会创建 AAAA::/60 这个 ip6.arpa 区域。如果您不指定前缀，cmdlet 会使用默认的前缀值 /128。

```yaml
Type: String
Parameter Sets: FileReverseLookupZone, ADReverseLookupZone
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个对象，表示您正在操作的该项内容。默认情况下，此 cmdlet 不会生成任何输出。

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

### -ReplicationScope
指定用于存储与 Active Directory 集成的区域的分区。该参数的可接受值包括：

- Custom.
Any custom directory partition that a user creates.
Specify a custom directory partition by using the *DirectoryPartitionName* parameter.
- Domain.
The domain directory partition.
- Forest.
The ForestDnsZone directory partition.
- Legacy.
A legacy directory partition.

```yaml
Type: String
Parameter Sets: ADForwardLookupZone, ADReverseLookupZone
Aliases:
Accepted values: Forest, Domain, Legacy, Custom

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ResponsiblePerson
指定负责该区域的人员。

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

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或整个计算机。

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

### -VirtualizationInstance
指定将要添加区域的虚拟化实例。虚拟化实例是DNS服务器中的逻辑分区，它能够独立托管多个区域及其相关范围。相同名称的区域和区域范围可以托管在不同的虚拟化实例中。该参数是可选的；如果未提供，则系统会将区域添加到默认的虚拟化实例中，该实例在功能上等同于一个标准的DNS服务器。

```yaml
Type: String
Parameter Sets: FileReverseLookupZone, FileForwardLookupZone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

### -ZoneFile
指定区域文件的名称。此参数仅适用于基于文件的DNS系统。

```yaml
Type: String
Parameter Sets: FileReverseLookupZone, FileForwardLookupZone
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerPrimaryZone

## 备注

## 相关链接

[将 zone 转换为 DNS 服务器主区域](./ConvertTo-DnsServerPrimaryZone.md)

[Restore-DnsServerPrimaryZone](./Restore-DnsServerPrimaryZone.md)

[Set-DnsServerPrimaryZone](./Set-DnsServerPrimaryZone.md)

