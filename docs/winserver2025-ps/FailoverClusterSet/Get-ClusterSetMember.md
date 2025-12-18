---
external help file: ClusterSetMember.cdxml-help.xml
Module Name: FailoverClusterSet
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusterset/get-clustersetmember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterSetMember
---

# 获取集群集合成员

## 摘要
{{ 填写剧情概述 }}

## 语法

### 按名称查找（默认方式）
```
Get-ClusterSetMember [[-ClusterName] <String[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ById
```
Get-ClusterSetMember [-Id <UInt64[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
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
{{ 填写工作描述 }}

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
{{ 填写集群名称及描述 }}

```yaml
Type: System.String[]
Parameter Sets: ByName
Aliases: MemberName, Name

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Id
{{ 填充ID及描述 }}

```yaml
Type: System.UInt64[]
Parameter Sets: ById
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
{{ 填充 ThrottleLimit 的描述 }}

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### System.UInt64[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#root/microsoft/windows/cluster/scaleout/MSFT_ClusterSetMember

## 备注

## 相关链接
