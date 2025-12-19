---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/resume-msmqoutgoingqueue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Resume-MsmqOutgoingQueue
---

# Resume-MsmqOutgoingQueue

## 摘要
恢复出站队列（即那些尚未被处理的请求或任务）。

## 语法

```
Resume-MsmqOutgoingQueue [-InputObject <OutgoingQueue[]>] [<CommonParameters>]
```

## 描述
` Resume-MsmqOutgoingQueue ` 这个 cmdlet 用于恢复处于待发送状态的队列（即那些尚未被实际发送出去的队列）。你需要使用 ` MsmqOutgoingQueue ` 对象来指定需要恢复的队列。执行该 cmdlet 后，它会返回那些已被成功恢复的 ` MsmqOutgoingQueue ` 对象。

## 示例

#### 示例 1：按名称恢复待发送的消息队列
```
PS C:\> Get-MsmqOutgoingQueue -Name "Order*" | Resume-MsmqOutgoingQueue
```

该命令使用 `Get-MsmqOutgoingQueue` cmdlet 来获取名称以 “Order” 开头的出站队列。然后通过管道运算符将查询结果传递给当前的 cmdlet，以便继续处理这些队列。

## 参数

### -InputObject
指定一个包含 `MsmqOutgoingQueue` 对象的数组。此cmdlet用于恢复由该参数指定的出站队列的运行状态。该参数支持管道输入（pipeline input）。

```yaml
Type: OutgoingQueue[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Msmq.PowerShell Commands.OutgoingQueue[]

## 输出

### System.Object

## 备注

## 相关链接

[Clear-MsmqOutgoingQueue](./Clear-MSMQOutgoingQueue.md)

[Get-MsmqOutgoingQueue](./Get-MSMQOutgoingQueue.md)

[暂停 MsmqOutgoingQueue](./Suspend-MsmqOutgoingQueue.md)

