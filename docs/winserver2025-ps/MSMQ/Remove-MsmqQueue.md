---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/remove-msmqqueue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-MsmqQueue
---

# Remove-MsmqQueue

## 摘要
删除队列。

## 语法

```
Remove-MsmqQueue -InputObject <MessageQueue[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-MsmqQueue` cmdlet 用于删除队列。您可以通过使用 `MsmqQueue` 对象来指定要删除的队列。此 cmdlet 不会返回任何内容。

## 示例

#### 示例 1：移除具有指定名称的公共队列
```
PS C:\> Get-MsmqQueue -Name "Order*" -QueueType Public | Remove-MsmqQueue
```

该命令使用 **Get-MsmqQueue** cmdlet 获取名称以 “Order” 开头的公共队列。通过管道运算符，该命令将查询结果传递给当前的 cmdlet（用于删除这些队列）。

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

### -InputObject
指定一个包含 **MsmqQueue** 对象的数组。该cmdlet会删除这些 **MsmqQueue** 对象所对应的队列。此参数支持管道输入（pipeline input）。

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
展示了如果该cmdlet运行会发生的结果。但实际上，该cmdlet并没有被执行。

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

### Microsoft.Msmq.PowerShell Commands.MessageQueue[]

## 输出

### System.Object

## 备注

## 相关链接

[Clear-MsmqQueue](./Clear-MSMQQueue.md)

[Get-MsmqQueue](./Get-MsmqQueue.md)

[New-MsmqQueue](./New-MsmqQueue.md)

[接收-MsmqQueue](./Receive-MsmqQueue.md)

[Send-MsmqQueue](./Send-MsmqQueue.md)

[Set-MsmqQueue](./Set-MsmqQueue.md)

