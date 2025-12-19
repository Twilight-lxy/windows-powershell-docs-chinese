---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dtc.PowerShell.dll-Help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/undo-dtcdiagnostictransaction?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Undo-DtcDiagnosticTransaction
---

# 撤销 DTC 诊断交易

## 摘要
对指定的事务调用“Abort”（终止）过程。

## 语法

```
Undo-DtcDiagnosticTransaction [-Transaction] <DtcDiagnosticTransaction> [<CommonParameters>]
```

## 描述
` Undo-DtcDiagnosticTransaction` cmdlet 会调用指定事务上的 `Abort` 过程。

## 示例

### 示例 1：撤销 DTC（诊断故障代码）相关的诊断操作
```
PS C:\> $Tx = New-DtcDiagnosticTransaction
PS C:\> Undo-DtcDiagnosticTransaction -Transaction $Tx
```

此命令创建一个新的诊断事务，并将其赋值给一个变量。

第二个命令会撤销该交易。

## 参数

### -Transaction
指定用于调用 `Abort` 过程的 `DtcDiagnosticTransaction` 对象。您可以使用管道运算符将此参数值传递给相应的 cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Complete-DtcDiagnosticTransaction](./Complete-DtcDiagnosticTransaction.md)

[New-DtcDiagnosticTransaction](./New-DtcDiagnosticTransaction.md)

[接收 DTC 诊断事务](./Receive-DtcDiagnosticTransaction.md)

[Send-DtcDiagnosticTransaction](./Send-DtcDiagnosticTransaction.md)

