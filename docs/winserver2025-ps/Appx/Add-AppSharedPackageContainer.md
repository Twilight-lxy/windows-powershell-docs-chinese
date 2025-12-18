---
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/add-appsharedpackagecontainer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AppSharedPackageContainer
---

# 添加应用程序共享包容器

## 摘要
部署共享的包容器定义。

## 语法

```
Add-AppSharedPackageContainer [-Path] <String> [-ForceApplicationShutdown] [-Merge]
 [-Force] [<CommonParameters>]
```

## 描述

`Add-AppSharedPackageContainer` cmdlet 用于为特定用户部署共享包容器定义。

## 示例

### 示例 1

```powershell
Add-AppSharedPackageContainer -Path C:\MyFolder\ContosoTestContainer.xml
```

此命令会部署在 ContosoTestContainer 文件中描述的配置内容。

## 参数

### -Force

将目标用户现有的同名容器替换为新建容器的配置信息。

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

关闭目前在共享包容器中运行的所有程序/包。

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

### -Merge

将新容器的定义合并到目标用户已有的同名容器定义中。

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

### -Path

XML定义文件的路径。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: PSPath

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接
