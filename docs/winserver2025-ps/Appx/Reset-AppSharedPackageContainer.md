---
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/reset-appsharedpackagecontainer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Reset-AppSharedPackageContainer
---

# 重置 AppSharedPackageContainer

## 摘要
会删除容器中的所有应用程序数据。

## 语法

```
Reset-AppSharedPackageContainer [-Name] <String> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

该cmdlet会删除容器中的所有应用程序数据，包括虚拟文件和注册表项。

## 示例

### 示例 1

```powershell
Reset-AppSharedPackageContainer -Name ContosoTestContainer
```

这个命令会清除共享包容器`ContosoTestContainer`中的所有应用程序数据。

## 参数

### -Force

跳过确认请求的步骤。

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

### -Name

容器的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
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

展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被运行。

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
