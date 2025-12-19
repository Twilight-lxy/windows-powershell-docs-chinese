---
external help file: Microsoft.Windows.Bcd.Cmdlets.dll-Help.xml
Module Name: Microsoft.Windows.Bcd.Cmdlets
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.bcd.cmdlets/new-bcdentry?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-BcdEntry
---

# New-BcdEntry

## 摘要
{{ 填写剧情简介 }}

## 语法

### 应用程序
```
New-BcdEntry -Application <String> [-Description <String>] [[-Id] <String>] [[-Store] <BcdStoreInfo>] [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 设备
```
New-BcdEntry [-Description <String>] [-Device] [[-Id] <String>] [[-Store] <BcdStoreInfo>] [-Force] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 继承
```
New-BcdEntry [-Description <String>] [[-Id] <String>] -Inherit <String> [[-Store] <BcdStoreInfo>] [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 默认值
```
New-BcdEntry [-Description <String>] [-Id] <String> [[-Store] <BcdStoreInfo>] [-Force] [-WhatIf] [-Confirm]
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

### -Application
{{ 填写应用程序描述 }}

```yaml
Type: System.String
Parameter Sets: Application
Aliases:

Required: True
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

### -Device
{{ 填写设备描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: Device
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
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
Parameter Sets: Application, Device, Inherit
Aliases: Identifier

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

```yaml
Type: System.String
Parameter Sets: Default
Aliases: Identifier

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Inherit
{{ 填写继承描述 }}

```yaml
Type: System.String
Parameter Sets: Inherit
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
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft.Windows.Bcd Cmdlets.BcdExtensions.BcdEntryInfo

## 备注

## 相关链接
