---
description: 通过添加 Windows 本地管理员密码解决方案（LAPS）相关的模式属性来扩展 Active Directory（AD）的模式结构。
external help file: lapspsh.dll-Help.xml
Module Name: LAPS
online version: https://learn.microsoft.com/powershell/module/laps/update-lapsadschema?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
Locale: en-US
ms.date: 04/10/2023
title: Update-LapsADSchema
---

# 更新 LapsADSchema

## 摘要
通过添加 Windows 本地管理员密码解决方案（LAPS）的架构属性来扩展 Active Directory（AD）的架构。

## 语法

```
Update-LapsADSchema [-Credential <PSCredential>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Update-LapsADSchema` cmdlet 用于将 LAPS 模式属性添加到 AD（Active Directory）模式中。这些模式扩展的具体内容可以在 [Windows LAPS 模式扩展参考文档](https://go.microsoft.com/fwlink/?linkid=2233804) 中找到。

可以使用 `Verbose` 参数来获取有关该 cmdlet 操作的更多信息。

## 示例

### 示例 1

```powershell
Update-LapsADSchema
```

```Output
The 'ms-LAPS-Password' schema attribute needs to be added to the AD schema.
Do you want to proceed?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): A
```

这个示例扩展了AD（Active Directory）架构，以添加LAPS属性。

## 参数

### -Credential

指定了一组用于扩展模式时的凭据。如果未指定，则使用当前用户的凭据。

```yaml
Type: System.Management.Automation.PSCredential
Parameter Sets: (All)
Aliases:

Required: False
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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Windows LAPS概述](https://go.microsoft.com/fwlink/?linkid=2233901)

[Windows LAPS模式扩展参考](https://go.microsoft.com/fwlink/?linkid=2233804)
