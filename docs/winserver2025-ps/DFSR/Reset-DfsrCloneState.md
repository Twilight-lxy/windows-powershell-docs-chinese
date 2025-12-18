---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/reset-dfsrclonestate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Reset-DfsrCloneState
---

# 重置 DFSR 的克隆状态

## 摘要
取消克隆操作。

## 语法

```
Reset-DfsrCloneState [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Reset-DfsrCloneState` cmdlet 会取消正在进行的分布式文件系统（DFS）复制数据库克隆操作，并将卷的数据库状态恢复到之前的状态。

当你取消导出操作时，DFS复制服务会恢复其在处理开始时创建的备份数据库副本。当你取消导入操作时，DFS复制服务会删除新的数据库副本。当你运行相应的cmdlet时，该cmdlet会发送重置指令，并等待DFS复制服务完成相应的操作。你可以使用**Get-DfsrState** cmdlet来查看当前的重置状态。

## 示例

### 示例 1：取消克隆操作
```
PS C:\> Reset-DfsrCloneState
```

此命令会取消正在进行的DFS复制克隆操作，并将卷的数据库恢复到之前的状态。

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

### -Force
强制命令执行，而无需询问用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Get-DfsrCloneState](./Get-DfsrCloneState.md)

