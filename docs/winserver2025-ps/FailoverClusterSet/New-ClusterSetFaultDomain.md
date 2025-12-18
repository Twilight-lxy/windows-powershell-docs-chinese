---
external help file: ClusterSetFaultDomain.cdxml-help.xml
Module Name: FailoverClusterSet
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusterset/new-clustersetfaultdomain?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ClusterSetFaultDomain
---

# 新集群集故障域（New-ClusterSetFaultDomain）

## 摘要
{{ 填写剧情简介 }}

## 语法

```
New-ClusterSetFaultDomain [-FDName] <String> [-ClusterName <String[]>]
 -FDType <MSCluster_ClusterSet_FaultDomainType> [-Description <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
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
{{ 填充为工作描述 }}

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

### -ClusterName
请帮我填写《ClusterName描述》的相关内容。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: MemberCluster

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Description
{{ 填写描述内容 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FDName
{{ 填写 FDName 说明 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Name

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FDType
{{ 填写 FD 类型描述 }}

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.MSCLUSTER.MSFT_ClusterSetFaultDomain.MSCluster_ClusterSet_FaultDomainType
Parameter Sets: (All)
Aliases: FaultDomainType
Accepted values: Logical

Required: True
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#root/microsoft/windows/cluster/scaleout/MSFT_ClusterSetFaultDomain

## 备注

## 相关链接
