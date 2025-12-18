---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterFaultDomain.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusterfaultdomainxml?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterFaultDomainXML
---

# 获取集群故障域的XML信息

## 摘要
将故障域以 XML 字符串的形式获取。

## 语法

```
Get-ClusterFaultDomainXML [-Flags <UInt32>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

## 描述

`Get-ClusterFaultDomainXML` cmdlet 以 XML 字符串的形式获取故障域信息。

## 示例

### 示例 1：以 XML 格式获取集群中的所有故障域

```powershell
Get-ClusterFaultDomainXML
```

这个命令会将集群中所有故障域的信息以XML格式获取到本地节点上。

## 参数

### -AsJob

将cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -Flags

指定一组可选的标志（flags），这些标志可以修改该cmdlet的功能。目前尚不支持任何标志；这些标志保留将来使用。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算出一个最优的限流值（即允许同时运行的操作数量）。这个限流值仅适用于当前的 cmdlet，而不影响整个会话或计算机本身。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Set-ClusterFaultDomainXML](./Set-ClusterFaultDomainXML.md)
