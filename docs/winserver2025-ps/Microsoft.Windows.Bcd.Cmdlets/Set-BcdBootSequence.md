---
external help file: Microsoft.Windows.Bcd.Cmdlets.dll-Help.xml
Module Name: Microsoft.Windows.Bcd.Cmdlets
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.bcd.cmdlets/set-bcdbootsequence?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-BcdBootSequence
---

# Set-BcdBootSequence

## 摘要
{{ 填写剧情概要 }}

## 语法

### AddFirstId
```
Set-BcdBootSequence [-AddFirst] [-Id] <String[]> [[-Store] <BcdStoreInfo>] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### AddFirstEntry
```
Set-BcdBootSequence [-AddFirst] [-Entry] <BcdEntryInfo[]> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### AddLastId
```
Set-BcdBootSequence [-AddLast] [-Id] <String[]> [[-Store] <BcdStoreInfo>] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### AddLastEntry
```
Set-BcdBootSequence [-AddLast] [-Entry] <BcdEntryInfo[]> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RemoveId
```
Set-BcdBootSequence [-Remove] [-Id] <String[]> [[-Store] <BcdStoreInfo>] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### RemoveEntry
```
Set-BcdBootSequence [-Remove] [-Entry] <BcdEntryInfo[]> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ReplaceId
```
Set-BcdBootSequence [-Id] <String[]> [[-Store] <BcdStoreInfo>] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ReplaceEntry
```
Set-BcdBootSequence [-Entry] <BcdEntryInfo[]> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
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
{{ 填充并添加第一段描述 }}

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
{{ 填充最后一段描述 }}

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
{{ 填写条目说明 }}

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
{{ 填写/删除描述 }}

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
请帮我填写店铺描述。

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
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Windows.Bcd Cmdlets.BcdExtensions.BcdEntryInfo[]

## 输出

### System.Object
## 备注

## 相关链接
