---
external help file: Microsoft.Windows.DeliveryOptimization.AdminCommands.dll-Help.xml
Module Name: DeliveryOptimization
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/deliveryoptimization/get-deliveryoptimizationlog?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DeliveryOptimizationLog
---

# 获取交付优化日志

## 摘要
{{ 填写剧情简介 }}

## 语法

```
Get-DeliveryOptimizationLog [-LevelFilter <UInt32>] [-Provider <ProviderType>] [[-Path] <String[]>]
 [-Flush] [<CommonParameters>]
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

### -Flush

{{ 填充说明（Fill Description） }}

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

### -LevelFilter

{{ 填充级别过滤器描述 }}

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

{{ 填充路径描述 }}

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: PSPath

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Provider

{{ 填写提供商描述 }}

```yaml
Type: Microsoft.Windows.DeliveryOptimization.AdminCommands.ProviderType
Parameter Sets: (All)
Aliases:
Accepted values: Dosvc, Domgmt

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### Microsoft.Windows.DeliveryOptimizationAdmin Commands.LogOutput

## 备注

## 相关链接
