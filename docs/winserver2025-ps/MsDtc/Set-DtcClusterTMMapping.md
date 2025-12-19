---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DtcClusterTMMappingTask_v1.0.cdxml-help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/set-dtcclustertmmapping?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DtcClusterTMMapping
---

# Set-DtcClusterTMMapping

## 摘要
修改现有的集群DTC映射关系。

## 语法

### ServiceSet
```
Set-DtcClusterTMMapping -Name <String> [-ClusterResourceName <String>] [-Local <Boolean>] -Service <String>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ResourceNameSet
```
Set-DtcClusterTMMapping -Name <String> -ClusterResourceName <String> [-Local <Boolean>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### LocalSet
```
Set-DtcClusterTMMapping -Name <String> [-ClusterResourceName <String>] -Local <Boolean>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ExeSet
```
Set-DtcClusterTMMapping -Name <String> [-ClusterResourceName <String>] [-Local <Boolean>]
 -ExecutablePath <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ComPlusSet
```
Set-DtcClusterTMMapping -Name <String> -ComPlusAppId <String> [-ClusterResourceName <String>]
 [-Local <Boolean>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Set-DtcClusterTMMapping` cmdlet 用于修改现有的集群分布式事务协调器（DTC）映射配置。该 cmdlet 仅支持在集群计算机上使用。

## 示例

### 示例 1：修改 DTC 集群映射
```
PS C:\> Set-DtcClusterTMMapping -ExecutablePath "C:\TestApp\SampleApp.exe" -Name "LocalTestAppMapping" -ClusterResourceName "DtcResource2"
```

此命令用于修改现有的DTC集群任务管理器（Task Manager, TM）映射配置。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
指定一个集群DTC资源的名称。此cmdlet会设置该资源对应的TM映射（即资源在系统中的标识）。

```yaml
Type: String
Parameter Sets: ServiceSet, LocalSet, ExeSet, ComPlusSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: ResourceNameSet
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
指定应用程序类型是否为本地类型。如果您指定的值为 $False，则该应用程序属于集群资源。

```yaml
Type: Boolean
Parameter Sets: ServiceSet, ResourceNameSet, ExeSet, ComPlusSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: Boolean
Parameter Sets: LocalSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要添加的 DTC（诊断测试代码）映射的名称。

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

### -Service
指定要与此映射关联的 Windows 服务的名称。

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
指定可以同时运行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算该命令的最佳限制值。此限制仅适用于当前运行的命令，不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### DtcClusterTMMapping

## 备注
* This cmdlet returns a **DtcClusterTMMapping** object that contains modified mapping information.

## 相关链接

[Add-DtcClusterTMMapping](./Add-DtcClusterTMMapping.md)

[Get-DtcClusterTMMapping](./Get-DtcClusterTMMapping.md)

[Remove-DtcClusterTMMapping](./Remove-DtcClusterTMMapping.md)

