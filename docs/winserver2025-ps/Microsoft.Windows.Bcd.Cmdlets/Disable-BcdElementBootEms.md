---
external help file: Microsoft.Windows.Bcd.Cmdlets.dll-Help.xml
Module Name: Microsoft.Windows.Bcd.Cmdlets
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.bcd.cmdlets/disable-bcdelementbootems?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-BcdElementBootEms
---

# 禁用 BCD 元素的启动功能

## 摘要
{{ 填写剧情简介 }}

## 语法

### 禁用（默认设置）
```
Disable-BcdElementBootEms [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ID
```
Disable-BcdElementBootEms [-Id] <String> [[-Store] <BcdStoreInfo>] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 条目
```
Disable-BcdElementBootEms [-Entry] <BcdEntryInfo> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
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

### -Entry
{{ 填写条目描述 }}

```yaml
Type: Microsoft.Windows.Bcd.Cmdlets.BcdExtensions.BcdEntryInfo
Parameter Sets: Entry
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Force
{{ 填充力描述 }}

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

### -Id
{{ 填充ID描述 }}

```yaml
Type: System.String
Parameter Sets: Id
Aliases: Identifier

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Store
{{ 填写店铺描述 }}

```yaml
Type: Microsoft.Windows.Bcd.Cmdlets.BcdExtensions.BcdStoreInfo
Parameter Sets: Id
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。不过实际上这个cmdlet并没有被运行。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### Microsoft.Windows.Bcd Cmdlets.BcdExtensions.BcdEntryInfo

## 输出

### System.Object
## 备注

## 相关链接
