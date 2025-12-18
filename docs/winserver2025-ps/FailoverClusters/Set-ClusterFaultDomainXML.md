---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterFaultDomain.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/set-clusterfaultdomainxml?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ClusterFaultDomainXML
---

# 设置集群故障域XML

## 摘要
使用XML设置集群故障域。

## 语法

```
Set-ClusterFaultDomainXML [-XML] <String> [-Flags <UInt32>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`Set-ClusterFaultDomainXML` cmdlet 使用 XML 来设置集群故障域。

## 示例

### 示例 1

```powershell
Set-ClusterFaultDomainXML -XML @"
<Topology>
 <Site Name="site1" Description="Site 1 with 4 nodes" Location="Site 1">
  <rack name="rack1_in_site_1" description="the only rack in site 1">
   <Node Name="K0617-VM02"/>
   <Node Name="K0617-VM03"/>
   <Node Name="K0617-VM04"/>
   <Node Name="K0617-VM05"/>
  </rack>
 </Site>
 <Site Name="site2" Description="Site 2 with 4 nodes" Location="Site 2">
  <rack name="rack1_in_site_2" description="the only rack in site 2">
   <Node Name="K0617-VM12"/>
   <Node Name="K0617-VM13"/>
   <Node Name="K0617-VM14"/>
   <Node Name="K0617-VM15"/>
  </rack>
 </Site>
 <Site Name="site3" Description="Site 3 with 4 nodes" Location="Site 3">
  <rack name="rack1_in_site_3" description="the only rack in site 3">
   <Node Name="K0621-VM17"/>
   <Node Name="K0621-VM18"/>
   <Node Name="K0621-VM19"/>
   <Node Name="K0621-VM20"/>
  </rack>
 </Site>
 <Site Name="site4" Description="Site 4 with 4 nodes" Location="Site 4">
  <rack name="rack1_in_site_4" description="the only rack in site 4">
   <Node Name="K0629-VM07"/>
   <Node Name="K0629-VM08"/>
   <Node Name="K0629-VM09"/>
   <Node Name="K0629-VM10"/>
  </rack>
 </Site>
</Topology>
"@
```

此命令使用示例中的XML配置来设置集群的故障域。

## 参数

### -AsJob

以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

指定在设置集群故障域时需要传递的任何标志（flags）。

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

该参数用于指定可以同时运行的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -XML

指定一个包含XML的字符串形式，该XML描述了需要将集群故障域设置为何值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-ClusterFaultDomainXML](./Get-ClusterFaultDomainXML.md)
