---
external help file: ClusterSetMember.cdxml-help.xml
Module Name: FailoverClusterSet
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusterset/register-clustersetvm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Register-ClusterSetVM
---

# 注册集群集合虚拟机（Register-ClusterSetVM）

## 摘要
{{ 填写剧情概述 }}

## 语法

### 按名称排序（默认值）
```
Register-ClusterSetVM [-ClusterName] <String[]> [[-VMId] <String>] [-VMName <String>] [-RegisterAll]
 [-AvailabilitySetName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ById
```
Register-ClusterSetVM -Id <UInt64[]> [[-VMId] <String>] [-VMName <String>] [-RegisterAll]
 [-AvailabilitySetName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### InputObject（cdxml）
```
Register-ClusterSetVM -InputObject <CimInstance[]> [[-VMId] <String>] [-VMName <String>] [-RegisterAll]
 [-AvailabilitySetName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
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
{{ 填写为工作描述 }}

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
{{ FillAvailabilitySetName Description }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: AvailabilitySet

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
请帮我填写《CimSession描述》的内容。

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
{{ 填写集群名称并描述该集群的功能 }}

```yaml
Type: System.String[]
Parameter Sets: ByName
Aliases: MemberName, Name

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Id
{{ 填写ID并说明用途 }}

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
请帮我填写《InputObject 描述》中的内容。

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

### -RegisterAll
{{ 填写 “RegisterAll” 的描述内容 }}

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

### -VMId
{{ 填写虚拟机ID并附上说明 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMName
{{ 填写虚拟机名称（VMName）和描述（Description） }}

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

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### System.UInt64[]

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance[]

### Microsoft.ManagementInfrastructure.CimInstance#root/microsoft/windows/cluster/scaleout/MSFT_ClusterSetVM[]

## 备注

## 相关链接
