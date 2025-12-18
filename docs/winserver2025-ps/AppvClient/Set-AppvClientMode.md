---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/set-appvclientmode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AppvClientMode
---

# 设置 AppVClient 模式

## 摘要
设置客户端运行的模式。

## 语法

### 正常
```
Set-AppvClientMode [-Normal] [<CommonParameters>]
```

### 卸载
```
Set-AppvClientMode [-Uninstall] [<CommonParameters>]
```

## 描述
`Set-AppvClientMode` cmdlet 用于设置客户端运行的模式。默认情况下，该 cmdlet 的设置为 “Normal”（正常模式），此时 Microsoft 应用虚拟化 (App-V) 客户端会正常运行。如果指定了 `Uninstall` 参数，App-V 客户端将阻止所有客户端操作的执行，包括添加和发布软件包以及创建虚拟环境等操作。

## 示例


## 参数

### -Normal
表示App-V客户端运行正常。这意味着所有添加和发布App-V包以及创建虚拟环境的过程都能正常进行。

```yaml
Type: SwitchParameter
Parameter Sets: Normal
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Uninstall
该命令表示会阻止 App-V 客户端添加或发布软件包，也不会创建任何虚拟环境。这样设置是为了确保 App-V 客户端的卸载操作能够正确完成。

```yaml
Type: SwitchParameter
Parameter Sets: Uninstall
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-AppvClientMode](./Get-AppvClientMode.md)

