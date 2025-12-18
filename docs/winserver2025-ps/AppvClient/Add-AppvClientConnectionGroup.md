---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/add-appvclientconnectiongroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AppvClientConnectionGroup
---

# 添加 Add-AppvClientConnectionGroup

## 摘要
创建由多个包组成的组合。

## 语法

```
Add-AppvClientConnectionGroup [-Path] <String> [<CommonParameters>]
```

## 描述
`Add-AppvClientConnectionGroup` cmdlet 用于创建一个 Microsoft 应用程序虚拟化（App-V）连接组。为了使该连接组生效，组中的所有软件包都必须添加到目标计算机上，并且这些软件包在目标计算机上不应处于运行状态。

此cmdlet也可用于更新已存在的连接组定义。

## 示例

### 示例 1：添加一个连接组
```
PS C:\> Add-AppvClientConnectionGroup -Path "C:\MyApps\MyGroup.xml"
```

此命令会根据提供的路径将连接组文件添加到计算机上。

## 参数

### -Path
指定App-V连接组定义文件。

```yaml
Type: String
Parameter Sets: (All)
Aliases: PSPath

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.AppvAgent.AppvClientConnectionGroup

## 备注

## 相关链接

[Disable-AppvClientConnectionGroup](./Disable-AppvClientConnectionGroup.md)

[Enable-AppvClientConnectionGroup](./Enable-AppvClientConnectionGroup.md)

[Get-AppvClientConnectionGroup](./Get-AppvClientConnectionGroup.md)

[Mount-AppvClientConnectionGroup](./Mount-AppvClientConnectionGroup.md)

[Remove-AppvClientConnectionGroup](./Remove-AppvClientConnectionGroup.md)

[修复-AppvClientConnectionGroup](./Repair-AppvClientConnectionGroup.md)

[Stop-AppvClientConnectionGroup](./Stop-AppvClientConnectionGroup.md)

