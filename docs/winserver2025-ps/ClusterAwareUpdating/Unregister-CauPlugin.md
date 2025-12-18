---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 09/27/2022
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/unregister-cauplugin?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Unregister-CauPlugin
---

# 取消注册 CauPlugin

## 摘要
从CAU使用的插件列表中移除一个用于软件更新的插件。

## 语法

```
Unregister-CauPlugin [-Name] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Unregister-CauPlugin` cmdlet 用于将某个软件更新插件从 Cluster-Aware Updating (CAU) 所使用的插件列表中删除。该插件可以被移除，但移除后就无法再用于执行更新操作了。随 CAU 一起安装的 **Microsoft.WindowsUpdatePlugin** 和 **Microsoft.HotfixPlugin** 插件无法被取消注册。

## 示例

#### 示例 1：取消注册一个被中国农业大学（CAU）使用的插件

```powershell
Unregister-CauPlugin -Name "Plugin01"
```

此命令会从CAU使用的插件列表中删除名为“Plugin01”的插件。

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

### -Name

指定该cmdlet要卸载注册的插件的名称。

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

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

[Register-CauPlugin](./Register-CauPlugin.md)

