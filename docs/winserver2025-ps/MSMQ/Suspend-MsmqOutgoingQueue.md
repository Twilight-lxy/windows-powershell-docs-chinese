---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/suspend-msmqoutgoingqueue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Suspend-MsmqOutgoingQueue
---

# 暂停 MsMQ 出站队列（Suspend-MsmqOutgoingQueue）

## 摘要
暂停出队操作（即停止将数据从队列中移除）。

## 语法

```
Suspend-MsmqOutgoingQueue -InputObject <OutgoingQueue[]> [<CommonParameters>]
```

## 描述
`Suspend-MsmqOutgoingQueue` cmdlet 用于暂停出队的操作。可以通过使用 `MsmqOutgoingQueue` 对象来指定需要暂停的队列。该 cmdlet 会返回被暂停的队列对象。

## 示例

### 示例 1：按名称暂停指定的出站队列
```
PS C:\> Get-MsmqOutgoingQueue -Name "Order*" | Suspend-MsmqOutgoingQueue
```

该命令使用 `Get-MsmqOutgoingQueue` cmdlet 获取所有名称以 “Order” 开头的出站队列。通过管道运算符（pipeline operator），该命令将结果传递给当前的 cmdlet，然后当前 cmdlet 会暂停这些队列的运行。

## 参数

### -InputObject
指定一个包含 **MsmqOutgoingQueue** 对象的数组。此 cmdlet 会暂停由该参数指定的出站队列的运行。该参数支持管道输入（pipeline input）。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Msmq.PowerShellCommands.OutgoingQueue[]

## 输出

### System.Object

## 备注

## 相关链接

[Clear-MsmqOutgoingQueue](./Clear-MSMQOutgoingQueue.md)

[Get-MsmqOutgoingQueue](./Get-MSMQOutgoingQueue.md)

[Resume-MsmqOutgoingQueue](./Resume-MsmqOutgoingQueue.md)

