---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dtc.PowerShell.dll-Help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/send-dtcdiagnostictransaction?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Send-DtcDiagnosticTransaction
---

# Send-DtcDiagnosticTransaction

## 摘要
将交易信息传播到指定的诊断资源管理器（Diagnostic Resource Manager）。

## 语法

```
Send-DtcDiagnosticTransaction [-Transaction] <DtcDiagnosticTransaction> [[-ComputerName] <String>]
 [[-Port] <Int32>] [[-PropagationMethod] <DtcTransactionPropagation>] [<CommonParameters>]
```

## 描述
`Send-DtcDiagnosticTransaction` cmdlet 将一笔交易（transaction）转发到指定的诊断资源管理器（Resource Manager，简称 RM）。可以使用 `PropagationMethod` 参数来指定交易转发的方式。

## 示例

#### 示例 1：发送一个 DTC（诊断交易码）
```powershell
PS C:\> $Tx = New-DtcDiagnosticTransaction
PS C:\> Send-DtcDiagnosticTransaction -Transaction $Tx -ComputerName "Host1" -PropagationMethod Push
```

第一个命令创建一个新的DTC诊断事务，并将其赋值给一个变量。

第二个命令将诊断数据发送到运行在名为Host1的计算机上的RM（可能是某种特定的管理系统或工具）。

## 参数

### -ComputerName
指定运行RM（Remote Management）的计算机的主机名。如果您没有指定主机名，该cmdlet将使用本地计算机的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Port
指定测试RM（Remote Manager）的监听端口。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: 3002
Accept pipeline input: False
Accept wildcard characters: False
```

### -PropagationMethod
指定要使用的传播机制（pull 或 push）。默认值为 pull。

```yaml
Type: DtcTransactionPropagation
Parameter Sets: (All)
Aliases:
Accepted values: Pull, Push

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Transaction
指定在事务传播过程中使用的 **DtcDiagnosticTransaction** 对象。您可以使用管道运算符将此参数值传递给 cmdlet。

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
此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Complete-DtcDiagnosticTransaction](./Complete-DtcDiagnosticTransaction.md)

[New-DtcDiagnosticTransaction](./New-DtcDiagnosticTransaction.md)

[接收 DTC 诊断事务](./Receive-DtcDiagnosticTransaction.md)

[Undo-DtcDiagnosticTransaction](./Undo-DtcDiagnosticTransaction.md)

