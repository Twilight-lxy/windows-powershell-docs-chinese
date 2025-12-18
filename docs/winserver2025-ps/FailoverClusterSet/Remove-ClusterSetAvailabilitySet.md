---
external help file: ClusterSetAvailabilitySet.cdxml-help.xml
Module Name: FailoverClusterSet
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusterset/remove-clustersetavailabilityset?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ClusterSetAvailabilitySet
---

# 删除集群集合可用性集

## 摘要
{{ 填写剧情概述 }}

## 语法

### 按名称排序（默认设置）
```
Remove-ClusterSetAvailabilitySet [-AvailabilitySetName] <String[]> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

### ById
```
Remove-ClusterSetAvailabilitySet -Id <UInt64[]> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [<CommonParameters>]
```

### InputObject（cdxml）
```
Remove-ClusterSetAvailabilitySet -InputObject <CimInstance[]> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

## 描述
{{ 填写描述内容 }}

## 示例

### 示例 1
```powershell
PS C:\> {{ Add example code here }}
```

{{ 在这里添加示例描述 }}

## 参数

### -AsJob
{{ 填写工作描述内容 }}

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

### -AvailabilitySetName
{{ Fill AvailabilitySetName Description }}

```yaml
Type: System.String[]
Parameter Sets: ByName
Aliases: Name

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
{{ 填写 CimSession 描述 }}

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

### -Id
{{ 填充ID及描述 }}

```yaml
Type: System.UInt64[]
Parameter Sets: ById
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputObject
{{ 填写 InputObject 的描述内容 }}

```yaml
Type: Microsoft.Management.Infrastructure.CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru
{{ 填充 PassThru 描述 }}

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

### -ThrottleLimit
{{ 填写 ThrottleLimit 的描述 }}

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### System.UInt64[]

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#root/microsoft/windows/cluster/scaleout/MSFT_ClusterSetAvailabilitySet

## 备注

## 相关链接
