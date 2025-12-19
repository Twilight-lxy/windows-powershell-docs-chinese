---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dtc.PowerShell.dll-Help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/receive-dtcdiagnostictransaction?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Receive-DtcDiagnosticTransaction
---

# 接收 DTC 诊断交易信息

## 摘要
将事务从给定的诊断资源管理器（Diagnostic Resource Manager）中传播出去。

## 语法

```
Receive-DtcDiagnosticTransaction [[-ComputerName] <String>] [[-Port] <Int32>]
 [[-PropagationMethod] <DtcTransactionPropagation>] [<CommonParameters>]
```

## 描述
`Receive-DtcDiagnosticTransaction` cmdlet 用于从指定的诊断资源管理器（Resource Manager，简称 RM）中获取交易信息。该交易首先在指定的 RM 上创建，然后通过拉取（pull）或推送（push）的方式传播到 Windows PowerShell® 客户端。您可以使用 `PropagationMethod` 参数来指定具体的传播机制。

## 示例

### 示例 1：接收诊断交易
```powershell
PS C:\> Receive-DtcDiagnosticTransaction -ComputerName "Host1" -Port 17123 -PropagationMethod Pull
```
```output
Id
--
d23fd4b1-1b54-486a-9e9f-a92550a19ce2
```

此命令从Host1的端口17123获取一个诊断交易数据。

## 参数

### -ComputerName
指定运行RM（Removal Manager）的计算机的主机名。如果您没有指定主机名，此cmdlet将使用本地计算机的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
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
Position: 1
Default value: 3002
Accept pipeline input: False
Accept wildcard characters: False
```

### -PropagationMethod
指定要使用的传播机制（pull或push）。默认值为pull。

```yaml
Type: DtcTransactionPropagation
Parameter Sets: (All)
Aliases:
Accepted values: Pull, Push

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Complete-DtcDiagnosticTransaction](./Complete-DtcDiagnosticTransaction.md)

[New-DtcDiagnosticTransaction](./New-DtcDiagnosticTransaction.md)

[Send-DtcDiagnosticTransaction](./Send-DtcDiagnosticTransaction.md)

[Undo-DtcDiagnosticTransaction](./Undo-DtcDiagnosticTransaction.md)

