---
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/remove-appsharedpackagecontainer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AppSharedPackageContainer
---

# 删除应用程序共享包容器

## 摘要
删除共享的软件包容器。

## 语法

```
Remove-AppSharedPackageContainer [-Name] <String> [-ForceApplicationShutdown] [-AllUsers]
 [<CommonParameters>]
```

## 描述

该cmdlet会删除特定用户的共享包容器定义。

## 示例

### 示例 1

```powershell
Remove-AppSharedPackageContainer -Name ContosoTestContainer
```

此命令会删除名为`ContosoTestContainer`的共享包容器定义。

## 参数

### -AllUsers

不受支持。这将导致“-AllUsers功能尚未实现”的错误。

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

### -ForceApplicationShutdown

关闭共享包容器中的所有包。

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

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.Object

## 备注

## 相关链接
