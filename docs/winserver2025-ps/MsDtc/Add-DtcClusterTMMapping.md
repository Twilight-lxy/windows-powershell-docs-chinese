---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DtcClusterTMMappingTask_v1.0.cdxml-help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/add-dtcclustertmmapping?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DtcClusterTMMapping
---

# Add-DtcClusterTMMapping

## 摘要
添加一个集群DTC（诊断跟踪代码）映射关系。

## 语法

### ServiceSet
```
Add-DtcClusterTMMapping -Name <String> -ClusterResourceName <String> -Local <Boolean> [-PassThru]
 -Service <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ExeSet
```
Add-DtcClusterTMMapping -Name <String> -ClusterResourceName <String> -Local <Boolean> [-PassThru]
 -ExecutablePath <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ComPlusSet
```
Add-DtcClusterTMMapping -Name <String> -ClusterResourceName <String> -ComPlusAppId <String> -Local <Boolean>
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Add-DtcClusterTM Mapping` cmdlet 用于添加集群中的分布式事务协调器（DTC）映射信息。此 cmdlet 仅支持在集群计算机上使用。

## 示例

### 示例 1：创建一个集群映射
```
PS C:\> Add-DtcClusterTMMapping -ClusterResourceName "DtcResource1" -ExecutablePath "C:\TestApp\App.exe" -Local $False -Name "LocalTestAppMapping"
```

此命令用于创建一个DTC集群的事务管理器（Transaction Manager, TM）映射关系。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的任务。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -ClusterResourceName
指定集群DTC资源的名称。此cmdlet将此映射与名称所指定的资源关联起来。

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

### -ComPlusAppId
指定要与此映射关联的 COM+ 应用程序标识符。

```yaml
Type: String
Parameter Sets: ComPlusSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExecutablePath
指定要与此映射关联的应用程序的路径。

```yaml
Type: String
Parameter Sets: ExeSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Local
该参数用于指定应用程序类型是否为本地类型的。如果指定值为 `$False`，则表示该应用程序是一个集群资源；如果应用程序类型是本地的，则该应用程序会映射到本地 DTC 实例，此时cmdlet会忽略 `**ClusterResourceName**` 参数的值。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要添加的 DTC 映射的名称。

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

### -PassThru
返回一个对象，该对象代表您正在操作的项。默认情况下，此cmdlet不会生成任何输出。

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

### -Service
指定要与此映射关联的Windows服务的名称。

```yaml
Type: String
Parameter Sets: ServiceSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算出一个最优的并发限制。这个并发限制仅适用于当前运行的命令，而不涉及整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-DtcClusterTMMapping](./Get-DtcClusterTMmapping.md)

[Remove-DtcClusterTMMapping](./Remove-DtcClusterTM Mapping.md)

[Set-DtcClusterTMMapping](./Set-DtcClusterTMMapping.md)

