---
description: 使用此主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/clear-msmqoutgoingqueue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-MsmqOutgoingQueue
---

# 清除 MsmqOutgoingQueue 队列

## 摘要
清空出站消息队列。

## 语法

```
Clear-MsmqOutgoingQueue -InputObject <OutgoingQueue[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Clear-MsmqOutgoingQueue` cmdlet 用于清空出站队列。可以通过使用 `MsmqOutgoingQueue` 对象来指定需要清除的队列。此 cmdlet 会返回一个表示已清除的出站队列的 `MsmqOutgoingQueue` 对象。

## 示例

### 示例 1：根据名称清除外出消息队列
```
PS C:\> Get-MsmqOutgoingQueue -Name "Order*" | Clear-MsmqOutgoingQueue
```

这个命令使用 **Get-MsmqOutgoingQueue** cmdlet 来获取所有名称以 “Order” 开头的出站消息队列。该命令通过管道运算符将结果传递给当前的 cmdlet，然后当前 cmdlet 会清空每个队列。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定一个包含 **MsmqOutgoingQueue** 对象的数组。此 cmdlet 会清除由该参数指定的出站队列。该参数支持管道输入（pipeline input）。

```yaml
Type: OutgoingQueue[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Msmq POWERShellCommands.OutgoingQueue[]

## 输出

### System.Object

## 备注

## 相关链接

[Get-MsmqOutgoingQueue](./Get-MsmqOutgoingQueue.md)

[Resume-MsmqOutgoingQueue](./Resume-MsmqOutgoingQueue.md)

[Suspend-MsmqOutgoingQueue](./Suspend-MsmqOutgoingQueue.md)

