---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dtc.PowerShell.dll-Help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/complete-dtcdiagnostictransaction?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Complete-DtcDiagnosticTransaction
---

# 完整的 DTC 诊断交易

## 摘要
如果指定的事务是根事务，则会调用提交（Commit）过程；否则，会在事务对象上调用完成（Complete）方法。

## 语法

```
Complete-DtcDiagnosticTransaction [-Transaction] <DtcDiagnosticTransaction> [<CommonParameters>]
```

## 描述
`Complete-DtcDiagnosticTransaction` cmdlet 会在指定的事务是根事务时调用 `Commit` 过程；否则，它会调用由 `DtcDiagnosticTransaction` 对象指定的事务对象上的 `Complete` 方法。

## 示例

### 示例 1：完成 DTC（故障诊断代码）诊断事务
```
PS C:\> $Tx = New-DtcDiagnosticTransaction
PS C:\> Complete-DtcDiagnosticTransaction -Transaction $Tx
```

第一个命令创建了一个新的DTC诊断事务，并将其赋值给一个变量。

第二个命令会调用事务的提交（Commit）流程。

## 参数

### -Transaction
指定要调用 **Complete** 方法或进行提交的 **DtcDiagnosticTransaction** 对象。

```yaml
Type: DtcDiagnosticTransaction
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 默认值
指定用于调用 `Complete` 方法的 `DtcDiagnosticTransaction` 对象。您可以使用管道运算符将此参数值传递给 cmdlet。

## 输出

## 备注

## 相关链接

[New-DtcDiagnosticTransaction](./New-DtcDiagnosticTransaction.md)

[接收 DTC 诊断事务](./Receive-DtcDiagnosticTransaction.md)

[Send-DtcDiagnosticTransaction](./Send-DtcDiagnosticTransaction.md)

[Undo-DtcDiagnosticTransaction](./Undo-DtcDiagnosticTransaction.md)

