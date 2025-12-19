---
external help file: Microsoft.Windows.Bcd.Cmdlets.dll-Help.xml
Module Name: Microsoft.Windows.Bcd.Cmdlets
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.bcd.cmdlets/set-bcdelement?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-BcdElement
---

# Set-BcdElement

## 摘要
{{ 填写剧情简介 }}

## 语法

### ID
```
Set-BcdElement [-Element] <String> [[-Id] <String>] [[-Store] <BcdStoreInfo>] -Type <ElementType> [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 设备ID
```
Set-BcdElement [-Element] <String> [[-Id] <String>] [[-Store] <BcdStoreInfo>] -Device <DeviceType> [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 条目
```
Set-BcdElement [-Element] <String> [-Entry] <BcdEntryInfo> -Type <ElementType> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 设备信息（Device Entry）
```
Set-BcdElement [-Element] <String> [-Entry] <BcdEntryInfo> -Device <DeviceType> [-Force] [-WhatIf] [-Confirm]
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

### -Device
{{ 填写设备描述 }}

```yaml
Type: Microsoft.Windows.Bcd.Cmdlets.SetBcdElementCommand+DeviceType
Parameter Sets: Device Id, Device Entry
Aliases:
Accepted values: Boot, Partition, File, Ramdisk, VHD, Locate, URI

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Element
{{ 填充元素描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Entry
{{ 填写条目描述 }}

```yaml
Type: Microsoft.Windows.Bcd.Cmdlets.BcdExtensions.BcdEntryInfo
Parameter Sets: Entry, Device Entry
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
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
{{ 填充ID描述 }}

```yaml
Type: System.String
Parameter Sets: Id, Device Id
Aliases: Identifier

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Store
{{ 填写店铺描述 }}

```yaml
Type: Microsoft.Windows.Bcd.Cmdlets.BcdExtensions.BcdStoreInfo
Parameter Sets: Id, Device Id
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Type
{{ 填写类型说明 }}

```yaml
Type: Microsoft.Windows.Bcd.Cmdlets.SetBcdElementCommand+ElementType
Parameter Sets: Id, Entry
Aliases:
Accepted values: Boolean, Integer, IntegerList, Entry, EntryList, String

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.Object
## 备注

## 相关链接
