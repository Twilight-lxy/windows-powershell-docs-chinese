---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_HgsClientConfiguration_v1.0.cdxml-help.xml
Module Name: HgsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsclient/get-hgsclientconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-HgsClientConfiguration
---

# Get-HgsClientConfiguration

## 摘要
获取Host Guardian Service客户端的配置信息。

## 语法

```
Get-HgsClientConfiguration [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述

`Get-HgsClientConfiguration` cmdlet 用于获取本地 Host Guardian Service 客户端的配置信息。

## 示例

### 示例 1：获取客户端配置信息

```powershell
Get-HgsClientConfiguration
```

这个命令用于获取本地Host Guardian Service客户端的配置信息。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: System.Diagnostics.Switch
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession

在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: Microsoft.Management.Infrastructure.CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell 会根据计算机上正在运行的 CIM cmdlet 数量来计算相应的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不影响整个会话或计算机本身的性能。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### CimInstance#MSFT_HgsClientConfiguration

此 cmdlet 以 **CimInstance** 对象的形式返回 Host Guardian Service 客户端的配置信息。**Microsoft.ManagementInfrastructure.CimInstance** 是一个包装类，用于显示 Windows Management Instrumentation (WMI) 对象。井号（`#`）后面的路径指定了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Set-HgsClientConfiguration](./Set-HgsClientConfiguration.md)
