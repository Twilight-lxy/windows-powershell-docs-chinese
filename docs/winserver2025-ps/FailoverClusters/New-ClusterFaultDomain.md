---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterFaultDomain.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/new-clusterfaultdomain?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ClusterFaultDomain
---

# 新集群故障域（New-ClusterFaultDomain）

## 摘要
在集群中创建一个故障域。

## 语法

```
New-ClusterFaultDomain -Name <String> [-FaultDomain <String>] -FaultDomainType <FaultDomainType>
 [-Description <String>] [-Location <String>] [-Flags <UInt32>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`New-ClusterFaultDomain` cmdlet 用于在集群中创建故障域。此外，在创建故障域时，您还可以指定这些故障域之间的关系。

## 示例

### 示例 1：在现有的故障域中创建一个集群故障域

```powershell
New-ClusterFaultDomain -Type Rack -Name "Rack1" -FaultDomain "Site001"
```

此命令在现有的故障域“Site001”中创建一个类型为“Rack”的集群故障域，命名为“Rack1”。

## 参数

### -AsJob

以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（about_Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -Description

指定此cmdlet创建的集群故障域的描述信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FaultDomain

指定故障域的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Parent

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FaultDomainType

指定此cmdlet创建的故障域的类型。

此参数的可接受值为：

- `Site`
- `Rack`
- `Chassis`
- `Node`

```yaml
Type: FaultDomainType
Parameter Sets: (All)
Aliases: Type
Accepted values: Site, Rack, Chassis, Node

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Flags

在创建集群故障域时需要传递的任何标志（flags）。

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

### -Location

一段用于描述将要创建的集群故障域位置的字符串。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

指定此cmdlet创建的集群故障域的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit

指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值（即并发操作的数量）。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-ClusterFaultDomain](./Get-ClusterFaultDomain.md)

[Remove-ClusterFaultDomain](./Remove-ClusterFaultDomain.md)

[Set-ClusterFaultDomain](./Set-ClusterFaultDomain.md)
