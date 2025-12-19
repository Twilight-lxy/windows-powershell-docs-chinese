---
external help file: Microsoft.Windows.Bcd.Cmdlets.dll-Help.xml
Module Name: Microsoft.Windows.Bcd.Cmdlets
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.bcd.cmdlets/set-bcdboottoolsdisplayorder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-BcdBootToolsDisplayOrder
---

# 设置 BCD 启动工具的显示顺序

## 摘要
{{ 填写剧情概要 }}

## 语法

### AddFirstId
```
Set-BcdBootToolsDisplayOrder [-AddFirst] [-Id] <String[]> [[-Store] <BcdStoreInfo>] [-Force] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### AddFirstEntry
```
Set-BcdBootToolsDisplayOrder [-AddFirst] [-Entry] <BcdEntryInfo[]> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### AddLastId
```
Set-BcdBootToolsDisplayOrder [-AddLast] [-Id] <String[]> [[-Store] <BcdStoreInfo>] [-Force] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### AddLastEntry
```
Set-BcdBootToolsDisplayOrder [-AddLast] [-Entry] <BcdEntryInfo[]> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### RemoveId
```
Set-BcdBootToolsDisplayOrder [-Remove] [-Id] <String[]> [[-Store] <BcdStoreInfo>] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### RemoveEntry
```
Set-BcdBootToolsDisplayOrder [-Remove] [-Entry] <BcdEntryInfo[]> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ReplaceId
```
Set-BcdBootToolsDisplayOrder [-Id] <String[]> [[-Store] <BcdStoreInfo>] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ReplaceEntry
```
Set-BcdBootToolsDisplayOrder [-Entry] <BcdEntryInfo[]> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
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

### -AddFirst
{{ 填充并添加第一个描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AddFirstId, AddFirstEntry
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AddLast
{{ 填充最后一段描述内容 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AddLastId, AddLastEntry
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Entry
{{ 填写条目描述 }}

```yaml
Type: Microsoft.Windows.Bcd.Cmdlets.BcdExtensions.BcdEntryInfo[]
Parameter Sets: AddFirstEntry, AddLastEntry, RemoveEntry, ReplaceEntry
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Force
{{ 填充力的描述 }}

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
{{ 填充ID说明 }}

```yaml
Type: System.String[]
Parameter Sets: AddFirstId, AddLastId, RemoveId, ReplaceId
Aliases: Identifier

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Remove
{{ 填充/删除描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: RemoveId, RemoveEntry
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Store
{{ 填写店铺描述 }}

```yaml
Type: Microsoft.Windows.Bcd.Cmdlets.BcdExtensions.BcdStoreInfo
Parameter Sets: AddFirstId, AddLastId, RemoveId, ReplaceId
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Windows.Bcd Cmdlets.BcdExtensions.BcdEntryInfo[]

## 输出

### System.Object
## 备注

## 相关链接
