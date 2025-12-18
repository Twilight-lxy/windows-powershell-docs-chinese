---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DnsClientGlobalSetting.cdxml-help.xml
Module Name: DnsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsclient/get-dnsclientglobalsetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsClientGlobalSetting
---

# Get-DnsClientGlobalSetting

## 摘要
检索全局DNS客户端设置，例如后缀搜索列表。

## 语法

```
Get-DnsClientGlobalSetting [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsClientGlobalSetting` cmdlet 用于检索全局性的 DNS 客户端设置，这些设置并不与特定的接口关联。这些设置会影响所有接口上的 DNS 客户端的行为。

## 示例

### 示例 1：获取全局 DNS 客户端设置
```
PS C:\> Get-DnsClientGlobalSetting
UseSuffixSearchList : True
SuffixSearchList    : {corp.contoso.com, na.corp.contoso.com}
UseDevolution       : True
DevolutionLevel     : 0
```

这个示例获取了所有的全局DNS客户端设置。

### 示例 2：获取与连接相关的后缀
```
PS C:\> $dnsCGSetting = Get-DnsClientGlobalSetting
PS C:\> $dnsCGSetting.SuffixSearchList
corp.contoso.com
na.corp.contoso.com
```

这个示例用于获取与连接相关的后缀信息。列表中的第一个条目是主要的DNS后缀（如果已配置的话）。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值为本地计算机上的当前会话。

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

### -ThrottleLimit
该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值（即并发操作的最多数量）。该限制仅适用于当前执行的 cmdlet，而不影响整个会话或整个计算机。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root\StandardCimv2\MSFT_DNSClientGlobalSetting
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Set-DnsClientGlobalSetting](./Set-DnsClientGlobalSetting.md)

