---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerZoneScope_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverzonescope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerZoneScope
---

# Add-DnsServerZoneScope

## 摘要
为现有的区域添加一个区域范围（zone scope）。

## 语法

```
Add-DnsServerZoneScope [-ZoneName] <String> [-Name] <String> [-LoadExisting] [-PassThru]
 [-ComputerName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
**Add-DnsServerZoneScope** cmdlet 用于在域名系统（DNS）服务器上的现有区域中添加一个区域范围。DNS 服务器可以从其数据文件中加载现有的区域范围。该范围的名称应遵循与区域名称相同的命名规则；同时，此 cmdlet 所添加的区域范围的名称不能与该区域的名称相同。

当创建一个作用域（scope）时，其数据会保存在名为 `%Systemroot%\system32\dns\<zone name>\scope name>.dns` 的文件中。

## 示例

#### 示例 1：在某个区域上添加一个作用域
```powershell
PS C:\> Add-DnsServerZoneScope -ZoneName "contoso.com" -Name "contoso_NorthAmerica" -Verbose -PassThru
VERBOSE: A scope contoso_NorthAmerica will be added for the zone contoso.com on server Server17.

ZoneScope                 FileName
---------                 --------
contoso_NorthAmerica      contoso_NorthAmerica.dns
```

这个命令会在名为 contoso.com 的现有区域上添加一个新的作用域（scope）。

### 示例 2：为已存在文件的区域添加作用域
```powershell
PS C:\> Add-DnsServerZoneScope -ZoneName "contoso.com" -Name "contoso_NorthAmerica" -LoadExisting -PassThru
ZoneScope                 FileName
---------                 --------
contoso_NorthAmerica      contoso_NorthAmerica.dns
```

此命令用于在名为 contoso.com 的现有区域上添加一个范围（scope）。该命令指定了 *LoadExisting* 参数，因此服务器会从现有的文件中加载该范围。

### 示例 3：添加缓存范围
```powershell
PS C:\> Add-DnsServerZoneScope -ZoneName "..cache" -Name "ContosoScope" -PassThru
ZoneScope             FileName
---------             --------
ContosoScope          cache.dns
```

此命令添加了一个名为 ContosoScope 的缓存范围。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话中或在远程计算机上运行该cmdlet。请输入计算机名称或会话对象，例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果。

默认值是本地计算机上的当前会话。

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
用于指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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
在运行 cmdlet 之前会提示您进行确认。

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

### -LoadExisting
表示服务器会加载该区域的现有文件。如果您不指定此参数，cmdlet 会自动创建默认的区域记录。

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
指定区域范围（zone scope）的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ZoneScope

Required: True
Position: 2
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

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最优限制。此限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被执行。

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

### -ZoneName
指定一个区域的名称。此 cmdlet 会将该区域添加到由该参数指定的区域中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsZoneScope

## 备注

## 相关链接

[Get-DnsServerZoneScope](./Get-DnsServerZoneScope.md)

[Remove-DnsServerZoneScope](./Remove-DnsServerZoneScope.md)

