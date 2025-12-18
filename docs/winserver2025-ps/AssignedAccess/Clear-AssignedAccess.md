---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: AssignedAccess-help.xml
Module Name: AssignedAccess
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/assignedaccess/clear-assignedaccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-AssignedAccess
---

# 清除已分配的访问权限

## 摘要
清除已分配的访问权限及配置的账户设置。

## 语法

```
Clear-AssignedAccess [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Clear-AssignedAccess` cmdlet 会清除已配置的访问权限设置，并将用户的账户设置恢复到默认状态。

如果用户已登录，或者电脑配备了 PS/2 键盘，那么必须重新启动电脑才能使更改生效。

“分配访问权限”（Assigned Access）相关的cmdlet仅支持Windows 10和Windows 11客户端操作系统。

## 示例

### 示例 1：清除已配置的访问权限设置
```
PS C:\> Clear-AssignedAccess
```

该命令配置了账户访问权限，并将用户的设置恢复为默认值。

## 参数

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。
您不能将输入内容通过管道（pipe）传递给这个cmdlet。

## 输出

### 没有（需要处理的内容）。
这个cmdlet不会生成任何输出。

## 备注

## 相关链接

[获取分配的访问权限](./Get-AssignedAccess.md)

[Set-AssignedAccess](./Set-AssignedAccess.md)

