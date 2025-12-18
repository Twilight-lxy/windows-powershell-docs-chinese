---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DnsClientGlobalSetting.cdxml-help.xml
Module Name: DnsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsclient/set-dnsclientglobalsetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsClientGlobalSetting
---

# Set-DnsClientGlobalSetting

## 摘要
设置DNS客户端的全局配置（与特定接口无关）。

## 语法

### 按名称排序（默认值）
```
Set-DnsClientGlobalSetting [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Set-DnsClientGlobalSetting [-InputObject <CimInstance[]>] [-SuffixSearchList <String[]>]
 [-UseDevolution <Boolean>] [-DevolutionLevel <UInt32>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsClientGlobalSettings` cmdlet 用于设置全局 DNS 客户端设置，这些设置是通用的（即不与特定接口关联）。这些设置会影响所有接口上的 DNS 客户端的行为。

## 示例

### 示例 1：设置 DNS 后缀搜索列表
```
PS C:\> Set-DnsClientGlobalSetting -SuffixSearchList @("corp.contoso.com", "na.corp.contoso.com")
```

这个示例将DNS后缀搜索列表设置在了计算机上。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: SwitchParameter
Parameter Sets: InputObject (cdxml)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: InputObject (cdxml)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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

### -DevolutionLevel
指定允许发生回退的标签数量。如果未指定此参数，则使用FRD算法；如果指定了该参数，那么回退过程将一直进行到指定的标签级别为止。当通过组策略已经配置了回退级别的设置时，就不能再修改这个参数的值了。

```yaml
Type: UInt32
Parameter Sets: InputObject (cdxml)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定要传递给此cmdlet的输入数据。您可以使用该参数，也可以通过管道（pipe）将输入数据传递给此cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: InputObject (cdxml)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SuffixSearchList
指定了一组全局后缀，DNS客户端可以按照指定的顺序使用这些后缀来解析计算机名称的IP地址。这些后缀会按指定的顺序被附加到要解析的计算机名称后面。如果后缀搜索列表设置已经通过组策略部署好了，则无法更改此参数的值。

```yaml
Type: String[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: InputObject (cdxml)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseDevolution
该参数用于指示是否启用了“DNS解析过程中的层次递归功能”（即devolution）。启用此功能后，DNS解析器会通过将单标签的未限定域名与父级DNS后缀名称进行拼接来生成新的FQDN（Fully Qualified Domain Name）。这一过程会持续进行，直到域名被成功解析，或者达到在*DevolutionLevel*参数中指定的层级为止。具体来说，解析器会依次去除最左边的域名标签，并继续查找对应的父级后缀。默认值为$True。

需要注意的是：如果已经通过组策略（Group Policy）设置了DNS解析过程中的层次递归功能，那么就无法再修改此参数的值了。

```yaml
Type: Boolean
Parameter Sets: InputObject (cdxml)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root\StandardCimv2\MSFT_DNSClientGlobalSetting
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root\StandardCimv2\MSFT_DNSClientGlobalSetting
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

`MSFT_DNSClientGlobalSetting` 类包含了 DNS 客户端的各种全局设置。这些全局设置包括那些不特定于任何接口的配置选项。

## 备注

## 相关链接

[Get-DnsClientGlobalSetting](./Get-DnsClientGlobalSetting.md)

