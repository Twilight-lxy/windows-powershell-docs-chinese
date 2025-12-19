---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dtc.PowerShell.dll-Help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/new-dtcdiagnostictransaction?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-DtcDiagnosticTransaction
---

# New-DtcDiagnosticTransaction

## 摘要
在本地计算机上的事务管理器中创建一个新的事务。

## 语法

```
New-DtcDiagnosticTransaction [[-Timeout] <Int32>] [[-IsolationLevel] <IsolationLevel>] [<CommonParameters>]
```

## 描述
`New-DtcDiagnosticTransaction` cmdlet 在本地计算机的事务管理器（Transaction Manager，简称 TM）中创建一个新事务。默认情况下，它会使用本地计算机上的默认事务管理器来创建事务。此 cmdlet 会返回一个事务对象，您可以将该对象传递给其他 cmdlets。

## 示例

### 示例 1：创建一个用于诊断问题的交易
```
PS C:\> New-DtcDiagnosticTransaction -Timeout 60 -IsolationLevel Serializable
Id
--
4625a5a3-af35-465d-a331-f224d79e4c85
```

这个命令创建了一个新的、可序列化的诊断事务，其超时时间为 60 秒。

## 参数

### -IsolationLevel
指定事务的隔离级别。该参数的可接受值为：

- Serializable
- RepeatableRead
- ReadCommitted
- ReadUncommitted
- Snapshot
- Chaos

If you do not specify this parameter, the cmdlet uses the default **IsolationLevel** value specified in the **System.Transactions.Transaction** object.

```yaml
Type: IsolationLevel
Parameter Sets: (All)
Aliases:
Accepted values: Serializable, RepeatableRead, ReadCommitted, ReadUncommitted, Snapshot, Chaos, Unspecified

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Timeout
指定事务的超时时间（以秒为单位）。如果您不指定此参数，cmdlet 将使用 **System.Transactions(Transaction** 对象中指定的默认超时值。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Complete-DtcDiagnosticTransaction](./Complete-DtcDiagnosticTransaction.md)

[Receive-DtcDiagnosticTransaction](./Receive-DtcDiagnosticTransaction.md)

[Send-DtcDiagnosticTransaction](./Send-DtcDiagnosticTransaction.md)

[Undo-DtcDiagnosticTransaction](./Undo-DtcDiagnosticTransaction.md)

