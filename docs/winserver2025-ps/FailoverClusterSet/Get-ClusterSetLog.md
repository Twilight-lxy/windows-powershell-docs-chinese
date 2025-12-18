---
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusterSet
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusterset/get-clustersetlog?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterSetLog
---

# 获取集群集日志

## 摘要
{{ 填写剧情简介 }}

## 语法

### InputObject（默认值）
```
Get-ClusterSetLog [-Node <StringCollection>] [-IncludeClusterLog] [-IncludeManagementClusterLog]
 [-TimeSpanInMinutes <UInt32>] [-DestinationFolderPath <String>] [-UseLocalTime] [-SkipClusterSetState]
 [-NoCollateLogs] [<CommonParameters>]
```

### ClusterSetCimSession
```
Get-ClusterSetLog [-ClusterSetCimSession <CimSession>] [-Node <StringCollection>] [-IncludeClusterLog]
 [-IncludeManagementClusterLog] [-TimeSpanInMinutes <UInt32>] [-DestinationFolderPath <String>] [-UseLocalTime]
 [-SkipClusterSetState] [-NoCollateLogs] [<CommonParameters>]
```

## 描述
{{ 请填写描述内容 }}

## 示例

### 示例 1
```powershell
PS C:\> {{ Add example code here }}
```

{{ 在这里添加示例描述 }}

## 参数

### -ClusterSetCimSession
{{ 填写 ClusterSetCimSession 的描述内容 }}

```yaml
Type: Microsoft.Management.Infrastructure.CimSession
Parameter Sets: ClusterSetCimSession
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -DestinationFolderPath
{{ 填写目标文件夹路径描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Destination

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeClusterLog
{{ 填写内容：包含集群日志描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeManagementClusterLog
{{ Fill IncludeManagementClusterLog Description }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoCollateLogs
{{ Fill NoCollateLogs Description }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Node
{{ 填充节点描述 }}

```yaml
Type: System.Collections.Specialized.StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipClusterSetState
生成集群集日志，但不检索集群集的状态信息。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: scs

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TimeSpanInMinutes
{{ Fill(TimeSpanInMinutes Description }}

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: TimeSpan

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseLocalTime
使用本地时间而不是GMT来生成集群日志。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: lt

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimSession

## 输出

### System.IO.FileInfo

## 备注

## 相关链接

[https://go.microsoft.com/fwlink/?LinkId=216212]

