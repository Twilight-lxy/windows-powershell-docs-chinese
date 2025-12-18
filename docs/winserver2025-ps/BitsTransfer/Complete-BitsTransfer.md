---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.BackgroundIntelligentTransfer.Management.dll-Help.xml
Module Name: BitsTransfer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitstransfer/complete-bitstransfer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Complete-BitsTransfer
---

# 完整比特传输

## 摘要
完成了一个BITS传输任务。

## 语法

```
Complete-BitsTransfer [-BitsJob] <BitsJob[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Complete-BitsTransfer` cmdlet 会结束一个或多个后台智能传输服务（BITS）的传输任务，然后将文件保存在客户端计算机上。如果发生错误，相关的 `BitsJob` 对象会被写入错误处理流程中。

## 示例

### 示例 1：完成当前用户拥有的所有 BITS（Binary Interface Transfer Service）传输任务
```
C:\PS>Get-BitsTransfer | Complete-BitsTransfer
```

该命令会完成当前用户所拥有的所有BITS传输任务。

在这个命令中，`Get-BitsTransfer` cmdlet 的输出被传递给 `Complete-BitsTransfer` cmdlet。输出结果是一组 `BitsJob` 对象。

### 示例 2：在计算机上完成所有BITS传输任务
```
PS C:\> $Bits = Get-BitsTransfer -AllUsers
PS C:\> Complete-BitsTransfer -BitsJob $Bits
```

这些命令完成了计算机上所有的BITS传输任务。

第一个命令会检索计算机上所有的**BitsJob**对象，然后将它们存储在$Bits变量中。

第二个命令使用了*BitsJob*参数，将存储在$Bits变量中的**BitsJob**对象传递给**Complete-BitsTransfer** cmdlet。

### 示例 3：通过显示名称完成 BITS 数据传输任务
```
PS C:\> Get-BitsTransfer -Name testjob1 | Complete-BitsTransfer
```

此命令完成了由指定显示名称标识的BITS传输任务。

`Get-BitsTransfer` cmdlet 的输出是一个 `BitsJob` 对象。这个输出结果会被传递给 `Complete-BitsTransfer` cmdlet。

## 参数

### -BitsJob
指定需要完成的 BITS（Bit Transfer Service）传输任务。您可以从返回 **BitsJob** 对象的其他 cmdlet（例如 **Get-BitsTransfer**）中将该对象的值传递给此参数。

```yaml
Type: BitsJob[]
Parameter Sets: (All)
Aliases: b

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您确认是否要继续执行操作。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft BackgroundIntelligentTransferManagement.BitsJob[]
此cmdlet接受一个或多个**BitsJob**对象作为输入，并将这些对象填充到*BitsJob*参数中。

## 输出

### 无
这个cmdlet不会生成任何输出。

## 备注

## 相关链接

[Add-BitsFile](./Add-BitsFile.md)

[Get-BitsTransfer](./Get-BitsTransfer.md)

[Remove-BitsTransfer](./Remove-BitsTransfer.md)

[Resume-BitsTransfer](./Resume-BitsTransfer.md)

[Set-BitsTransfer](./Set-BitsTransfer.md)

[开始位传输](./Start-BitsTransfer.md)

[暂停位传输](./Suspend-BitsTransfer.md)

