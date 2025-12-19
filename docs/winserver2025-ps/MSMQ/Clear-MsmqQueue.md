---
description: 使用此主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/clear-msmqqueue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-MsmqQueue
---

# 清空 MsmqQueue

## 摘要
清除队列中的等待项。

## 语法

```
Clear-MsmqQueue -InputObject <MessageQueue[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Clear-MsmqQueue` cmdlet 用于清空消息队列。可以通过使用 `MessageQueue` 对象来指定需要清空的队列。该 cmdlet 会返回一个 `MessageQueue` 对象，表示被清空的消息队列。

## 示例

### 示例 1：根据名称清除消息队列
```
PS C:\> Get-MsmqQueue -Name "Order*" | Clear-MsmqQueue
```

该命令使用 `Get-MsmqQueue` cmdlet 获取所有名称以 “Order” 开头的消息队列。通过管道运算符（pipeline operator），该命令将查询结果传递给当前的 cmdlet，然后当前 cmdlet 会清空每个队列中的内容。

## 参数

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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
用于指定一个包含 **MessageQueue** 对象的数组。此cmdlet会清除这些 **MessageQueue** 对象所对应的队列。该参数支持管道输入（pipeline input）。

```yaml
Type: MessageQueue[]
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Msmq.PowerShellCommands.MessageQueue[]

## 输出

### System.Object

## 备注

## 相关链接

[Get-MsmqQueue](./Get-MsmqQueue.md)

[New-MsmqQueue](./New-MsmqQueue.md)

[Receive-MsmqQueue](./Receive-MsmqQueue.md)

[Remove-MsmqQueue](./Remove-MsmqQueue.md)

[Send-MsmqQueue](./Send-MsmqQueue.md)

[Set-MsmqQueue](./Set-MsmqQueue.md)

