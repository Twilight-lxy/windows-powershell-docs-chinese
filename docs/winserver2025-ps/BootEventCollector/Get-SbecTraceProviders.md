---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/get-sbectraceproviders?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-SbecTraceProviders
---

# Get-SbecTraceProviders

## 摘要
获取 ETW 跟踪提供者（ETW Trace Providers）。

## 语法

```
Get-SbecTraceProviders [-Uncached] [<CommonParameters>]
```

## 描述
`Get-SbecTraceProviders` cmdlet 可以获取 ETW（Event Tracing Windows）跟踪提供程序的列表，并构建用于名称与 GUID 之间相互转换的哈希表。

`Get-SbecTraceProviders` 返回一个哈希表，其中包含以下嵌套的哈希表：

- `<ByName>`: Finds the provider object by name.
- `<ByGuid>`: Finds the provider object by GUID.
- `<NameToGuid>`: Translation of provider name (key) to GUID string (value).
- `<GuidToName>`: Translation of provider GUID (key) to name (value).

当GUID转换为字符串时，会在其末尾添加弯曲的大括号（{ }）。

返回的哈希表也会被保存为缓存，并在后续调用中再次使用。如果定义了任何新的提供者（provider），它们将会被添加到缓存中（从而也会被包含在之前返回的引用中）。

## 示例


## 参数

### -Uncached
表示此操作会绕过缓存。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 哈希表

## 备注

## 相关链接

[Clear-SbecProviderCache](./Clear-SbecProviderCache.md)

