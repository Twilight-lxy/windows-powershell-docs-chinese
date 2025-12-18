---
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/get-appsharedpackagecontainer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppSharedPackageContainer
---

# Get-AppSharedPackageContainer

## 摘要
获取有关共享包容器的相关信息。

## 语法

```
Get-AppSharedPackageContainer [[-Name] <String>] [[-Id] <String>] [-AllUsers]
 [<CommonParameters>]
```

## 描述

该cmdlet会显示有关任何共享包容器的信息，特别是其中包含哪些包。

## 示例

### 示例 1

```powershell
Get-AppSharedPackageContainer -Name Contoso*
```

```output
Name               : ContosoTestContainer
Id                 : ContosoTestContainer_1
PackageFamilyNames : {Contoso.SpellCheckPlugin.1.0.0.0_7pneu3d8sswe, Notepad++.2.0.0.1_ohjis898f1}

Name               : ContosoTestContainer
Id                 : ContosoTestContainer_2
PackageFamilyNames : {Contoso.SpellCheckPlugin2.1.0.0.0_7pneu3d8sswe, Notepad++.2.0.0.1_ohjis898f1}
```

该命令会显示所有以“Contoso”为前缀的共享包容器中的包。

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

### -Id

容器的ID。可以通过运行`Get-AppSharedPackageContainer`命令来获取。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

容器的名称。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.Object

## 备注

## 相关链接
