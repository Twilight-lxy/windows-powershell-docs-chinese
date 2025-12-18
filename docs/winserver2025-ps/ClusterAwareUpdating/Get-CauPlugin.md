---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 09/27/2022
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/get-cauplugin?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-CauPlugin
---

# 获取Cau插件

## 摘要
获取有关在本地计算机上注册的一个或多个软件更新插件的信息。

## 语法

```
Get-CauPlugin [[-Name] <String>] [<CommonParameters>]
```

## 描述

`Get-CauPlugin` cmdlet 可以获取有关在本地计算机上注册的一个或多个软件更新插件的信息。可以指定特定的插件，也可以检索所有已注册插件的相关信息。

在执行更新时，CAU总是会使用插件。默认使用的插件是**Microsoft.WindowsUpdatePlugin**。该插件与Windows Update代理进行通信，这种代理软件用于从Windows Update、Microsoft Update或Windows Server Update Services (WSUS)服务器下载更新时。有关插件在CAU中工作原理的更多信息，请参阅[How CAU Plug-ins Work](https://go.microsoft.com/fwlink/p/?LinkId=235333)。

## 示例

### 示例 1：获取有关软件更新插件的信息

```powershell
Get-CauPlugin | Format-List -Property "*"
```

这个命令用于获取有关在本地CAU工具中注册的软件更新插件的信息。

## 参数

### -Name

指定此 cmdlet 获取信息的插件的名称。如果未指定，则会返回所有已注册插件的信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft-cluster Aware-Updating.CauPlugin

## 备注

## 相关链接

[注册 Cau 插件](./Register-CauPlugin.md)

[Unregister-CauPlugin](./Unregister-CauPlugin.md)

