---
description: 使用此主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/get-msmqqueueacl?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MsmqQueueACL
---

# Get-MsmqQueueACL

## 摘要
获取队列访问控制列表。

## 语法

```
Get-MsmqQueueACL [-InputObject] <MessageQueue[]> [<CommonParameters>]
```

## 描述
`Get-MsmqQueueACL` cmdlet 可用于获取 `MsmqQueueAcl` 对象。该 cmdlet 适用于私有队列、公共队列、系统日志队列、系统死信队列以及系统事务性死信队列。

## 示例

### 示例 1：获取消息队列的访问控制列表（ACL）
```
PS C:\> Get-MsmqQueue -Name "Order*" | Get-MsmqQueueACL
```

这个命令使用 **Get-MsmqQueue** cmdlet 来获取名称以 “Order” 开头的消息队列。该命令通过管道运算符（pipeline operator）将查询结果传递给当前的 cmdlet，然后当前的 cmdlet 会获取这些队列的访问控制列表（ACLs）。

## 参数

### -InputObject
指定一个包含 **MsmqQueue** 对象的数组。该 cmdlet 会获取由这些 **MsmqQueue** 对象所指定的队列的访问控制列表（ACL）信息。此参数支持管道输入（pipeline input）。

```yaml
Type: MessageQueue[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Msmq.PowShell Commands.MessageQueue[]

## 输出

### System.Object

## 备注

## 相关链接

[Get-MsmqQueue](./Get-MsmqQueue.md)

[Set-MsmqQueueACL](./Set-MsmqQueueACL.md)

