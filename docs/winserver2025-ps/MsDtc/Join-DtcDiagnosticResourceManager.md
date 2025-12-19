---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Dtc.PowerShell.dll-Help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/join-dtcdiagnosticresourcemanager?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Join-DtcDiagnosticResourceManager
---

# Join-DtcDiagnostic ResourceManager

## 摘要
为某个事务对象（transaction object）分配一个用于诊断目的的资源管理器（Diagnostic Resource Manager）。

## 语法

```
Join-DtcDiagnosticResourceManager [-Transaction] <DtcDiagnosticTransaction> [[-ComputerName] <String>]
 [[-Port] <Int32>] [-Volatile] [<CommonParameters>]
```

## 描述
`Join-DtcDiagnostic ResourceManager` cmdlet 为指定的事务对象注册一个诊断资源管理器（Resource Manager，简称 RM）。首先需要将该事务发送到资源管理器中。

## 示例

### 示例 1：创建一个新的诊断事务
```
PS C:\> $Transaction = New-DtcDiagnosticTransaction
PS C:\> Join-DtcDiagnosticResourceManager -Transaction $Transaction
```

第一个命令使用 `New-DtcDiagnosticTransaction` cmdlet 创建一个事务，然后将该事务存储在 `$Transaction` 变量中。

第二个命令将存储在 `$Transaction` 变量中的交易信息提交给诊断资源管理器。

## 参数

### -ComputerName
指定运行RM（Remote Management）程序的计算机的主机名。如果您未指定主机名，此cmdlet将使用本地计算机的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Port
指定测试RM（Remote Management）的监听端口。如果您没有指定端口号，此cmdlet会使用本地计算机的名称作为监听端口。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Transaction
指定用于将RM（资源管理器）添加到其中的交易对象。

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

### -Volatile
这表示该 cmdlet 会创建一个“临时的”（易变的）注册记录。如果您不指定此参数，cmdlet 将创建一个“持久的”（稳定的）注册记录。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Start-DtcDiagnostic ResourceManager](./Start-DtcDiagnosticResourceManager.md)

[Stop-DtcDiagnostic ResourceManager](./Stop-DtcDiagnosticResourceManager.md)

[New-DtcDiagnosticTransaction](./New-DtcDiagnosticTransaction.md)

