---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 09/27/2022
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/register-cauplugin?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Register-CauPlugin
---

# Register-CauPlugin

## 摘要
在本地计算机上注册一个用于更新CAU软件的插件。

## 语法

```
Register-CauPlugin [-Path] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Register-CauPlugin` cmdlet 用于在本地计算机上注册一个支持集群感知更新（Cluster-Aware Updating，简称 CAU）的软件更新插件。

在执行更新时，CAU始终会使用某个插件。不过实际上你无需手动注册该插件，因为CAU默认使用了**Microsoft.WindowsUpdatePlugin**这个插件。该插件会与每个节点上安装的Windows Update代理软件进行通信；这种软件在从Windows Update、Microsoft Update或Windows Server Update Services (WSUS)服务器下载更新时也会被使用。有关插件在CAU中工作原理的更多信息，请参阅[CAU插件的工作原理](https://go.microsoft.com/fwlink/p/?LinkId=235333)。

## 示例

### 示例 1：注册位于指定文件夹中的特定插件

```powershell
Register-CauPlugin -Path "C:\PluginDevelopment\Plugin01.dll" -Force
```

该命令注册了一个名为 Plugin01.dll 的插件，该插件位于 C:\PluginDevelopment 文件夹中。由于命令指定了 **Force** 参数，因此此 cmdlet 在运行时不会显示确认提示。

## 参数

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

指定实现该插件的二进制文件的路径。那些实现了插件接口并使用了 `plugin` 属性进行装饰的类，会通过反射机制被检测到并被注册到系统中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行该 cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft-cluster Aware-Updating.CauPlugin

## 备注

## 相关链接

[Get-CauPlugin](./Get-CauPlugin.md)

[Unregister-CauPlugin](./Unregister-CauPlugin.md)

